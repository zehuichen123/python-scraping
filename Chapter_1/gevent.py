#!/usr/bin/env python3
#from gevent import monkey;monkey.patch_all()
import gevent
import requests

def run_task(url):
	print('visit-->%s'%url)
	try:
		response=requests.get(url)
		data=response.text
		print('%d byte received from %s.'%(len(data),url))
	except Exception as e:
		print(e)

urls=['https://github.com/','https://lovesnowbest.site','https://www.baidu.com']
greenlets=[gevent.spawn(run_task,url) for url in urls]
gevent.joinalll(greenlets)