# -*- coding: utf-8 -*-
'''
用户管理程序
1. 一开始定义了函数order, changepwd, manager， 他们有个共同的特点就是必须检测用户是否登录，因为登录
之后才可使用这些操作。
2. 因为1中所描述的，我们可以使用装饰器。
3. 应用场景，装饰器经常被用于写权限的验证等方面
'''

LOGIN_USER = {'is_login': False}


def outer(func):
    def inner(*arg, **kwargs):
        if LOGIN_USER['is_login']:
            r = func()
            return r
        else:
            print('请登录')
    return inner


@outer
def order():
    #if LOGIN_USER['is_login']:
        print('欢迎%s登录' % LOGIN_USER['current_user'])
    #else:
       # print('请登录')

@outer
def changepwd():
    #if LOGIN_USER['is_login']:
        print('欢迎%s登录' % LOGIN_USER['current_user'])
    #else:
        #print('请登录')

@outer
def manager():
    #if LOGIN_USER['is_login']:
        print('欢迎%s登录' % LOGIN_USER['current_user'])
    #else:
        #print('请登录')


def login(user, pwd):
    if user == 'jqx' and pwd == '123':
        LOGIN_USER['is_login'] = True
        LOGIN_USER['current_user'] = user
        manager()


def main():
    while True:
        inp = input('1. 后台管理\n2. 登陆')
        if inp == '1':
            manager()
        elif inp == '2':
            username= input('请输入用户名:')
            pwd = input('请输入密码:')
            login(username, pwd)


main()