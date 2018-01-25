#!/usr/bin/env python3
# coding:utf-8

import sqlite3

class DataOutput(object):
	def __init__(self):
		self.cx=sqlite3.connect("MTime.db")
		self.create_table('MTime')
		self.datas=[]

	def create_table(self,table_name):
		values='''
		id interger primary key,
		MovieId integer,
		MovieTitle varchar(40) Not NULL,
		RatingFinal Real Not NULL Default 0.0,
		RDirectorFinal Real Not NULL Default 0.0,
		TotalBoxOffice varchar(20) Not NULL,
		Rank integer Not NULL Default 0,
		ShowDays integer Not NULL Default 0,
		isRelease integer Not NULL
		'''
		self.cx.execute('Create table if not exists %s(%s)'
			    	''%(table_name,values))

	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)
		if len(self.datas)>10:
			self.output_db('MTime')

	def output_db(self,table_name):
		for data in self.datas:
			self.cx.execute("Insert into %s (MovieId,"
				"MovieTitle,RatingFinal,RDirectorFinal,"
				"TotalBoxOffice,Rank,ShowDays,isRelease)"
				 "values(?,?,?,?,?,?,?,?)"
				 ""%table_name,data)
			self.datas.remove(data)
		self.cx.commit()

	def output_end(self):
		if len(self.datas)>0:
			self.output_db('MTime')
		self.cx.close()
