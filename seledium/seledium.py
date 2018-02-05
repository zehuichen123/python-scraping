#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
currentPath=os.path.abspath('.')
currentPath=os.path.join(currentPath,'chromedriver')

driver=webdriver.Chrome(currentPath,chrome_options=options)

driver.get('http://localhost:4000/')
'''
go_on_read=driver.find_element_by_xpath("//div[@class='flod-button']")
'''
time.sleep(2)
#driver.execute_script('arguments[0].scrollIntoView();', go_on_read[-1]) #拖动到可见的元素去
#go_on_read.click()

# -----------------------滑动到窗口最底部，以将所有的girl都刷新出来-----------------------
# 由于页面很长，并且需要不断下拉才会刷新，因此通过javascript来控制器滚动条向下滑动
# 但是一次滑动并不能到达底部，需要多次，那么需要多少次呢？这里采用的方式是不停的向下
# 滑动，每滑动一次，都查询下是否到达底部，怎么查询呢？这是通过查到底部的一个标志图片来判断，
# 如果没找到标志，就说明还没到达底部，需要继续滑动，如果找到就跳出循环
# 为了快速滑动，先设置超时时间为1秒
driver.implicitly_wait(1)
'''
# 不停的滑啊滑
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        # 定位页面底部的一个图片
        driver.find_element_by_xpath("//div[@class='x-page next']")
        # 如果没抛出异常就说明找到了底部标志，跳出循环
        break
    except NoSuchElementException as e:
        # 抛出异常说明没找到底部标志，继续向下滑动
        pass
# 将超时时间改回10秒
page=driver.find_element_by_xpath("//div[@class='page_mark']")
#driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
next_page=driver.find_element_by_xpath("//div[@class='x-page next']").send_keys(Keys.DOWN)
next_page.click()

assert "Python" in driver.title
elem=driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
'''