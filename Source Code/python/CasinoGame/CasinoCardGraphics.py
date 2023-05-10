### ------- Card Graphics (ex. loading the images, taking cards off the table, putting them in the right spot, etc.) ------- ###

import pygame, sys
from pygame.locals import *
from CasinoVariables import w, buildRankDict
from CasinoBoardGraphics import BLACK, WHITE, RED, GREEN, BLUE, BEIGE, YELLOW 


##TO DO##
#-display all of the cards that you and the other player took at the end like how I sort out my cards when playing with physical cards
#-don't let one player select another player's cards
#-QUESTION: can I use window in this file? or does it have to be in the same file as where the window is created??

path = ''
#load all of the card images
c1 = pygame.image.load(path+'c1.png')
s1 = pygame.image.load(path+'s1.png')
h1 = pygame.image.load(path+'h1.png')
d1 = pygame.image.load(path+'d1.png')
c2 = pygame.image.load(path+'c2.png')
s2 = pygame.image.load(path+'s2.png')
h2 = pygame.image.load(path+'h2.png')
d2 = pygame.image.load(path+'d2.png')
c3 = pygame.image.load(path+'c3.png')
s3 = pygame.image.load(path+'s3.png')
h3 = pygame.image.load(path+'h3.png')
d3 = pygame.image.load(path+'d3.png')
c4 = pygame.image.load(path+'c4.png')
s4 = pygame.image.load(path+'s4.png')
h4 = pygame.image.load(path+'h4.png')
d4 = pygame.image.load(path+'d4.png')
c5 = pygame.image.load(path+'c5.png')
s5 = pygame.image.load(path+'s5.png')
h5 = pygame.image.load(path+'h5.png')
d5 = pygame.image.load(path+'d5.png')
c6 = pygame.image.load(path+'c6.png')
s6 = pygame.image.load(path+'s6.png')
h6 = pygame.image.load(path+'h6.png')
d6 = pygame.image.load(path+'d6.png')
c7 = pygame.image.load(path+'c7.png')
s7 = pygame.image.load(path+'s7.png')
h7 = pygame.image.load(path+'h7.png')
d7 = pygame.image.load(path+'d7.png')
c8 = pygame.image.load(path+'c8.png')
s8 = pygame.image.load(path+'s8.png')
h8 = pygame.image.load(path+'h8.png')
d8 = pygame.image.load(path+'d8.png')
c9 = pygame.image.load(path+'c9.png')
s9 = pygame.image.load(path+'s9.png')
h9 = pygame.image.load(path+'h9.png')
d9 = pygame.image.load(path+'d9.png')
c10 = pygame.image.load(path+'c10.png')
s10 = pygame.image.load(path+'s10.png')
h10 = pygame.image.load(path+'h10.png')
d10 = pygame.image.load(path+'d10.png')
c11 = pygame.image.load(path+'c11.png')
s11 = pygame.image.load(path+'s11.png')
h11 = pygame.image.load(path+'h11.png')
d11 = pygame.image.load(path+'d11.png')
c12 = pygame.image.load(path+'c12.png')
s12 = pygame.image.load(path+'s12.png')
h12 = pygame.image.load(path+'h12.png')
d12 = pygame.image.load(path+'d12.png')
c13 = pygame.image.load(path+'c13.png')
s13 = pygame.image.load(path+'s13.png')
h13 = pygame.image.load(path+'h13.png')
d13 = pygame.image.load(path+'d13.png')
back = pygame.image.load(path+'back.png')

cardImageNames = {'c1': c1, 's1': s1, 'h1': h1, 'd1': d1, 'c2': c2, 's2': s2, 'h2': h2, 'd2': d2,
                  'c3': c3, 's3': s3, 'h3': h3, 'd3': d3, 'c4': c4, 's4': s4, 'h4': h4, 'd4': d4,
                  'c5': c5, 's5': s5, 'h5': h5, 'd5': d5, 'c6': c6, 's6': s6, 'h6': h6, 'd6': d6,
                  'c7': c7, 's7': s7, 'h7': h7, 'd7': d7, 'c8': c8, 's8': s8, 'h8': h8, 'd8': d8,
                  'c9': c9, 's9': s9, 'h9': h9, 'd9': d9, 'c10': c10, 's10': s10, 'h10': h10, 'd10': d10,
                  'c11': c11, 's11': s11, 'h11': h11, 'd11': d11, 'c12': c12, 's12': s12, 'h12': h12, 'd12': d12,
                  'c13': c13, 's13': s13, 'h13': h13, 'd13': d13}


