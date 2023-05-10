import os
import random

##################
##################
#####CLASSES######
##################
##################

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
    
    def setup(self):
        print("ohihi")
    
    def instructions(self):
        print(  '------------------------------------------------',
                'When it\'s your turn you will be able to see your',
                'hand and the cards on the table like this:',
                'Your Cards:',
                '    12 of heart',
                '    5 of clubs',
                '    2 of diamonds',
                '    9 of spades',
                'Center',
                'Built Value: 5',
                '    5 of diamonds',
                'Built Value: 11',
                '    11 of diamonds',
                'Built Value: 2',
                '    2 of clubs',
                'Built Value: 10',
                '    10 of hearts',
                '------------------------------------------------',
                'Examples of possible commands you can do:',
                '"play 0"      - plays the first card in your hand (12)',
                '"build 2 3"   - builds the 3rd and last card in the center (2+10)',
                '"collect -1 -2" - collects the last two piles in the center (2+10)',
                '"take 0" - moves the first card from the center into your discard pile(5)',
                sep='\n'
        )


    def printTable(self, player, center):
        print(f"{player.name}'s Cards: ")
        for card in player.hand:
            print(f"        {card.value} of {card.suit}")
        print('There are %d cards in your discard pile.' % len(player.discard))
        print("Center:")
        for pile in center:
            if pile.isBuilt:
                print(f"    Built Value: {pile.builtValue}.")
                for card in pile.pile:
                    print(f"        {card.value} of {card.suit}")
            else:
                print(f"    Collect Value: {pile.builtValue}.")
                for card in pile.pile:
                    print(f"        {card.value} of {card.suit}")
    
    def results(self, players):
        ordinals = ['first', 'second', 'third', 'fourth']
        print(f'The winner is: {players[0].name}! Congratulations! \n')
        for i in range(len(players)):
            print(f'\n {players[i].name}, you came in {ordinals[i]} place with {players[i].points} points!',
            f'You also got {players[i].spades} spades and {players[i].aces} aces')
        for player in players:
            if player.bigCasino == 2:
                print(f'{player.name} got the big casino (10 of diamonds).')
            if player.littleCasino == 1:
                print(f'{player.name} got the little casino (2 of spades).')
        print('Thank you for playing!')
    
    def easterEggShow(player):
        print(f'This is your discard pile have {player.points} points')

            

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discard = []
        self.cards = 0
        self.spades = 0
        self.aces = 0
        self.littleCasino = 0
        self.bigCasino = 0
        self.points = 0
    
    def count(self):
        self.cards = len(self.discard)
        for card in self.discard:
            if card.suit == 'spades' : self.spades += 1 
            if card.value == 1 : self.aces += 1 
            if card.suit == 'spades' and card.value == 2 : self.littleCasino = 1 
            if card.suit == 'diamonds' and card.value == 10 : self.bigCasino = 2 
        
        self.points += (self.aces + self.littleCasino + self.bigCasino)
        return self.cards, self.spades
    
    def handToDiscard(self, indexOne):
        self.discard.append(self.hand.pop(indexOne))


