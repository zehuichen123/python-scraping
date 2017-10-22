#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj=BeautifulSoup(html,'html.parser')
nameList=bsObj.findAll("span",{"class":"green"})
for name in nameList:
	print(name.get_text())

# get_text() strips all tags from the document 
# you are working with and returns a string co-
# taining the text only.

# findAll(tag,attributes,recursive,text,limit,keywords)
# find(tag,attributes,recursive,text,keywords)
# recursive is a boolean defining whether to looks
# into children and children's children.

nameList2=bsObj.findAll(text="the prince")
print((nameList2))