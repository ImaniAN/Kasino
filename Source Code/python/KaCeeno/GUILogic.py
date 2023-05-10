'''
Created on 24.2.2014

@author: Paleksi
'''
import random

from PyQt4 import QtGui, QtCore
from game import Game
from card import Card
from newgamedialog import newGameDialog

class GUILogic(QtGui.QFrame):
    '''
    The parent of this class is the MainWindow.
    
    Handles the basic GUI-logic of the game and has the game loop.
    Calls functions from the Game-class. Everything the game does,
    happens through here.
    '''
    
    SPEED = 100 # Game speed in ms

    def __init__(self, parent=None):
        super(GUILogic, self).__init__(parent)
        self.game = None
        self.running = False    # Boolean value whether the game is on. Used when creating a new game
        self.timer = QtCore.QBasicTimer()
        self.timerOn = False
        
    # Basic Getter
    ########################################
    def get_game(self):
        return self.game
    ########################################  
        
    # Update all the different GUI-parts separately
    def updateGUI(self):
        self.parent().get_sidepanel().update_points()
        self.parent().get_tablegui().update_table(self.game.get_table())
        self.parent().get_handgui().update_hand(self.game.get_player_in_turn())  
    
    def new_game(self): 
        # Request a confirmation if a game is already running
        if (self.running):
            confirm = QtGui.QMessageBox()
            choice = confirm.question(self, "Are you sure?", "Are you sure you want to start a new game?\n"
                                                             "All unsaved data will be lost.",
                                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if (choice == QtGui.QMessageBox.No):
                return
            
        player_amount = QtGui.QInputDialog.getInt(self, "New Game", "Number of players:", 0, Game.MIN_PLAYERS, Game.MAX_PLAYERS)
        names = []
        types = []
        if (player_amount[1]):  # Index 1 is a boolean value
            if (self.running):  # Clear the sidepanel if we already have a game going on
                self.parent().get_sidepanel().clear()
                
            dial = newGameDialog(player_amount[0])
            if not(dial.exec_()):   # New game cancelled
                return

            names = dial.get_names()
            types = dial.get_types()
            deck_amount = dial.get_decks()
            
            for ptype in types:
                if (ptype == "Surprise me!"):   # Random AI type
                    rand = random.randint(1,len(Game.PLAYER_TYPES) - 2)
                    ai_type = Game.PLAYER_TYPES[rand]
                    index = types.index(ptype)
                    types[index] = ai_type
                    
            n = 0
            final_names = []
            while (n < len(names)):
                if not (types[n] == "Human"):   # Change the AI-names to describe their types
                    j = 1
                    for name in final_names:
                        if (types[n] in name):
                            j += 1
                    final_names.append(types[n] + " " + str(j))
                else:   # Human player
                    final_names.append(names[n])
                n += 1
            
            game = Game()   # Create game
            game.new_game(final_names, types, deck_amount)    # make a new game
            self.game = game
            self.game.deal_cards()  # Deal cards for the new game
            self.running = True
            self.parent().get_sidepanel().init_players(self.game.get_players())
            self.parent().get_sidepanel().enable_buttons()
            self.updateGUI()
    
            self.parent().get_textbox().clear_text()    # Clear old text
            text = "==New Game=="
            self.parent().get_textbox().update_text(text)
            player = self.game.get_player_in_turn()
            text = "==It is " + player.get_name() + "\'s turn now=="
            self.parent().get_textbox().update_text(text)
            
            self.timer.start(GUILogic.SPEED, self)
            self.timerOn = True
        # /if player_amount
    # /new_game()
        
    def save_game(self, filename):
        if (len(filename) > 0):
            message = self.game.save_game(filename)
            message = "==" + message + "=="
            self.parent().get_textbox().update_text(message)
    
    def load_game(self, filename):
        game = Game()
        success, message = game.load_game(filename)
        if (success):
            self.parent().get_textbox().clear_text()
            self.game = game
            if not (self.timerOn):
                self.timer.start(GUILogic.SPEED, self)
            message = "==" + message + "=="
            self.parent().get_textbox().update_text(message)
            self.running = True
            self.parent().get_sidepanel().enable_buttons()
            self.parent().get_sidepanel().init_players(self.game.get_players())
            self.updateGUI()
            message = "==It is " + self.game.get_player_in_turn().get_name() + "\'s turn now=="
            self.parent().get_textbox().update_text(message)
            if (self.game.get_player_in_turn().has_played()):
                self.parent().get_textbox().update_text(self.game.get_player_in_turn().get_name() + " has played a card this turn")
            if (self.game.get_player_in_turn().has_taken()):
                self.parent().get_textbox().update_text(self.game.get_player_in_turn().get_name() + " has taken cards this turn")
        else:
            message = "==" + message + "=="
            self.parent().get_textbox().update_text(message)
    
    # The function that handles the checking of new rounds and whether the game is over
    # Also handles the ComputerPlayer turn-overview printing.
    ###################################################################################
    ###################################################################################
    def play(self):
        # Check if the game is over
        if not (self.game.game_over()):
            # Check if a new round should begin
            if (self.game.round_over()):
                self.get_round_overview()
                self.game.new_round()   # Initialize new round
                
                if (self.game.game_over()): # New points calculated
                    self.game_over()
                    return
                self.updateGUI()
                text = "==New round Starting=="
                self.parent().get_textbox().update_text(text)
            # /if round_over()
            # Check if the turn has ended
            if (self.game.has_turn_ended()):
                self.game.new_turn()
                if (self.game.get_player_in_turn().is_human()):
                    self.updateGUI()
                else:   # Don't update the hand if the player is not human
                    self.parent().get_sidepanel().update_points()
                    self.parent().get_tablegui().update_table(self.game.get_table())
                player = self.game.get_player_in_turn()
                text = "==It is " + player.get_name() + "\'s turn now=="
                self.parent().get_textbox().update_text(text)
            # /if has_turn_ended() 
            
            # AI-player turn
            if not (self.game.get_player_in_turn().is_human()):
                table_card_amount = len(self.game.get_table().get_cards())
                name, played_card, taken_cards = self.game.computer_turn()
                # Update the textbox before moving to the next turn
                # name = string
                # played_card = Card
                # taken_cards = List of list of Cards
                text = name + " played: " + str(played_card)
                self.parent().get_textbox().update_text(text)
                
                if (len(taken_cards) > 0): # Successful taking
                    i = 0
                    for cards in taken_cards:
                        text = name + " took:"
                        for card in cards:
                            i += 1
                            text += " " + str(card)
                        self.parent().get_textbox().update_text(text)
                    # /for
                    if (self.game.get_table().is_empty()):
                        if (i == table_card_amount):
                            text = name + " has emptied the table!"
                            self.parent().get_textbox().update_text(text)
            # /AI-player turn
                
        else:   # Should not be reached, unless loading a finished game
            self.game_over()
            
    ###################################################################################
    ###################################################################################
    
    # Called when the game is over by play()
    # Handles the printing of the winners to a QMessageBox, stops
    # the timer and disables the sidepanel buttons.
    def game_over(self):
        self.updateGUI()
        text = "==Game over==\n"
        text += "Thanks for playing!"
        self.parent().get_textbox().update_text(text)
        winners = self.game.get_winners()
        box = QtGui.QMessageBox()
        box.setWindowTitle("Game over!")
        if (len(winners) > 1):
            message = "The winners are:\n"
        else:
            message = "The winner is:\n"
        for player in winners:
            message += player.get_name() + "\n"
        message += "Amount of points: " + str(winners[0].get_points()) + "\n"
        message += "Congratulations!"
        box.setText(message)
        box.exec_()
        self.parent().get_sidepanel().disable_buttons()
        self.timer.stop()   # Stop the timer
        self.timerOn = False
        self.running = False
         
    # Called everytime a round has ended   
    def get_round_overview(self):
        # Round overview to the textBox
        text = "==Round over=="
        self.parent().get_textbox().update_text(text)
        for player in self.game.get_players():
            # Gather the info of the player
            name = player.get_name()
            cottages = player.get_cottages()
            collected = player.get_collected()
            col_amount = len(collected)
            spades = 0
            for card in collected:
                if (card.get_suit() == Card.SPADES):
                    spades += 1
            text = name + " collected " + str(col_amount) + " cards (" + str(spades) + " spades) this round and" \
                    " emptied the table "
            if (cottages == 1): # Grammar nazi strikes
                text += str(cottages) + " time.\n"
            else:
                text += str(cottages) + " times.\n"
            text += "Additionally " + name + " collected:\n"
            for card in collected:
                if (card.get_suit() == Card.DIAMONDS) and ((card.get_value() == 16) or (card.get_value() == 10)):
                    text += str(card) + " (2 pts)\n"
                if (card.get_suit() == Card.SPADES) and ((card.get_value() == 15) or (card.get_value() == 2)):
                    text += str(card) + " (1 pt)\n"
                if (card.get_value() == 1) or (card.get_value() == 14):
                    text += str(card) + "(1 pt)\n"
            self.parent().get_textbox().update_text(text)
        # /for
              
    # Game loop
    ########################################
    # Just calls the self.play() as long as there is a game running
    def timerEvent(self, event):
        if (event.timerId() == self.timer.timerId()):
                self.play()      
        else:
            # This was in the zetcode.com tutorial for the Tetris game, so I included it also.
            # Don't really know what it does.
            super(GUILogic, self).timerEvent(event)      
    ########################################
    # These are called from the buttons in sidepanel
    ########################################
    def play_card(self):
        self.game.play_card()
        player = self.game.get_player_in_turn()
        card = player.get_selected_card()
        text = player.get_name() + " played: " + str(card)
        self.parent().get_textbox().update_text(text)
    
    def take_cards(self):
        player = self.game.get_player_in_turn()
        cards = self.game.get_table().get_selected()
        amount = len(player.get_collected())    # Length of the collected stack before taking cards
        self.game.take_cards()
        self.updateGUI()
        if (amount != len(player.get_collected())): # Successful taking
            text = player.get_name() + " took:"
            for card in cards:
                text += " " + str(card)
            self.parent().get_textbox().update_text(text)
            if (self.game.get_table().is_empty()):
                text = player.get_name() + " has emptied the table!"
                self.parent().get_textbox().update_text(text)
        else:
            text = player.get_name() + " couldn't take the card(s) (not the same value)."
            self.parent().get_textbox().update_text(text)
        
    def end_turn(self):
        player = self.game.get_player_in_turn()
        self.game.end_turn()
        text = "==" + player.get_name() + " ended his/her turn=="
        self.parent().get_textbox().update_text(text)
    ########################################