# -*- encoding: utf-8 -*-
'''
加密模块 hashlib:
用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
'''

import hashlib

md5_obj = hashlib.md5()
# python 3.x 需要将字符串转换成字节
md5_obj.update(bytes('123', encoding='utf-8'))
result = md5_obj.hexdigest()
# '123'加密后成了md5值:202cb962ac59075b964b07152d234b70
print(result)

'''
如果想在上面的基础上在加密的话，可以如下操作
'''
md5_obj = hashlib.md5(bytes('abc', encoding='utf-8'))
md5_obj.update(bytes('123', encoding='utf-8'))
result = md5_obj.hexdigest()
# 这样的话'123'加密后成了e99a18c428cb38d5f260853678922e03，这样就相对与上面更安全了，因为每个人创建md5时给的
# 那个值是可以不同的。
print(result)




