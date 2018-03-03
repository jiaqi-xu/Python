#-*- coding: utf-8 -*-
old_dict = {
    '#1': 8,
    '#2': 4,
    '#4': 2
}

new_dict = {
    '#1': 8,
    '#2': 4,
    '#3': 2
}

'''
用新采集的数据更新旧数据
1. 应该删除哪些槽位的数据 old_dict中存在的，new_dict不存在的

2. 应该更新哪些槽位的数据
3. 应该添加哪些槽位的数据
'''

old_set = set(old_dict.keys())

new_set = set(new_dict.keys())

remove_set = old_set.difference(new_set)
print remove_set
add_set = new_set.difference(old_set)
print add_set
update_set = old_set.intersection(new_set)
print update_set




