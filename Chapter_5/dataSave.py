#!/usr/bin/env python3
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import json
import csv
from lxml import etree
import re
# using json to save data
'''
url="http://seputu.com/"
r=requests.get(url)
print(r.text)
soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')

content=[]
for mulu in soup.find_all(class_='mulu'):
	h2=mulu.find('h2')
	if h2!=None:
		h2_title=h2.string
		my_list=[]
		for a in mulu.find(class_='box').find_all('a'):
			href=a.get('href')
			box_title=a.get('title')
			my_list.append({'href':href,'box_title':box_title})
		content.append({'title':h2_title,'content':my_list})


with open('temp.json','w')	as f:
	json.dump(content,f,indent=4)		
'''

# save as csv
'''
headers=['ID','UserName','Password','Age','Country']
rows=[(1001,'qiye','qiye_pass',24,'China'),
	  (1002,'mary','mary_pass',20,'USA')
	]
with open('qiye.csv','w') as f:
	f_csv=csv.writer(f)
	f_csv.writerow(headers)
	f_csv.writerow(rows)
'''

# get csv from file
'''
with open('qiye.csv') as f:
	f_csv=csv.reader(f)
	headers=next(f_csv)
	print(headers)
	print('-------')
	for row in f_csv:
		print(row)
'''
'''
r=requests.get('http://seputu.com/')
html=etree.HTML(r.text)
div_mulus=html.xpath('//*[@class="mulu"]')
pattern=re.compile(r'\s*\[(.*)\]\s+(.*)')

rows=[]

for div_mulu in div_mulus:
	div_h2=div_mulu.xpath('./*[@class="mulu-title"]/center/h2/text()')
	if len(div_h2)>0:
		#print(div_h2)		# this is a list here
		h2_title=div_h2[0]
		a_s=div_mulu.xpath('./*[@class="box"]/ul/li/a')
		for a in a_s:
			href=a.get('href')
			box_title=a.get('title')
			print(box_title)
			match=pattern.search(box_title)
			if match!=None:
				date=match.group(1)
				read_title=match.group(2)
				content=(h2_title,read_title,href,date)
				#print(content)
				rows.append(content)

headers=['title','real_title','href','date']
with open('temp1.csv','w') as f:
	f_csv=csv.writer(f)
	f_csv.writerow(headers)
	f_csv.writerow(rows)

'''






