#this is the top left corner coordinates of each card spot#
cardLocations = {"mh1": (24*15, 24*24), "mh2": (24*19, 24*24), "mh3": (24*23,24*24), "mh4": (24*27,24*24),

                 "yh1": (24*15, 24), "yh2": (24*19, 24), "yh3": (24*23,24), "yh4": (24*27,24),

                 "t1": (24*19,24*12), "t2": (24*15,24*12), "t3": (24*11,24*12), "t4": (24*7,24*12),
                 "t5": (24*21,24*7), "t6": (24*17,24*7), "t7": (24*13,24*7), "t8": (24*9,24*7),"t9": (24*5,24*7),
                 "t10": (24*21,24*17), "t11": (24*17,24*17), "t12": (24*13,24*17), "t13": (24*9,24*17), "t14": (24*5,24*17),

                 "bA1": (24*25,24*9), "bA2": (24*25,24*10), "bA3": (24*25,24*11), "bA4": (24*25,24*12), "bA5": (24*25,24*13),
                 "bA6": (24*25,24*14), "bA7": (24*25,24*15), "bA8": (24*25,24*16), "bA9": (24*25,24*17), "bA10": (24*25,24*18),

                 "bB1": (24*29,24*9), "bB2": (24*29,24*10), "bB3": (24*29,24*11), "bB4": (24*29,24*12), "bB5": (24*29,24*13),
                 "bB6": (24*29,24*14), "bB7": (24*29,24*15), "bB8": (24*29,24*16), "bB9": (24*29,24*17), "bB10": (24*29,24*18),

                 "bC1": (24*33,24*9), "bC2": (24*33,24*10), "bC3": (24*33,24*11), "bC4": (24*33,24*12), "bC5": (24*33,24*13),
                 "bC6": (24*33,24*14), "bC7": (24*33,24*15), "bC8": (24*33,24*16), "bC9": (24*33,24*17), "bC10": (24*33,24*18),

                 "bD1": (24*37,24*9), "bD2": (24*37,24*10), "bD3": (24*37,24*11), "bD4": (24*37,24*12), "bD5": (24*37,24*13),
                 "bD6": (24*37,24*14), "bD7": (24*37,24*15), "bD8": (24*37,24*16), "bD9": (24*37,24*17), "bD10": (24*37,24*18)}


locationOrder = ["mh1","mh2","mh3","mh4","yh1","yh2","yh3","yh4",
                 "t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12","t13","t14",
                 "bA1","bA2","bA3","bA4","bA5","bA6","bA7","bA8","bA9","bA10",
                 "bB1","bB2","bB3","bB4","bB5","bB6","bB7","bB8","bB9","bB10",
                 "bC1","bC2","bC3","bC4","bC5","bC6","bC7","bC8","bC9","bC10",
                 "bD1","bD2","bD3","bD4","bD5","bD6","bD7","bD8","bD9","bD10"]


#each cardSpot object is one of the 61 spots that a card could be in on the board. they contain info on what card is in that spot, etc.
class cardSpot():
    def __init__(self, name, side="Front"):
        self.name = name #string to describe the spot
        self.location = cardLocations[name]
        self.side = side #front or back (only back for the other player's cards
        self.card = None #all spots start empty, but you can put one card in each spot using the assignCard method
        self.selected = False #helps to tell which table cards are going to be played as well as where to put a yellow outline

    def assignCard(self, card): #put a card into that spot (such as when dealing, making a build, or discarding)
        self.card = card

    def removeCard(self): #taking the card out of that spot (like when playing from your hand, or taking)
        self.card = None
        self.selected = False #you don't want a yellow outline around nothing!

    def select(self):
        #only lets you select if its a face-up card that exists on the board
        if self.card != None and self.side != "Back":
            
            #if it is in my hand, selecting this card unselects the rest of them, because you can only play one card at once
            if self.name[0] == "m":
                for spot in cardSpots[:4]:
                    spot.selected = False
            elif self.name[0] == "b": #if it is in a build, select everything in the build at once
                if self.name[1] == "A":
                    i = 22
                elif self.name[1] == "B":
                    i = 32
                elif self.name[1] == "C":
                    i = 42
                elif self.name[1] == "D":
                    i = 52
                for spot in cardSpots[i:i+10]:
                    if spot.card != None:
                            spot.selected = True


        self.selected = True #select this card

    def unselect(self):
        self.selected = False
        if self.name[0] == "b": #turning everything in the build unselected at once
                if self.name[1] == "A":
                    i = 22
                elif self.name[1] == "B":
                    i = 32
                elif self.name[1] == "C":
                    i = 42
                elif self.name[1] == "D":
                    i = 52
                for spot in cardSpots[i:i+10]:
                    if spot.card != None:
                            spot.selected = False


#makes a list that contains all of the cardSpot objects. *this is a big, important list*
cardSpots = [cardSpot(name) for name in locationOrder]    
for i in range(4,8): #the other player's cards should be face down
    cardSpots[i].side = "Back"


def spotFromCoordinates(x, y): #how to tell what spot was clicked by the mouse coordinates
    for spot in cardSpots:
        if (spot.location[0] < x < spot.location[0]+24*3) and (spot.location[1] < y < spot.location[1]+24*4):
            return spot
    return None #if it was just a random place on the board, not a spot


###-- functions that place cards on and off the table (partners with the move classes from the game logic) --###

