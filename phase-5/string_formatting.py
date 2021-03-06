# -*- coding: utf-8 -*-
'''
Python的字符串格式化有两种方式: 百分号方式、format方式
1. 百分号方式：%[(name)][flags][width].[precision]typecode
2. Format方式：[[fill]align][sign][#][0][width][,][.precision][type]
'''


'''
1. 百分号方式：%[(name)][flags][width].[precision]typecode
'''
# %s %d
s = 'name %s age %d' % ('jqx', 18)

# (name) 可选 用于选择指定的key
s = 'name %(name)s age %(age)d' % {'name': 'jqx', 'age': 18}
print(s)

# flags: 可供选择的值
# width：占位符所占的宽度
'''
+ 右对齐；正数前加正好，负数前加负号；
- 左对齐；正数前无符号，负数前加负号；
空格 右对齐；正数前加空格，负数前加负号；
0 右对齐；正数前无符号，负数前加负号；用0填充空白处
'''
s = 'name %(name)+10s age %(age)d' % {'name': 'jqx', 'age': 18}
print(s)

#.precision   可选，小数点后保留的位数
s = 'name %(name)+10s age %(age)d  %(p).2f' % {'name': 'jqx', 'age': 18, 'p':1.23456}
print(s)

# typecode    必选
'''
s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
o，将整数转换成 八  进制表示，并将其格式化到指定位置
x，将整数转换成十六进制表示，并将其格式化到指定位置
e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
%，当字符串中存在格式化标志时，需要用 %%表示一个百分号
'''
s = 'aaaaa %c bbbb %o cccc %x dddd %e' % (65, 15, 15, 1000000000)
print(s)

# 单独测试一下百分号
s1 = 'jqx %'
print(s1) # jqx %
# 当格式化时，字符串中出现占位符%s.. 则需要使用%%输出%
s2 = 'jqx %s %%' % ('xx') # jqx xx %
print(s2)


'''
2. Format方式：[[fill]align][sign][#][0][width][,][.precision][type]:
fill  【可选】空白处填充的字符
align 【可选】对齐方式（需配合width使用）
    <，内容左对齐
    >，内容右对齐(默认)
    ＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
    ^，内容居中
sign  【可选】有无符号数字
    +，正号加正，负号加负；
     -，正号不变，负号加负；
    空格 ，正号空格，负号加负；
#    【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
， 【可选】为数字添加分隔符，如：1,000,000
width 【可选】格式化位所占宽度
.precision 【可选】小数位保留精度
type  【可选】格式化类型
    传入” 字符串类型 “的参数
            s，格式化字符串类型数据
            空白，未指定类型，则默认是None，同s
    传入“ 整数类型 ”的参数
            b，将10进制整数自动转换成2进制表示然后格式化
            c，将10进制整数自动转换为其对应的unicode字符
            d，十进制整数
            o，将10进制整数自动转换成8进制表示然后格式化；
            x，将10进制整数自动转换成16进制表示然后格式化（小写x）
            X，将10进制整数自动转换成16进制表示然后格式化（大写X）
    传入“ 浮点型或小数类型 ”的参数
            e， 转换为科学计数法（小写e）表示，然后格式化；
            E， 转换为科学计数法（大写E）表示，然后格式化;
            f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
            g， 自动在e和f中切换
            G， 自动在E和F中切换
            %，显示百分比（默认显示小数点后6位）
'''

s1 = 'name{0}age{1}'.format('jqx', 18)
print(s1)

s2 = '---{name:s}, ---{age:d}==={name:s}'.format(name='jqx', age=18)
print(s2)

s3 = '------{:*^20}======={:+d}-------{:#b}'.format('jqx', 123, 15)
print(s3)

s4 = '-----{:%}'.format(0.123)
print(s4)


