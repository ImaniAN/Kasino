### ------- Board Graphics (ex. displaying the score, instructions, etc) ------- ###
import pygame, sys
from pygame.locals import *
from CasinoVariables import w
from CasinoLogic import rankChoices4Build


##TO DO##
#-fix buildChoicesDict which sometimes shows too many choices

# set up the colors
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (205, 0, 0)
GREEN =(0, 150, 0)
BLUE =(0, 0, 205)
BEIGE = (255, 255, 204)
YELLOW = (255, 255, 0)


##Unfortunately, I named everything "buildX" which is annyoing because it has nothing to do with the casino concept of building. Maybe I'll change this later.


##def buildNametags(window=w): #to tell you what the rank of each build on the table is
##    for i in range(4):
##        if buildRankDict[i] != 0:
##            nametag = pygame.font.Font('freesansbold.ttf', 18)
##            tag = nametag.render("Build: "+str(buildRankDict[i]), True, BEIGE, GREEN)
##            tagRectObj = tag.get_rect()
##            tagRectObj.topleft = ((24*(i*4+25)),24*8)
##            window.blit(tag, tagRectObj)


def buildScore(playerONE, playerTWO, window=w):
    #who is top and bottom
    if playerONE.side == "top":
        p1 = playerONE
        p2 = playerTWO
    else:
        p1 = playerTWO
        p2 = playerONE

    #write in their current total scores (minus what's in progress in the current game)
    players = [p1, p2]
    scoreFont = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(2):
        score = scoreFont.render(players[i].name+"'s Score: "+str(players[i].totalPoints), True, BLUE, GREEN)
        scoreRectObj = score.get_rect()
        scoreRectObj.topleft = (24*3.5,24*(i*1.5+1.5))
        window.blit(score, scoreRectObj)

    #add in who is the dealer this turn
    if p1.dealer == True:
        d = 0
    else:
        d = 1

    dealerFont = pygame.font.Font('freesansbold.ttf', 13)
    dealer = dealerFont.render("(Dealer)", True, BLUE, GREEN)
    dealerRectObj = dealer.get_rect()
    dealerRectObj.topleft = (24*1.2,24*(d*1.5+1.7))
    window.blit(dealer, dealerRectObj)


def buildGameScore(player1, player2, window=w): #to display the score (briefly) at the end of a game
    pygame.draw.rect(window, BEIGE, (24*14, 24*10, 24*17, 24*7))
    #who is top and bottom
    if player1.side == "top":
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1

    #write in their current total scores
    players = [p1, p2]
    scoreFont = pygame.font.Font('freesansbold.ttf', 30)
    for i in range(2):
        score = scoreFont.render(players[i].name+"'s Score: "+str(players[i].calculatePoints()), True, RED, BEIGE)
        scoreRectObj = score.get_rect()
        scoreRectObj.topleft = (24*14.5,24*(i*2+13))
        window.blit(score, scoreRectObj)

    #displaying who won
    p1Score = p1.calculatePoints()
    p2Score = p2.calculatePoints()
    if p1Score == p2Score:
        result = "It's a tie!"
    elif p1Score > p2Score:
        result = p1.name+" Wins!"
    else:
        result = p2.name+" Wins!"

    win = scoreFont.render(result, True, RED, BEIGE)
    winRectObj = score.get_rect()
    winRectObj.topleft = (24*14.5,24*11)
    window.blit(win, winRectObj)


def buildRoundScore(player1, player2, window=w): #to display the score (briefly) at the end of a game
    pygame.draw.rect(window, RED, (24*14, 24*10, 24*17, 24*7))
    #who is top and bottom
    if player1.side == "top":
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1

    #write in their current total scores
    players = [p1, p2]
    scoreFont = pygame.font.Font('freesansbold.ttf', 30)
    for i in range(2):
        score = scoreFont.render(players[i].name+"'s Score: "+str(players[i].totalPoints), True, BEIGE, RED)
        scoreRectObj = score.get_rect()
        scoreRectObj.topleft = (24*14.5,24*(i*2+13))
        window.blit(score, scoreRectObj)

    #displaying who won
    if p1.totalPoints == p2.totalPoints:
        result = "It's a tie!"
    elif p1.totalPoints > p2.totalPoints:
        result = p1.name+" Wins the round!"
    else:
        result = p2.name+" Wins the round!"

    scoreFont2 = pygame.font.Font('freesansbold.ttf', 24)
    win = scoreFont2.render(result, True, BEIGE, RED)
    winRectObj = score.get_rect()
    winRectObj.topleft = (24*14.5,24*11)
    window.blit(win, winRectObj)


