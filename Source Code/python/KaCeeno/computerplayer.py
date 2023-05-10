'''
Created on Apr 5, 2014

@author: Aleksi
'''

from player import Player
from card import Card
import random

# The Over-class for all AI-players. Just so that don't have to repeat is_human() everywhere
class ComputerPlayer(Player):
    '''
    ComputerPlayer is the upper-class for all the AI players. It holds the AI logic and the
    actual AI classes only have the init() and play_turn() which then calls the functions
    from this class. More AI classes can then be easily added without having to re-implement
    everything (unless the AI works with a completely different logic).
    '''
    # Priority order for AI-players
    COTTAGE = 50
    D10 = 10    # 10-Diamonds
    SP2 = 5     # 2-Spades
    ACE = 5     # Ace-(all suits)
    SPADE = 1
    NORMAL = 0.5
    
    DECK_MIN_CARDS = 3
    
    def __init__(self, name):
        super(ComputerPlayer, self).__init__(name)
        
    # Overwrite from Player.is_human()
    def is_human(self):
        return False
    
    # Checks the priority value of the cards on the table that
    # the parameter card can take.
    # Called by SUBCLASS.play_turn()
    def check_options(self, card):
        table_cards = self._game.get_table().get_cards()
        if (self._game.get_table().is_empty()):
            return 0
        value = 0
        for tmp in table_cards:
            value += tmp.get_value()
        if (card.get_value() == value): # Cottage has the highest priority
            return ComputerPlayer.COTTAGE
        combos = self.get_combos(card.get_value(), table_cards)

        return self.get_priority(combos)
    
    # Gets all the possible combinations of cards the computer can take with the given card
    # Called by play_turn() and check_options()
    def get_combos(self, value, cards):
        combos = []  # List of lists
        for card1 in cards:
            combo = []     # Re-initialize the stack each loop
            table_value = card1.get_value()
            combo.append(card1)
            if (table_value == value):
                combos.append(combo)
                continue    # If the first card value == value, no point looping it
            elif (table_value > value):
                continue    # Same goes if its over the value
            for card2 in cards:
                if (card1 == card2):
                    continue
                table_value += card2.get_value()
                combo.append(card2)
                if (table_value == value):
                    combos.append(combo)
                elif (table_value > value): # If the value is over, remove the the second card from the combination
                    table_value -= card2.get_value()
                    combo.remove(card2)
            # /for
        # /for
        # Remove the combinations that have same cards as other combinations and with lower priority
        for combo1 in combos:
            for combo2 in combos:
                if (combo1 == combo2):
                    continue
                has_same = self.has_same_cards(combo1, combo2)
                if (has_same):  # Discard the combination with the lower priority value
                    prior1 = self.count_priority(combo1)
                    prior2 = self.count_priority(combo2)
                    if (prior1 >= prior2):
                        combos.remove(combo2)
            # /for
        # /for

        return combos
    
    # Checks if the two lists have same cards
    # Called by get_combos()
    def has_same_cards(self, list1, list2):
        for card1 in list1:
            for card2 in list2:
                if (card1.get_value() == card2.get_value()) and (card1.get_suit() == card2.get_suit()):
                    return True
        return False
    
    # Count the priority points for a card combination
    # Called by get_combos() and get_priority()
    def count_priority(self, cards):
        priority = 0
        for card in cards:
            if ((card.get_value() == 10) and (card.get_suit() == Card.DIAMONDS)) or (card.get_value() == 16):
                priority += ComputerPlayer.D10  # 10-Diamonds
            elif (card.get_value() == 2) and (card.get_suit() == Card.SPADES)  or (card.get_value() == 15):
                priority += ComputerPlayer.SP2 + ComputerPlayer.SPADE   # 2-Spades
            elif (card.get_value() == 1 or card.get_value() == 14):
                priority += ComputerPlayer.ACE  # Ace
                if (card.get_suit() == Card.SPADES):    # Ace-Spades
                    priority += ComputerPlayer.SPADE
            elif (card.get_suit() == Card.SPADES):
                priority += ComputerPlayer.SPADE    # Spades
            else:
                priority += ComputerPlayer.NORMAL   # Everything else
        # /for
        
        return priority
    
    # Sum the priority points for a set of card combinations
    # Called by check_options()
    def get_priority(self, combos):
        priority = 0
        amount = 0
        # Combos == list of lists
        for cards in combos:
            priority += self.count_priority(cards)
            amount += len(cards)
        if (amount == len(self._game.get_table().get_cards())):
            return ComputerPlayer.COTTAGE   # Cottage has the highest priority
            
        return priority
    
    # Finds the card in the players hand that has the worst priority and also so that the next
    # player will less likely get a combo next turn, by placing a very high card on the table
    # unless the table is empty, in which case it will choose a small card. Also when the deck
    # is about to finish, it will choose a small card to better get the last pick from the table
    # to get the cards at the end of the round
    # Called by SUBCLASS.play_turn()
    def get_worst_card(self):
        worst = 20  # Just a random value that is higher than any single card priority value
        worst_card = None
        for card in self._hand:
            tmp = []    # make a tmp list so we can call the count_priority() function
            tmp.append(card)
            prior = self.count_priority(tmp)
            if (prior <= worst):
                if (worst_card == None) or (prior < worst):    # First round or worse card
                    worst_card = card
                # Empty table or only a few cards left in the deck
                elif (self._game.get_table().is_empty()) or (len(self._game.get_deck().get_cards()) < ComputerPlayer.DECK_MIN_CARDS):
                    if (card.get_value() < worst_card.get_value()):
                        worst_card = card
                elif (worst_card.get_value() > 13): # Aces, 2-Spades and 10-Diamonds should not be discarded, unless you have to
                    worst_card = card
                else:   # There are cards on the table and deck has enough cards
                    if (worst_card.get_value() < card.get_value()):
                        worst_card = card
                worst = prior
        
        return worst_card
    
