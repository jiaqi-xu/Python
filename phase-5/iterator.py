'''
迭代器
'''

# myrange()是一个生成器
def myrange(arg):
    start = 0
    while True:
        if start == arg:
            return
        yield start
        start += 1

ret = range(3) # range函数这个生成器返回ret这个迭代器

print(type(ret))

for item in ret:
    print(item)


'''
另外一个例子
'''
li = [123, 321]
print(iter(li))
for item in iter(li):
    print(item)
