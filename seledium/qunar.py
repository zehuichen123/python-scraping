#!/usr/bin/env python3
# author: lovesnowbest
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"')
# get your current absolute content
currentPath=os.path.abspath('.')		
currentPath=os.path.join(currentPath,'chromedriver')
# add ChromeDriver.exe to your webdriver
driver=webdriver.Chrome(currentPath,chrome_options=options)

url='https://hotel.qunar.com'
driver.get(url)
# let our brower be the maximized size
driver.maximize_window()
time.sleep(2)

# find the element we need: the city,
# when we want to live in : today
# when we want to leave : tommorrow
# search button to click
dest=driver.find_element_by_name('toCity')
from_date=driver.find_element_by_name('fromDate')
to_date=driver.find_element_by_name('toDate')
search_btn=driver.find_element_by_xpath("//div[@class='search-btn']")

to_city='shanghai'
date_from=datetime.date.today().strftime('%Y-%m-%d')
date_to=datetime.date.today()+datetime.timedelta(days=1)
date_to=date_to.strftime('%Y-%m-%d')

# input the information we want
# then click the search button
dest.clear()
dest.send_keys(to_city)
from_date.clear()
from_date.send_keys(date_from)
to_date.clear()
to_date.send_keys(date_to)
search_btn.click()

# find three pages about our hotel
# then save these information into 
# hotel.txt
for page_num in range(1,4):
	# continue to scroll to end
	while True:
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		try:
		    # find the bottom element to let brower load hotels the second time
		    driver.find_element_by_class_name('num')
		    print('find element num at page'+str(page_num))
		    # if no exception raised, it means find this element
		    break
		except Exception as e:
		    # if exception raised, the page hasn't been scrolled to the bottom
		    pass
	# wait the page to load the second time
	time.sleep(3)
	while True:
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		try:
		    driver.find_element_by_class_name('num')
		    print('find element num at page'+str(page_num))
		    break
		except Exception as e:
		    pass

	# get the html source of current page
	html=driver.page_source
	# tranform it into beautifulSoup
	html_bf=BeautifulSoup(html,'html.parser')
	# find the hotel results (it should be a list)
	hotel_info=html_bf.find_all('div',id='jxContentPanel')
	# open the hotel.txt with append type
	with open('hotel.txt','a') as f:
		for info in hotel_info:
			# remove the redundent '\n' and space
			content=info.get_text().replace(" ","").replace("\t","").strip()
			for line in [ln for ln in content.splitlines() if ln.strip()]:
				f.write(line)
				f.write('\r\n')
			f.write("***"*5+'\n')
	time.sleep(2)
	# find the next page buttion and click to the next page
	try:
		next_page=WebDriverWait(driver,10).until(
			EC.visibility_of(driver.find_element_by_xpath("//a[@class='num icon-tag']"))
			)
		next_page.click()
	except Exception as e:
		print(e)

























