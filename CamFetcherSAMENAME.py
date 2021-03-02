import datetime
import urllib.request
import time
import os

camname = "NameHere"

os.system("title " + camname + "CamFetcher")

curvalue = 0

while True:

	url = "urlhere"

	times = datetime.datetime.now().strftime('%H.%M.%S')
	date = datetime.datetime.now().strftime('%Y-%m-%d')

	timerr = (date + " " + times)
	full_name = (camname + "_" + timerr + ".jpg")

	urllib.request.urlretrieve(url, full_name)
	
	curvalue = 1 + curvalue

	print("Image downloaded! Image: " + full_name)
	print("Next picture in 15 minutes...")
	print("Images downloaded this session: " + str(curvalue))
	print("")

	time.sleep(900)
