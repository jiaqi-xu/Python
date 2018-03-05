#-*- coding: utf-8 -*-
# 1. def关键字，创建函数
# 2. 函数名
# 3. ()
# 4. 函数体
# 5. 返回值
def sendmail():

    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["jqx", 'exmaple@126.com'])
        msg['To'] = formataddr(["走人", '405715350@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25) # 在邮箱里开启smtp服务
        server.login("exmaple@126.com", "emailpassword")
        server.sendmail('exmaple@126.com', ['405715350@qq.com', ], msg.as_string())
        server.quit()
    except:
        # 发送失败
        return False
    else:
        # 发送成功
        return True


ret = sendmail()
if ret:
    print('发送成功')
else:
    print('发送失败')


def sendmail_parameter(email_address):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["jqx", 'exmaple@126.com'])
        msg['To'] = formataddr(["走人", '405715350@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)  # 在邮箱里开启smtp服务
        server.login("exmaple@126.com", "emailpassword")
        server.sendmail('exmaple@126.com', [email_address, ],
                        msg.as_string())
        server.quit()
    except:
        # 发送失败
        return False
    else:
        # 发送成功
        return True


while True:
    em = input('请输入邮箱地址：')
    result = sendmail_parameter(em)
    if result:
        print('发送成功')
    else:
        print('发送失败')


# 参数
# 1. 普通参数（严格按照顺序，将实际参数赋值给形式参数）
# 2. 默认参数 (必须放置在参数列表的最后)
# 3. 指定参数 (将实际参数赋值给指定的形式参数)
# 4. 动态参数 * 默认将传入的参数，全部放置在元组中
# 5. 动态参数 ** 默认将传入的参数，全部放置在字典中
# 6. 万能参数 f3

def f1(*args):
    print args

f1(1,2,3, type(args))
li = [1,2,3]
f1(li, 44) # 元组([1,2,3], 44)
f1(*li) # (1, 2, 3)


def f2(**args):
    print(args, type(args))

f2(n1='alex', n2=18) # {'n1':'alex', 'n2':18} <class 'dict'>
dict = {'k1': 'v1', 'k2': 'v2'}
f2(k1=dict) # {'k1': {'k1': 'v1', 'k2': 'v2'}} <class'dict'>
f2(**dict) # {'k2':'v2', 'k1':'v1'} <class 'dict'>

# 万能参数

def f3(*args, **kwargs):
    print(args)
    print(kwargs)


f3(11, 22, 33, 44, k1='v1', k2='v2')
'''
(11, 22, 33, 44)
{'k2': 'v2', 'k1': 'v1'}
'''

# 利用动态参数实现format功能
'''
以前提过另外一种格式化输出：
'%s %d'% ('jqx', 18)
str.format()
str.format格式化输出
'''
s1 = "I am {0}, age {1}".format('jqx', 18)
print(s1)

s2 = "I am {0}, age {1}".format(*['jqx', 20])# format(*args, **kwargs)
print(s2)

s3 = "I am {name}, age {age}".format(name="jqx", age=18)
print(s3)

dict = {'name': 'jqx', 'age': 18}
s4 = "I am {name}, age {age}".format(**dict)
print(s4)



# 函数之内容补充
def f1(a1, a2):
    return a1 + a2

def f1(a1, a2):
    return a1 * a2

result = f1(8, 8)
print(result)
'''
输出64， 为什么呢？
因为一开始第一个方法被存入内存，f1指向其；但当定义第二个函数的时候，第二个函数也被加入内存，
且f1重新指向了内存中的第二个函数。
值得注意的是：此时内存中的第一个函数没有引用指向他，python的垃圾回收机制会定时查找这些没有索引的内存中
的变量／函数，进行回收。
'''

# 简化而言，上面的例子和以下的过程是类似的：
'''
name = 'jqx'
name = 'jqx_1'
print(name) #jqx_1
'''


# 函数的参数传递时，到底是传引用呢，还是再传一份值
def f1(a):
    a.append(999)

li = [11, 22, 33]
f1(li)
print(li) # [11, 22, 33, 999]
'''
因为如果传的是另外一份值，结果是不应该有999的。由输出结果可以见，传递的是引用。
'''


# 全局变量, 所有的作用域都可读
# 对全局变量重新赋值，需要global一下
# 特殊：列表，字典，可修改（i.e. 添加值），不可重新赋值
name = 'jqx_global'

def f1():
    age = 18
    # name = '123' # 是不能修改全局的name的。如果想在函数里修改全局的变量，可以加一个关键字 global
    global name # 表示name是全局变量
    name = '123'
    print(name, age)

def f2():
    age = 19
    print(name, age)
'''
最后，请注意，其实所有的全局变量都必须是大写NAME，这是一个默认的规则。
'''

