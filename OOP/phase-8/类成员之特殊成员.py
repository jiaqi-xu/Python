# -*- encoding: utf-8 -*-
'''
类成员之特殊成员
'''

class Foo:

    """
    类的描述信息
    """


    # 构造方法
    def __init__(self, name, age):
        print('init')
        self.name = name
        self.age = age

    # 析构方法
    def __del__(self):
        pass

    # 使用对象()触发
    def __call__(self, *args, **kwargs):
        print('obj()触发执行')

    def __str__(self):
        return "%s - %s" % (self.name, self.age)

    def __add__(self, other):
        temp = self.age + other.age
        print(temp)

# 可以得到类的描述信息
print(Foo.__doc__)

p = Foo('jqx', 18)
print(p.__module__)
print(p.__class__)

# 构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
Foo('jqx', 18)()

# print对象或者str()对象的时候，会自动触发对象的__str__方法
print(p)
ret = str(p)
print(ret)

# 调用__add__方法
p2 = Foo('young_jqx', 12)
total_age = p + p2

# 获取对象p中封装的成员数据
print(p.__dict__)

# 获取类中封装的成员信息
print(Foo.__dict__)
