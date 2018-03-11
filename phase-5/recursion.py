# -*- encoding: utf-8 -*-
'''
递归
'''

def func(n):
    n += 1
    if n >= 4:
        return 'end'
    return func(n)

a = func(1)
print(a)

'''
用递归实现： 1*2*3*4*5*6*7
'''

def factorial(arg):
    if arg == 1 or arg == 0:
        return 1
    else:
        return factorial(arg-1) * arg

ret = factorial(7)
print(ret)
