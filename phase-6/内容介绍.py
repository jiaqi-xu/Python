# -*- encoding: utf-8 -*-
'''
内容介绍:
一. ATM作业讲解
二. 模块
    logging
    time/datetime

    json/pickle
    requests
三. 反射
    反射最初是由web http(get, post, ...)请求中衍生而来的
实例: 伪造Web框架的路由系统
反射: 基于字符串的形式去对象(模块)中操作(寻找/检查/删除/设置)其成员
    getattr, delattr, setattr, hasattr
扩展: 导入模块
    import xxx
    from xxx import xxx
    obj = __import__('xxx')
    obj = __import__('xxx.ooo.xxx', fromlist=True)
'''