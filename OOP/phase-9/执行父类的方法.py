# -*- encoding: utf-8 - *-
'''
使用super调用父类的方法
'''


class C1:

    def f1(self):
        print('c1.f1')


class C2(C1):

    def f1(self):
        # 执行父类的f1方法
        super(C2, self).f1()
        print('c2.f1')
        C1.f1(self) # python3.0之后不建议使用这种方式(因为f1通常得用对象去访问，但是这里传了self也可以)

obj = C2()
obj.f1()
