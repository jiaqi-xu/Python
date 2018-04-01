# -*- encoding: utf-8 -*-
'''
pickle load对象的时候会出现的问题
如果在文件中不引入那个对象所属的类，当执行该文件时，那个类当然是不存在内存中，所以load的时候
会失败

AttributeError: Can't get attribute 'Foo' on <module '__main__' from '/Users/jiaqixu/PycharmProjects/PythonLearning/面向对象基础/phase-8/pickle常见问题_2.py'>
出错的原因是，加载对象的时候，对象的类没有写在内存中；想要load成功，必须将类加载到内存：
1. 可以直接将类写在此文件里
2. 可以from pickle常见问题_1 import Foo
'''

import pickle
from pickle常见问题_1 import Foo
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name)

re = pickle.load(open('db', 'rb'))
print(re)