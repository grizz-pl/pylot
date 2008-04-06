#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylot ver. 0.3 by grizz - Witek Firlej http://grizz.pl

__author__    = "Witold Firlej (http://grizz.pl)"
__version__   = "0.3"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import sys,os
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import QThread 
import pylot_remote
import pylot_config
import pylot_notification

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    
    def tray(self):
        self.tray=QtGui.QSystemTrayIcon(QtGui.QIcon(pylot_config.directory + "ico.png"))
        myapp.connect(self.tray,QtCore.SIGNAL("activated (QSystemTrayIcon::ActivationReason)"),self.trayActivated)
        self.tray.show()

    def trayActivated(self,reason):
        if reason==QtGui.QSystemTrayIcon.MiddleClick:
            myapp.close()
        else:
            self.tray.showMessage("Pylot", u'Kliknij środkowym przyciskiem by zamknąć', QtGui.QSystemTrayIcon.Information, 3000)
            pylot_notification.msg(pylot_config.whatIsEnabled,  "sterowanie aktywne")
        


class A (QThread):
    def __init__(self):
        QThread.__init__(self)
        self._Timer = QtCore.QTimer(self)
#        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.test)
        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), pylot_remote.watch)
#        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), self.tryIcoChange("1"))
        
    def start (self):
        self._Timer.start(pylot_config.timerDelay)
    
    def tryIcoChange(self, icoNumber):
        print icoNumber
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.tray() 
    print 'Pylot ver.'+ __version__ +  ' by ' + __author__
    pylot_notification.msg("Pylot ver. " + __version__, __author__)
    licznik=A()
    licznik.start()
    sys.exit(app.exec_())


