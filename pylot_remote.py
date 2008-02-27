  #!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial,os
ser = serial.Serial(0,19200, timeout=None)
def test():
    command = "echo \"Tratat!\" | osd_cat -c green -s 2 -p middle -d 1"
    os.system(command)

def watch():    
    temp=ser.read()
    ser.flushInput()
    x=ord(temp)
    print temp
    print x
    if x == 12:
        loop="false"
    if x == 32:
        command='dcop amarok player prev' 
        os.system(command)
        command='dcop amarok player showOSD'
        os.system(command)
    if x == 33:
        command='dcop amarok player next' 
        os.system(command)
        command='dcop amarok player showOSD'
        os.system(command)
    if x == 10:
        command='dcop amarok player stop' 
        os.system(command)
    if x == 0:
        command='dcop amarok player play' 
        os.system(command)
        command='dcop amarok player showOSD'
        os.system(command)
    if x == 14:
        command='dcop amarok player pause' 
        os.system(command)
    if x == 16:
        command='dcop amarok player volumeUp' 
        os.system(command)
    if x == 17:
        command='dcop amarok player volumeDown' 
        os.system(command)
    if x == 60:
        command='dcop amarok player showOSD'
        os.system(command)
#ser.close() #here?
