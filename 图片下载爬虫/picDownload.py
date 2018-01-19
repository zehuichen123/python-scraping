#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests,re
from bs4 import BeautifulSoup


url='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=saber&ct=201326592&ic=0&lm=-1&width=&height=&v=flip'
req=requests.get(url)
html=req.text
pic_url=re.findall('"objURL":"(.*?)",',html,re.S)


for i,each in enumerate(pic_url):
    print(each)
    try:
        pic=requests.get(each,timeout=5)
    except requests.exceptions.ConnectionError:
        print('图片加载失败')
        continue
    string='picture/'+str(i)+'.jpg'
    with open(string,'wb') as f:
        f.write(pic.content)