# -*- coding: utf-8 -*-
import pynotify
import pylot_config

    
def msg(title,  msg):
    if pylot_config.notyficationsEnabled:
        if pynotify.init("Pylot"):
            if title =="kaffeine":
                ico = "kaffeine"
            elif title == "amarok":
                ico = "amarok"
            elif title == "smplayer":
                ico = "smplayer"
            else:
                ico = pylot_config.directory + "ico.png"
            n = pynotify.Notification(title, msg, ico)
            n.set_timeout(pylot_config.notyficationsTimeout*1000)
            n.show()
        else:
            print "there was a problem initializing the pynotify module"
