### ------- Main Game Loop ------- ###

##TO DO##
#-add in a way to play multiple games
#-
#-
#-
#-


import pygame, sys
from pygame.locals import *
import random
import itertools
from CasinoVariables import * #this is just a file that defines the window for the game
from CasinoCardGraphics import *
from CasinoBoardGraphics import*
from CasinoInteractive import getCard, getTableCards, getSelectedBuildRank, buildChoicesSpots, buildFromCoordinates
from CasinoComputerPlayer import cardsValue, discardValue, getComputerMove
from CasinoLogic import suits, Card, Deck, Player, ComputerPlayer, HumanPlayer, Table, multiplesCheck, Move, TakeLastCards, Discard, Take, Build, rankChoices4Build
from GameState import GameState



pygame.init()
pygame.display.set_caption('Casino v5')


## Global Variables (is that what I mean?) ##

gameState = GameState() #it starts in the prep state

gameNumber = 0 #0+
handNumber = 0 #0-5
turnNumber = 0 #0-7

firstTime = True #keeps track of whether its the computer's first move or not, to display what move it made
                
deck = Deck()
deck.shuffle()
table = Table()

player1 = HumanPlayer(False, "Alicia")
player2 = ComputerPlayer(True)


#keeps track of what move the human is currently working on
#moveType = None  ###<<--- this is now in the variables doc


#keeps track of what move the computer is currently working on
computerMoveType = None
computerMove = None
tup = None

buildRank = 0 #what build we're currently talking about.... its a horrible variable.

illegalMove = False #once the player presses enter, was that an illegal move or not?

#keeps track of whether the last move they made was taking or not, to see who picks up all of the last cards
p1Last = 0
p2Last = 0


##--##--##--##
    

while True: # main game loop    
    #-- Managing all of the waiting states (give the while loop an opportunity to go all the way through and refresh the cards) --#        
    if gameState.waitGM:
        gameState.clear()
        gameState.gettingMove = True
        
    elif gameState.waitP:
        gameState.clear()
        gameState.prep = True
        
    elif gameState.waitGO:
        pygame.time.wait(4000) #give the player time to see the results of "last"
        gameState.clear()
        gameState.gameOver = True
        
    elif gameState.waitCM:
        if turnNumber == 0:
            pygame.time.wait(3000)
            #if handNumber == 0: it would be nice to put something here saying "its a new game! you're the dealer!"
        gameState.clear()
        gameState.computerMove = True
        
    elif gameState.displayCM:
        gameState.clear()
        pygame.time.wait(1000) #give the player time to see the computer's selections
        
        if turnNumber == 7:
            gameState.waitP = True
            turnNumber = 0
            if handNumber == 5:
                gameState.clear()
                gameState.last = True
            else:
                handNumber += 1
        else:
            turnNumber += 1
            gameState.waitGM = True
   
    elif gameState.waitCM2:
        gameState.clear()
        gameState.displayCM = True

    elif gameState.waitRO:
        pygame.time.wait(3000)
        gameState.clear()
        gameState.roundOver = True


    #-- the prep state: dealing cards to the two players and possibly the table --#
    if gameState.prep:
        #on the first hand, deal 4 to the table
        if handNumber == 0:
            for i in range(4):
                table.allCards.append(deck.draw())

            dealToTableUI(table.allCards)

        #on all 6 hands, deal 4 cards to each player
        for i in range(4):
            player1.hand.append(deck.draw())
            player2.hand.append(deck.draw())


        populateHandsUI(player1, player2)

        buildChoicesDict = updatedBuildChoicesDict(player1)

        #changing the state based on who is the dealer
        gameState.clear()
        if player1.dealer:
            gameState.waitCM = True
        else:
            gameState.waitGM = True
       


    #-- drawing stuff onto the screen --#
    w.fill(GREEN)
    buildScore(player1, player2)
    buildInstructions()
    
    if firstTime == False:
        buildComputerMove(tup, computerMoveType)
    
    if gameState.gettingMove:
        if moveType != None:
            buildMoveType(moveType)
        if illegalMove != False:
            buildIllegalMove(illegalMove)

    if moveType == "Build":
        if buildRank > 0:
            selectBuildChoice(buildRank, buildChoicesDict)
        buildBuildChoices(player1, buildChoicesDict)

    if handNumber == 5:
        buildLast()

    if gameState.last:
        if p1Last > p2Last: #I tried to do this by saying lastPlayer = player1 or 2, but the score didn't get added
            selectLastCardsUI(player1)
            TakeLastCards(table, None, player1, player2).execute()
        else:
            selectLastCardsUI(player2)
            TakeLastCards(table, None, player2, player1).execute()

        gameState.clear()
        gameState.waitGO = True

    if gameState.newGame:
        pygame.time.wait(4000) #gives them time to see the score of the last round

        #reset all of the variables and stuff
        gameNumber += 1
        handNumber = 0
        turnNumber = 0

        firstTime = True
                        
        deck = Deck()
        deck.shuffle()
        table = Table()

        moveType = None

        computerMoveType = None
        computerMove = None
        tup = None

        buildRank = 0

        illegalMove = False

        p1Last = 0
        p2Last = 0

        for spot in cardSpots:
            spot.removeCard()
            

        
        #clearing the hands, piles, etc.
        player1.clearEverything()
        player2.clearEverything()

        #switching who is dealer
        oneWasDealer = player1.dealer
        
        if oneWasDealer:
            player1.dealer = False
            player2.dealer = True
        else:
            player1.dealer = True
            player2.dealer = False

        gameState.clear()
        gameState.prep = True


    if gameState.roundOver:
        buildRoundScore(player1, player2)
        

    if gameState.gameOver:
        player1.totalPoints += player1.calculatePoints()
        player2.totalPoints += player2.calculatePoints()
        buildGameScore(player1, player2)

        gameState.clear()
        if player1.totalPoints < 21 and player2.totalPoints < 21:
            gameState.newGame = True
        else:
            for spot in cardSpots:
                spot.removeCard()
            gameState.waitRO = True

        
    else:
        buildNametags()
        paintAllCards()


    if gameState.displayCM: #here is when we actually execute the move
        if computerMoveType == "Discard":
            computerMove = Discard(table, tup[0], player2, player1)
            discardUI(tup[0])
        elif computerMoveType == "Take":
            computerMove = Take(table, tup[0], player2, player1, tup[1], tup[2])
            takeFromTableUI(tup[0], tup[1]) #hand card, table card list
            if tup[2] > 0:
                takeBuildUI(tup[2])
                for i in range(4): #reset this build spot to have nothing in it.
                    if buildRankDict[i] == tup[2]:
                        buildRankDict[i] = 0
            
            if handNumber == 5:
                p2Last = turnNumber

        else:
            computerMove = Build(table, tup[0], player2, player1, tup[1], tup[2])
            if tup[2] not in buildRankDict.values(): #create the build in the dictionary if its new
                for i in range(4): 
                    if buildRankDict[i] == 0:
                        buildRankDict[i] = tup[2]
                        break
                addToBuildUI(tup[0], tup[1], tup[2])
                buildRank = 0

            if handNumber == 5:
                p2Last = turnNumber

        computerMove.execute()
        for spot in cardSpots:
            spot.unselect()

    if  gameState.computerMove:
            computerMoveType, tup = getComputerMove(player2, player1, table)
            toSelect = [tup[0]]+tup[1]
            if tup[2] > 0 and tup[2] in table.builds:
                toSelect += table.builds[tup[2]]
            for spot in cardSpots:
                if spot.card in toSelect:
                    spot.select()
                if spot.card == tup[0]:
                    spot.side = "Front"
                
            firstTime = False
            
            gameState.clear()
            gameState.waitCM2 = True



