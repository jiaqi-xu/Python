# -*- encoding: utf-8 -*-
'''
面向对象：
封装，继承，多态
'''

# 封装
class c1:

    def __init__(self, name, obj):
        self.name = name
        self.obj = obj


class c2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)


class c3:

    def __init__(self, a1):
        self.money = 123
        self.aaa = a1


c2_obj = c2('aa', 11)
c1_obj = c1('bb', c2_obj)
print(c1_obj.obj.name)
c3_obj = c3(c1_obj)
print(c3_obj.aaa)


# 单继承
class F1: # 父类(aka. 基类)
    def show(self):
        print('show')

    def foo(self):
        print(self.name)


class F2(F1): # 子类(aka. 派生类)
    def __init__(self, name):
        self.name = name

    def bar(self):
        print('bar')

    def show(self):
        print('F2.show')

class F3(F2):
    pass


obj = F2('jqx')
obj.show()
obj.bar()
obj.foo()

# 多继承(在没有共同顶层父类的情况下，深度优先寻找要执行的函数)
class C0:
    def f2(self):
        print('C0.f2')

class C1(C0):
    def f2(self):
        print('C1.f2')

class C2:
    def f2(self):
        print('C2.f2')

class C3(C1, C2):
    def f3(self):
        print('C3.f3')

obj = C3()
obj.f2() # 会执行C1的f2，因为继承的时候，先继承的C1，如果C1中没有f2，则会去C0中找f2。