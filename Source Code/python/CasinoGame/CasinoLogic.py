### ------- Logic (just the game, no graphics) ------- ###

import random
import itertools

##TO DO##
#-Make the Move class less messy

suits = ["c","s","h","d"]

class Card():
        def __init__(self, rank, suit):
                self.rank = rank
                self.suit = suit
                if rank > 9: #I don't think I actually use this later on, but it could maybe be helpful if I were to make another card game using these classes
                        self.faceCard = True
                else:
                        self.faceCard = False

                
class Deck():
        def __init__(self):
                self.remaining = [] #what cards are left, haven't been dealt yet
                for s in suits: #populating the deck with 52 cards
                        for i in range(1, 14):
                                self.remaining.append(Card(i, s))
                self.played = [] #what cards have already been played

        def shuffle(self):
                random.shuffle(self.remaining)

        def draw(self):
                if self.count() == 0:
                        return "Sorry, your deck is empty, there are no cards to be drawn." #this shouldn't happen in Casino
                drawnCard = self.remaining.pop() #draw a card, taking it out of the list of remaining cards
                self.played.append(drawnCard) #and put it into the list of already played cards
                return drawnCard

        def count(self): #if you wanted to know how many cards were left (also not used in Casino)
                return len(self.remaining)


class Player():

        def calculatePoints(self): #to calculate points at the end of a round
                #note: this doesn't directly add the points to your total points, you have to do that yourself.
                points = 0

                #most cards#
                if len(self.pile) > 26:
                        points += 3
                elif len(self.pile) == 26:
                        points += 1.5

                #most spades#
                spadeCount = 0
                for card in self.pile:
                        if card.suit == "s":
                                spadeCount += 1
                if spadeCount > 6:
                        points += 1

                #Aces, big casino, little casino
                for card in self.pile:
                        if card.rank == 1:
                                points += 1
                        elif card.rank == 2 and card.suit == "s":
                                points += 1
                        elif card.rank == 10 and card.suit == "d":
                                points += 2

                return points

        def clearEverything(self): #at the end of a game, to clear your hand, builds, and pile (in case it wasn't already done)
                self.hand = []
                self.currentBuilds = []
                self.pile = []


class ComputerPlayer(Player):
        def __init__(self, dealer):
                self.name = "The Computer"
                self.side = "top" #always put the computer player on the top of the screen so you can be on the bottom
                self.dealer = dealer #True or False for whether the computer is the dealer or not
                self.hand = [] #a list of cards currently in the player's hand
                self.currentBuilds = [] #a list of numbers representing the ranks of builds being built
                self.pile = [] #the cards they've collected
                self.totalPoints = 0


class HumanPlayer(Player):
        def __init__(self, dealer, name):
                self.name = name #for displaying the score
                self.dealer = dealer #True or False
                self.side = "bottom" #a human player should always show up on what is the bottom of their screen....not sure what I'll do for two human players
                self.hand = [] #a list of cards currently in the player's hand
                self.currentBuilds = [] #a list of numbers representing the ranks of builds being built
                self.pile = [] #the cards they've collected
                self.totalPoints = 0



class Table():
        def __init__(self):
                self.allCards = []
                self.builds = {} #format: key: 7, value: [card, card, card]

        def availableCards(self): #all cards not currently captured in builds
                #I made this a method instead of an attribute because it has to change when allCards changes all the time
                captured = []
                for builds in self.builds.values():
                        captured += builds

                availableCards = []
                for card in self.allCards:
                        if card not in captured:
                                availableCards.append(card)
                
                return availableCards   

        def removeCard(self, card):
                self.allCards.remove(card)
                
        def removeBuild(self, rank):
                for card in self.builds[rank]:
                        self.allCards.remove(card)
                del self.builds[rank]
                


### Move classes & subclasses ### -> 4 types of moves: Discard, Take, Build, TakeLastCards


def multiplesCheck(rank, cards): #this checks if a set of cards could be legaly taken by a card of rank "rank"
        if rank > 10: #face cards can only take other cards of the same rank (but as many as they want)
            for card in cards:
                if card.rank != rank:
                    return False
            return True

        #for non-face cards, I'm going to use "set" to discribe a group of cards who, together, add up to exactly the rank
        maxLen = min(rank, len(cards)) #no set can be bigger than how many cards there are or how high the rank is (imagine all aces)
        size = 1 #what size set to look for adding up to rank. this will increase, but we need to start looking from the smallest size sets
        #because otherwise we risk things like using up all the small cards and leaving big cards that can't combine, even though the player could make it work
        cardsLeft = cards[:] #these two lists add up to the original card list, we're done when there are no cards left
        setsDone = []
        while len(cardsLeft) >= size:
                possibilities = list(itertools.combinations(cardsLeft, size))
                found = False
                for choice in possibilities:
                        group = list(choice) #wtf was happening?? choice was a list too but I couldn't use it and had to make group...
                        groupRanks = [card.rank for card in group]
                        if sum(groupRanks) == rank:
                                setsDone.append(group) #put all the cards in this set into setsDone
                                for i in range(len(group)):
                                        cardsLeft.remove(group[i]) #and delete them all from cardsLeft
                                found = True #this tells us we found a set of length size, and now we'll go back up to the while loop and look for another one of the same size
                                break #we have to break out of the for loop though, because the next choice in possibilities could have some overlapping cards with what we just removed from cardsLeft
                if found == False: #if we didn't find anything after going through the whole for loop, we have to try for sets with more cards
                    size +=1

        #we get here when the while loop breaks because cardsLeft is smaller than the setsize we're looking for...
        if len(cardsLeft) == 0: #either because there are no cards left (yay!)
                return True
        else: #or because we can't find any sets among the cards left
                return False




