#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('/Users/kirito/Documents/python/scraping/seledium/chromedriver')
driver.get('https://www.baidu.com')
assert(u'百度' in driver.title)
elem=driver.find_element_by_name('wd')
elem.clear()
elem.send_keys(u'lovesnowbest')
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert(u'lovesnowbest' not in driver.page_source)
driver.close()