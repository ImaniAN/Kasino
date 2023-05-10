'''
Created on 4.5.2014

@author: Paleksi
'''

from PyQt4 import QtGui, QtCore
from game import Game

class newGameDialog(QtGui.QDialog):
    '''
    The dialog that appears when a new game is started. It asks the player types, names
    and amount of decks. They are transformed to a good format in the get_names() and 
    get_types() function so we don't have to make the complicated changes elsewhere.
    This dialog enables that the human players have not got to be first and it adds a
    little extra surprise to the game.
    '''


    def __init__(self, player_amount, parent=None):
        super(newGameDialog, self).__init__(parent)
        self.player_amount = player_amount
        self.name_edits = []    # List of QLineEdits
        self.name_labels = []   # List of QLabels
        self.type_edits = []    # List of QComboBoxes
        self.deck_edit = QtGui.QComboBox()
        self.layout = QtGui.QVBoxLayout(self)
        self.setUp()
        self.setFixedWidth(300)
        
    def setUp(self):
        okButton = QtGui.QPushButton("Ok")
        cancelButton = QtGui.QPushButton("Cancel")
        type_list = Game.PLAYER_TYPES
        # Player setup
        for n in range(0, self.player_amount):
            text = "Player " + str(n+1)
            self.name_labels.append(QtGui.QLabel(text + ':'))
            self.name_edits.append(QtGui.QLineEdit(text))
            self.type_edits.append(QtGui.QComboBox())
            for pType in type_list:
                self.type_edits[n].addItem(pType)
                
        player_layout = QtGui.QGridLayout()
        pWidget = QtGui.QWidget()
        for n in range (0, self.player_amount):
            player_layout.addWidget(self.name_labels[n], n, 0)
            player_layout.addWidget(self.name_edits[n], n, 1)
            player_layout.addWidget(self.type_edits[n], n, 2)
        
        pWidget.setLayout(player_layout)
        self.layout.addWidget(pWidget)
        
        # Deck setup
        dlayout = QtGui.QGridLayout()
        dlabel = QtGui.QLabel("Amount of Decks:")
        for n in range (0,3):
            self.deck_edit.addItem(str(n+1))    # numbers 1-3
        dlayout.addWidget(dlabel, 0, 0)
        dlayout.addWidget(self.deck_edit, 0, 1)
        dwidget = QtGui.QWidget()
        dwidget.setLayout(dlayout)
        self.layout.addWidget(dwidget)
        
        # Button setup
        button_layout = QtGui.QGridLayout()
        button_layout.addWidget(okButton, 0, 0)
        button_layout.addWidget(cancelButton, 0, 1)
        bWidget = QtGui.QWidget()
        bWidget.setLayout(button_layout)
        self.layout.addWidget(bWidget)
        
        # Button connections
        self.connect(okButton, QtCore.SIGNAL('clicked()'), self.verify)
        self.connect(cancelButton, QtCore.SIGNAL('clicked()'), self.refuse)
        
    # Buttons connections
    ########################################
    # Ok-clicked
    def verify(self):
        for n in range (0, self.player_amount):
            if (self.type_edits[n].itemText(self.type_edits[n].currentIndex()) == "Human"):
                current = self.name_edits[n].text()
                count = 0
                for name in self.name_edits:
                    if (current == name.text()):
                        count += 1
                if (count > 1):
                    warning = QtGui.QMessageBox()
                    warning.setWindowTitle("Warning")
                    warning.setText("The names must be unique")
                    warning.exec_()
                    return
                
        self.accept()
        
    # Cancel-clicked
    def refuse(self):
        self.reject()
    
    ########################################
        
    # Getters
    ########################################
    
    def get_names(self):
        names = []
        for name_line in self.name_edits:
            names.append(name_line.text())    
        return names
    
    def get_types(self):
        types = []
        for type_line in self.type_edits:
            types.append(type_line.itemText(type_line.currentIndex()))  
        return types
    
    def get_decks(self):
        return int(self.deck_edit.itemText(self.deck_edit.currentIndex()))
    