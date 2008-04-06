# -*- coding: utf-8 -*-

import serial,os,pylot_config,pylot_notification
ser = serial.Serial(pylot_config.portNumber,19200, timeout=0)

    
def test():
    """Function for testings"""
    command = "echo \"Tratat!\" | osd_cat -c green -s 2 -p middle -d 1"
    os.system(command)
    print "pętla"
    temp=ser.read()
    ser.flushInput()
    print temp
    x=ord(temp)
    print x


def watch():
    """Get remote code and perform an action"""
    try: 
        temp=ser.read()
        ser.flushInput()
        x=ord(temp)
        ### switching between progz ###
        if x == 55: #amarok
            pylot_config.whatIsEnabled = "amarok"
            print "amarok"
        elif x == 54: #kaffeine
            pylot_config.whatIsEnabled = "kaffeine"
            print "kaffeine"
        elif x == 50: #smplayer
            pylot_config.whatIsEnabled = "smplayer" 
            print "smplayer"
            ###bindings ###
        elif pylot_config.whatIsEnabled == "amarok":  # amarok
            if x == 32: command='dcop amarok player prev' 
            if x == 33: command='dcop amarok player next' 
            if x == 10: command='dcop amarok player stop' 
            if x == 0:  command='dcop amarok player play' 
            if x == 14: command='dcop amarok player playPause' #works as pause/play
            if x == 59: command='dcop amarok player playPause' #works as pause/play
            if x == 16: command='dcop amarok player volumeUp' 
            if x == 17: command='dcop amarok player volumeDown' 
            if x == 13: command='dcop amarok player mute'  #mute/unmute
            if x == 60: command='dcop amarok player showOSD'
            if x == 45 or x >= 1 and x <=9: command='dcop amarok player setRating ' + str(x) #rate a song!
        elif pylot_config.whatIsEnabled == "kaffeine": #kaffeine
            if x == 32: command='dcop kaffeine KaffeineIface posPlus' #go forword
            if x == 33: command='dcop kaffeine KaffeineIface posMinus' #rewind
            if x == 10: command='dcop kaffeine KaffeineIface stop' #hmm 
            if x == 0:   command='dcop kaffeine KaffeineIface play' #start playing from a begining
            if x == 14: command='dcop kaffeine KaffeineIface pause' #works as pause/play
            if x == 59: command='dcop kaffeine KaffeineIface pause' #works as pause/play
            if x == 17: command='dcop kaffeine KaffeineIface volDown' 
            if x == 16: command='dcop kaffeine KaffeineIface volUp' 
            if x == 13: command='dcop kaffeine KaffeineIface mute'  #mute/unmute
        elif pylot_config.whatIsEnabled == "smplayer": #smplayer
            if x == 14: command='smplayer -send-action pause'#works as pause/play
            if x == 59: command='smplayer -send-action pause'#works as pause/play
            if x == 10: command='smplayer -send-action stop'
            if x == 0: command='smplayer -send-action play'
            if x == 16: command='smplayer -send-action increase_volume'
            if x == 17: command='smplayer -send-action decrease_volume'
            if x == 13: command='smplayer -send-action mute'  #mute/unmute
            if x == 5: command='smplayer -send-action dec_sub_scale' #decrease subtitles
            if x == 8: command='smplayer -send-action inc_sub_scale' #increase subtitles
            if x == 7: command='smplayer -send-action rewind1' #small jump
            if x == 9: command='smplayer -send-action forward1'
            if x == 4: command='smplayer -send-action rewind2' #madium jump
            if x == 6: command='smplayer -send-action forward2'
            if x == 1: command='smplayer -send-action rewind3'#large jump
            if x == 3: command='smplayer -send-action forward3'
        else:
            print "This text should never be printed"
        os.system(command)
        print 'Keycode: ' + str(x) + ' = ' + command #useful for configure bindings
    except:
        try: #nice construction, huh?
            print 'Keycode: ' + str(x) + ' isn\'t binded'#useful for configure bindings
            pylot_notification.msg(pylot_config.whatIsEnabled,  "sterowanie aktywne")
        except:
            pass
        pass
    return pylot_config.whatIsEnabled
   


        #ser.close() #here?
