  #!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial,os
ser = serial.Serial(0,19200, timeout=None)

whatIsEnabled = 1 # 0=off   1=amarok(default)  2=kaffeine    3=smplayer

def test():
    command = "echo \"Tratat!\" | osd_cat -c green -s 2 -p middle -d 1"
    os.system(command)
    print "pętla"

def watch():
    temp=ser.read()
    ser.flushInput()
    x=ord(temp)
    print temp
    print x
    if x == 55: #amarok
        whatIsEnabled = 1
    elif x == 54: #kaffeine
        whatIsEnabled = 2
    elif x == 50: #smplayer
        whatIsEnabled = 3  
    elif whatIsEnabled == 1:  # amarok
        if x == 32:
            command='dcop amarok player prev' 
            #command='dcop amarok player showOSD'
        if x == 33:
            command='dcop amarok player next' 
#            command='dcop amarok player showOSD'
        if x == 10:
            command='dcop amarok player stop' 
        if x == 0:
            command='dcop amarok player play' 
#            command='dcop amarok player showOSD'
        if x == 14:
            command='dcop amarok player pause' 
        if x == 16:
            command='dcop amarok player volumeUp' 
        if x == 17:
            command='dcop amarok player volumeDown' 
        if x == 60:
            command='dcop amarok player showOSD'
    elif whatIsEnabled == 2: #kaffeine
        if x == 32:
            command='dcop amarok player prev' 
#            command='dcop amarok player showOSD'
        if x == 14:
            command='dcop kaffeine player pause' 
    elif whatIsEnabled == 3: #smplayer
        if x == 14:
            command='smplayer -send-action pause'
    else:
        print "This text should never be printed"

    os.command(command)

        #ser.close() #here?
