# -*- encoding: utf-8 -*-
'''
作业需求: 实现一个计算器，要求具有+，-，*，／功能
e.g.: 8*12+(6-(5*6-2)/77+2)*(3-7)+8
    1. 从前到后找，找到第一个(开始，)结尾，中间不包含括号 -> regex: \(中间不包含括号\)
    2. 定义一个函数处理加减乘除
    3. 定义一个函数处理括号:
        e.g. def 处理括号(表达式):
                while True:
                    re.split('\((中间不包含括号)\)', 表达式, 1 )
                    # 加了分组之后可以得到三个部分 8*12+(6-,  5*6-2,  /77+2)*(3-7)+8
                    ret = 处理加减乘除(5*6-2)
                    # 组成新的表达式，继续上述过程
                    8*12+(6- ret /77+2)*(3-7)+8
'''

import re

x = input('请输入你要计算的计算式：')  # 用户输入
# 判断用户输入的是否有字母，括号个数是否正确，同时处理字符串中的空格

if re.findall('[a-zA-Z]', x):
    print('输入错误，算式中出现字母！')
    exit()
if '(' in x or ')' in x:
    if x.count('(') != x.count(')'):
        print('输入错误，括号个数不正确！')
        exit()
if ' ' in x:
    x = x.replace(' ', '')


# 定义一个处理乘法和除法的函数，在只有加减乘除的运算中，除法若是最优先运算的话，不会出错。
# 经过这个函数处理后，计算式中的 乘除法就处理完了，只剩下加减法了
def multiplication_division(calculate):
    # 在计算完括号里面的计算式时，如果得到一个负数，那么替换后会出现 '*-' '/-' '+-' '--' 这么几种情况，故函数先判断处理这种情况。
    while '*-' in calculate:
        if re.search('-[0-9.]+\*-', calculate):
            replace1 = re.search('-[0-9.]+\*-', calculate).group()
            replace = replace1.replace('*-', '*')
            replace = replace.replace('-', '+')
            calculate = calculate.replace(replace1, replace)
        elif re.search('\+[0-9.]+\*-', calculate):
            replace1 = re.search('\+[0-9.]+\*-', calculate).group()
            replace = replace1.replace('*-', '*')
            replace = replace.replace('+', '-')
            calculate = calculate.replace(replace1, replace)
    while '/-' in calculate:
        if re.search('-[0-9.]+/-', calculate):
            replace1 = re.search('-[0-9.]+/-', calculate).group()
            replace = replace1.replace('/-', '/')
            replace = replace.replace('-', '+')
            calculate = calculate.replace(replace1, replace)
        elif re.search('\+[0-9.]+/-', calculate):
            replace1 = re.search('\+[0-9.]+/-', calculate).group()
            replace = replace1.replace('/-', '/')
            replace = replace.replace('+', '-')
            calculate = calculate.replace(replace1, replace)
    while '/' in calculate:
        if re.findall('^-[0-9.]+/[0-9.]+', calculate):
            division = re.findall('-[0-9.]+/[0-9.]+', calculate)[0]
            result = re.findall('(-[0-9.]+)/([0-9.]+)', division)[0]
            result = float(result[0]) / float(result[1])
            calculate = calculate.replace(division, str(result))
        else:
            division = re.findall('[0-9.]+/[0-9.]+', calculate)[0]
            result = re.findall('([0-9.]+)/([0-9.]+)', division)[0]
            result = float(result[0]) / float(result[1])
            calculate = calculate.replace(division, str(result))
    while '*' in calculate:
        if re.findall('^-[0-9.]+\*[0-9.]+', calculate):
            multiplication = re.findall('-[0-9.]+\*[0-9.]+', calculate)[0]
            result = re.findall('(-[0-9.]+)\*([0-9.]+)', multiplication)[0]
            result = float(result[0]) * float(result[1])
            calculate = calculate.replace(multiplication, str(result))
        else:
            multiplication = re.findall('[0-9.]+\*[0-9.]+', calculate)[0]
            result = re.findall('([0-9.]+)\*([0-9.]+)', multiplication)[0]
            result = float(result[0]) * float(result[1])
            calculate = calculate.replace(multiplication, str(result))
    return calculate


# 定义一个处理只有加减法的函数
def addition_subtraction(calculate):
    if '+-' in calculate:
        calculate = calculate.replace('+-', '-')
    elif '--' in calculate:
        calculate = calculate.replace('--', '+')
    list_number = []
    list_number_ = re.findall('[+-]?[0-9.]+', calculate)
    for i in list_number_:
        list_number.append(float(i))
    return sum(list_number)


# 找到最里面的括号，并传给前面的乘除法运算和加减法运算，得到最终的结果
def final(x):
    while '(' in x:
        process = re.findall('\(([^()]+)\)', x)
        for calculate in process:
            y = multiplication_division(calculate)
            y = addition_subtraction(y)
            x = x.replace('(' + calculate + ')', str(y))
    x = multiplication_division(x)
    return addition_subtraction(x)

print(1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ))
print(final(x))