#----------- going through the mouse clicks and key presses -------------#    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()



        if gameState.gettingMove:
            if (event.type == KEYDOWN and event.key == K_d):
                moveType = "Discard"
                illegalMove = False
            elif (event.type == KEYDOWN and event.key == K_t):
                moveType = "Take"
                illegalMove = False
            elif (event.type == KEYDOWN and event.key == K_b):
                moveType = "Build"
                illegalMove = False



            elif (event.type == KEYUP and (event.key == K_KP_ENTER or event.key == K_RETURN)):                
                cardPlayed = getCard()
                if cardPlayed == None:
                    illegalMove = "noHandCard"

                else:
                    if moveType == "Discard":
                        move = Discard(table, cardPlayed, player1, player2)

                    elif moveType == "Take":
                        tableCardList = getTableCards()
                        buildTaken = getSelectedBuildRank()          

                        if tableCardList == [] and buildTaken == 0: #if they didn't select any cards to take
                            illegalMove = "noTableCards"
                        else:
                            move = Take(table, cardPlayed, player1, player2, tableCardList, buildTaken)
                            
                            if handNumber == 5:
                                p1Last = turnNumber

                    elif moveType == "Build":
                        tableCardList = getTableCards()
##
##                        if tableCardList == []: #if they didn't select any cards to take
##                            illegalMove = "noTableCards"
                        if True:
                            if buildRank == 0:
                                illegalMove = "noBuildRank"
                            else:
                                move = Build(table, cardPlayed, player1, player2, tableCardList, buildRank)

                                if handNumber == 5:
                                    humanPlayerLast = turnNumber                    
                        
                    if moveType != None and illegalMove == False:
                        if move.legal():
                            if moveType == "Discard":
                                discardUI(cardPlayed)
                            elif moveType == "Take":
                                takeFromTableUI(cardPlayed, tableCardList)
                                if buildTaken > 0:
                                    takeBuildUI(buildTaken)
                                    for i in range(4): #reset this build spot to have nothing in it.
                                        if buildRankDict[i] == buildTaken:
                                            buildRankDict[i] = 0
                            elif moveType == "Build":
                                if buildRank not in buildRankDict.values(): #create the build in the dictionary if its new
                                    for i in range(4): 
                                        if buildRankDict[i] == 0:
                                            buildRankDict[i] = buildRank
                                            break
                                addToBuildUI(cardPlayed, tableCardList, buildRank)
                                buildRank = 0
                                buildChoicesDict = updatedBuildChoicesDict(player1)

                            move.execute()

                            gameState.clear()

                            if turnNumber == 7:
                                gameState.waitP = True
                                turnNumber = 0
                                if handNumber == 5:
                                    gameState.clear()
                                    gameState.last = True
                                else:
                                    handNumber += 1
                            else:
                                turnNumber += 1
                                gameState.waitCM = True
                            
                        else:
                            illegalMove = "badMath"
                            
                    if moveType == None:
                        illegalMove = "noMoveType"
                for spot in cardSpots:
                    spot.unselect()
                moveType = None
                buildChoicesDict = updatedBuildChoicesDict(player1)


                        
            
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                spot = spotFromCoordinates(mousex, mousey)
                if spot != None:
                    if spot.card != None:
                            illegalMove = False
                            if spot.selected == True:
                                spot.unselect()
                            else:
                                spot.select()
                else:
                    buildChoiceSpot = buildFromCoordinates(mousex, mousey)
                    if buildChoiceSpot != None:
                        if buildChoiceSpot in buildChoicesDict.keys():
                            if buildChoicesDict[buildChoiceSpot] != None:
                                buildRank = buildChoicesDict[buildChoiceSpot]
                        
    pygame.display.update()
