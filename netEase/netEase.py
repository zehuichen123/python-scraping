#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author : lovesnowbest
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import pymysql
header={
	'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
datas = {
	'uid': '107948356',
	'type': '0',
	'params': 'omVn+M+0MLjIZemA9918G3f5KdkNonc9V858JCrRutQEUSoFW9d5+RjfEooWwEkm4L0FduF4tveH9frjgEPfBVcIKeMI+CMJQr9F9Rj/J370mfSjFzTH3M8R8EUUO1JmECbzdtXEaDQ9LJILWDBR8FE9zINdgO2F4FF8YYwclm35Og06qR7SXleDG0ZInf3MUWotx/i/7JodxnfsS9nzrw==',
	'encSecKey': '5eea474d42a3dbaa409d73a1fa71594616c770cc0e38f701f233c410001d604ef868df63441359098d9055ba8abf16e8a1523c3ac56023c1c4a43f9282a8fa5902b60fc3224605304586571a64fea107b1392a75595cfdbbae461427b449a14b91a5d932aad5c8269eb7aecead13d2aa6980630e48929b47a3a40962694443bb'
}
proxies = {
    'http': 'http://58.62.86.216:9999',
    'http': 'http://202.201.3.121:3128',
    'http': 'http://119.29.201.134:808',
    'http': 'http://61.155.164.112:3128',
    'http': 'http://123.57.76.102:80',
    'http': 'http://116.199.115.78:80'
}
old_ids2=pymysql.connect('localhost','root',
		'chlxgy5573108','old_ids2',charset='utf8')
db2=pymysql.connect('localhost','root',
		'chlxgy5573108','netEase2',charset='utf8')

cursor1=old_ids2.cursor()
cursor2=db2.cursor()

class urlManager(object):
	def __init__(self):
		self.new_ids=set()

	def has_new_id(self):
		return self.new_id_size()!=0

	def add_old_id(self,old_id):
		sql="""insert into ids(uid)
			VALUES('%s')"""%old_id
		try:
			cursor1.execute(sql)
			old_ids2.commit()
		except Exception as e:
			print(e)
			old_ids2.rollback()

	def get_new_id(self):
		new_id=self.new_ids.pop()
		self.add_old_id(new_id)
		return new_id

	def find_old_id(self,new_id):
		sql=""" select * from userinfo where uid='%s'"""%new_id
		try:
			cursor2.execute(sql)
			results=cursor2.fetchall()
			if len(results)==0:
				return True
			else:
				return False
		except Exception as e:
			print(e)
			print('Error: unable to fetch data')

	def add_new_id(self,new_id):
		if new_id is None or self.new_id_size()+self.old_id_size()>200000 or self.new_id_size()>1000:
			return
		if new_id not in self.new_ids and self.find_old_id(new_id):	
			self.new_ids.add(new_id)

	def add_new_ids(self,new_ids):
		if new_ids is None or len(new_ids)==0:
			return
		for new_id in new_ids:
			self.add_new_id(new_id)

	def new_id_size(self):
		return len(self.new_ids)

	def old_id_size(self):
		sql="""select count(*) from ids"""
		try:
			cursor1.execute(sql)
			results=cursor1.fetchall()
		except Exception as e:
			print(e)
			print('in old_id_size')
		return results[0][0]
	'''
	def save_id(self):
		with open('old_ids2.csv','a') as old_id_saver:
			old_id_writer=csv.writer(old_id_saver)
			for old_id in self.old_ids2:
				old_id_writer.writerow(old_id)
		with open('new_ids.csv','a') as new_id_saver:
			new_id_writer=csv.writer(new_id_saver)
			for new_id in self.new_ids:
				new_id_writer.writerow(new_id)
	'''
class htmlManager(object):
	def getUserInfo(self,new_id):
		url="http://music.163.com/user/home?id=" + str(new_id)
		
		user={}
		req=requests.get(url,headers=header,proxies=proxies)
		req_bs=BeautifulSoup(req.text,'html.parser')

		infoArea=req_bs.findAll("h2",{"id":"j-name-wrap"})
		infoArea_bs=BeautifulSoup(str(infoArea),'html.parser')
		user["name"]=infoArea_bs.find("span",{"class":"tit f-ff2 s-fc0 f-thide"}).text
		user["level"]=infoArea_bs.find("span",{"class":"lev u-lev u-icn2 u-icn2-lev"}).text
		sexInfo=infoArea_bs.findAll("i")[-1]["class"][-1][-1]
		if sexInfo=='1':
			user['sex']='male'
		else:
			user['sex']='female'
		song=req_bs.find("div",{"id":"rHeader"}).find("h4").text
		songNum=int(song[4:-1])
		user["songNum"]=songNum
		return user

	def getUserFollower(self,new_id):
		url = 'http://music.163.com/weapi/user/getfollows/%s?csrf_token=' % str(new_id)
		response=requests.post(url,headers=header,data=datas,proxies=proxies).content
		json_text=json.loads(response.decode('utf-8'))
		followers=json_text['follow']
		new_ids=[]
		for new_id in followers:
			new_ids.append(new_id['userId'])
		return new_ids

class dataOutput(object):
	def __init__(self):
		pass

	def output_data(self,info):  
		if info is None:
			return
		#with open('netEase2.csv','a') as csv_file:
			#writer = csv.writer(csv_file)
			#writer.writerow(info.values())
		sql=""" insert into userinfo(sex,songNum,level,name)
				VALUES('%s','%s','%s','%s')"""%(info['sex'],info['songNum'],info['level'],info['name'])
		try:
			cursor2.execute(sql)
			db2.commit()
		except Exception as e:
			print(e)
			db2.rollback()
			db2.close()

	def output_finish(self):
		db2.close()

class netEase2Spider(object):
	def __init__(self):
		self.manager=urlManager()
		self.parser=htmlManager()
		self.output=dataOutput()

	def crawl(self,root_id):
		self.manager.add_new_id(root_id)
		while (self.manager.has_new_id() and self.manager.old_id_size()<200000):
			try:
				new_id=self.manager.get_new_id()
				user=self.parser.getUserInfo(new_id)
				followers_id=self.parser.getUserFollower(new_id)
				self.manager.add_new_ids(followers_id)
				self.output.output_data(user)
				print('has get %s ids'%self.manager.old_id_size())
			except Exception as e:
				print(e)
		self.output.output_finish()

myspider=netEase2Spider()
myspider.crawl("123614459")




