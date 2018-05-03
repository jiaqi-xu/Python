# -*- encoding: utf-8 -*-
'''
pickle load对象的时候会出现的问题
'''
class Foo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


import pickle

obj = Foo('jqx')
pickle.dump(obj, open('db', 'wb'))
