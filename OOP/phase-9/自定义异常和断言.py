# -*- encoding: utf-8 -*-
"""
自定义异常和断言
"""

class JiaqiXuException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise JiaqiXuException('my custom exception')
except JiaqiXuException as ex:
    print(ex)


'''
断言assert应用:
有一个对象p，他有一个start方法，但是在调用这个方法之前，得先执行一个p.status = False；如果不满足这个条件，start方法会出错
解决方法:
可以在start方法里先判断assert p.status == False
p = object()
p.status = True
p.status() # 应该先执行一个asser p.status == False
'''
