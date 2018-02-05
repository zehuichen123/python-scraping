#!/usr/bin/env python3
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"')
currentPath=os.path.abspath('.')
currentPath=os.path.join(currentPath,'chromedriver')

driver=webdriver.Chrome(currentPath,chrome_options=options)
url='https://hotel.qunar.com'
driver.get(url)
driver.maximize_window()
time.sleep(2)

dest=driver.find_element_by_name('toCity')
from_date=driver.find_element_by_name('fromDate')
to_date=driver.find_element_by_name('toDate')
search_btn=driver.find_element_by_xpath("//div[@class='search-btn']")

to_city='shanghai'
date_from=datetime.date.today().strftime('%Y-%m-%d')
date_to=datetime.date.today()+datetime.timedelta(days=1)
date_to=date_to.strftime('%Y-%m-%d')
dest.clear()
dest.send_keys(to_city)
from_date.clear()
from_date.send_keys(date_from)
to_date.clear()
to_date.send_keys(date_to)
search_btn.click()

for page_num in range(1,4):
	while True:
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		try:
		    # 定位页面底部的一个图片
		    driver.find_element_by_class_name('num')
		    print('find element num at page'+str(page_num))
		    # 如果没抛出异常就说明找到了底部标志，跳出循环
		    break
		except Exception as e:
		    # 抛出异常说明没找到底部标志，继续向下滑动
		    pass
	time.sleep(3)
	while True:
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		try:
		    # 定位页面底部的一个图片
		    driver.find_element_by_class_name('num')
		    print('find element num at page'+str(page_num))
		    # 如果没抛出异常就说明找到了底部标志，跳出循环
		    break
		except Exception as e:
		    # 抛出异常说明没找到底部标志，继续向下滑动
		    pass
	html=driver.page_source
	html_bf=BeautifulSoup(html,'html.parser')
	hotel_info=html_bf.find_all('div',id='jxContentPanel')
	with open('hotel.txt','a') as f:
		for info in hotel_info:
			content=info.get_text().replace(" ","").replace("\t","").strip()
			for line in [ln for ln in content.splitlines() if ln.strip()]:
				f.write(line)
				f.write('\r\n')
			f.write("***"*5+'\n')
	time.sleep(2)
	try:
		next_page=WebDriverWait(driver,10).until(
			EC.visibility_of(driver.find_element_by_xpath("//a[@class='num icon-tag']"))
			)
		next_page.click()
	except Exception as e:
		print(e)

























