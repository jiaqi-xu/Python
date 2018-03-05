#-*- coding: utf-8 -*-
'''
内置函数
'''

# abs绝对值
n = abs(-1)
print(n)

# 为False的一些值： 0， None, "", [], (), {}
print(bool(1))


# all函数的参数为一个可迭代的参数，所有的元素为True才为True
n = all([1, 2, 0])
print(n)

# any函数参数也为一个可迭代的参数，只要有一个为True就为True
n = any([1, 2, 0])
print(n)

# ascii函数自动执行对象的__repr__方法
class Foo():
    def __repr__(self):
        return '111'
n = ascii(Foo())
print(n)

# bin函数，将10进制数转换成2进制
print(bin(5))
# oct函数，将10进制数转换成8进制
print(oct(9))
# hex函数，将10进制数转换成16进制
print(hex(16))

# utf-8 一个汉字：三个字节
# gbk  一个汉字：两个字节
'''
字符串转换成字节类型
可以用bytes(要转换成的字符串，按照什么编码)
'''
s = '你好'
n = bytes(s, encoding="utf-8")
print(n) #'\xe4\xbd\xa0\xe5\xa5\xbd'
n= bytes(s, encoding='gbk')
print(n) #'\xc4\xe3\xba\xc3'

# 字节转换成字符串
'''
bytes(s, encoding="utf-8")是字节（类型）
'''
new_str = str(bytes(s, encoding="utf-8"), encoding='utf-8')
print(new_str)

