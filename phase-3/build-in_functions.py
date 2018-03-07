#-*- coding: utf-8 -*-
'''
内置函数
'''

# abs绝对值
n = abs(-1)
print(n)

# 为False的一些值： 0， None, "", [], (), {}
print(bool(1))


# all函数的参数为一个可迭代的参数，所有的元素为True才为True
n = all([1, 2, 0])
print(n)

# any函数参数也为一个可迭代的参数，只要有一个为True就为True
n = any([1, 2, 0])
print(n)

# ascii函数自动执行对象的__repr__方法
class Foo():
    def __repr__(self):
        return '111'
n = ascii(Foo())
print(n)

# bin函数，将10进制数转换成2进制
print(bin(5))
# oct函数，将10进制数转换成8进制
print(oct(9))
# hex函数，将10进制数转换成16进制
print(hex(16))

# utf-8 一个汉字：三个字节
# gbk  一个汉字：两个字节
'''
字符串转换成字节类型
可以用bytes(要转换成的字符串，按照什么编码)
'''
s = '你好'
n = bytes(s, encoding="utf-8")
print(n) #'\xe4\xbd\xa0\xe5\xa5\xbd'
n= bytes(s, encoding='gbk')
print(n) #'\xc4\xe3\xba\xc3'

# 字节转换成字符串
'''
bytes(s, encoding="utf-8")是字节（类型）
'''
new_str = str(bytes(s, encoding="utf-8"), encoding='utf-8')
print(new_str)

# callable函数
def f1():
    pass

f2 = 123

print(callable(f1))
print(callable(f2))

# chr函数 ord函数
r = chr(65)
print(r)
n = ord('B')
print(n)




'''
compile()
eval()
exec()
python <文件.py>
1. 读取文件内容（相当于open），得到字符串str，加载到到内存
2. python内部把字符串 -》编译 -》特殊代码
3. 执行代码 
'''

# python内部先编译，后执行

s = 'print(123)'

# 编译 single, eval, exec
r = compile(s, '<string>', 'exec')  # 把字符串s编译成代码
print(r)

# 执行 python 代码或者字符串
exec(r) # 执行编译好的代码

s = '8*8'
ret = eval(s)
print(ret)

'''
exec() 和eval()区别
'''
# exec()执行python代码，接收：代码或者字符串，无返回值
# 如果你传的是字符串，则exec内部会先编译字符串，再执行；
# 如果给的是编译好的代码，则exec会直接执行。
r1 = exec('print(2)')
r2 = exec('7+8+9')
print(r1)
print(r2)

# 执行表达式，并且获取结果
ret = eval('7+8+9')
print(ret)

# dir函数
# 可以查看对象提供了哪些功能
print(dir(list))

# help函数
# 可以查看对象具体有哪些功能
help(list)

# divmod函数
'''
一共有97条数据，每页显示10条数据，共需要多少页
'''
r = divmod(97, 10)
print(r) # (9, 7) 返回元组，第一个元素商和第二个元素余数

shang, yushu = divmod(97, 10)
print(shang, yushu)

# isinstance函数
# 用于判断对象是否是某个类的实例
s ='jqx'
r = isinstance(s, str)
print(r)
s2 = [1,2]
r2 = isinstance(s2, dict)
print(r2)


# filter
def f2(a):
    if a > 22:
        return True


li = [11, 22, 33, 44]
# filter内部，会循环第二个参数
'''
filter内部做了以下功能:
result = []
for item in 第二个参数:
    r = 第一个参数(item)
    if r:
        result.append(item)
return result
可以知道filter循环第二个参数，让每一个循环元素去执行第一个参数（函数），如果函数返回True，表示合法。
'''

ret = filter(f2, li)
print(list(ret))


# lambda自动return
f1 = lambda a: a > 30
ret = f1(90)
print(ret)

li = [11, 22, 33, 44, 55]
result = filter(lambda a: a > 33, li)
print(list(result))


# map函数(函数，可迭代的对象(可以for循环的东西))
li = [11, 22, 33, 44, 55]
'''
def f1(args):
    result = []
    for i in args:
        result.append(100 + i)

    return result

r = f1(li)
print(r)
'''
'''
def f2(a):
    return a + 100

result = map(f2, li)
print(list(result))
'''
result = map(lambda a:a+100, li)
print(list(result))


# local()与global()
NAME = 'jqx'

def show():
    a = 123
    c = 456
    print(locals()) # 列出所有局部变量
    print(globals()) # 列出所有全局变量

show()

# hash函数
s1 = 'hhh'
s2 = 'aaaaa'
print(hash(s1))
print(hash(s2))

# id函数 查看内存地址
print(id(s1))
print(id(s2))

# len函数
'''
# python2 是按字节长度算的，所以是6
# python3 默认是按字符长度算的，所以是2
'''
s = '你好'
print(len(s))

# min, max, sum
li = [11, 22, 33, 1]
max = max(li)
min = min(li)
sum = sum(li)
print(max, min, sum)

# pow() 几的几次方
print(pow(2, 10))

# repr函数
'''
使用repr(对象)，会去调用这个对象所属类中的__repr__方法，如果没有这个方法则会报错
'''
class Foo:
    def __repr__(self):
        return '123'

r = repr(Foo())
print(r)

# reversed函数
li = [11, 22, 1]
#li.reverse()
print(li)
a = reversed(li)
print(list(a))

# round函数
r = round(1.8)
print(r)
r = round(1.4)
print(r)


# sorted函数

li = [11, 22, 1]
#li.sort()
print(li)
a = sorted(li)
print(a)

# 使用zip函数实现某个功能
l1 =['jq', 11 ,22 ]
l2 = ['is', 22 ,33]
l3 =['good', 33, 45]
r = zip(l1,l2,l3)
temp = list(r)[0]
result = ' '.join(temp)
print(result)