'''
Created on 26.2.2014

@author: Paleksi
'''

from PyQt4 import QtGui

class SidePanel(QtGui.QDockWidget):
    '''
    This Class is the panel on the left side of the main window. Initially the sidepanel
    has only 3 buttons, which all of are disabled. Once a game starts it will load the players'
    names and points under the buttons and update them every time a round ends. Once the game has
    ended, the three buttons are disabled again, unless a new game is started. The three buttons are
    "End turn", "Play card" and "Take cards".
    '''


    def __init__(self, parent=None):
        super(SidePanel, self).__init__(parent)
        
        self.buttons = []
        self.players = []       # QWidget objects
        self.game_players = []  # Player objects
        self.layout = self.setUp()
        
        
    def setUp(self):
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        layout = QtGui.QGridLayout()
        widget = QtGui.QWidget()
        widget.setLayout(layout)
        
        self.setWidget(widget)
        
        endButton = QtGui.QPushButton("End Turn")
        endButton.setStatusTip("End your turn.")
        endButton.setDisabled(True)
        endButton.clicked.connect(self.end_turn)
        self.buttons.append(endButton)
        
        playButton = QtGui.QPushButton("Play card")
        playButton.setStatusTip("Select a card from your hand and play it.")
        playButton.setDisabled(True)
        playButton.clicked.connect(self.play_card)
        self.buttons.append(playButton)
        
        takeButton = QtGui.QPushButton("Take cards")
        takeButton.setStatusTip("Take cards from the table.")
        takeButton.setDisabled(True)
        takeButton.clicked.connect(self.take_cards)
        self.buttons.append(takeButton)
        
        layout.addWidget(endButton, 0, 0)
        layout.addWidget(playButton, 1, 0)
        layout.addWidget(takeButton, 2, 0)
        
        return layout
    
    # Getter
    #####################################
    def get_layout(self):
        return self.layout
    
    #####################################
    
    # Called every time a new round begins or a new game.
    # Called by update_points()
    def init_players(self, players):
        self.clear()
        self.players = []
        self.game_players = players
        for player in players:
            pWidget = QtGui.QWidget()
            pLayout = QtGui.QGridLayout()
            name = QtGui.QLabel()
            name.setText(player.get_name())
            points = QtGui.QLabel()
            points.setText(str(player.get_points()))
            pLayout.addWidget(name, 0, 0)
            pLayout.addWidget(points, 0, 1)
            pWidget.setLayout(pLayout)
            self.players.append(pWidget)
    
    # Remove all the Players from the sidepanel when starting
    # a new game.
    def clear(self):
        for pwidget in self.players:
                pwidget.layout().removeItem(pwidget.layout().itemAtPosition(0, 0))
                pwidget.layout().removeItem(pwidget.layout().itemAtPosition(0, 1))
                self.layout.removeWidget(pwidget)
                pwidget.deleteLater()
       
    # Enable buttons when a game is loaded and disable buttons when a game ends. 
    ########################################
    def enable_buttons(self):
        for button in self.buttons:
            button.setDisabled(False)
    
    def disable_buttons(self):
        for button in self.buttons:
            button.setDisabled(True)
    ########################################
            
    # QPushButton
    def end_turn(self):
        player = self.parent().get_guilogic().get_game().get_player_in_turn()
        if (player.is_human()):
            if not (player.has_played()):
                warning = QtGui.QMessageBox()
                warning.setWindowTitle("Invalid move")
                warning.setText("You must play one card before ending your turn!")
                warning.exec_()
            else:
                    self.parent().get_guilogic().end_turn()
        
    # QPushButton
    def play_card(self):
        player = self.parent().get_guilogic().get_game().get_player_in_turn()
        if (player.is_human()):
            if (player.get_selected_card() == None):
                return
            self.parent().get_guilogic().play_card()
        
    # QPushButton    
    def take_cards(self):
        player = self.parent().get_guilogic().get_game().get_player_in_turn()
        if (player.is_human()):
            if not (player.has_played()):
                warning = QtGui.QMessageBox()
                warning.setWindowTitle("Invalid move")
                warning.setText("You must play one card before taking cards from the table!")
                warning.exec_()
            else:
                self.parent().get_guilogic().take_cards()
        
    # Called every time a new round begins
    def update_points(self):
        self.init_players(self.game_players)        
        n = len(self.buttons)+1 # Start putting players after the buttons
        for pWidget in self.players:
            self.layout.addWidget(pWidget, n, 0)
            n += 1