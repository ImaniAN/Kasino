'''
Created on 18.2.2014

@author: Paleksi
'''

from card import Card

class Player(object):
    '''
    Holds the data of a single player. This class holds the actions for all human players and is inherited by ComputerPlayer, which
    calls Player's functions based on it's own logic. Each player knows it's name, points and the cards directly appointed to it 
    (hand, collected stack) as well as the game it currently is in. 
    '''

    def __init__(self, name=''):
        self._name = name
        self._hand = []                 # Card objects
        self._collected = []            # Card objects collected this round
        self._points = 0                # Player's score
        self._round_cottages = 0        # Cottages made this round
        self._game = None               # The game where the player is, Used to acces save_game(), load_game(), and the table
        self._played_this_turn = False  # Put a card on the table this turn
        self._taken_cards = False       # Taken cards from the table this turn
        self._type = "H"                # Used to get the proper type of player when loading
        
    # Setters and getters
    ########################################
    
    def is_human(self): # Overwritten for AI-players
        return True
    
    def get_name(self):
        return self._name

    def get_hand(self):
        return self._hand

    def get_collected(self):
        return self._collected
    
    def get_points(self):
        return self._points
    
    def get_cottages(self):
        return self._round_cottages
    
    def get_game(self):
        return self._game
    
    def get_selected_card(self):
        for card in self._hand:
            if (card.is_selected()):
                return card
        return None  
    
    def set_game(self, game):
        self._game = game
        
    # Point adding
    ########################################    
    def add_cottage(self):
        self._round_cottages += 1
        
    def add_points(self, amount):
        self._points += amount
    
    # SHOULD NOT BE CALLED OUTSIDE load_game()!!    
    def set_name(self, name):   # String
        self._name = name
    # !!
    
    # Checkers for the boolean values
    ########################################
    def has_played(self):
        return self._played_this_turn
    
    def has_taken(self):
        return self._taken_cards
        
    ########################################
        
    # Initialize a player for a new round.
    # Called by Game.new_round()
    def new_round(self):
        self._collected = []
        self._played_this_turn = False
        self._taken_cards = False
        self._round_cottages = 0
        
    # Draw a card from the deck. Change the position to "Hand" and handle the value changes
    # of special cards.
    # Called by end_turn()
    def draw_card(self):
        card = self._game.get_deck().draw_card()
        card.set_position("Hand")
        self._hand.append(card)
        
    # Plays the given card if the player hasn't taken any cards yet this turn.
    # Called by Game.play_card()
    def play_card(self, card):
        if not (self._taken_cards):
            self._game.get_table().play_card(card)
        self._played_this_turn = True
        
    # Add the cards taken from the table into the collected-stack.
    # Also called when the round ends to give the person who played last the cards from the table.
    # Over is a boolean value which determines whether the round is over. It is called
    # with the value "False" every time it's not the end of the round.
    # Called by Game.take_cards()
    def take_cards(self, cards, over):
        collected = self._game.get_table().take_cards(self, cards, over)
        if not (len(collected) > 0):    # No selected cards
            return
        for card in collected:
            card.set_position("Collected")  # Could be done with one line, but easier handling like this
            self._collected.append(card)
        self._taken_cards = True
        
    # Ends the player's turn and does the appropriate actions, i.e. putting the played card in either
    # the collected-stack (took cards this turn) or on the table (didn't take cards). Also draws a 
    # card from the deck if there's still any cards left.
    # Called by Game.end_turn()
    def end_turn(self):
        for card in self._hand:
            if (card == self._game.get_table().get_played_card()):
                played = card
                break
        if (self._taken_cards): # Add the played card to your collected stack
            played.set_position("Collected")
            self._collected.append(played)
            self._hand.remove(played)
        else:   # Place the played card on the table, if the player didn't take cards
            self._game.get_table().place_card(played)
            self._hand.remove(played)
            
        self._game.get_table().reset_played_card()  # ONLY PLACE WHERE THIS SHOULD BE CALLED!
        
        if (len(self._game.get_deck().get_cards()) > 0):    # Draw a card if there are cards left in the deck
            self.draw_card()
        # Reset booleans for the next turn
        self._played_this_turn = False
        self._taken_cards = False
        
    # Save and Load  
    ###############################################################################################    
    ###############################################################################################    
    # Adds the save information of the player into a string format and returns it.
    # The save info consist of the Player's name, points, cottages-this-round, the
    # boolean values for having played and taken cards this turn, the hand of the Player
    # and also the collected-stack. All headers are of format XXXYY, where XXX is three
    # letters giving the header title (e.g. NAM = Name, PTS = Points) and YY is the total
    # size of the chunk. If a Player's name was "Toby" the NAM block would be "NAM04Toby".
    # All EXCEPT the CCD-info work this way, because there may be a special case where the
    # Player has over 33 cards in his/her collected-stack and since it takes 3 characters to
    # save a card it would go over 100 with 34 cards and the size wouldn't match
    # Called by Game.save_game()
    def save_game(self):
        text = ''
        name = self._name
        name_len = str(len(name))
        if (int(name_len) < 10):
            name_len = '0' + name_len
        text += "NAM" + name_len + name # Name
        pts = str(self._points)
        if (int(pts) < 10):
            pts = '0' + pts
        text += "PTS" + pts # Points
        cot = str(self._round_cottages)
        if (int(cot) < 10):
            cot = '0' + cot
        text += "COT" + cot # Cottages
        if (self._played_this_turn):
            text += "PLD01" # has already played this turn
        else:
            text += "PLD00"
        if (self._taken_cards):
            text += "TKN01" # Has already taken cards this turn
        else:
            text += "TKN00"
        card_text = ''
        for card in self._hand:
            card_text += card.save_card()
        card_text += "END"  # End of the hand
        card_len = str(len(card_text))
        if (int(card_len) < 10):
            card_len = '0' + card_len                        
        text += "HND" + card_len + card_text   # Hand
        card_text = ''
        for card in self._collected:
            card_text += card.save_card()
        card_text += "END"  # End of the cottages
        card_len = str(len(card_text))
        if (int(card_len) < 10):
            card_len = '0' + card_len
        if (int(card_len) < 100):   # If < 10 then of course it's also < 100
            card_len = '0' + card_len
        text += "CCD" + card_len + card_text   # Collected
        text += "---"   # End of the player block
        
        text_len = str(len(text))
        if (int(text_len) < 100):   # size of the whole Player-save-info
            text_len = '0' + text_len
        final = "PLR" + self._type + text_len + text
        return final
        
    # Loads the data written by save_game() to retrieve a player's info from a string
    # All headers are the same as in save_game() and the sizes match. The game is set
    # in the Game-class' load_game().
    # Called by Game.load_game()
    def load_game(self, chunk):
        part = chunk[0:3]    # Read the first header
        while (part != "---"):
            chunk = chunk[3:len(chunk)]
            if (part == "NAM"):     # name
                try:
                    size = int(chunk[0:2])
                except ValueError:
                    return False
                chunk = chunk[2:len(chunk)]
                name = chunk[0:size]
                chunk = chunk[size:len(chunk)]
                self.set_name(name)
            elif (part == "PTS"):     # points
                points = int(chunk[0:2])
                self.add_points(points)
                chunk = chunk[2:len(chunk)]
            elif (part == "COT"):     # cottages this round
                try:
                    points = int(chunk[0:2])
                except ValueError:
                    return False
                n = 0
                while (n < points):
                    self.add_cottage()
                    n += 1
                chunk = chunk[2:len(chunk)]
            elif (part == "PLD"):     # played this turn
                try:
                    played = int(chunk[0:2])
                except ValueError:
                    return False
                if (played != 0):   # False by default
                    self._played_this_turn = True
                chunk = chunk[2:len(chunk)]
            elif (part == "TKN"):     # taken this turn
                try:
                    taken = int(chunk[0:2])
                except ValueError:
                    return False
                if (taken != 0):    # False by default
                    self._taken_cards = True
                chunk = chunk[2:len(chunk)]
            elif (part == "HND"):     # hand
                try:
                    size = int(chunk[0:2])
                except ValueError:
                    return False
                chunk = chunk[2:len(chunk)]
                hand = chunk[0:size]
                chunk = chunk[size:len(chunk)]
                info = hand[0:3]
                while (info != "END"):
                    hand = hand[3:len(hand)]
                    card = Card(1, Card.SPADES) # Just to init
                    loaded = card.load_card(info)        # This loads the card properly
                    if not (loaded):
                        return False
                    card.set_position("Hand")
                    self._hand.append(card) # add card to hand 
                    info = hand[0:3]
                # /while
            elif (part == "CCD"):     # collected
                try:
                    size = int(chunk[0:3])
                except ValueError:
                    return False
                chunk = chunk[3:len(chunk)]
                collected = chunk[0:size]
                chunk = chunk[size:len(chunk)]
                info = collected[0:3]
                while (info != "END"):
                    collected = collected[3:len(collected)]
                    card = Card(1, Card.SPADES) # Just to init
                    card.load_card(info)
                    self._collected.append(card)
                    info = collected[0:3]
                # /while
            else:   # Unknown header
                return False
            part = chunk[0:3]   # Read the next header
        # /while
        return True    
            
    ###############################################################################################    
    ###############################################################################################
        