# -*- encoding: utf-8 -*-
'''
序列化之json:
1. json.dumps 可以将基本数据类型转化成字符串
2. json.loads 可以将具有基本数据类型的字符串形式转化成基本数据类型
3. json.dump 先进行序列化，然后写到文件里
4. json.load 从文件里读出来，然后反序列化
'''
# dumps与loads
import json
dict = {'k1': 'v1'}
print(dict, type(dict))
# 将python基本数据类型转化成字符串形式
result = json.dumps(dict)
print(result, type(result))


str1 = '{"k1": "v1"}'
print(str1, type(str1))
# 将python字符串转化成基本数据类型
result = json.loads(str1)
print(result, type(result))


str2 = '["v1", "v2"]'
print(str2, type(str2))
result = json.loads(str2)
print(result, type(result))

# dump与load
import json
li = [11, 22, 33]
json.dump(li, open('db', 'w'))
r = json.load(open('db', 'r'))
print(type(r), li)

'''
例子：基于天气API获取相关JSON数据
http://wthrcdn.etouch.cn/weather_mini?city=<city-name> API
'''

import requests
import json

response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=上海')
'''
#使用apparent_encoding可以获得真实编码
print response.apparent_encoding
'''
response.encoding = 'utf-8'
print(response.text, type(response.text))

dict = json.loads(response.text)
print(dict, type(dict))