def buildMoveType(moveType, window=w): #shows the move you've selected right above the cards in your hand
        moveTypeFont = pygame.font.Font('freesansbold.ttf', 18)
        moveTypeText = moveTypeFont.render(moveType, True, YELLOW, GREEN)
        moveTypeRect = moveTypeText.get_rect()
        moveTypeRect.center = (540, 552)      
        window.blit(moveTypeText, moveTypeRect)


def buildIllegalMove(illegalMove, window=w): #gives you a hint about why the move you tried to do isn't valid
        if illegalMove == "badMath":
            warning = "That move is illegal, please try again"
        elif illegalMove == "noHandCard":
            warning = "Please play a card from your hand"
        elif illegalMove == "noTableCards":
            warning = "Please select cards from the table"
        elif illegalMove == "noMoveType":
            warning = "Please indicate the type of move"
        elif illegalMove == "noBuildRank":
            warning = "Please select a rank to build to"
        badFont = pygame.font.Font('freesansbold.ttf', 23)
        badText = badFont.render(warning, True, RED, GREEN)
        badRect = badText.get_rect()
        badRect.center = (540, 24*22)      
        window.blit(badText, badRect)

def buildLast(window=w): #writing out LAST to signify that it is the last hand of the game
        lastFont = pygame.font.Font('freesansbold.ttf', 30)
        lastText = lastFont.render("L A S T", True, YELLOW, GREEN)
        lastRect = lastText.get_rect()
        lastRect.center = (540, 24*6)      
        window.blit(lastText, lastRect)

def buildInstructions(window=w): #A little box at the bottom that gives instructions on how to use the keyboard and mouse in this game
    pygame.draw.rect(window, RED, (24*1.7, 24*22.7, 24*11.6, 24*5.3))
    insFont = pygame.font.Font('freesansbold.ttf', 14)
    ins1 = insFont.render("Click on cards from the table and in", True, BEIGE, RED)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.topleft = (24*2,24*23)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render("your hand to select or unselect them.", True, BEIGE, RED)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.topleft = (24*2,24*23.8)
    window.blit(ins2, ins2RectObj)

    ins3 = insFont.render("Type <d> to discard, <t> to take, and", True, BEIGE, RED)
    ins3RectObj = ins3.get_rect()
    ins3RectObj.topleft = (24*2,24*24.6)
    window.blit(ins3, ins3RectObj)

    ins4 = insFont.render("<b> to build. Once you are satisfied", True, BEIGE, RED)
    ins4RectObj = ins4.get_rect()
    ins4RectObj.topleft = (24*2,24*25.4)
    window.blit(ins4, ins4RectObj)

    ins5 = insFont.render("with your move type and selections,", True, BEIGE, RED)
    ins5RectObj = ins5.get_rect()
    ins5RectObj.topleft = (24*2,24*26.2)
    window.blit(ins5, ins5RectObj)

    ins6 = insFont.render("press Enter.", True, BEIGE, RED)
    ins6RectObj = ins6.get_rect()
    ins6RectObj.topleft = (24*2,24*27)
    window.blit(ins6, ins6RectObj)

def textForCard(card): #a function that prints out a word description of the rank and suit of a card
    if card.rank == 1:
        n = "Ace"
    elif card.rank == 11:
        n = "Jack"
    elif card.rank == 12:
        n = "Queen"
    elif card.rank == 13:
        n = "King"
    else:
        n = str(card.rank)

    if card.suit == "c":
        s = "Clubs"
    elif card.suit == "d":
        s = "Diamonds"
    elif card.suit == "h":
        s = "Hearts"
    else:
        s = "Spades"

    return n+" of "+s


