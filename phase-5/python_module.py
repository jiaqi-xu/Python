# -*- coding: utf-8 -*-
'''
python 模块
在python中：叫模块 相当于其他语言的类库
先导入后使用
'''

'''
1. 为什么要有模块？
将代码归类，设计架构

2. 模块导入的依据／规则是什么？
模块必须存在于sys.path中，才能导入成功。否则找不到

3. 模块名称的重要性
不能重名：一定不要创建与内置模块名一样的模块，否则会先去找你自己定义的模块

4. 导入模块方式：
   import 
   from xx import xxx 
   from xx import *  星号(asterisk)表示导入模块中的所有函数
   from A import c  as a1
   from B import c  as b1

5. 下载第三方模块
   pip下载: pip install xxx
   源码安装：cd 文件解压路径 
            python setup.py install
   
'''

import sys

print(sys.argv)

for item in sys.path:
    print(item)
