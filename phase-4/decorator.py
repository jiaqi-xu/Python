#-*- coding: utf-8 -*-
'''
装饰器
'''


def outer(func):
    def inner():
        print('before')
        r = func()
        print(r)
        print('after')
        return r
    print('first')
    return inner


'''
#@+函数名， 功能：
#1. 自动执行outer函数并且将其下面的函数名f1当作参数传递
#2. 将outer函数的返回值，重新赋值给f1
'''
@outer
def f1():
    print('f1')
    return 'hello'

@outer
def f2():
    print('f2')

@outer
def f100():
    print('f100')


f1()
f2()


'''
装饰器流程剖析之参数
用了装饰器之后，你原来函数(f1)有几个参数，那么装饰器的inner就得定义几个参数
def outer(func):
    def inner(arg):
        print('log')
        r = func(arg)
        print(r)
        print('after')
        return r
    print('first')
    return inner

@outer
def f1(arg):
    print(arg)
    print('f1')
    return 'hello'

f1('miss')
'''