from Utils.utils import I_see_u 
from time import sleep

def run():
	while 1:
		try:
			Log = I_see_u('fjefefkefef',10)
			Log.Run()
		except Exception:
			sleep(120)
			 
run()
	