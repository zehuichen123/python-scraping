#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests,sys,re
from bs4 import BeautifulSoup

#download txt of <long zu IV>
class downloader(object):
	def __init__(self):
		self.server='http://www.shunong.com/'
		self.target='http://www.shunong.com/xh/8692/'
		self.names=[]
		self.urls=[]
		self.nums=0

	def get_download_url(self):
		req=requests.get(url=self.target)
		req.encoding='utf-8'
		div_bf=BeautifulSoup(req.text)
		menu=div_bf.find_all('div',class_='book_list')
		chapter_bf=BeautifulSoup(str(menu[0]))
		chapter=chapter_bf.find_all('a')
		self.nums=len(chapter)
		for each in chapter:
			self.names.append(each.string)
			self.urls.append(self.server+each.get('href'))

	def get_contents(self,target):
		req=requests.get(url=target)
		req.encoding='utf-8'
		div_bf=BeautifulSoup(req.text)
		div=div_bf.find_all('div',class_='contentbox')
		texts=div[0].text.replace('\xa0'*8,'\n\n')
		return texts

	def writer(self,name,path,text):
		write_flag=True
		with open(path,'a',encoding='utf-8') as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')

dl=downloader()
dl.get_download_url()
print("《龙族IV奥丁之渊开始下载》：")
for i in range(dl.nums):
	dl.writer(dl.names[i],'龙族IV奥丁之渊.txt',dl.get_contents(dl.urls[i]))
	sys.stdout.write('downloading:%.3f%%'%float(i/dl.nums)*100+'\r')
	sys.stdout.flush()

print('download finished!')
'''
target='http://www.shunong.com/xh/8692/283851.html'
req=requests.get(url=target)
req.encoding='utf-8'
html=req.text
div_bf=BeautifulSoup(html)
div=div_bf.find_all('div',class_='contentbox')
texts=div[0].text.replace('\xa0'*8,'\n\n')
print(texts)
'''

'''
target='http://www.shunong.com/xh/8692/'
req=requests.get(url=target)
req.encoding='utf-8'
html=req.text
div_bf=BeautifulSoup(html)
menu=div_bf.find_all('div',class_='book_list')
chapter=BeautifulSoup(str(menu[0]))
a=chapter.find_all('a')
for each in a:
	print(each.string+' '+each.get('href'))

'''