class CenterPile:
    def __init__(self):
        self.pile = [] 
        self.builtValue = 0
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
            self.pile.pop(indexOne)
        else:
            say.illegal(player.name)
        

    def collectCards(self, indexOne, indexTwo):
        if self.pile[indexOne].builtValue == self.pile[indexTwo].builtValue:
            for i in range(len(self.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

            self.pile[indexTwo].isBuilt = False
            self.pile.pop(indexOne)
        else:
            say.illegal(player.name)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value 
        self.wasLastPlayed = False

    def return_card(self):
        return self.suit, self.value


##################
##################
#GLOBAL FUNCTIONS#
##################
##################


def create_deck():
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    deck = []
    for suit in suits:
        for value in range(1, 14):
            deck.append(Card(suit, value))
    random.shuffle(deck)
    return deck


def deal_to_center(deck, numCards):
    for i in range(numCards):
        center.pile.append(CenterPile())
        center.pile[-1].pile.append(deck.pop(0))
        center.pile[-1].builtValue = center.pile[-1].pile[0].builtValue


def deal_to_player(deck, player, numCards):
    for i in range(numCards):
            player.hand.append(deck.pop(0))


def deal_cards(deck, players):
    if deck:
        if len(deck) == 52:
                for i in range(2):
                    for player in players:
                        deal_to_player(deck, player, 2)
                deal_to_center(deck, 4)

        else:
            for i in range(2):
                    for player in players:
                        deal_to_player(deck, player, 2)


def move_to_center(player, indexCard):
    center.pile.append(CenterPile())
    center.pile[-1].pile.append(player.hand.pop(indexCard))
    center.pile[-1].builtValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].pile[0].wasLastPlayed = True
    center.pile[-1].pile[0].isBuilt = True


def move_from_center(player, indexCenterPile):
    temp = False
    for card in center.pile[indexCenterPile].pile:
        if card.wasLastPlayed:
            temp = True
            break

    if not center.pile[indexCenterPile].isBuilt and temp:
        while center.pile[indexCenterPile].pile:
            player.discard.append(center.pile[indexCenterPile].pile.pop(0))
        center.pile.pop(indexCenterPile)
    else:
        say.error()


def results(players):
    cardList = []
    spadesList = []
    playerList = players
    podium = []
    
  
    for player in players:
        playerCards, playerSpades = player.count()
        cardList.append(playerCards)
        spadesList.append(playerSpades)
    
    highestCards = [total for total in cardList if total == max(cardList)]
    
    highestSpades = [total for total in spadesList if total == max(spadesList)]

    if len(highestCards) == 1:
        cardWinner = players[cardList.index(max(cardList))]
        cardWinner.points += 3 
    
    if len(highestSpades) == 1:
        spadesWinner = players[spadesList.index(max(spadesList))]
        spadesWinner.points += 1

    while playerList:
        i = playerList.index(max(playerList.points))
        podium.append(playerList[i])
        players.pop(i)

    return podium


def setup():
    players = []
    deck = create_deck()
    count = 0

    numPlayers = input('Enter how many players: ')
    if numPlayers.isdigit() and (1 < int(numPlayers) < 5):
        numPlayers = int(numPlayers)
        for i in range(numPlayers):
            playername = input('Enter your name: ')
            players.append(Player(playername))
    else:
        quit()
    
    yuh = ['yes' or 'yea' or 'yeah' or 'y' or 'yep']
    instruction = input('Do you want instructions? (y/n) ')
    if instruction in yuh:
        say.instructions()
        ready = input('Are you ready to start?')
        

    return players, deck, count


def is_digit(strings, player):
    for i in strings:
        if i.startswith('-') and i[1:].isdigit():
            return True
        elif i.isdigit():
            return True
        else:
            say.invalid(player.name)
            return False


def is_in_range(commands, list, player):
    commands = [(int(index)) for index in commands]
    for index in commands:
        if not((-len(list)) <= index <= (len(list) - 1)):
            say.range(player.name)
            return False
    return True



def check_input(commands, player, possibleActions):
    if commands:
        if commands[0] in possibleActions:
            if commands[0] == possibleActions[0] and len(commands) == 1: # quit
                return True
            elif commands[0] == possibleActions[1] and len(commands) == 1: # end
                return True
            elif commands[0] == possibleActions[2] and len(commands) == 2 and is_digit(commands[1::], player) and is_in_range(commands[1::], player.hand, player): # play
                return True
            elif commands[0] == possibleActions[3] and len(commands) == 2 and is_digit(commands[1::], player) and is_in_range(commands[1::], center.pile, player): # take
                return True
            elif commands[0] == possibleActions[4] and len(commands) == 3 and is_digit(commands[1::], player) and is_in_range(commands[1::], player.hand, player): #build
                return True
            elif commands[0] == possibleActions[5] and len(commands) == 3 and is_digit(commands[1::], player) and is_in_range(commands[1::], player.hand, player): #collect
                return True
            elif commands[0] == possibleActions[6] and len(commands) == 3 and is_digit(commands[1::], player) and is_in_range(commands[1::], player.hand, player) and is_in_range(commands[1::], center.pile, player): #quick
                return True
    say.invalid(player.name)
    return False


def playersTurn(player):
    say.printTable(player, center.pile)
    action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')
    commands = action.split()
    possibleActions = ['quit', 'end', 'play', 'take', 'build', 'collect', 'quick', 'show']

    temp = 0
    isRunning = True


    while isRunning:
        if check_input(commands, player, possibleActions):
            # add here
            if commands[0] == possibleActions[0]: #quit
                quit()

            elif commands[0] == possibleActions[1] and temp < 1: #end
                say.illegal(player.name)
                
            elif commands[0] == possibleActions[1] and temp == 1: #end
                isRunning = False
                break

            elif commands[0] == possibleActions[2]: #play
                if temp > 0:
                    say.illegal(player.name)
                else:
                    move_to_center(player, int(commands[1]))
                    temp += 1

            elif commands[0] == possibleActions[3]: #take
                move_from_center(player, int(commands[1]))

            elif commands[0] == possibleActions[4]: #build
                center.buildCards(int(commands[1]), int(commands[2]), player)

            elif commands[0] == possibleActions[5]: #collect
                center.collectCards(int(commands[1]), int(commands[2]))

            elif commands[0] == possibleActions[6]: #quickTake 
                if player.hand[int(commands[1])].value == center.pile[int(commands[2])].builtValue:
                    player.handToDiscard(int(commands[1]))
                    center.pile[int(commands[2])].isBuilt = False
                    center.pile[int(commands[2])].pile[0].wasLastPlayed = True
                    move_from_center(player, int(commands[1]))
                    temp += 1
                    
            elif commands[0] == possibleActions[7]: #show
                print("asdf")

        say.printTable(player, center.pile)
        action = input('Enter (play, build, collect, take, quick or end) and the corresponding indices: ')
        commands = action.split()
    print("Next person's turn...")





##################
##################
#####GAME.PY######
##################
##################

say = Print()
players, deck, count = setup()
center = Center()

while count < 49:
    temp = False
    for player in players:
        if player.hand:
            temp = False
            break
        else:
            temp = True
    if temp:
        deal_cards(deck, players)

    player = players[count % len(players)]

    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    
    playersTurn(player)

    count += 1


podium = results(players)
say.results(podium)


