'''
Created on 18.2.2014

@author: Paleksi
'''

class Card(object):
    '''
    Holds the information of a single card: its suit and value as well as its
    images for both being selected and not selected to be used for a GUI and
    also a boolean value to determine whether it is selected. Initially all
    cards are in the deck
    '''
    CLUBS = 0
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3


    def __init__(self, value, suit):
        self._value = value         # Int
        self._suit = suit           # Enum
        self._position = 'Deck'     # string
        self._image = ''
        self._select_image = ''
        self._selected = False
        
    # Setters and getters
    ########################################
    
    def get_value(self):
        return self._value
    
    def get_suit(self):
        return self._suit
    
    def get_position(self):
        return self._position
    
    def get_image(self):
        return self._image
    
    def get_select_image(self):
        return self._select_image
    
    def set_value(self, value):
        self._value = value
        
    def set_position(self, pos):
        self._position = pos
        self.change_value(pos)  # Change the value
    
    def set_image(self, path):
        self._image = path
        
    def set_select_image(self, path):
        self._select_image = path
        
    def is_selected(self):
        return self._selected
        
    def select(self):
        self._selected = not self._selected
        
    ########################################
    
    # Changes the card's value depending on it's position
    # Called by Player.draw_card() (and some other functions, that change the value
    # back to a more easily-readable format) and Table.place_card()
    def change_value(self, position):
        if (position == "Hand"):
            if (self._value== 1): # Ace
                self._value = 14
            elif (self._value == 10) and (self._suit == Card.DIAMONDS):    # 10-Diamonds
                self._value = 16
            elif (self._value == 2) and (self._suit == Card.SPADES):    # 2-Spades
                self._value = 15
        else:   # Table, Deck, Collected
            if (self._value == 14):      # Ace
                self._value = 1
            elif (self._value == 16):    # 10-Diamonds
                self._value = 10
            elif (self._value == 15):    # 2-Spades
                self._value = 2
    
    # Used for the textbox or other game-info text area, so it's easier to check
    # what was played last turn etc.
    def __str__(self):
        output = ''
        # Value part
        if (self._value == 1) or (self._value == 14):
            output += 'Ace'
        elif (self._value == 11):
            output += 'Jack'
        elif (self._value == 12):
            output += 'Queen'
        elif (self._value == 13):
            output += 'King'
        else:
            output += str(self._value)
        # /Value part
        # Suit part
        if (self._suit == Card.CLUBS):
            output += '-Clubs'
        elif (self._suit == Card.SPADES):
            output += '-Spades'
        elif (self._suit == Card.HEARTS):
            output += '-Hearts'
        else:
            output += '-Diamonds'
        # /Suit part
              
        return output
    
    # SHOULD NOT BE CALLED OUTSIDE save_game() and load_game() !! 
    # Print card information for the save file
    def save_card(self):
        output = ''
        if (self._value == 14):
            output += '01'
        elif (self._value == 15):   # 2-Spades
            output += '02'
        elif (self._value == 16):   # 10-Diamonds
            output += '10'
        elif(self._value < 10): # add a 0 to the front so we get equal size values
            output += '0' + str(self._value)
        else:
            output += str(self._value)
        
        if (self._suit == Card.CLUBS):
            output += 'C'
        elif (self._suit == Card.SPADES):
            output += 'S'
        elif (self._suit == Card.HEARTS):
            output += 'H'
        else:
            output += 'D'
        
        return output
    
    # Load card information from the save file
    def load_card(self, info):
        try:
            value = int(info[0:2])
            suit = info[2]
        except ValueError:
            return False
        if (value > 0):
            self._value = value
        else:
            return False
        if (suit == 'C'):
            self._suit = self.CLUBS
        elif (suit == 'S'):
            self._suit = self.SPADES
        elif (suit == 'H'):
            self._suit = self.HEARTS
        elif (suit == 'D'):
            self._suit = self.DIAMONDS
        else:
            return False
        
        # Set images for the card
        if (self._suit == Card.CLUBS):
            suit = 'Clubs'
        elif (self._suit == Card.DIAMONDS):
            suit = 'Diamonds'
        elif (self._suit == Card.HEARTS):
            suit = 'Hearts'
        else:
            suit = 'Spades'
        path = "Images/%s (%d)"%(suit, self._value)
        self.set_image(path)
        path += " selected"
        self.set_select_image(path)
        
        return True
    # !!
