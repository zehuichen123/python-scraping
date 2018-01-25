#!/usr/bin/env python3
# coding:utf-8

import requests
class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			return None
		user_agent='Mozilla/4.0(compatible; MSTE 5.5;Windows NT)'
		headers={'User-Agent':user_agent}
		r=requests.get(url,headers=headers)
		if r.status_code==200:
			return r.text
		return None