#list of what rank is being built in each of the four spots
#buildRankDict = {0: 0 , 1: 0, 2: 0, 3: 0} ### where do these get assigned? ###

def playCardUI(card):
    #find the card that was played from one of the two player's hands, remove it.
    #this happens every turn, regardless of the play, and is incorporated in the other functions
    for spot in cardSpots[:8]:
        if spot.card == card:
            spot.removeCard()

def dealToTableUI(initialDealList): #this gets called once at the beginning of each game, just on the first hand
    for i in range(4):
          cardSpots[i+8].assignCard(initialDealList[i])

def discardUI(card):
    #this adds the discarded card onto the table in the first available spot, and takes the card out of your hand
    playCardUI(card) #first, take it out of your hand
    for spot in cardSpots[8:22]:
        if spot.card == None:
            spot.assignCard(card)
            break

def takeFromTableUI(cardPlayed, cardList): #this gets rid of the cards you took and your card (which go into your pile in the logic section)
    playCardUI(cardPlayed)
    for card in cardList:
        for spot in cardSpots[8:]:
            if spot.card == card:
                spot.removeCard()

def addToBuildUI(cardPlayed, cardList, rank):
    takeFromTableUI(cardPlayed, cardList) #take the cards that'll be involved off of the general table (in the process, it also takes the card played out of your hand)
    for rankSpot in buildRankDict.keys():
        if buildRankDict[rankSpot] == rank: #figure out what spot to put it all into
            if rankSpot == 0:
                j = 0
            elif rankSpot == 1:
                j = 10
            elif rankSpot == 2:
                j = 20
            elif rankSpot == 3:
                j = 30

    toBePlaced = cardList+[cardPlayed]
    for spot in cardSpots[j+22:j+32]: #put all of the cards into the build spot
        if spot.card == None:
            spot.assignCard(toBePlaced.pop())
            if len(toBePlaced) == 0:
                break
    

def takeBuildUI(rank): #sometimes this will get called at the same time as takeFromTableUI if you're taking lots of different stuff at once
    for i in range(4):
        if buildRankDict[i] == rank: #find the space on the board where this build lives
            if i == 0:
                j = 0
            elif i == 1:
                j = 10
            elif i == 2:
                j = 20
            elif i == 3:
                j = 30
    for spot in cardSpots[j+22:j+32]:
        spot.removeCard()


    
def populateHandsUI(player1, player2):
    #only to be called at the beginning of a hand when the two players get dealt
    #this puts the cards that are newly in player1 and 2's hands into the cardSpots list

    #to determine whose hand to put the cards in
    for player in [player1, player2]:
        if player.side == "top":
            j = 4
        else:
            j = 0
            
        for i in range(4):
            cardSpots[j+i].assignCard(player.hand[i])
            if player.side == "top":
                cardSpots[j+i].side = "Back"

def selectLastCardsUI(player, window=w): #at the end of the last hand, select all of the cards left
    for cardSpot in cardSpots[8:22]:
        if cardSpot != None:
            cardSpot.select()

    #this makes a rectangle on the board telling who gets the last cards
    pygame.draw.rect(window, BLUE, (24*27, 24*11.5, 24*13, 24*5))
    insFont = pygame.font.Font('freesansbold.ttf', 22)
    ins1 = insFont.render(player.name+" was the", True, BEIGE, BLUE)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.topleft = (24*28,24*12)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render("last to take cards,", True, BEIGE, BLUE)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.topleft = (24*28,24*13)
    window.blit(ins2, ins2RectObj)

    ins3 = insFont.render("and therefore wins", True, BEIGE, BLUE)
    ins3RectObj = ins3.get_rect()
    ins3RectObj.topleft = (24*28,24*14)
    window.blit(ins3, ins3RectObj)

    ins4 = insFont.render("all of the cards left.", True, BEIGE, BLUE)
    ins4RectObj = ins4.get_rect()
    ins4RectObj.topleft = (24*28,24*15)
    window.blit(ins4, ins4RectObj)



## drawing the cards into the screen ##

def paintCard(card, loc, window=w): #I named it paint just to not confuse this with drawing (as in taking) a card from a deck
    window.blit(cardImageNames[card.suit+str(card.rank)],loc)                


def paintAllCards(window=w):
    for spot in cardSpots:
        if spot.card != None:
            if spot.selected:
                pygame.draw.rect(window, YELLOW, (spot.location[0]-6, spot.location[1]-6, 24*3+12, 24*4+12))
            if spot.side == "Back":
                window.blit(back, spot.location)
            else:
                paintCard(spot.card, spot.location)

#to tell you what the rank of each build on the table is
def buildNametags(window=w):
    for i in range(4):
        if buildRankDict[i] != 0:
            nametag = pygame.font.Font('freesansbold.ttf', 18)
            tag = nametag.render("Build: "+str(buildRankDict[i]), True, BEIGE, GREEN)
            tagRectObj = tag.get_rect()
            tagRectObj.topleft = ((24*(i*4+25)),24*8)
            window.blit(tag, tagRectObj)