class Move():
        #this class is a mess..... because there are so many arguments being passed in and its hard to remember what to put where. Ideas:
        #-make it so that you have to pass it in as player="Alicia", otherPlayer="Computer"
        #-put these all inside of Player so that you don't have to pass in player and other player
        #-is it silly to make a class and only have an init function? should I restructure all of it?
        
        def __init__(self, currentTable, cardPlayed, player, otherPlayer, tableCards=[], buildRank=0):
                self.currentTable = currentTable
                self.cardPlayed = cardPlayed
                self.player = player
                self.otherPlayer = otherPlayer
                self.tableCards = tableCards #this is a list of all of the cards
                        #to be involved in the move that are already on the table,
                        #it would be empty on a discard move
                        #cards in a build on the table are figured out elsewhere based on the build's rank
                self.buildRank = buildRank #the rank of the build to either be taken or built (I should probably split these up??)

class TakeLastCards(Move):
    def execute(self):
        for card in self.currentTable.allCards:
            self.player.pile.append(card)
        for card in self.currentTable.allCards: #Question: why couldn't I do this all at once? When I tried it didn't get them all...
            self.currentTable.removeCard(card)

class Discard(Move):
        def execute(self):
                self.currentTable.allCards.append(self.cardPlayed)
                self.player.hand.remove(self.cardPlayed)

        def legal(self):
                if len(self.player.currentBuilds) == 0: #can't discard if you're building something
                        return True
                return False

class Take(Move):
        def execute(self):
                for card in self.tableCards:
                        self.currentTable.allCards.remove(card)
                        self.player.pile.append(card)

                self.player.hand.remove(self.cardPlayed)
                self.player.pile.append(self.cardPlayed)
                
                if self.buildRank != 0: #if we're also taking a build
                    for card in self.currentTable.builds[self.buildRank]:
                            self.player.pile.append(card) #put them in your pile
                    if self.buildRank in self.player.currentBuilds:
                        self.player.currentBuilds.remove(self.buildRank) #and take them out of your list of current builds (to free you up to discard)
                    else:
                        self.otherPlayer.currentBuilds.remove(self.buildRank) #or if you're stealing it from the other player, take it out of their list
                    self.currentTable.removeBuild(self.buildRank)   

        def legal(self):
            #first, make sure playing this card won't stop you from taking any builds you've made and are leaving on the table
            handRanksLeft = [card.rank for card in self.player.hand if card != self.cardPlayed] #list of the ranks left in the hand

            #player's builds that'll be left on the table after this turn            
            if self.buildRank == 0 or self.buildRank not in self.player.currentBuilds:
                    buildsLeft = self.player.currentBuilds[:]
            else:
                if self.buildRank in self.player.currentBuilds:
                    buildsLeft = self.player.currentBuilds[:].remove(self.buildRank)

            if buildsLeft != [] and buildsLeft != None:
                    for buildRank in buildsLeft: #if the card you're taking with (same as buildRank) is one of the builds you're leaving on the table,
                        if buildRank not in handRanksLeft: #there better be another one of that card left in your hand.
                            return False

            #next, checking that the math is correct   
            if self.buildRank > 0:
                buildCardsTaken = self.currentTable.builds[self.buildRank]
            else:
                buildCardsTaken = []
            return multiplesCheck(self.cardPlayed.rank, self.tableCards+[self.cardPlayed]+buildCardsTaken) #I'm not sure I needed to put self.cardPlayed in here....


class Build(Move):                               
        def legal(self):
            #first, make sure playing this card won't stop you from taking any builds you've made and are leaving on the table
            handRanksLeft = [card.rank for card in self.player.hand if card != self.cardPlayed] #list of the ranks left in the hand
            buildsLeft = self.player.currentBuilds[:]+[self.buildRank] #player's builds that'll be left on the table after this turn (its okay to add in self.buildRank twice if it has already been built) 
            for buildRank in buildsLeft:
                if buildRank not in handRanksLeft:
                    return False

            #second, don't let anyone build something that's just one card (although you can add just one card)
            if self.buildRank not in self.player.currentBuilds and self.tableCards == []:
                return False

            #third, check that the math is correct
            return multiplesCheck(self.buildRank, self.tableCards+[self.cardPlayed]) #here the self.cardPlayed definitely is necessary


        def execute(self):
                if self.buildRank not in self.player.currentBuilds: #for if its a new build
                    self.player.currentBuilds.append(self.buildRank) #add it to the player's list of current builds
                    self.currentTable.builds[self.buildRank] = [] #start the build in the table

                self.currentTable.builds[self.buildRank] += self.tableCards[:]+[self.cardPlayed] #put your card and all the newly captured cards into the build
                self.currentTable.allCards.append(self.cardPlayed) #add your card to the table
                self.player.hand.remove(self.cardPlayed) #and take it out of your hand
                


def rankChoices4Build(player): #returns which ranks a player could build to based on what is in their hand
    choices = set()
    for card in player.hand:
        if card.rank < 11: #you can't build to face cards
            choices.add(card.rank)
    return list(choices)
    
