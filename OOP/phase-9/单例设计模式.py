# -*- encoding: utf-8 -*-
'''
Singleton设计模式，应用场景：JDBC, 数据库连接池，通过单例模式使其只创建一份连接池
'''


class Foo:

    instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls):
        # cls 类名
        if cls.instance:
            return cls.instance
        else:
            obj = cls('jqx')
            cls.instance = obj
            return obj


# 这样的话，obj和obj_2是一样的
obj = Foo.get_instance()
obj_2 = Foo.get_instance()
print(obj)
print(obj_2)