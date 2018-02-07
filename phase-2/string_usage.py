#-*- coding: utf-8 -*-
'''
字符串常见功能：
1. 移除空白 strip
2. 分割 split
3. 切片 slice

'''
'''
username = raw_input('user:')

if username.strip() == 'Jiaqi Xu':
    print 'Welcome'
'''
names = 'alex,jack,rain'
split_name = names.split(',')  # 分割字符串
print split_name

print ('|'.join(split_name))  # 合并字符串

print ('alex' in names)  # 判断字符串中有无某个字符串

print names.capitalize()  # 使首字母大写

msg = 'Hello, {name}, Are you {age}'
print msg.format(name="Jiaqi", age=18)
msg_2 = 'Hello, {0}, Are you {1}'
print msg_2.format('Chris', '12')

print names[5:9] # 切片

print names.center(40, '-') # 整个字符串为40，如果不满40，用'-'在两边均匀的填充起来

print names.find('j')  # 找到，返回index （第一个出现位置）
print names.find('Z')  # 没找到则返回-1

print names.isalnum()  # 检测字符串是否由字母和数字组成 (也就是不能包含特殊字符呗)

print names.endswith('n')
print names.startswith('a')

print names.upper().lower()  # 先大写再小写

