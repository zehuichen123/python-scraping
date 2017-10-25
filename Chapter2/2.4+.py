#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(articleUrl):
	html=urlopen('http://en.wikipedia.org'+articleUrl)
	BSObj=BeautifulSoup(html,'html.parser')
	try:
		print(BSObj.h1.get_text())
		print(BSObj.find(id="mw-content-text").findAll('p')[0])
		print(BSObj.find(id='ca-edit').find('span').find('a').attrs['href'])
	except AttributeError:
		print('lack of some attributes, but not neccessay')

	for link in BSObj.findAll('a',href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# we meet a new page never met before
				newPage=link.attrs['href']
				print('-----------\n'+newPage)
				# print(newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")
# warnings: href is an attribute of html label, so do
# not forget to add .attrs after link!!!