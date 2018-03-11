# -*- coding: utf-8 -*-
'''
生成器 generator: 一个具有生成指定条件数据的能力的一个对象
'''

li = [11, 22, 33, 44]
result = filter(lambda x: x > 22, li)
print(result) # result是一个具有生成指定条件数据的能力的一个对象（生成器generator）

'''
range(10)会在内存中生成一个list包含所有的元素，但是试想如果是range(10.....0)，这些在内存
中占用的空间就会很大；所以为了节约内存，我们可以使用xrange()这个函数，这个函数是会生成一个具有生成
数据能力的一个对象（生成器），通过遍历这个对象，我们可以得到所有的数据，并且对于已经生成的那些不会再使用的数据，
python的垃圾回收机制也可以回收，不会占用太多空间。
另外注意：python3中，没有xrange，xrange都被整合到range中了。
In [10]: range(10)
Out[10]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [11]: xrange(10)
Out[11]: xrange(10)

In [12]: for item in xrange(10):
    ...:     print item
    ...:
0
1
2
3
4
5
6
7
8
9
'''

'''
生成器，使用函数创造
'''

# 普通函数
def func():
    return 123
ret =func()
print(ret)

# 普通的函数中如果加入yield，则这个函数就称之为生成器
def func2():
    print('1111')
    yield 1
    print('2222')
    yield 2
    print('3333')
    yield 3
ret = func2()
print(ret) #<generator object func2 at 0x10212d1a8>

'''
进入函数找到yield，获取yield后面的数据并停止；下次获取下个yield的时候会继续从停止的地方执行.
以下代码也可以用以下代码具有相同的功能:
for i in ret: 
    print(i)
'''
r1 = ret.__next__() # 进入函数找到yield，获取yield后面的数据并保存此时代码执行到的位置；相当于只执行了print('1111')和yield 1
print(r1)

r2 = ret.__next__() # 进入函数，从上次保存的位置继续执行，获取下一个yield后面的数据并停止；相当于只执行了print('2222')和yield 1
print(r2)

r3 = ret.__next__() # 同上
print(r3)



