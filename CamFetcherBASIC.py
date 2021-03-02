import datetime
import urllib.request
import time

cn = "NameHere"

while True:

	url = "urlhere"

	ti = datetime.datetime.now().strftime('%H.%M.%S')
	da = datetime.datetime.now().strftime('%Y-%m-%d')

	tiD = (da + " " + ti)
	fn = (cn + "_" + tiD + ".jpg")

	urllib.request.urlretrieve(url, fn)

	print("Image downloaded \n")

	time.sleep(900)