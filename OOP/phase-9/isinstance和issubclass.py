# -*- encoding: utf-8 -*-
'''
isinstance, issubclass
'''
class Bar:
    pass

class Foo(Bar):
    pass

obj = Foo()
# obj, Bar
ret = isinstance(obj, Foo)
ret2 = isinstance(obj, Bar)
print(ret)
print(ret2)

ret3 = issubclass(Foo, Bar)
print(ret3)


