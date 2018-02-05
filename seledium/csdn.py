#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"')
currentPath=os.path.abspath('.')
currentPath=os.path.join(currentPath,'chromedriver')

driver=webdriver.Chrome(currentPath,chrome_options=options)

driver.get('https://passport.csdn.net/account/login')

username.clear()
password.clear()

username=driver.find_element_by_name('username')
password=driver.find_element_by_name('password')

login_btn=driver.find_element_by_xpath("//input[@type='button']")

username.send_keys('18117352126')
password.send_keys('chlxgy5573108')

login_btn.click()