# /ComputerPlayer

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

class GreedyAI(ComputerPlayer):
    '''
    The GreedyAI will always try to take cards from the table, and unless it can, it will choose the worst priority
    card to discard.
    
    Tests have proved that this AI is actually hard to beat (at least for me...)
    '''    
    
    def __init__(self, name=""):
        super(GreedyAI, self).__init__(name)
        self._type = "G"
           
    # Defines what the AI does during it's turn 
    def play_turn(self):
        possibilities = {}  # Dictionary
        card_to_play = None
        for card in self._hand: # Get all priority-values listed
            priority = self.check_options(card)
            possibilities[card] = priority
        highest = 0
        for card in self._hand: # Get the best card
            if (possibilities[card] > highest):
                highest = possibilities[card]
                card_to_play = card
            # In case of 2 same cards, should play e.g. Ace-Spades instead of Ace-Diamonds
            elif (possibilities[card] == highest):
                if not (card_to_play == None):
                    tmp1 = tmp2 = []
                    tmp1.append(card_to_play)
                    tmp2.append(card)
                    prior1 = self.count_priority(tmp1)
                    prior2 = self.count_priority(tmp2)
                    if (prior2 > prior1):   # card > card_to_play
                        card_to_play = card
                else:
                    card_to_play = card
        if (highest == 0):  # Can't take any card from the table
            card_to_play = self.get_worst_card()    # Choose the worst card from hand and play it
            self.play_card(card_to_play)
            return card_to_play, [] # For printing to the wanted output
        else:   # highest > 0 == can take cards from table
            combos = self.get_combos(card_to_play.get_value(), self._game.get_table().get_cards())
            self.play_card(card_to_play)
            for cards in combos:    # take everything you can
                self.take_cards(cards, False)
            if (self._game.get_table().is_empty()):
                self._round_cottages += 1
            return card_to_play, combos # For printing to the wanted output



# /GreedyAI

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

class PassiveAI(ComputerPlayer):
    '''
    The passiveAI only takes cards if the priority goes above PASSIVE_LIMIT or unless it can take more than 1 "set"
    of cards. For example if there is a 2-Hearts + 3-Clubs the Prior value would be 1, but if there was e.g 5-Diamonds
    on the table as well, it can take the 2-Hearts + 3-Clubs AND 5-Diamonds combo with another 5.
    
    This AI is kind of a AI that you SHOULD win always, but I won't guarantee it... :D
    '''
    
    PASSIVE_LIMIT = 2
    
    def __init__(self, name=""):
        super(PassiveAI, self).__init__(name)
        self._type = "P"
        
    # Defines what the AI will do during it's turn
    def play_turn(self):
        possibilities = {}  # Dictionary
        card_to_play = None
        for card in self._hand: # Get all priority-values listed
            priority = self.check_options(card)
            possibilities[card] = priority
        highest = 0
        for card in self._hand: # Get the best card
            if (possibilities[card] > highest):
                highest = possibilities[card]
                card_to_play = card
        combos = []
        if (card_to_play != None):  # There came an error without this, probably because the hand was empty
            combos = self.get_combos(card_to_play.get_value(), self._game.get_table().get_cards())
        if not (len(combos) > 1) or not (highest > PassiveAI.PASSIVE_LIMIT):  # Can't take anything over the limit or more than 1 combo
            card_to_play = self.get_worst_card()    # Choose the worst card from hand and discard it
            self.play_card(card_to_play)
            return card_to_play, [] # Return value for the output
        else:   # highest > PASSIVE_LIMIT == Will take cards from table
            self.play_card(card_to_play)
            for cards in combos:    # take everything you can
                self.take_cards(cards, False)
            if (self._game.get_table().is_empty()):
                self._round_cottages += 1
            return card_to_play, combos # Return values for the output
        
# /PassiveAI

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

class RandomAI(ComputerPlayer):
    '''
    The RandomAI will choose a card from it's hand in random and plays it. If it can take cards from the table with it,
    it will take every card it can, but if it couldn't take any cards from the table, it will just end it's turn.
    '''
    
    def __init__(self, name=""):
        super(RandomAI, self).__init__(name)
        self._type = "R"
        
    def play_turn(self):
        index = random.randint(0, len(self._hand)-1)  # Choose a random card from hand to play
        card_to_play = self._hand[index]
        combos = self.get_combos(card_to_play.get_value(), self._game.get_table().get_cards())
        if (len(combos) == 0):  # Take no cards from the table
            self.play_card(card_to_play)
            return card_to_play, [] # The print
        else:
            self.play_card(card_to_play)
            for cards in combos:    # take everything you can with the card
                self.take_cards(cards, False)
            if (self._game.get_table().is_empty()):
                self._round_cottages += 1
            return card_to_play, combos # For printing to the wanted output