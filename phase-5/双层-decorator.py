# -*- coding: utf-8 -*-
'''
双层装饰器
'''
USER_INFO = {}


def check_login(func):
    def inner(*arg, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*arg, **kwargs)
            return ret
        else:
            print('请登录')
    return inner


# def check_admin(func):
#     def inner(*arg, **kwargs):
#         if USER_INFO.get('is_login', None):
#             if USER_INFO.get('user_type', None) ==2:
#                 ret = func(*arg, **kwargs)
#                 return ret
#             else:
#                 print('无权限查看')
#         else:
#             print('请登录')
#     return inner


def check_admin(func):
    def inner(*arg, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*arg, **kwargs)
            return ret
        else:
            print('无权限查看')
    return inner

'''
双层装饰器，解释的时候是从下往上解释的，形成一个嵌套的函数，然后执行
执行是从上往下执行的。
'''
@check_login
@check_admin
def index():
    '''
    管理员的功能
    :return:
    '''
    print('Index')


@check_login
def home():
    print('home')


def login():
    user = input('请输入用户名:')
    if user == 'admin':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 1


def main():
    while True:
        inp = input('1. 登录; 2. 查看信心; 3. 超级管理员管理')
        if inp == '1':
            login()
        elif inp == '2':
            home()
        elif inp == '3':
            index()


main()
