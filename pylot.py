#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylot ver. 0.1 by grizz - Witek Firlej http://grizz.pl

__author__    = "Witold Firlej (http://grizz.pl)"
__version__   = "0.2"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import sys,os,pydcop
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer, QThread #hmm quite stupid?
#from pylot_form import Ui_Form
#from pylot_settings_form import Ui_Dialog
import pylot_remote
import pylot_config
#from pylot_form import Ui_Form_Main # NO GUI so far


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #self.ui = Ui_Form_Main() #Only tray is needed so far
        #self.ui.setupUi(self)
#        self._Timer = QtCore.QTimer(self)
#        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.test)
        #self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.watch)
    
    def tray(self):
        self.tray=QtGui.QSystemTrayIcon(QtGui.QIcon(pylot_config.directory + "ico.png"))
        menu=QtGui.QMenu(self)
        myapp.connect(self.tray,QtCore.SIGNAL("activated (QSystemTrayIcon::ActivationReason)"),self.trayActivated)
        #menu.addMenu(self.statusMenu)
        #menu.addSeparator()
        #menu.addAction(self.tr("Close"),self.trayQuit)
        #app.connect(self.tray,QtCore.SIGNAL("activated (QSystemTrayIcon::ActivationReason)"),self.trayActivated)
        self.tray.setContextMenu(menu)
        self.tray.show()

    def trayActivated(self,reason):
        if reason==QtGui.QSystemTrayIcon.MiddleClick:
            myapp.close()
        else:
            self.tray.showMessage("Pylot", u'Kliknij środkowym przyciskiem by zamknąć', QtGui.QSystemTrayIcon.Information, 3000)
        # show or hide main window
#        if reason==QtGui.QSystemTrayIcon.Trigger:
#            if self.isHidden():
#                self.show()
#            else:
#                self.hide()
    
#    def closeEvent(self,event):
     #  event.ignore()   #switched of during testing
    # myapp.hide()

class A (QThread):
    def __init__(self):
        QThread.__init__(self)
        self._Timer = QtCore.QTimer(self)
#        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.test)
        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.watch)
        
    def start (self):
        self._Timer.start(pylot_config.timerDelay)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    #myapp.show() #maybe in future ;p
    myapp.tray() 
    #myapp._Timer.start(100)
    print 'Pylot ver.'+ __version__ +  ' by ' + __author__
    licznik=A()
    licznik.start()
    sys.exit(app.exec_())


