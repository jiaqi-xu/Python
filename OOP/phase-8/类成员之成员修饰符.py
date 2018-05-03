# -*- encoding: utf-8 -*-
'''
类成员之成员修饰符
如果在字段前面加两个下划线__，就可以将该字段设置为私有变量
'''

class Foo:

    #定义一个静态字段
    __cc = '123'

    def __init__(self, name, age):
        # 公有变量
        self.name = name
        # 私有变量
        self.__age = age

    def f1(self):
        print(self.name)
        print(self.__age)

    def f3(self):
        print(Foo.__cc)

    @staticmethod
    def f4():
        print(Foo.__cc)

obj = Foo('jqx', 18)
print(obj.name)
# 因为age是私有的，所以只能在内部访问，在外部无法访问
#print(obj.age)
# f1是内部函数，可以通过他访问私有变量
obj.f1()

#print(Foo.__cc) # AttributeError: type object 'Foo' has no attribute '__cc'
obj.f3() # 私有的静态字段也必须通过内部访问
Foo.f4() # 也可以通过静态方法调用私有静态字段
# print(obj._Foo__cc)

class Bar(Foo):
    def f2(self):
        print(self.name)
        print(self.__age)

obj_f2 = Bar('jqx_f2', 19)
# 会报错，看来子类的内部函数无法访问父类的私有变量
# 其实，在python私有变量，只有他本身才可以访问，其他谁来都不行
# obj_f2.f2()  # AttributeError: 'Bar' object has no attribute '_Bar__age'