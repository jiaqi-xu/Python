# -*- encoding: utf-8 -*-
'''
正则分组匹配
'''

import re

origin = 'has shasdasda12312s'

# 无分组
r = re.match('h\w+', origin)
print(r.group())  # 获取匹配到的所有结果 has
print(r.groups()) # 获取模型中匹配到的分组结果 ()
print(r.groupdict()) # 获取模型中匹配到的分组结果 {}

# 有分组
r = re.match('h(\w+)', origin)
print(r.group())  # 获取匹配到的所有结果  has
print(r.groups()) # 获取模型中匹配到的分组结果 ('as',)
print(r.groupdict()) # 获取模型中匹配到的分组结果 {}

# 有分组，并且对分组设置一个key，这样groupdict就有值了
r = re.match('h(?P<name>\w+)', origin)
print(r.group())  # 获取匹配到的所有结果  has
print(r.groups()) # 获取模型中匹配到的分组结果 ('as',)
print(r.groupdict()) # 获取模型中匹配到的分组结果  {'name': 'as'}

# findall函数的分组匹配
origin = 'has sdasd hal 12123'
r = re.findall('h(\w+)', origin)
print(r) # 只返回分组的内容，不会匹配所有的，所以结果是 ['as', 'al']


origin = 'hasaabc sdasd halaabc 12123'
r = re.findall('h(\w+)a(ab)c', origin)
print(r) # [('as', 'ab'), ('al', 'ab')]

# sub函数与分组匹配无关

'''
split函数无分组与分组对比
'''
# 无分组
origin = 'hello alex bcd alex lge alex acd 19'
r = re.split('alex', origin, 1)
print(r) # ['hello ', ' bcd alex lge alex acd 19']

# 有分组
r = re.split('a(le)x', origin, 1)
print(r) # ['hello ', 'le', ' bcd alex lge alex acd 19'] 括号表示要从匹配到的值中拿取分组中所有的值


