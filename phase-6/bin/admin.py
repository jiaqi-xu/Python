# -*- encoding: utf-8 -*-
'''
目的：将admin所在的phase-6加入到sys.path中
假设bin文件下为可执行文件，如果要其文件中需要调用lib或者其他文件夹下的模块，就
需要我们将phase6加入sys.path中，这样无论将项目移到哪里，都可以调用到其文件夹下的
模块
'''

import sys
# sys.path.append('/Users/jiaqixu/PycharmProjects/PythonLearning/phase-6') # 不能这样，因为如果phase6的这文件夹不在这个路径下，就不能使用了

'''
print(__file__) #  /Users/jiaqixu/PycharmProjects/PythonLearning/phase-6/bin/admin.py
print(os.path.abspath(__file__)) /Users/jiaqixu/PycharmProjects/PythonLearning/phase-6/bin/admin.py

如果去bin目录下，然后在执行python admin.py
print(__file__)  # admin.py
print(os.path.abspath(__file__)) /Users/jiaqixu/PycharmProjects/PythonLearning/phase-6/bin/admin.py
由此可以见只有第二种方法无论合适都会获得文件的绝对路径
'''
print(__file__)
import os
print(os.path.abspath(__file__)) # 获取某个文件的绝对路径
ret = os.path.dirname(os.path.abspath(__file__)) # 得到admin的上一级目录bin
print(ret)
ret_1 = os.path.dirname(ret)  #得到bin的上一级目录phase-6
print(ret_1)
sys.path.append(ret_1)


