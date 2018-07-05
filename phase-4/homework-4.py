# -*- coding: utf-8 -*-
'''
作业需求:
用户管理程序
    普通用户：登录，注册，修改密码，查看用户信息
    管理员用户：登录，注册，修改密码，查看用户信息；
    删除,添加普通用户
    修改普通用户密码
    查看所有普通用户，按照指定关键字搜索用户信息
    提高普通用户权限

要求：
1. 用户信息存在文件中
2. 权限要用装饰器

用户信息可以放在文件中：
jqx|123|email|phone|...| 1 # 比如1代表普通用户，2代表管理员用户
'''

USER_INFO = {'is_login': False}


def check_login(func):
    def inner(*arg, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*arg, **kwargs)
            return ret
        else:
            print('请登录')
    return inner


def check_admin(func):
    def inner(*arg, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*arg, **kwargs)
            return ret
        else:
            print('无权限查看')
    return inner


def login(username, password):
    with open('userinfo_database', 'r') as reader:
        for user_info in reader:
            user_info_list = user_info.split('|')
            user_from_db = user_info_list[0]
            pwd_from_db =  user_info_list[1]
            if user_from_db == username and pwd_from_db == password:
                USER_INFO['is_login'] = True
                USER_INFO['current_user'] = username
            else:
                continue

    print('输入的账户或密码错误')


def register():
    while True:
        print('欢迎进行用户注册->')
        username = input('请输入用户名：')
        # 验证此用户是否已经存在
        with open('userinfo_database', 'r') as reader:
            for user_info in reader:
                user_info_list = user_info.split('|')
                user_from_db = user_info_list[0]
                if username == user_from_db:
                    print('此用户名已经存在')
                    continue

        password = input('请输入密码')
        re_password = input('请再次输入密码')
        if password != re_password:
            print('两次密码输入不一致，请重新进行注册！')
            continue
        else:
            email = input('请输入注册邮箱：')
            phone = input('请输入')

@check_login
@check_admin
def index():
    pass


def main():
    inp = input('1. 登录 2. 注册')
    if inp == '1':
        username = input('请输入用户名：')
        pwd = input('请输入密码：')
        login(username, pwd)
    elif inp == '2':
        register()
    else:
        print('请输入正确的命令！')
