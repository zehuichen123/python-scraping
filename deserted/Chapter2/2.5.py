#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import datetime
import random
import re

pages=set()
random.seed(datetime.datetime.now())

# get all internalLinks in the current page
def getInternalLinks(bsObj,includeUrl):
	internalLinks=[]
	for link in bsObj.findAll('a',href=re.compile('^|.*'+includeUrl+')')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

# get all externalLinks in the current page
def getExternalLinks(bsObj,excludeUrl):
	externalLinks=[]
	for link in bsObj.findAll('a',href=re.compile('^(http|www)((?!"+excludeUrl+").)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts=address.replace('http://','').split('/')
	return addressParts

def getRandomExternalLink(startingPage):
	print('----')
	html=urlopen(startingPage)
	bsObj=BeautifulSoup(html,'html.parser')
	externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
	if len(externalLinks)==0:
		internalLinks=getInternalLinks(startingPage)
		return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalLinks(startingSite):
	externalLink=getRandomExternalLink(startingSite)
	print('random site is '+externalLink)
	followExternalLinks(externalLink)

followExternalLinks('http://oreilly.com')















