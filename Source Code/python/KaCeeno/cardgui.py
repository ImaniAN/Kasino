'''
Created on 6.3.2014

@author: Paleksi
'''
from PyQt4 import QtGui


class cardGUI(QtGui.QWidget):
    '''
    The parent of CardGUI is either the HandGUI or the TableGUI, depends where this
    constuctor is called. That's why to access the mainwindow we have to call the parent of
    this class' parent. BUT since HandGUI inherits QDockWidget and TableGUI inherits
    QFrame, then to access the HandGUI or the TableGUI we have to call self.parent().parent().
    I think... Also might be something to do with the super(...).__init__(parent) in this class
    I honestly don't know...
    
    The GUI of a Card-object. Knows the card it is connected to and handles the setting
    of a correct image for the card (selected or not selected). This Class has a
    mousePressEvent that handles the calling of set_image() with a correct parameter.
    '''


    def __init__(self, card, parent=None):
        super(cardGUI, self).__init__(parent)
        self.card = card
        self.selected = card.is_selected()
        self.selected_image = QtGui.QPixmap(self.card.get_select_image())
        self.not_selected_image = QtGui.QPixmap(self.card.get_image())
        self.label = QtGui.QLabel(self)
        self.set_image(self.selected)
        self.setMaximumSize(75, 100)
       
    # Getters and setters
    #####################################    
    def get_label(self):
        return self.label
    
    def get_card(self):
        return self.card
    
    def is_selected(self):
        return self.selected
    
    # called only by mousePressEvent() and init()
    def set_image(self, selected):
        if (selected): 
            pixmap = self.selected_image
            self.label.setPixmap(pixmap)
        else:
            pixmap = self.not_selected_image
            self.label.setPixmap(pixmap)
        
    #####################################      
    
    # Selects or de-selects cards from the hand or table
    # A card from the hand is always selected, after you first select one
    # since you have to play at least one card to the table in your turn.
    def mousePressEvent(self, event):
        pos = self.card.get_position()
        if (pos == "Hand"): # Card in hand
            gfather = self.parent().parent()    # HandGUI
            game = gfather.parent().get_guilogic().get_game()   # mainwindow.get_guilogic()
            # Disable selecting cards if player has already taken cards from the table
            if not (game.get_player_in_turn().has_taken()):
                hand = game.get_player_in_turn().get_hand()
                # Only 1 card from the hand may be selected at once
                for card in hand:
                    if (card.is_selected()):
                        card.select()   # de-select the already selected card
                        handcards = gfather.get_cards() # handgui.get_cards()
                        for cardgui in handcards:
                            if (cardgui.get_card() == card):    # De-select also the GUI
                                cardgui.selected = not cardgui.selected
                                cardgui.set_image(cardgui.is_selected())
                        # /for gui in hand
                        break
                # /for card in hand
                self.card.select()  # Select the new card. This prevents from desselecting a card if pressed the same cardgui again
                self.selected = not self.selected
                self.set_image(self.selected)
            # /if not taken
        # /if Hand
        else:   # pos == "Table"
            self.card.select()  # No restrictions to table cards
            self.selected = not self.selected
            self.set_image(self.selected)