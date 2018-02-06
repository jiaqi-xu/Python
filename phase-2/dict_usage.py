#-*- coding: utf-8 -*-

# 有重复的键，会自动去重
id_db = {
    '1': {
        'name': 'Jiaqi Xu',
        'age': '18'
    },

    '2': {
        'name': 'Alex',
        'age': 17
    },

}
print id_db

'''
print id_db['1'] # 查看

id_db['1']['name'] = 'jiaqixu' # 更改
print id_db['1']


del id_db['1']['age'] # 删除
print id_db['1']

id_db.pop('2') #用pop删除
print id_db

id_db['1'].pop('age') # 用pop删除
print id_db
'''

name = id_db.get('1')
print name

age = id_db.get('Age', "不存在") #默认第二个参数是None
print age

new_id = {'3': {'name': 'new_one', 'age': 19}}
id_db.update(new_id)
print id_db

print id_db.items() #将字典变成了列表，一般不要这样做，字典转列表耗时间
print id_db.values() # 字典所有的values
print id_db.keys() # 字典的key列表
print id_db.has_key('1') # only in 2.x
print '1' in id_db # equal to above (2.x 和 3.x 都可以这样用)


print id_db.setdefault('1') # 如果存在就返回key所对应的value;

print id_db.setdefault('9', 'XXXXX') # 如果不存在，就默认设置一个默认key_value 值，并且返回默认值；
print id_db

print id_db.fromkeys([1, 0], 'kengkeng') # 此处有坑，以后用的化可能会碰到
print id_db

print id_db.popitem()  # 随机删除了一个item
print id_db

'''
for k, v in id_db.items(): # 一般不用，效率低。因为有一个字典dict转换成list的过程，比较花时间当数量大的时候。
    print k, v
'''
for key in id_db.keys():  # 效率高
    print key, id_db.get(key)

for key in id_db:
    print key, id_db.get(key)



