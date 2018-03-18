# -*- encoding: utf-8 -*-
'''
sys模块用于提供对python解释器相关的操作:
import sys
sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.exit(n)        #退出程序，正常退出时exit(0)
sys.version        #获取Python解释程序的版本信息
sys.maxint         #最大的Int值
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
'''

# 进度条
import sys
import time
def viewbar(num, total):
    rate = num/total
    rate_number = int(rate*100)
    r = '\r%s>%d%%' % (num*'=',rate_number, ) #\r表示重新回到当前行的首个位置
    #print(r) # print默认加换行符
    sys.stdout.write(r) # write不加换行符
    sys.stdout.flush() # 清空输出


if __name__ == "__main__":
    for i in range(0, 101):
        time.sleep(0.1)
        viewbar(i, 100)