# -*- encoding: utf-8 -*-
'''
类成员之特殊成员—2
'''


class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)
        print(type(key))
        if type(key) == slice:
            print(key.start)
            print(key.stop)
            print(key.step)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        print(type(key), type(value))

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'xujiaqi'   # 自动触发执行 __setitem__
del obj['k1']           # 自动触发执行 __delitem__

# python3之后用__getitem__代替__getslice__、__setitem__代替__setslice__、__delitem__代替__delslice__
ret = obj[1:4:2]
obj[1:4] = [11, 22, 33, 44, 55, 66]
del obj[1:4]


class Bar:

    def __iter__(self):
        yield 1
        yield 2

obj = Bar()

for item in obj:
    print(item)
