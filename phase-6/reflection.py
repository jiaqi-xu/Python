# -*- encoding: utf-8 -*-
'''
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
#import manager
#import account
#import commons
# obj = __import__('commons')
# obj.login()
'''
def run():
    inp = input('请输入要访问的url:')
    if inp == 'login':
        commons.login()
    elif inp == 'logout':
        commons.logout()
    elif inp == 'home':
        commons.home()
    else:
        print('404')
'''

def run():
    # 输入'commons/login'
    inp = input('请输入要访问的url:')
    # 利用字符串的形式去对象(模块)中操作(寻找/检查/删除/设置)成员 --->反射
    #delattr(commons, inp) 基于内存
    #setattr(commons, inp) 基于内存

    m, f = inp.split('/') # 以字符串的形式导入了模块，还以字符串的形式找到了函数
    # obj = __import__('lib.' + m, fromlist=True)
    print(obj)

    if hasattr(obj, f):
        func = getattr(obj, f)
        func()
    else:
        print('404')


if __name__ == '__main__':
    run()