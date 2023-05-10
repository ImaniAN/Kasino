'''
Created on 18.2.2014

@author: Paleksi
'''
from card import Card
import random

class Deck(object):
    '''
    This class holds (max.) 52 Card-objects that it creates in set_deck(). A new deck is
    made every round and the old deck discarded (pretty rough, but that's virtual Casino
    for you all right). The deck only knows what cards it has and will only pop() the
    last item when a card is drawn from it.
    '''

    def __init__(self):
        self._cards = []
        
    # Setters and getters
    ########################################    
        
    # The real initialization of a deck, but since load_game() adds the cards separately, this can't be in the init.
    def set_deck(self):
        # Initialize the card deck. Create 52 card objects and add them to the self._cards stack.
        
        i = 0   # Suit index
        suits = [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]
        while (i < 4):  # Clubs - Diamonds
            suit = suits[i]
            n = 0   # Card value
            while (n < 13): # Ace - King
                card = Card(n+1, suit)
                self._cards.append(card)
                n += 1
            # /while
            i += 1
        # /while
        # Set images for the cards
        for card in self._cards:
            suit = ''
            if (card.get_suit() == Card.CLUBS):
                suit = 'Clubs'
            elif (card.get_suit() == Card.DIAMONDS):
                suit = 'Diamonds'
            elif (card.get_suit() == Card.HEARTS):
                suit = 'Hearts'
            else:
                suit = 'Spades'
            path = "Images/%s (%d)"%(suit, card.get_value())
            card.set_image(path)
            path += " selected"
            card.set_select_image(path)
        # /for
            
    def get_cards(self):
        return self._cards
    
    def set_card(self, card):
        self._cards.append(card)
    
    ########################################
    
    def draw_card(self):
        return self._cards.pop()
    
    def shuffle_deck(self):
        random.shuffle(self._cards)
    
    # Get the card data for the save-file and return a string
    # Containing all the data from the cards and also the size
    # of the string in a format YYY. If there are 3 cards left
    # in the deck the YYY will be "009" since it takes 3 characters
    # to print a single card to save-format
    def save_deck(self):
        text = ''
        for card in self._cards:
            text += card.save_card()
        card_length = len(text)
        if (card_length < 10):
            card_length = '00' + str(card_length)
        elif (card_length < 100):
            card_length = '0' + str(card_length)
        else:
            card_length = str(card_length)
        
        final = "DCK" + card_length + text
        return final
    
    # Load the deck data from a save file
    def load_deck(self, chunk):
        while (len(chunk) > 0):
            info = chunk[0:3]
            card = Card(1, Card.SPADES) # just init the card
            loaded = card.load_card(info)        # loaded properly here
            if not (loaded):
                return False
            self._cards.append(card)
            chunk = chunk[3:len(chunk)]
        return True
        