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
	for link in BSObj.findAll('a',href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# we meet a new page never met before
				newPage=link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")
# warnings: href is an attribute of html label, so do
# not forget to add .attrs after link!!!