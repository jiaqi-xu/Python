# -*- encoding: utf-8 -*-


'''
Python中使用线程有两种方式：函数或者用类来包装线程对象。
Low-level threading API
'''

import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ('Thread-1', 2))
    _thread.start_new_thread(print_time, ('Thread-2', 4))
except:
    print('error')

while 1:
    pass
