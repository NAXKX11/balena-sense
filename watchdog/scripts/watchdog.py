#!/usr/bin/env python3

import urllib.request
import time
import os

def urlfetch(url):
	return urllib.request.Request(
		url,
		data = None,
		headers = {
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
		}
	)

while 1:
	url = 'https://jamesdrakewilson.com/watchdog.php?key=&method=add&watchdog=home-sense-%s&timer=125' % (os.environ.get('RESIN_DEVICE_NAME_AT_INIT'))
	req = urlfetch(url)
	data = urllib.request.urlopen(req).read()

	time.sleep(60)

