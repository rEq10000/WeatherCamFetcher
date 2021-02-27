import datetime
import urllib.request
import time
import os

camname = "NameHere"

os.system("title " + camname + "CamFetcher")

curvalue = 0

starttime = datetime.datetime.now().strftime('%H:%M:%S')
startdate = datetime.datetime.now().strftime('%Y-%m-%d')

started = (startdate + " " + starttime)

while True:

	url = "urlhere"

	times = datetime.datetime.now().strftime('%H.%M.%S')
	date = datetime.datetime.now().strftime('%Y-%m-%d')

	timerr = (date + " " + times)
	full_name = (camname + "_" + timerr + ".jpg")

	urllib.request.urlretrieve(url, full_name)

	curvalue = 1 + curvalue
	
	sleeptime = 900

	with open ('CamFetcher.html', 'w') as f:
		f.write('<html> <body> <h1>' + camname + 'CamFetcher</h1> <ul> <li>Last download: ' + timerr + '</li> <li>Started at: ' + started + '</li> <li>Images downloaded this session: ' + str(curvalue) + '</li> <li> Image URL: ' + url + '</li> <li> Next picture in ' + str(sleeptime) + ' seconds</li> </ul> <p>Last Image Downloaded:</p> <img src="' + full_name + '" </body> </html>')

	print("Image downloaded! Image: " + full_name)
	print("Next picture in 15 minutes...")
	print("Images downloaded this session: " + str(curvalue))
	print("")

	time.sleep(sleeptime)