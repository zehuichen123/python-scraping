#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj=BeautifulSoup(html,'html.parser')
for child in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(child)

# .children is to limit only find descendants
# that are children