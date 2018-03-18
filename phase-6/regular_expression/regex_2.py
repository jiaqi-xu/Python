# -*- encoding: utf-8 -*-
'''
正则表达式模块_2

函数:
1. re.match: 只从字符串的起始位置开始匹配
          如果匹配成功，会得到一个match对象
2. re.search: 只会找到第一个的匹配
3. re.findall: 把所有匹配到的字符放到以列表中的元素返回
4. re.finditer: 与findall的唯一区别就是：findall返回一个列表，finditer返回一个迭代对象
5. re.sub(pattern, repl, string, max=0): 找到并替换字符串
6. re.split
7. re.compile
8. 有一些函数有flag，这表示了匹配模式:
    re.I 使匹配对大小写敏感
    re.L 做本地化识别(local-ware)匹配
    re.M 多行匹配，影响^和$
    re.S 使.匹配包括换行在内的所有字符
9. 反斜杠的困扰
与大多数编程语言相同，正则表达式里使用"\"作为转义字符，
这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，
那么使用编程语言表示的正则表达式里将需要4个反斜杠"\\\\"：
前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。
Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r"\\"表示。
同样，匹配一个数字的"\\d"可以写成r"\d"。有了原生字符串，你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观
'''

import re
a = re.sub('g.t', 'have', 'I get one, I got one', 1)
# I have one, I got one
print(a)


b = re.split('\d+', 'one1two2three3four4')
['one', 'two', 'three', 'four', '']
print(b)

text = 'JGood is a handsome boy, he is cool, clever, and so on...'
regex = re.compile('\w*oo\w*')
c = regex.findall(text)
# ['JGood', 'cool']
print(c)

# re模块需要接受2个反斜杠，才能转成1个匹配字符串的反斜杠，所以得给python传4个，python解释器
# 转成2个传给re模块
d = re.findall('\\\\com', 'abc\com')
print(d)

# 为了解决上面反斜杠的困扰，我们可以使用原生字符串
e = re.findall(r'\\com', 'abc\com')
print(e)
