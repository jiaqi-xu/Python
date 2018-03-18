# -*- encoding: utf-8 -*-
'''
模块中特殊变量学习
'''

import s2
from bin import admin
#print(vars(s2))
# 查看一些内置变量与函数，如abs,...
print(s2.__dict__)

# __doc__  获取文件的注释（文件顶头三引号中的注释）
print(__doc__)

# __file__
print(__file__)  # 表示py文件所在的路径（见bin/admin）

# __package__
print(__package__) # None
print(admin.__package__) # bin

# __cached__ python在导入某个模块时，在__pycache__文件夹中会自动生成其pyc文件

# 执行当前文件的时候，当前文件特殊变量__name__ == "__main__"
print(__name__)


def func():
    print('main file')


if __name__ == "main":
    func()






