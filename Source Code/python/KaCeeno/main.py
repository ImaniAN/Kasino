'''
Created on 18.2.2014

@author: Paleksi
'''

from PyQt4 import QtGui
from mainwindow import MainWindow
import sys

 
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
 
    gui = MainWindow()
    gui.show()
 
    sys.exit(app.exec_())