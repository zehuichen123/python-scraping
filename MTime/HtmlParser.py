#!/usr/bin/env python3
# coding:utf-8
import re,json

class HtmlParser(object):
	def parser_url(self,page_url,response):
		pattern=re.compile(r'http://movie.mtime.com/(\d+)')
		urls=pattern.findall(response)
		if urls!=None:
			return list(set(urls))
		else:
			return None

	def parser_json(self,page_url,response):
		print(response)
		pattern=re.compile(r'=(.*?);')
		result=pattern.findall(response)[0]
		if result!=None:
			value=json.loads(result)
			#print(value)
			try:
				isRelease=value.get('value').get('isRelease')
			except Exception as e:
				print('in parser_json')
				print(e)
				return None
			if isRelease:
				if value.get('value').get('boxOffice')!=None:
					return self._parser_release(page_url,value)
				else:
					return self._parser_no_release(page_url,
									value,isRelease=2)
			else:
				return self._parser_no_release(page_url,value)

	def _parser_release(self,page_url,value):
		try:
			isRelease=1
			movieRating=value.get('value').get('movieRating')
			boxOffice=value.get('value').get('boxOffice')
			movieTitle=value.get('value').get('movieTitle')
			RDirectorFinal=movieRating.get('RDirectorFinal')
			RatingFinal=movieRating.get('RatingFinal')

			MovieId=movieRating.get('MovieId')
			TotalBoxOffice=boxOffice.get('TotalBoxOffice')
			TotalBoxOfficeUnit=boxOffice.get('TotalBoxOfficeUnit')

			ShowDays=boxOffice.get('ShowDays')

			try:
				Rank=boxOffice.get('Rank')
			except Exception as e:
				Rank=0

			return (MovieId,movieTitle,RatingFinal,
					RDirectorFinal,TotalBoxOffice+TotalBoxOfficeUnit,
					Rank,ShowDays,isRelease)
		except Exception as e:
			print('_parser_release')
			print(e,page_url,value)
			return None

	def _parser_no_release(self,page_url,value,isRelease=0):
		try:
			movieRating=value.get('value').get('movieRating')
			#boxOffice=value.get('value').get('boxOffice')
			movieTitle=value.get('value').get('movieTitle')
			RDirectorFinal=movieRating.get('RDirectorFinal')
			RatingFinal=movieRating.get('RatingFinal')

			MovieId=movieRating.get('MovieId')

			Rank=0
			boxOffice=None

			return (MovieId,movieTitle,RatingFinal,
					RDirectorFinal,u'无',Rank,0,isRelease)
		except Exception as e:
			print('_parser_no_release')
			print(e,page_url,value)
			return None










