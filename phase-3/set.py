#-*- coding: utf-8 -*-

'''
1. set, 无序, 不重复序列
'''

'''
# list创建
a_list = [1, 2, 3, 1, 4]
list((11, 22, 44)) # __init__ 内部会执行一个for循环，遍历元组中的元素并加入到列表中

a_dict = {'k1': 'v1'}

# set 创建
a_set = {'123', '456'}
b_set = set(a_list) # 会自动去重
print b_set
print type(a_set)


# set 操作
s = set()
print s
s.add(123)
print s
s.add(123) #再次验证不重复性
print s

s.clear() # 清除元素
print s

s1 = {11, 22, 33}
s2 = {22, 33, 44}
s3 = s1.difference(s2) # A中存在，B中不存在的元素
print s3

s3 = s1.symmetric_difference(s2)
print s3 #对称差集

print s1, s2


#s1.difference_update(s2) # 先找A中存在B中不存在的，然后用结果替换（更新）s1中
#print s1

s1.symmetric_difference_update(s2) #用结果更新S1
print s1


s1 = {11, 22, 33}
#s1.discard(11)  #移除元素（如果元素不存在，不报错。）
print s1

#s1.remove(11) #移除元素，（如果元素不存在，会报错）
print s1

re = s1.pop()  # 用于随机移除一个元素,返回值是移除的那个元素
print s1
print re


s1 = {11, 22, 33}
s2 = {22, 33, 44}
print s1.intersection(s2) # 取交集
#s1.intersection_update(s2) # 集合中的方法凡是有update的，都用于更新主集合(除了update方法)
print s1
print s1.union(s2) #求并集 set([33, 44, 22])

list1= [44, 77, 88]
#s1.add(44)
#s1.add(77)
#s1.add(88)
s1.update(list1) #相当于批量添加add, 参数是可迭代对象，如list, string，tuple
print s1

for i in 'jiaqixu':
    print i
'''
# 带双下划线的方法都有特殊的意义，这是面向对象中的知识
# 以下操作都会调用类中相应的方法
li = [11, 22, 33] # list __init__
li() # list __call__
li[0] # list __get_item__
li[0] = 123 # list __setitem__
del li[1] # list __delitem__





