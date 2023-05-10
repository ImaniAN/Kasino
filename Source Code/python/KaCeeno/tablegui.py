'''
Created on 2.3.2014

@author: Paleksi
'''
from PyQt4 import QtGui
from cardgui import cardGUI

class TableGUI(QtGui.QFrame):
    '''    
    Parent of this GUI is the MainWindow.
    
    Handles the GUI of the table. The table is given to is a parameter when
    updating the table so this class knows nothing of the game. First I had
    the scaling of the TableGUI when the window is resized, but since my original
    plan didn't work, I'm not using it anymore.
    '''
    CARDS_PER_COL = 2   # How many cards are listed for each column

    def __init__(self, parent=None):
        super(TableGUI, self).__init__(parent)
        
        self.background = QtGui.QPixmap("Images/background2.png")
        self.layout = None
        self.setUp()
        
        
    def setUp(self):

        self.layout = QtGui.QGridLayout(self) # card layout     
        self.setLayout(self.layout)
        self.setStyleSheet("TableGUI {background-image: url(Images/background2.png);}") # Set background

    
    def clear_table(self, deck_amount):
        limit = int(((52*deck_amount) / 2) + 1)
        for n in range(0,limit):
            broken = False
            for i in range(0,TableGUI.CARDS_PER_COL):
                if (self.layout.itemAtPosition(i, n)):
                    widget = self.layout.itemAtPosition(i, n).widget()
                    self.layout.removeWidget(widget)
                    widget.deleteLater()
                else:   # No more items on the table
                    broken = True
                    break
            if (broken):
                break
        
    # Called every time window size is changed or something happens on the table
    def update_table(self, table=None):
        if (table==None):
            return
        row = col = 0
        deck_amount = self.parent().get_guilogic().get_game().get_amount_of_decks()
        self.clear_table(deck_amount)
        for card in table.get_cards():
            cardgui = cardGUI(card, self)   # Create CardGUI for each card
            if (row >= TableGUI.CARDS_PER_COL):
                col += 1
                row = 0  
            self.layout.addWidget(cardgui, row, col)
            cardgui.get_label().show()
            cardgui.setStatusTip("Table: " + str(card))
            row += 1
            