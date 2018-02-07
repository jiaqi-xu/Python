#-*-encoding:utf-8-*-
'''
name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print name
name.insert(7, 'H')
print name
# 因为是逆向索引，所以加在了索引元素的左边
name.insert(-1, 'X')
print name
# 截取元素切片 slice
name2 = name[2:5]
print name2
# 修改元素
name2[2] = 'Z'
print name2

print name
# 删除某一段元素
del name[5:7]
print name

# 每隔一个元素打印一个元素
print name[::2] # 最后一个值表示步长

number_list = [1, 2, 4, 5, 7, 9, 8, 8, 9]

sub_list = ['A', 'B', 'C', 'D', 'E', 'F', 1, 1, 2]

# 得到某个元素在列表中出现的第一个位置index
if 9 in number_list:
    num_of_ele = number_list.count(9)
    position_of_ele = number_list.index(9)
    print number_list
    print '[%s] 9 is/are in the number list, the ' \
          'first 9 is int the position: [%d]' % (num_of_ele, position_of_ele)

# 将元素9都替换成999
for i in range(number_list.count(9)):
    ele_index = number_list.index(9)
    number_list[ele_index] = 999

print number_list


# extend 将列表追加到自己的列表中，原来的列表还是存在的，只是相当于copy了一下列表的值
number_list.extend(sub_list)
print number_list

# 反转列表
number_list.reverse()
print number_list

#删除列表中的一个元素并且返回这个元素
number_list.pop(2)
print number_list
'''
import copy
num_1 = [3, 3, 4, 4, [1, 2, 3], 5]
num_2 = num_1.copy() #python2 list没有copy函数
'''
num_2 = copy.copy(num_1) 这个copy和list.copy是一摸一样的，都是浅拷贝 （就是做了软链接）
num_3 = copy.deepcoyp() 完全从外到里复制了一份
'''

num_1[0] = 'A'
num_1[4][0] = 'BBBBB'
'''
>>> print(num_1)
['A', 3, 4, 4, ['BBBBB', 2, 3], 5]
>>> print(num_2)
[3, 3, 4, 4, ['BBBBB', 2, 3], 5]
'''
print(num_1)
print(num_2)

# 元组tuple相当于只读列表，不可以修改元素
r = (1, 2, 3)





