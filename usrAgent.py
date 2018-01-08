#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
url='http://www.whatismyip.com.tw/'
proxies={
	'http':'http://101.68.73.54:53281',
	'https':'http://101.68.73.54:53281'
}
head={}
head['user-agent']='Mozilla/5.0 (Linux; Android 4.1.1;Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
req=requests.get(url,headers=head,proxies=proxies)
print(req.text)