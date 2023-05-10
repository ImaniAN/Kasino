'''
Created on 22.2.2014

@author: Paleksi
'''

from PyQt4 import QtGui, QtCore
from GUILogic import GUILogic
from sidepanel import SidePanel
from tablegui import TableGUI
from handgui import handGUI
from textbox import TextBox

class MainWindow(QtGui.QMainWindow):
    '''
    Creates the main window for the program and creates the widgets and menus for it.
    Works as a path for GUILogic, sidepanel, tablegui and handgui to contact each other.
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.tablegui = TableGUI(self)
        self.setCentralWidget(self.tablegui)    # Central Widget
        self.gui = GUILogic(self)
        self.sidepanel = SidePanel(self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.sidepanel)
        self.handgui = handGUI(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.handgui)
        self.textbox  = TextBox(self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.textbox)
        
        self.handgui.setStatusTip("Your hand.")
        self.tablegui.setStatusTip("Table")
        
        self.sidepanel.setFixedWidth(100)
        self.handgui.setFixedWidth(100)
        
        menubar = QtGui.QMenuBar(self)
        self.setMenuBar(menubar)
        self.menubar = self.create_menus(menubar)
        self.statusbar = self.statusBar()
        self.resize(850,680)
        self.setWindowTitle("Kasino")
        self.setMinimumSize(700, 500)
        
        text = "Welcome to play Kasino!"
        self.textbox.update_text(text)
        
    # Getters
    ########################################
    def get_sidepanel(self):
        return self.sidepanel
    
    def get_menubar(self):
        return self.menubar
    
    def get_guilogic(self):
        return self.gui
    
    def get_tablegui(self):
        return self.tablegui
    
    def get_handgui(self):
        return self.handgui
    
    def get_textbox(self):
        return self.textbox
    
    ########################################
    
    def create_menus(self, menubar):
        # File menu
        fileMenu = menubar.addMenu("&File")
        # File actions
        newAction = fileMenu.addAction("&New Game")
        saveAction = fileMenu.addAction("&Save")
        loadAction = fileMenu.addAction("&Load")
        fileMenu.addSeparator()
        exitAction = fileMenu.addAction("E&xit")
        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Start a new game.')
        newAction.triggered.connect(self.newAct)
        
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save your current game.')
        saveAction.triggered.connect(self.saveAct)
        
        loadAction.setShortcut('Ctrl+O')
        loadAction.setStatusTip('Load game.')
        loadAction.triggered.connect(self.loadAct)

        exitAction.setStatusTip('Exit application.')
        exitAction.triggered.connect(self.close)    # built-in close thingy
        
        # Help menu
        helpMenu = menubar.addMenu("&Help")
        # Help actions
        rulesAction = helpMenu.addAction("&Rules and hints")
        aboutAction = helpMenu.addAction("&About")
        
        rulesAction.setStatusTip('Show rules of the game.')
        rulesAction.triggered.connect(self.rulesAct)
        aboutAction.setStatusTip('Show information about the game.')
        aboutAction.triggered.connect(self.aboutAct)
        
        return menubar
        
        
    def newAct(self):
        self.sidepanel.enable_buttons()
        self.gui.new_game()
        
    def saveAct(self):
        if (self.gui.get_game() != None):
            fileName = QtGui.QFileDialog.getSaveFileName(None, 'Save Game', '', '.txt')
            self.gui.save_game(fileName)
        else:   # In case of trying to save a game with no game on
            box = QtGui.QMessageBox()
            box.setWindowTitle("Error")
            box.setIcon(QtGui.QMessageBox.Critical)
            box.setText("You must create a game first!")
            box.addButton(QtGui.QMessageBox.Ok)
            box.exec_()
            
    def loadAct(self):
        fileName = QtGui.QFileDialog.getOpenFileName(None, 'Load Game', '', '.txt')
        if (fileName):
            self.gui.load_game(fileName)
        
    def rulesAct(self):
        try:
            file = open("rules.txt", 'r')
            text = ''
            box = QtGui.QMessageBox()
            box.setWindowTitle("Rules and hints")
            for line in file:
                line = line.rstrip()
                text += line + '\n'
            box.setText(text)
            box.setFixedSize(400,300)
            box.exec_()        
        except IOError:
            error = QtGui.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("An error occured while trying to open the file.")
            error.exec_()
    
    def aboutAct(self):
        about = QtGui.QMessageBox()
        about.setWindowTitle("About")
        about.setText("This game was made for the Python course CSE-A1121 in Spring 2014.\n" + \
                      "Project done by Aleksi Simell.")
        
        about.exec_()
        