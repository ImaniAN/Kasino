'''
Created on 20.3.2014

@author: Paleksi
'''

from PyQt4 import QtGui

class TextBox(QtGui.QDockWidget):
    '''
    The parent of this class is the MainWindow.
    
    The little text frame at the bottom of the screen that updates
    the events of each turn, just to make it easier to follow the game
    when playing especially with AI.
    '''


    def __init__(self, parent=None):
        super(TextBox, self).__init__(parent)
        self.layout = self.setUp()
        self.textbox = QtGui.QTextBrowser()
        self.layout.addWidget(self.textbox, 0, 0)
        self.textbox.setMinimumWidth(400)
        self.textbox.setFixedHeight(120)
        
    def setUp(self):
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        layout = QtGui.QGridLayout()
        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)
        
        return layout
        
    def update_text(self, text):
        self.textbox.append(text)
        
    def clear_text(self):
        self.textbox.clear()