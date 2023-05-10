import os

class Print:
    def __init__(self):
        self.invalidVar = "you typed an invalid command" #too many commands, typo
        self.rangeVar = "slow down there buckaroo, that index was out of range" # indexing something that's out of range
        self.illegalVar = "illegal move, you cant do that" #play >1, end too soon, invalid collect, build, quick, take.
        self.errorVar = "there was an error" # something went wrong, general error

    def invalid(self, name):
        print(name + ", " + self.invalidVar)
        os.system("say " + name + ", " + self.invalidVar)
    
    def range(self, name):
        print(name + ", " + self.rangeVar)
        os.system("say " + name + ", " + self.rangeVar)

    def illegal(self, name):
        print(name + ", " + self.illegalVar)
        os.system("say " + name + ", " + self.illegalVar)

    def error(self):
        print(self.errorVar)
        os.system("say " + ", " + self.errorVar)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discard = []
        self.cards = 0
        self.spades = 0
        self.aces = 0
        self.smallCasino = 0
        self.bigCasino = 0
        self.points = 0
        
    def show_points(self):
        print(self.points)
    
    def count(self):
        self.cards = len(self.discard)
        for card in self.discard:
            if card.suit == 'spades' : self.spades += 1 
            if card.value == 1 : self.aces += 1 
            if card.suit == 'spades' and card.value == 2 : self.smallCasino = 1 
            if card.suit == 'diamonds' and card.value == 10 : self.bigCasino = 2 
        
        self.points += (self.aces + self.smallCasino + self.bigCasino)
        return self.cards, self.spades
    
    def handToDiscard(self, indexOne):
        # print(self.hand.pop(indexOne])
        self.discard.append(self.hand.pop(indexOne))


class CenterPile:
    def __init__(self):
        self.pile = [] 
        self.builtValue = 0 
        self.collectValue = self.builtValue
        self.isBuilt = True


class Center:
    def __init__(self):
        self.pile = []

    def buildCards(self, indexOne, indexTwo, player):
        temp = False
        newBuiltValue = (self.pile[indexOne].builtValue + self.pile[indexTwo].builtValue)
        for i in range(len(player.hand)):
            if newBuiltValue == player.hand[i].value:
                temp = True
                break

        if self.pile[indexOne].isBuilt and self.pile[indexTwo].isBuilt and temp:
            for i in range(len(self.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

        
            self.pile[indexTwo].builtValue = newBuiltValue
            self.pile[indexTwo].collectValue = newBuiltValue
            self.pile.pop(indexOne)
        else:
            print("NEIN")
        

    def collectCards(self, indexOne, indexTwo):
        if self.pile[indexOne].collectValue == self.pile[indexTwo].collectValue:
            for i in range(len(self.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

            self.pile[indexTwo].isBuilt = False
            self.pile.pop(indexOne)
        else:
            print("NEIN")
            # say.nein(player.name)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value 
        self.wasLastPlayed = False #at the end of each turn, all of the .wasLastPlayed values should be set to False

    def return_card(self):
        return self.suit, self.value
