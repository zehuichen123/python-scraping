#!/usr/bin/env python3
# coding:utf-8

from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

class SpiderMan(object):
	def __init__(self):
		self.manager=UrlManager()
		self.downloader=HtmlDownloader()
		self.parser=HtmlParser()
		self.output=DataOutput()

	def crawl(self,root_url):
		self.manager.add_new_url(root_url)

		while (self.manager.has_new_url() and 
			self.manager.old_url_size()<50):
			try:
				new_url=self.manager.get_new_url()
				html=self.downloader.download(new_url)
				if html==None:
					print('failded to get pages')
				new_urls,data=self.parser.parser(new_url,html)
				self.manager.add_new_urls(new_urls)
				self.output.store_data(data)
				print('has scraped %s links'%self.manager.old_url_size())
			except Exception as e:
				print('crawl failed')
		self.output.output_html()
		'''
		new_url=self.manager.get_new_url()
		#print(new_url)
		#print('----------1-------------')
		html=self.downloader.download(new_url)
		#print(html)
		#print('-----------2-------------')
		new_urls,data=self.parser.parser(new_url,html)
		#print('----------4---------------')
		#print(new_urls,data)
		self.manager.add_new_urls(new_urls)
		#print('-------------5-------------')
		self.output.store_data(data)
		self.output.output_html()
		#print('----------------66------------')
		#print('has scraped %s links'%self.manager.old_url_size())
		'''
if __name__=='__main__':
	spider_man=SpiderMan()
	spider_man.crawl('https://baike.baidu.com/item/%E6%97%85%E8%A1%8C%E9%9D%92%E8%9B%99')