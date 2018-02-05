#!/usr/bin/env python3
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import json
import csv

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
headers=['ID','UserName','Password','Age','Country']
rows=[(1001,'qiye','qiye_pass',24,'China'),
	  (1002,'mary','mary_pass',20,'USA')
	]
with open('qiye.csv','w') as f:
	f_csv=csv.writer(f)
	f_csv.writerow(headers)
	f_csv.wirterow(rows)























