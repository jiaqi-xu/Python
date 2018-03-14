# -*- encoding: utf-8 -*-
'''
序列化之pickle:
1. pickle.dumps
2. pickle.loads
3. pickle.dump
4. pickle.load
'''
import pickle

# dumps与loads
li = [11, 22, 33]
ret = pickle.dumps(li)
print(ret, type(ret))

r = pickle.loads(ret)
print(r, type(r))

# dump与load: 只支持以字节的方式去写和读
pickle.dump(li, open('db', 'wb'))

r = pickle.load(open('db', 'rb'))
print(r)

'''
### json与pickle的区别
1. pickle可以对所有数据类型做操作（序列化; json只能对基本数据类型做操作（序列化），更适合跨语言
2. pickle的缺点：仅使用于python，并且有可能还得统一python版本
'''