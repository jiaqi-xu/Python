# -*- encoding:utf-8 -*-
'''
python时间处理之datatime模块
'''
import time
import datetime

print(datetime.date.today()) # 输出格式 2018-03-11
print(datetime.date.fromtimestamp(time.time())) # 直接把时间戳转换成日期

current_time = datetime.datetime.now()
print(current_time) # 输出2018-03-11 16:36:17.427490

print(current_time.timetuple()) # 返回struct_time对象格式

# 时间的加减
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=10)) # 比现在加10天
print(datetime.datetime.now() + datetime.timedelta(days=-10)) # 比现在减10天
print(datetime.datetime.now() + datetime.timedelta(hours=3, minutes=-4)) # 比现在加3小时和比现在少4分钟

# 时间替换
print(current_time.replace(2014, 9, 12))

print(datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"))
