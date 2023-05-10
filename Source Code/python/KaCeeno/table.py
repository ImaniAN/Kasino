'''
Created on 18.2.2014

@author: Paleksi
'''

from card import Card

class Table(object):
    '''
    This class handles everything that is related to the table. That includes knowing
    the cards on the table, the card that was played this turn and also the player who
    took cards last from the table. This class handles the checking that the cards the
    player wants to take match the card played in value.
    '''

    def __init__(self):
        self._cards = []  # The cards on the table. Initially there are no cards
        self._last_player = None # The latest Player-object, who took cards from the table
        self._played_card = None # The card that was played during this turn. Used when handling the take_cards() function
        self._image = 'Images/background2.png'
        
        
    # Setters and getters
    ########################################
    
    def get_cards(self):
        return self._cards
    
    def is_empty(self):
        if (len(self._cards) == 0):
            return True
        return False
    
    def get_latest(self):
        return self._last_player
    
    def get_image(self):
        return self._image
    
    def get_selected(self):
        selected = []
        for card in self._cards:
            if (card.is_selected()):
                selected.append(card) 
        return selected
    
    def set_latest(self, player):
        self._last_player = player
        
    def set_image(self, path):
        self._image = path
        
    def get_played_card(self):
        return self._played_card
    
    def reset_table(self):
        self._cards = []
        
    # SHOULD ONLY BE CALLED FROM Player.end_turn()!!!
    def reset_played_card(self):
        self._played_card = None
    # !!
    
    def play_card(self, card):  # Called from Player-class
        self._played_card = card
    
    ########################################    
    
    # Places a card from the players hand and handles the possible value changes
    # for the special cards. Used as the discarded card
    def place_card(self, card):
        card.set_position("Table")
        if(card.is_selected()):
            card.select()   # De-select chosen card    
        
        self._cards.append(card)
    
    # Takes cards from the table equal to the value of the the placed card
    # and returns the cards taken
    def take_cards(self, player, cards, over=False):
        if (over):  # Should be entered only when the round is over
            return self._cards
        value = 0
        for card in cards:
            value += card.get_value()
        if not (value == self._played_card.get_value()):    # Value doesn't match
            return []
        for card in cards:
            for table_card in self._cards:
                if card.get_value() == table_card.get_value() and card.get_suit() == table_card.get_suit():
                    self._cards.remove(table_card)
        self.set_latest(player)
        return cards
    
    
    # SHOULD ONLY BE CALLED BY save_game() AND load_game()
    # Print the table details for the save file
    def save_table(self):
        text = ''
        if (self._last_player == None):
            text += "LST00"
        else:
            name = self._last_player.get_name()
            name_len = str(len(name))
            if (int(name_len) < 10):
                name_len = '0' + name_len
            text += "LST" + name_len + name
        if (self._played_card == None):
            text += "PLD00"
        else:
            text += "PLD" + self._played_card.save_card()
        text += "CRD"   # Cards
        card_text = ''
        for card in self._cards:
            card_text += card.save_card()
        card_len = str(len(card_text))
        if (int(card_len) < 10):
            card_len = '0' + card_len
        text += card_len + card_text
        tbl_length = len(text)
        if (tbl_length < 10):
            tbl_length = '00' + str(tbl_length)
        elif (tbl_length < 100):
            tbl_length = '0' + str(tbl_length)
        else:
            tbl_length = str(tbl_length)
        
        final = "TBL" + tbl_length + text
        return final
    
    # Load the details of the table from the save file.
    # The last player is not included here, because this class
    # does not know the players of the game.
    def load_table(self, chunk, game):
        part = chunk[0:3]
        while (len(chunk) > 0):
            chunk = chunk[3:len(chunk)]
            # Last player who took cards from the table
            if (part == "LST"):   # This is already handled in the Game-class
                try:
                    size = int(chunk[0:2])
                except ValueError:
                    return False
                chunk = chunk[2:len(chunk)]
                tmp = chunk[0:size]
                chunk = chunk[size:len(chunk)]
            # The card the player-in-turn played this turn, if any
            elif (part == "PLD"):
                test = int(chunk[0:2])
                if (test > 0):  # Check whether there is a played card this turn
                    # There is no "size" for the played card since it's always three. If there
                    # Isn't a played card, it is just 00, so we don't need to change the size of
                    # chunk here
                    info = chunk[0:3]
                    chunk = chunk[3:len(chunk)]
                    tmp = Card(1, Card.SPADES)  # The played card
                    loaded = tmp.load_card(info)
                    if not (loaded):
                        return False
                    tmp.set_position("Hand")    # The card is still in hand
                    player = game.get_player_in_turn()
                    for card in player.get_hand():
                        if (card.get_value() == tmp.get_value()) and (card.get_suit() == tmp.get_suit()):
                            card.select()
                            self._played_card = card
                    # /for
                # /if
                else:
                    chunk = chunk[2:len(chunk)]
            # The cards on the table
            elif (part == "CRD"):
                try:
                    size = int(chunk[0:2])
                except ValueError:
                    return False
                chunk = chunk[2:len(chunk)]
                while (size > 0):
                    info = chunk[0:3]
                    chunk = chunk[3:len(chunk)]
                    card = Card(1, Card.SPADES)
                    loaded = card.load_card(info)
                    if not (loaded):
                        return False
                    self.place_card(card)
                    size -= 3
            else:   # Unknown chunk
                return False
            part = chunk[0:3]   # Get new header
        # /while
        return True