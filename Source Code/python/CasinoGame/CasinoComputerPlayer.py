### ------- Computer Player (how to know which move to make) -------- ###

import itertools
from CasinoLogic import multiplesCheck

##TO DO##
#-Allow the computer to build
#-Have the computer think ahead, like throwing a 4 if you have another 4 to take it with
#-Have the computer be smart about LAST (ex. holding on to face cards until the end)


def cardsValue(cardList): #counts up how valuable a list of cards would be if you took it
    points = 0
    for card in cardList:
        points += 0.111 #just for being a card  -->  3/27 because 27 cards gets you 3 points
        if card.suit == "s":
            points += 0.143 # --> 1/7 because 7 spades gets you 1 point
            if card.rank == 2:
                points += 1
        elif card.suit == "d" and card.rank == 10: #the big casino
            points += 2
        if card.rank == 1: #the little casino
            points += 1
    return points

def discardValue(card): #if you're trying to decide what card to discard, use this to find out what a card's value is, and then minimize over it
    return cardsValue([card])

def getComputerMove(player, otherPlayer, table):
    ###this function returns a tuple with (0) the type of move followed by (1) a tuple with:
    ###(0) the card to be played from the hand
    ###(1) the list of cards from the table to play
    ###(2) what build, if any, is involved
    
    discardChoices = player.hand[:] #you could discard any card in your hand
    takeChoices = {} #this will get populated with different possibilities for what to take
    buildChoices = {}
    buildRank = 0
    
    allCardCombinations = []
    for i in range(1,len(table.availableCards())+1):
        allCardCombinations += list(itertools.combinations(table.availableCards(),i))


##------------ Populating the takeChoices dictionary -----------##
        
    takePossible = False #if this stays False, we'll discard

    for card in player.hand: #here we go through each card in the hand to see what cards from the table it could take
        takeChoices[card] = []
        cardCanTake = False
        for combination in allCardCombinations:
            if multiplesCheck(card.rank, list(combination)): #if that combination would be a legal move to take with a card of this rank
                takeChoices[card].append(list(combination)) #put it in the list
                takePossible = True #which means we can take (don't have to discard)...
                cardCanTake = True #...and more specifically: that card from the hand can take
                
        if card.rank in table.builds.keys(): #if the card from the hand is the same rank as something currently being built
            cardCanTake = True #we could take it
            takePossible = True
            takeChoices[card].append([]) #put another move into the list of ways to take cards with this card
                                        #its empty for now because each possiblity will get the build added to it
                                        #so there will be one take choice that is just taking the build
            for combo in takeChoices[card]:
                combo += table.builds[card.rank]

        if cardCanTake == False:
            del takeChoices[card] #we can get rid of the blank dictionary entry if it turns out that card couldn't actually take anything


##------------ Populating the buildChoices dictionary -----------##

    buildPossible = False #if this stays False, we'll discard

    if len(player.hand) > 1: #you can't build unless you have another card to take with!
        for card in player.hand: #this will be the card to take with next time
            if card.rank <= 10 and card.rank not in otherPlayer.currentBuilds:
                buildChoices[card] = []
                cardCanTakeBuild = False
                otherCardsList = player.hand[:]
                otherCardsList.remove(card)
                for combination in allCardCombinations:               
                    for otherCard in otherCardsList: #the other card from your hand has to be in the resulting build                
                        if multiplesCheck(card.rank, list(combination)+[otherCard]): #if that combination would be a legal build to take with a card of this rank
                            buildChoices[card].append(list(combination)+[otherCard]) #put it in the list (with the card to actually play this time at the end
                            buildPossible = True #which means we can build (don't have to discard)...
                            cardCanTakeBuild = True
                        
                if card.rank in player.currentBuilds: #if we're already building to that
                    for c in otherCardsList:
                        if c.rank == card.rank: #if there's a second card of this rank still in your hand
                            cardCanTakeBuild = True
                            buildChoices[card].append([c]) #you could just add that to the build

                #if card.rank > 10 or card.rank in otherPlayer.currentBuilds:
#                    if card.rank in otherPlayer.currentBuilds:
#                        print "i fixed this bug!"
#                    cardCanTakeBuild = False
                if cardCanTakeBuild == False:
                    del buildChoices[card] #we can get rid of the blank dictionary entry if it turns out that card couldn't actually take a build of anything


##------------ Deciding what move to do -----------##


    if takePossible: #if we can take cards, first figure out what the best way to take cards is
        flattenedTakeChoices = []
        for Hcard in takeChoices.keys(): #of all the cards you can take with,
            for combo in takeChoices[Hcard]: #for each set of table cards that was takeable,
                flattenedTakeChoices.append([Hcard]+combo) #make a new list that has all of those table cards plus the card from your hand
                                                            #because this is the entire set that will get added to our pile, so we want to maximize those points 
        bestTakeMove = max(flattenedTakeChoices, key=cardsValue)

    if buildPossible: #if we can build something, figure out which build is best
        flattenedBuildChoices = []
        for Hcard in buildChoices.keys(): #of all the cards you can take a future build with
            for combo in buildChoices[Hcard]: #for each set of table cards that was buildable,
                flattenedBuildChoices.append([Hcard]+combo) #make a new list that has all of those table cards plus the card from your hand
                                                            #because this is the entire set that will get added to our pile next turn, so we want to maximize those points 
        bestBuildMove = max(flattenedBuildChoices, key=cardsValue)

    buildBetter = False
    takeBetter = False

    
    if buildPossible and takePossible:
        if cardsValue(bestBuildMove) > cardsValue(bestTakeMove):
            buildBetter = True
        else:
            takeBetter = True


    if takePossible and not buildPossible or takeBetter:
        if bestTakeMove[0].rank in table.builds.keys():
            buildRank = bestTakeMove[0].rank
        return ("Take", (bestTakeMove[0], [i for i in bestTakeMove if i in table.availableCards()], buildRank)) #move[0] is the card from the hand
                                                                                                #the list comprehension makes sure to leave out the build cards
    elif buildPossible and not takePossible or buildBetter:
        buildRank = bestBuildMove[0].rank
        return ("Build", (bestBuildMove[-1], [i for i in bestBuildMove[1:] if i in table.availableCards()], buildRank)) #move[-1] is the card from the hand to play this turn
                                                        #the list comprehension makes sure to leave out the build cards and the card to take with next time        
        
    else:
        return ("Discard", (min(discardChoices, key=discardValue), [],0)) #discard the least valuable card


