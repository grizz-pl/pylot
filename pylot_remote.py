  #!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial,os,pylot_config
ser = serial.Serial(1,19200, timeout=0)
print "port otwarty"


def test():
    command = "echo \"Tratat!\" | osd_cat -c green -s 2 -p middle -d 1"
    os.system(command)
    print "pętla"
    temp=ser.read()
    ser.flushInput()
    print temp
    x=ord(temp)
    print x


def watch():
    try: 
        temp=ser.read()
        ser.flushInput()
        x=ord(temp)
        if x == 55: #amarok
            pylot_config.whatIsEnabled = 1
            print "amarok"
            pass
        elif x == 54: #kaffeine
            pylot_config.whatIsEnabled = 2
            print "kaffeine"
            pass
        elif x == 50: #smplayer
            pylot_config.whatIsEnabled = 3  
            print "smplayer"
            pass
        elif pylot_config.whatIsEnabled == 1:  # amarok
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
            pass
        elif pylot_config.whatIsEnabled == 2: #kaffeine
            if x == 32:
                command='dcop amarok player prev' 
            #            command='dcop amarok player showOSD'
            if x == 14:
                command='dcop kaffeine KaffeineIface pause' 
            pass
        elif pylot_config.whatIsEnabled == 3: #smplayer
            if x == 14:
                command='smplayer -send-action pause'
            pass
        else:
            print "This text should never be printed"
    
        os.system(command)
        print command
    except:
        x = 999
        command ="echo brak polecenia"
   


        #ser.close() #here?
