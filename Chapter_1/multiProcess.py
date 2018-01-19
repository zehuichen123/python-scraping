#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process,Pool
import time,random

# using fork to create multi-process

print('current Process (%s) start ...'%(os.getpid()))
pid=os.fork()
if pid<0:
	print('error in fork')
elif pid==0:
	print('I am child process(%s) and my parent process is (%s)'
		%(os.getpid(),os.getppid()))
else:
	print('I(%s) created a child process (%s)'%(os.getpid(),pid))

# using multiprocessing to create multi-process

def run_proc(name):
	print('Child Process %s(%s) running...'%(name,os.getpid()))

print('Parent Process %s.'%os.getpid())
for i in range(5):
	p=Process(target=run_proc,args=(str(i),))
	print('Process will start...')
	p.start()
p.join()
print('Process end')


# using Pool
def run_task(name):
	print('task %s (pid=%s) is running...' %(name,os.getpid()))
	time.sleep(random.random()*3)
	print('task %s end.'%name)

print('current process %s'%os.getpid())
p=Pool(processes=3)
for i in range(5):
	p.apply_async(run_task,args=(i,))
print('Waiting for all child process done...')
p.close()
p.join()
print('all child process done')