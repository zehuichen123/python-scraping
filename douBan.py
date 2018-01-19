#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from os import remove
from PIL import Image
import pickle
#import http.cookiejar as cookielib
url='https://www.douban.com/login'
data={'source':None,
	  'remember':'on'
	}

headers = {'Host':'www.douban.com',
           'Referer': 'https://www.douban.com/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding':'gzip, deflate, br'}

Session=requests.session()
# 读取是否保存有cookie
try:
	with open('cookie','rb') as f:
		Session.cookies=pickle.load(f)
		#这里我将读到的cookie输出
		print(Session.cookies)
# 如果没有cookie，就读入用户输入
except:
	data['form_email']=input('Please input your account:')
	data['form_password']=input('Please input your password:')

# 获得登陆界面的验证码
def get_captcha():
	req=requests.post(url,data=data)
	page_bf=BeautifulSoup(req.text,'html.parser')
	# 寻找验证码的图片（有可能不需要验证码 这时返回NULL）
	try:
		img_src=page_bf.find('img',id='captcha_image').get('src')
	except:
		return 'NULL','NULL'
	# 如果需要验证码下载该验证码并打开
	img=requests.get(img_src)
	if img.status_code==200:
		with open('captcha.jpg','wb') as f:
			f.write(img.content)
	image=Image.open('captcha.jpg')
	image.show()
	# 让用户根据验证码图片输入验证码
	captcha=input('please input the captcha:')
	remove('captcha.jpg')
	# 由于post-data里还要求captcha-id所以我从图片网址中截取id
	captcha_id=img_src[img_src.find('=')+1:]
	captcha_id=captcha_id[:captcha_id.find('&')]
	return captcha,captcha_id

def login():
	#获得验证码和验证码id
	captcha,captcha_id=get_captcha()
	if captcha!='NULL':
		data['captcha-solution']=captcha
		data['captcha-id']=captcha_id
	# 进行登陆
	page_login=Session.post(url,data=data,headers=headers)
	# 为了验证是否登陆成功我将登陆返回的页面html打印出来发现登陆失败
	#print(page_login.text)
	page_login_bf=BeautifulSoup(page_login.text,'html.parser')
	# 如果登陆成功就可以找到热点新闻并打印
	hot_topic=page_login_bf.find_all('a',class_='rec_topics_name')
	for i,topic in enumerate(hot_topic):
		print('%d.%s'%(i+1,topic.string))
	# 将此时的cookie保存方便下次登陆
	with open('cookie', 'wb') as f:
		pickle.dump(Session.cookies,f)

if __name__=='__main__':
	login()









