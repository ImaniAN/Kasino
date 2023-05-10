'''
Created on 18.2.2014

@author: Paleksi
'''

from player import Player
from computerplayer import GreedyAI, PassiveAI, RandomAI
from card import Card
from deck import Deck
from table import Table

class Game(object):
    '''
    Holds the actual game logic. Keeps track of the players, table and deck.
    Has a bunch of functions that are called from the user in GUILogic, but
    has no graphic elements in it, so could be used as an ASCII-game just as
    easily. This class calls the appropriate functions from Player-, Deck- and
    Table-classes, so some unnecessary repetitions may be found (like load_game()
    is called through MainWindow.load_game() --> GUILogic.load_game() -->
    self.load_game() though I have afterwards changed them to do something else 
    other than just call the next class's load_game() function).
    '''
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    POINTS_TO_WIN = 16
    PLAYER_TYPES = ["Human", "Greedy", "Passive", "Random", "Surprise me!"]
    # "Surprise me!" should ALWAYS be the last option


    def __init__(self):
        self._deck = None
        self._amount_of_decks = 0
        self._players = []
        self._table = None
        self.player_in_turn = None  # The Player object of who is playing
        self.dealer = 0     # Index of the Player who is the "dealer"
        self.turn_played = False
        
    
    # Setters and getters
    ########################################
    
    def set_deck(self, deck):
        self._deck = deck
        
    def set_table(self, table):
        self._table = table
        
    def add_player(self, player):
        self._players.append(player)
        
    def get_deck(self):
        return self._deck

    def get_amount_of_decks(self):
        return self._amount_of_decks

    def get_players(self):
        return self._players

    def get_table(self):
        return self._table
    
    def get_turn(self):
        return self.turn
    
    def get_player_in_turn(self):
        return self.player_in_turn
    
    def turn_over(self, over):
        self.turn_played = over
    
    # Called by the GUI- or UILogic
    def has_turn_ended(self):
        return self.turn_played
    
    ########################################
    
    def new_game(self, names, types, deck_amount):
        n = 0
        superDeck = Deck()
        self._amount_of_decks = deck_amount
        while (n < deck_amount):
            deck = Deck()  # Create deck
            deck.set_deck()
            for card in deck.get_cards():
                superDeck.set_card(card)
            n += 1
        superDeck.shuffle_deck()
        self.set_deck(superDeck)
        table = Table()
        self.set_table(table)
        n = 0
        while (n < len(names)):
            if (types[n] == "Human"):
                player = Player(names[n])    # Create players
            elif (types[n] == "Greedy"):
                player = GreedyAI(names[n])
            elif (types[n] == "Passive"):
                player = PassiveAI(names[n])
            elif (types[n] == "Random"):
                player = RandomAI(names[n])
            player.set_game(self)
            self._players.append(player)
            n+=1
        
        self.player_in_turn = self._players[0]  # First player starts
        self.dealer = len(self._players) - 1    # Last player is the dealer on the first round
        
    def round_over(self):
        empty_hands = 0
        for player in self._players:
            if (len(player.get_hand()) != 0):
                break
            empty_hands += 1
                
        if (empty_hands == len(self._players)):   # If all players have no cards left in hand
            return True
        return False
    
    # Reinitialize the deck and deal the cards, move the dealer position to the next player
    def new_round(self):
        self.count_points()
        if not (self.game_over()):
            superDeck = Deck()
            n = 0
            while (n < self._amount_of_decks):
                deck = Deck()  # Create a new deck
                deck.set_deck()
                for card in deck.get_cards():
                    superDeck.set_card(card)
                n += 1
            superDeck.shuffle_deck()
            self.set_deck(superDeck)
            self._table.reset_table()
            
            self.dealer = (self.dealer + 1) % len(self._players)
            self.deal_cards()
            self.next_player_turn()
            for player in self._players:
                player.new_round()  # Reset Collected-stacks, cottages and booleans for the players
    
    # Called every time new_round() is called
    def game_over(self):
        for player in self._players:
            if (player.get_points() >= Game.POINTS_TO_WIN):
                return True
        return False
    
    # Called every time new_round() is called
    def count_points(self):
        max_spades = -1
        max_cards = -1
        max_players = False    # A boolean to determine if more than 1 player has most collected cards
        spade_players = False  # A Similar boolean for most spades
        max_player = None
        spade_player = None
        # Go through all players
        for player in self._players:
            player.add_points(player.get_cottages())    # 1 point for each cottage
            spades = 0
            # Go through each collected card for the player
            for card in player.get_collected():
                if (card.get_suit() == Card.SPADES):
                    spades += 1
                if (card.get_value() == 14) or (card.get_value() == 1): # 1 point for each ace
                    player.add_points(1)
                if ((card.get_value() == 16) or (card.get_value() == 10)) and (card.get_suit() == Card.DIAMONDS):
                    player.add_points(2)    # 2 points for 10-Diamonds
                if ((card.get_value() == 15) or (card.get_value() == 2)) and (card.get_suit() == Card.SPADES):
                    player.add_points(1)    # 1 point for 2-Spades
            # /for
            if (spades > max_spades):
                max_spades = spades
                spade_players = False  # Reset the highest spades
                spade_player = player
            elif (spades == max_spades):
                spade_players = True    # More than one player has the most spades
                
            if (len(player.get_collected()) > max_cards):
                max_cards = len(player.get_collected())
                max_players = False     # Reset highest cards
                max_player = player
            elif (len(player.get_collected()) == max_cards):
                max_players = True  # More than one player has the most cards collected
        # /for
        if not (spade_players):
            spade_player.add_points(2)    # 2 points if there's only one who has the most spades
        if not (max_players):
            max_player.add_points(1)    # 1 point if there's only one who has the most cards
    # /count_points()
    
    # Called only when the game is over !!
    def get_winners(self):
        winners = []
        points = Game.POINTS_TO_WIN
        for player in self._players:
            if (player.get_points() > points):
                winners = []
                winners.append(player)
                points = player.get_points()
            elif (player.get_points() == points):
                winners.append(player)
                
        return winners
    # !!
    
    # Deal cards for the players and table. Error-handling added
    # if there were more than 13 players. Player-amount reduced
    # to 6, but could be changed so handling remains
    def deal_cards(self):
        for n in range(0,4):    # 4 cards for each player
            for player in self._players:
                if (len(self._deck.get_cards()) == 0):
                    return  # Error-handling for too many players
                player.draw_card()
        for n in range(0,4):    # 4 cards on the table
            if (len(self._deck.get_cards()) == 0):
                    return  # Error-handling for too many players
            card = self._deck.draw_card()
            self._table.place_card(card)
    
    def next_player_turn(self):
        i = self._players.index(self.player_in_turn) + 1    # Next index
        i = i % len(self._players)  # Check if it's over the player-amount
        self.player_in_turn = self._players[i]
    
    # The possible actions by the player during his/her turn.
    # The proper calling of these functions are handled in the UI/GUILogic.
    #####################################
    #####################################
    
    # Called when a new turn begins
    def new_turn(self):
        self.turn_over(False)
        self.next_player_turn()
    
    def end_turn(self):
        self.get_player_in_turn().end_turn()
        self.turn_over(True)
        cards = self._table.get_selected()
        for card in cards:  # Deselect all cards for the new turn
            card.select()
        if (self.round_over()): # Check if players have cards still in hand
            player = self._table.get_latest()
            if not (player == None):    # Cards have actually been taken this round
                player.take_cards(self._table.get_cards(), True)
            self._table.reset_table()
    
    def take_cards(self):
        player = self.player_in_turn
        cards = self._table.get_selected()
        player.take_cards(cards, False)    # Error handling in Player-class
        if (self._table.is_empty()):
            player.add_cottage()
    
    def play_card(self):
        player = self.player_in_turn
        card = player.get_selected_card()
        player.play_card(card)  # Error handling in Player-class
    
    # Plays the turn of an AI player
    # Called by the game loop
    def computer_turn(self):
        played_card, collected =  self.player_in_turn.play_turn()
        name = self.player_in_turn.get_name()
        card = played_card
        self.end_turn()
        return name, card, collected
    
    # Save and load functions   
    #####################################
    #####################################
    
    def save_game(self, filename):
        save_text = "KASINO001"
        for player in self._players:
            save_text += player.save_game()     # Player
        save_text += "DLR" + str(self.dealer)   # dealer
        name_len = str(len(self.player_in_turn.get_name()))
        if (int(name_len) < 10):
            name_len = '0' + name_len
        save_text += "PIT" + name_len + self.player_in_turn.get_name()  # Player-in-turn
        save_text += self._table.save_table()  # Table
        save_text += self._deck.save_deck()    # Deck
        save_text += "AOD" + str(self._amount_of_decks) # Amount of decks is always < 10
        save_text += "END000"
        
        try:
            parts = filename.split('.')
            if (len(parts) != 2):   # add '.txt' to the name if not already added
                filename += ".txt"
            file = open(filename, 'w')
            file.write(save_text)
            file.close()
            return "Game saved succesfully"
        except IOError:
            return "--!--And error occured while saving the game--!--"
    
    
    def load_game(self, filename):
        error_message = "--!--Error while loading the game: Invalid file--!--"
        try:
            file = open(filename, 'r')
            chunk = ''.join(self.read_fully(9, file))
            if (chunk != "KASINO001"):
                file.close()
                return False, error_message
            chunk = ''.join(self.read_fully(3, file)) # Read the next header
            while (chunk != "END"):
                if (chunk == "PLR"):    # Player
                    player_type = ''.join(self.read_fully(1, file))
                    try:
                        size = int(''.join(self.read_fully(3, file)))
                    except ValueError:
                        file.close()
                        return False, error_message
                    chunk = ''.join(self.read_fully(size, file))
                    # Create the right type of player with no name
                    if (player_type == "H"):   # Human
                        player = Player()
                    elif (player_type == "G"): # Greedy
                        player = GreedyAI()
                    elif (player_type == "P"): # Passive
                        player = PassiveAI()
                    elif (player_type == "R"):
                        player = RandomAI()
                    success = player.load_game(chunk)
                    if (success):
                        player.set_game(self)
                        self.add_player(player)
                    else:
                        file.close()
                        return False, error_message
                elif (chunk == "DLR"):    # Dealer
                    try:
                        dealer = int(''.join(self.read_fully(1, file)))
                    except ValueError:
                        file.close()
                        return False, error_message
                    self.dealer = dealer
                elif (chunk == "PIT"):    # Player-in-turn
                    try:
                        name_len = int(''.join(self.read_fully(2, file)))
                    except ValueError:
                        file.close()
                        return False, error_message
                    name = ''.join(self.read_fully(name_len, file))
                    for player in self._players:
                        if (player.get_name() == name):
                            self.player_in_turn = player
                    if (self.player_in_turn == None):   # Unable to set a player in turn
                        file.close()
                        return False, error_message
                elif (chunk == "TBL"):    # Table
                    try:
                        size = int(''.join(self.read_fully(3, file)))
                    except ValueError:
                        file.close()
                        return False, error_message
                    chunk = ''.join(self.read_fully(size, file))
                    table = Table()
                    name_len = int(chunk[3:5])
                    if (name_len > 0):
                        name = chunk[5:(5+name_len)]    # Set the latest player
                        for player in self._players:
                            if (player.get_name() == name):
                                table.set_latest(player)
                        if (table.get_latest() == None):  # Unable to find latest player
                            file.close()
                            return False, error_message
                    success = table.load_table(chunk, self) # The rest is handled here
                    if (success):
                        self.set_table(table)
                    else:
                        file.close()
                        return False, error_message
                elif (chunk == "DCK"):    # Deck
                    try:
                        size = int(''.join(self.read_fully(3, file)))
                    except ValueError:
                        file.close()
                        return False, error_message
                    chunk = ''.join(self.read_fully(size, file))
                    deck = Deck()   # Create empty deck
                    success = deck.load_deck(chunk)
                    if (success):
                        self._deck = deck
                    else:
                        file.close()
                        return False, error_message
                elif (chunk == "AOD"):  # Amount of Decks
                    try:
                        amount = int(''.join(self.read_fully(1, file)))
                        self._amount_of_decks = amount
                    except ValueError:
                        file.close()
                        return False,error_message
                else:   # Unknown chunk
                    file.close()
                    return False, error_message
                chunk = ''.join(self.read_fully(3, file)) # Read the next header
                
            # /while
            file.close()
            # Check that all the correct parts were in the save file
            if (len(self._players) == 0) or (self._table == None) or (self._deck == None) or (self.player_in_turn == None):
                return False, error_message
            return True, "Game loaded"  # Succesful loading
                
        except IOError:
            file.close()
            return False, error_message
    
    # Copy-paste from U3E1 chunkIO.py
    def read_fully(self, count, file):
        read_chars = file.read(count)
        
        # If the file end is reached before the buffer is filled
        # an exception is thrown.    
        if len(read_chars) != count:
            raise IOError("Unexpected end of file.")

        return list(read_chars)