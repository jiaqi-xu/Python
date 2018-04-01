# -*- encoding: utf-8 -*-
'''
面向对象之类成员
'''

class Foo():
    # 字段(静态字段)
    CC = 123

    def __init__(self):
        # 字段(普通的字段)
        self.name = 'jqx'

    def show(self):
        print(self.name)


class Province:

    country = 'China'

    def __init__(self, name):
        self.name = name
        # 每个对象都有这个country字段，为了节约内存，可以将该字段作为静态字段(让所有对象共享一份)
        # self.country = 'China'

    # 普通方法，由对象调用执行(方法属于类)
    def show(self):
        print(self.name)

    @staticmethod
    def f1(arg1, arg2):
        # 静态方法, 由类调用执行
        print('static method')
        print(arg1,arg2)

    @classmethod
    def f2(cls): # cls的全拼是class
        # cls是类名，cls()是创建对象
        # 类方法，至少要有一个参数叫做cls，类方法是静态方法的一种
        print(cls)

    @property
    def f3(self):
        return self.name

    @f3.setter
    def f3(self, value):
        print(value)

    @f3.deleter
    def f3(self):
        print('del f3')

# 一般的情况下：自己访问自己的字段
# 规则:
#   普通字段只能用对象去访问
#   静态字段用类访问(万不得已的时候可以用对象去访问）
# 类加载的时候，静态字段就已经创建
print(Province.country)
hn = Province('HeNan')
hb = Province('HeBei')
sd = Province('ShanDong')
db = Province('HeiLongjiang')
print(hn.country)

Province.f1('jqx', 18)
Province.f2()

# 调用property(男儿身(方法)，通过女性(字段)方式访问), 完全伪造成字段的样子
# hn.name
print(hn.f3) # 获取
#hn.name = 'qqq'
hn.f3 = 'setter' # 设置
#del hn.name
del hn.f3



'''
属性:调用property(男儿身(方法)，通过女性(字段)方式访问), 完全伪造成字段的样子(
像字段一样可以获取，设置，删除值)
'''
class Pager:
    def __init__(self, all_count):
        self.all_count = all_count

    @property
    def all_pager(self):
        a1, a2 = divmod(self.all_count, 10)
        if a2 ==0:
            return a1
        else:
            return a1+1

    @all_pager.setter
    def all_pager(self, value):
        print(value)

    @all_pager.deleter
    def all_pager(self):
        # del self.all_pager
        print('del all_pager')

p = Pager(101)
# 获取属性（）
result = p.all_pager
print(result)
# 设置值
p.all_pager = '100'
# 删除
del p.all_pager

'''
属性的另外一种表达方法
'''
class Pager:

    def __init__(self, all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self, value):
        print('set value %s' % value)

    def f3(self):
        print('del value')

    foo = property(fget=f1, fset=f2, fdel=f3)


p = Pager(101)
result = p.foo
print(result)
p.foo = 'jqx'
del p.foo





