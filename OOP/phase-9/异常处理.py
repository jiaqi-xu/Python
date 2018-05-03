# -*- encoding: utf-8 -*-
"""
基本的异常处理
"""

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        li = []
        li[100]
        result = int(num1) + int(num2)
    except ValueError as ex: # 只能捕获制定的值错误
        print(ex)
    except IndexError as ex:
        print(ex)
    except Exception as ex: # ex 是 Exception的一个对象，封装了错误信息
        print(ex)



# 主动抛出异常
try:
    raise ValueError('value is error') # self.message = 'value is error'
    print('start')
except ValueError as ex:
    print(ex) # __str__, return self.message
else:
    pass
finally:
    pass

