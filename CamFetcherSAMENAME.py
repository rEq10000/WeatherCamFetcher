import datetime
import urllib.request
import time
import os

camname = "NameHere"

os.system("title " + camname + "CamFetcher")

while True:

    url = "urlhere"

    times = datetime.datetime.now().strftime('%H.%M.%S')
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    timerr = (date + " " + times)
    full_name = (camname + "IMG_" + timerr + ".jpg")

    urllib.request.urlretrieve(url, full_name)

    print("Image downloaded! Image: " + full_name)
    print("Next picture in 15 minutes...")
    print("")

    time.sleep(900)
