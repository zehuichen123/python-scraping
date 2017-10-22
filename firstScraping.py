#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError and URLError as e:
		return None
	try:
		bsObj=BeautifulSoup(html.read(),"html.parser")
		title=bsObj.body.h1
	except AttributeError as e:
		print('h1 can not be found')
		return None
	return title

title=getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
	print('title could not be found')
else:
	print('title')
