#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import pymysql

db=pymysql.connect('localhost','root',
		'chlxgy5573108','netEase4',charset='utf8')
db2=pymysql.connect('localhost','root',
		'chlxgy5573108','old_ids4',charset='utf8')
print('link to netease')

cursor=db.cursor()
cursor2=db2.cursor()

cursor.execute("drop table if exists userinfo")
cursor2.execute("drop table if exists ids")

sql="""create table userinfo(
		sex char(7),
		songNum char(6),
		level char(3),
		name char(30),
		uid char(12))"""

sql2="""create table ids(
		uid char(11))"""
try:
	cursor.execute(sql)
	cursor2.execute(sql2)
except Exception as e:
	print(e)
	print('ha>>>???')
'''
#       insert
sql=""" insert into userinfo(sex,songNum,level,name,uid)
		VALUES('%s','%s','%s','%s','%s')"""%('male','14234','6','特别特别冷','1252534')
try:
	cursor.execute(sql)
	db.commit()
except Exception as e:
	print(e)
	db.rollback()
'''
#       search
'''
sql=""" select * from userinfo where uid='%s'"""%_id
try:
	cursor.execute(sql)
	results=cursor.fetchall()
	if len(results)==0:
		print('new uid')
	else:
		print('uid has already exists')
except Exception as e:
	print(e)
	print('Error: unable to fetch data')

sql="""select count(*) from userinfo"""
try:
	cursor.execute(sql)
	results=cursor.fetchall()
	print(results[0][0])
except Exception as e:
	print(e)
	print('opps')
'''
db.close()
db2.close()