def buildComputerMove(tup,moveType, window=w): #Gives a description of the last move a computer made
    if moveType == "Discard":
        first = "The computer discarded:"
        second = textForCard(tup[0])
    elif moveType == "Take":
        first = "The computer took:"
        second = ""
        for card in tup[1]:
            second += textForCard(card)+", "
        if tup[2] > 0:
            second += "the built "+str(tup[2])+"s"
        third = "With the:"
        fourth = textForCard(tup[0])
    else:
        first = "The computer built:"
        second = str(tup[2])+"s"
        third = "By playing the:"
        fourth = textForCard(tup[0])
        
    pygame.draw.rect(window, BEIGE, (24*31, 24*1, 24*11, 24*6))
    insFont = pygame.font.Font('freesansbold.ttf', 18)
    ins1 = insFont.render(first, True, RED, BEIGE)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.center = (24*37,24*2)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render(second, True, RED, BEIGE)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.center = (24*37,24*3)
    window.blit(ins2, ins2RectObj)

    if moveType != "Discard":
        ins3 = insFont.render(third, True, RED, BEIGE)
        ins3RectObj = ins3.get_rect()
        ins3RectObj.center = (24*37,24*5)
        window.blit(ins3, ins3RectObj)

        ins4 = insFont.render(fourth, True, RED, BEIGE)
        ins4RectObj = ins4.get_rect()
        ins4RectObj.center = (24*37,24*6)
        window.blit(ins4, ins4RectObj)


#buildChoicesDict = {} #a dictionary of all of the ranks you could build to, with the keys being the place in the list of choices list (not the same as the spot on the board)
#this should get cleared after each move

def updatedBuildChoicesDict(player):
    d = {}
    x = rankChoices4Build(player)[:] #find out what the player could build to
    x.sort() #put the ranks in order to be prettier
    i = 0
    for rank in x: #make the dictionary
        d[i] = rank
        i += 1
    return d

def buildBuildChoices(player, buildChoicesDict, window=w): #once the player indicates that they want to build, this shows the options of what to build to
##    buildChoicesDict = {}
##    x = rankChoices4Build(player)[:] #find out what the player could build to
##    x.sort() #put the ranks in order to be prettier
##    i = 0
##    for rank in x: #make the dictionary
##        buildChoicesDict[i] = rank
##        i += 1

    #print buildChoicesDict
    
    buildTypeFont = pygame.font.Font('freesansbold.ttf', 23)

    buildTypeFont0 = pygame.font.Font('freesansbold.ttf', 20)
    buildTypeText0 = buildTypeFont0.render("What do you want to build to?", True, BEIGE, GREEN)
    buildTypeRect0 = buildTypeText0.get_rect()
    buildTypeRect0.topleft = (24*31.5,24*23.5)       
    window.blit(buildTypeText0, buildTypeRect0)

    if len(buildChoicesDict) > 0:
        pygame.draw.rect(window, GREEN, (24*33, 24*25, 24*1.3, 24*1))
        buildTypeText = buildTypeFont.render(str(buildChoicesDict[0]), True, BEIGE, GREEN)
        buildTypeRect = buildTypeText.get_rect()
        buildTypeRect.midtop = (24*33.6,24*25)       
        window.blit(buildTypeText, buildTypeRect)

    if len(buildChoicesDict) > 1:
        pygame.draw.rect(window, GREEN, (24*35, 24*25, 24*1.3, 24*1))
        buildTypeText1 = buildTypeFont.render(str(buildChoicesDict[1]), True, BEIGE, GREEN)
        buildTypeRect1 = buildTypeText1.get_rect()
        buildTypeRect1.midtop = (24*35.6,24*25)       
        window.blit(buildTypeText1, buildTypeRect1)

    if len(buildChoicesDict) > 2:
        pygame.draw.rect(window, GREEN, (24*37, 24*25, 24*1.3, 24*1))
        buildTypeText2 = buildTypeFont.render(str(buildChoicesDict[2]), True, BEIGE, GREEN)
        buildTypeRect2 = buildTypeText2.get_rect()
        buildTypeRect2.midtop = (24*37.6,24*25)       
        window.blit(buildTypeText2, buildTypeRect2)

    if len(buildChoicesDict) > 3:
        pygame.draw.rect(window, GREEN, (24*39, 24*25, 24*1.3, 24*1))
        buildTypeText3 = buildTypeFont.render(str(buildChoicesDict[3]), True, BEIGE, GREEN)
        buildTypeRect3 = buildTypeText3.get_rect()
        buildTypeRect3.midtop = (24*39.6,24*25)       
        window.blit(buildTypeText3, buildTypeRect3)

def selectBuildChoice(rank, buildChoicesDict, window=w): #draw a yellow rectangle around the selected build rank
    for key in buildChoicesDict.keys():
        if buildChoicesDict[key] == rank:
            pygame.draw.rect(window, YELLOW, (24*(33+key*2)-6, 24*25-6, 24*1.3+12, 24*1+12))

