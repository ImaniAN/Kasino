import os
import random

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
        center.pile[-1].collectValue = center.pile[-1].pile[0].builtValue


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
    center.pile[-1].collectValue += center.pile[-1].pile[0].builtValue
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


def compare_players(players):
    cardList = []
    spadesList = []
  
    for player in players:
        playerCards, playerSpades = player.count()
        cardList.append(playerCards)
        spadesList.append(playerSpades)
    
    highestCards = [total for total in cardList if total == max(cardList)]
    
    highestSpades = [total for total in spadesList if total == max(spadesList)]

    print(highestCards, highestSpades)

    if len(highestCards) == 1:
        cardWinner = players[cardList.index(max(cardList))]
        cardWinner.points += 3 
    
    if len(highestSpades) == 1:
        spadesWinner = players[spadesList.index(max(spadesList))]
        spadesWinner.points += 1


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
    printTable(player, center.pile)
    action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')
    commands = action.split()
    possibleActions = ['quit', 'end', 'play', 'take', 'build', 'collect', 'quick']

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
                    move_from_center(player, int(commands[2]))
                    temp += 1

        printTable(player, center.pile)
        action = input('Enter (play, build, collect, take, quick or end) and the corresponding indices: ')
        commands = action.split()
    print("Next person's turn...")


def prettyPrint(players, centerList):
    for p in players:
    
        print(f"Player: {p.name}")
        print(f"    Hand:")
        for card in p.hand:
            print(f"        {card.value} of {card.suit}")#". %d" % card.builtValue)
        print(f"    Discard:")
        for discardCard in p.discard:
            print(f"        {discardCard.value} of {discardCard.suit}")
        print(f"-----------------------------")
    
    print("Center:")
    for pile in centerList:
        print("    Pile:")# % pile.builtValue)
        for c in pile.pile:
            print(f"        {c.value} of {c.suit}")
    print("#################################")


def printTable(player, center):
    print(f"{player.name}'s Cards: ")
    for card in player.hand:
        print(f"        {card.value} of {card.suit}")
    print('There are %d cards in the discard pile.' % len(player.discard))
    print("Center:")
    for pile in center:
        print(f"    Pile: Collect: {pile.collectValue}. Build: {pile.builtValue}.") # % pile.builtValue)
        for card in pile.pile:
            print(f"        {card.value} of {card.suit}")
