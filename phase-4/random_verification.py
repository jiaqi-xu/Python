#-*- coding: utf-8 -*-
'''
随机验证码
'''

import random

li = []
for i in range(6):
    r = random.randrange(0, 5) # 可以保证每一位都有可能是数据
    if r == 2 or r == 4:
        num = random.randrange(0, 10)
        li.append(str(num))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)

result = "".join(li)
print(result)