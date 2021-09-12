from pyHook import HookManager
from pynput import keyboard
from win32gui import PumpMessages, PostQuitMessage
import ckeys
import winsound
#import beepy
import os
import time
import pyttsx3
       

class Keystroke_Watcher(object):
    
    left = 37
    right = 39
    up = 38
    down = 40
    space = 32
    
    codes ={
        left:0x1E,
        right:0x20,
        up:0x11,
        down:0x1F,
        space:0x39
    }

    knames ={
        left:"left",
        right:"right",
        up:"up",
        down:"down",
        space:"space"
    }

    undo = 90 #z
    reset = 82 #r

    fresh_start = 220 #\ 
    start = 219 #[
    stop = 221 #]
    play = 186 #;
    save = 222 #'
    inputc = 73 #i
    load = 76 #l

    stop_rec = 79 #o
    pause_rec = 80 #p
    dec_rec = 189 #-
    inc_rec = 187 #+

    recording = False
    levelinput = False

    pno = 0
    rec = []

    keyboard = None

    lcode = ""
    levelname = ""
    levels = {
        "FO":"forest",
        "CA":"cavern",
        "SP":"space",
        "CH":"chasm",
        "FA":"fall",
        "GA":"garden",
        "MO":"mountain",
        "QU":"question",
        "DE":"depths",
        "AB":"abc"
    }

    engine = None
    folder = "baba record" #TODO get it with API
    
    def __init__(self):
        # initialize Text-to-speech engine
        self.engine = pyttsx3.init()
        self.announce("Launched")
        #exit()
        
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
   

    def on_keyboard_event(self, event):
        try:
            #print(event.KeyID)
            if not(self.recording or self.levelinput):
                if event.KeyID == self.fresh_start:
                    self.announce("New Recording started")
                    #beepy.beep(sound='coin')
                    self.recording = True
                    self.rec = []
                if event.KeyID == self.start:
                    self.announce("Continue record")
                    #beepy.beep(sound='coin')
                    self.recording = True
                if  event.KeyID == self.play:
                    #beepy.beep(sound='coin')
                    self.pno += 1
                    self.announce(f"Playback {self.pno} started")
                    print(self.rec)
                    for k in self.rec:
                        ks = self.codes[k]
                        print(f"{self.knames[k]} ", end = '', flush=True)
                        ckeys.press(ks)
                    #beepy.beep(sound='ready')
                    print()
                    self.announce(f"Playback {self.pno} ended")

                if  event.KeyID == self.save:
                    if self.levelname == "":
                        self.announce(f"Level not set. To Save, set level first by pressing I and entering level code")
                        #beepy.beep(sound='error')
                        return True
                    fname = self.getfilename(self.levelname)
                    if os.path.isfile(fname):
                        self.announce(f"Backing up {self.levelname}")
                        os.rename(fname, f'{fname[:-4]} - {time.strftime("%Y %m %d - %H %M %S")}.txt')
                    self.announce(f"Saving {self.levelname}")                    
                    with open(fname, 'w') as f:
                        for k in self.rec:
                            f.write(str(k) + '\n')
                            f.flush()
                    #beepy.beep(sound='coin')

                if  event.KeyID == self.inputc:
                    #beepy.beep(sound='coin')
                    self.announce("Enter level code")
                    self.levelinput = True
                    self.lcode = ""
                    return True
                    #TODO input level code once for save and load - done
                    #TODO level list
                    #TODO text to speech - prerecorded or used as library
                    #TODO playback speed +/- stop, pause, start

                if event.KeyID == self.load:
                    if self.levelname == "":
                        self.announce(f"Level not set. To Load, set level first by pressing I and entering level code")
                        #beepy.beep(sound='error')
                        return True
                    fname = self.getfilename(self.levelname)
                    if os.path.isfile(fname):
                        with open(fname, 'r') as f:
                            self.rec = [int(line.rstrip('\n')) for line in f]
                        self.announce(f"{self.levelname} loaded")
                        #beepy.beep(sound='ready')
                    else:
                        self.announce(f"{self.levelname} not found")
                        #beepy.beep(sound='error')
   
            if self.levelinput:           
                    self.lcode += chr(event.KeyID)
                    print(chr(event.KeyID),end="", flush=True)
                    winsound.Beep(4000, 10)
                    if len(self.lcode) == 4:
                        print()
                        self.announce("Level input done")
                        co = self.lcode[0:2]
                        no = self.lcode[2:4]
                        if co in self.levels:
                            self.levelname = f'{self.levels[co]}-{no}'
                            self.announce(f"{self.levelname} Level name set")
                            #beepy.beep(sound='ready')
                        else:
                            self.announce(f'Incorrect level code: {self.lcode}. {self.levelname} level name kept.')
                            #beepy.beep(sound='error')                        
                        self.levelinput = False
                        self.lcode = ""

            if self.recording:
                if  event.KeyID == self.stop:
                    self.announce("Recording stopped")
                    #beepy.beep(sound='ready')
                    self.recording = False
                if event.KeyID in (self.left, self.right, self.up, self.down, self.space):
                    self.rec.append(event.KeyID)
                    winsound.Beep(5000, 10)
                    print(f"{self.knames[event.KeyID]} ",end= "", flush = True)
                if  event.KeyID == self.undo:
                    if len(self.rec) == 0:
                        self.announce("Nothing to undo")
                        return True
                    k = self.rec.pop()
                    winsound.Beep(3000, 10)                 
                    print(f"Undone {self.knames[k]}")
                if  event.KeyID == self.reset:
                    self.announce("Reset")
                    #self.rec=[]
                
                            
            
        finally:
            return True
    
    def shutdown(self):
        PostQuitMessage(0)
        self.hm.UnhookKeyboard()
    
    def announce(self, text):
        print(text)
        self.engine.say(text)
        # play the speech
        self.engine.runAndWait()

    def getfilename(self, levelname):
        return f"{self.folder}/{levelname}.txt"



watcher = Keystroke_Watcher()
PumpMessages()