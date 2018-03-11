# -*- coding: utf-8 -*-
'''
基于生成器实现range功能
'''
def myrange(arg):
    start = 0
    while True:
        if start == arg:
            return
        yield start
        start += 1

'''
Test myrange()
'''
for i in myrange(10):
    print(i)