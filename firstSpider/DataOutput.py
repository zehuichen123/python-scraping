#!/usr/bin/env python3
# coding:utf-8

class DataOutput(object):
	def __init__(self):
		self.datas=[]
	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		with open('baike.html','w') as fout:
			print('begin to write')
			fout.write('<html>\n')
			fout.write('<head>\n')
			fout.write('<meta charset="UTF-8">\n')
			fout.write('</head>\n')
			fout.write('<body>\n')
			fout.write('<table>\n')
			for data in self.datas:
				fout.write('<tr>\n')
				fout.write('<td>%s</td>\n'%data['url'])
				fout.write('<td>%s</td>\n'%data['title'])
				fout.write('<td>%s</td>\n'%data['summary'])
				fout.write('</tr>\n')
				self.datas.remove(data)
			fout.write('</table>\n')
			fout.write('</body>\n')
			fout.write('</html>\n')
			print('write finished')
			

