'''
Created on 12.3.2014

@author: Paleksi
'''

from PyQt4 import QtGui
from cardgui import cardGUI

class handGUI(QtGui.QDockWidget):
    '''
    The parent of this class is the MainWindow.
    
    The GUI of the player's hand. Removes all the previous CardGUI objects from Layout
    before making new CardGUI objects so that when the hand is about to finish, it will
    update correctly.
    '''


    def __init__(self, parent=None):
        super(handGUI, self).__init__(parent)
        
        self.layout = self.setUp()
        self.cards = [] # CardGUI objects
        
    def setUp(self):
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        layout = QtGui.QGridLayout()
        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)
        
        return layout
    
    #Getter
    #####################################
    def get_cards(self):
        return self.cards
    #####################################
    
    def clear_hand(self):
        # A hand can hold a maximum of 4 cards. The index 5 is just to make sure
        # we have all the cards removed
        for n in range(0,5):
            if (self.layout.itemAtPosition(n, 0)):
                widget = self.layout.itemAtPosition(n, 0).widget()
                self.layout.removeWidget(widget)
                widget.deleteLater()
    
    # Called every time a new turn begins, unless the player in turn is an AI.
    def update_hand(self, player=None):
        if (player == None):
            return
        self.clear_hand()
        n = 0
        self.cards = [] # Reset the hand
        for card in player.get_hand():
            cardgui = cardGUI(card, self)   # Create CardGUI for each card
            self.layout.addWidget(cardgui, n, 0)
            cardgui.get_label().show()
            self.cards.append(cardgui)
            cardgui.setStatusTip("Hand: " + str(card))
            n += 1
            