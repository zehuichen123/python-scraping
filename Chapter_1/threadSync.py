#!/usr/bin/env python3
#-*- coding:python3 -*-
import threading

# threading synchronazation
# using RLock to control that only one threading
# can modify data at a time with `acquire` and 
# `release` method
mylock=threading.RLock()
num=0
class myThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self,name=name)

	def run(self):
		global num
		while True:
			mylock.acquire()
			print('%s locked, Number: %d'%(threading.current_thread().name,num))
			if num>=4:
				mylock.release()
				print('%s released, Number: %d'%(threading.current_thread().name,num))
				break
			num+=1
			print('%s released, Number: %d'%(threading.current_thread().name,num))
			mylock.release()

thread1=myThread('Thread_1')
thread2=myThread('Thread_2')
thread1.start()
thread2.start()