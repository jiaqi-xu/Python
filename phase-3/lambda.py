#-*- coding: utf-8 -*-

'''
对于简单的函数，我们可以用lambda表达式来写
'''


def f1(a):
    return a + 100


ret = f1(10)
print(ret)

#lambda表达式
f2 = lambda a1, a2=10: a1 + a2 + 9# 与 f1 表达的是一样的
ret_1 = f2(100)
print(ret_1)



