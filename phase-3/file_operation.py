#-*- coding: utf-8 -*-

'''
文件操作
'''

# 1. 打开文件
'''
打开文件的模式：
'''
f = open('db', 'r') # 只读模式【默认】
f = open('db', 'w') # 只写模式【不可读；不存在则创建；存在则清空内容；】
f = open('db', 'x') # 只写模式(python3 新加的功能)【不可读；不存在则创建并写内容，存在则报错】
f = open('db', 'a') # 追加模式【可读；不存在则创建；存在则只追加内容；】


'''
二进制方式读写
注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型
'''
f = open('db', 'rb')
data = f.read()
print(data, type(data)) # b'admin|123' <class 'bytes'>

f = open('db', 'ab')
# f.write('hello') #TypeError: a bytes-like object is required, not 'str'
f.write(bytes('Hello', encoding='utf-8')) # 写二进制有助于跨平台
f.close()

'''
+表示可以同时读写某个文件
'''
f = open('db', 'r+', encoding='utf-8')
data = f.read()
print(data)
f.write('777') # 因为前面已经读了，文件指针位置达到了最后，所以当你写的时候是在末尾加上了内容
f.close()

# 为了在特定的位置开始写，可以用seek函数
f = open('db', 'r+', encoding='utf-8')
# 如果打开模式无b,则read，按照字符读取；
# 因为是r不是rb，所以会读取一个字符；反之读取一个字节
data = f.read(1)
# tell当前指针所在的位置 （字节）
print(f.tell()) # 3,因为第一个是中文，三个字节
print(data)
# 调整当前指针的位置（字节）
f.seek(1) # 无论是r或者rb，都是以字节位置算，所以中文三个字节在重写的时候就会被劈开出现乱码
# 从当前指针位置开始覆盖
f.write('888')
f.close()

'''
注意w+和a+没有r+这么常用，因为w+，往往都会先清空，a+总是会在最后添加内容无论你如何调整指针。
所以当我们想重写（覆盖）一些内容时，不是那么的好用。
'''


# 2. 操作文件
'''
read() # 无参数，读全部内容；有参数，b按字节，无b，按字符读。
tell() # 获取当前指针位置（按字节算）
seek() # 指针跳转到指定位置（按字节算）
write() # 写数据，b，字节；无b, 字符
close() # 关闭文件
fileno() # 文件描述符
flush() # 将缓存中的内容强制刷入（写入）硬盘 
readable() # 判断文件是否可读，比如一个文件是以w方式打开的，则是不可读的。
readline() # 仅读取一行
truncate() # 截断，清空文件中指针后面的内容
# 常用的操作
f = open('db', 'r+', encoding='utf-8')
for line in f:
    print(line)
'''

# 3. 关闭文件
'''
文件操作完毕后，可以用
f.close();另外如果是以with打开的，with代码块里的文件操作执行完之后会自动关闭文件。
'''
with open('db', 'r+') as f:
    pass



# 文件操作之with处理上下文

with open('xb') as f:
    pass

# 读一行，写一行
with open('db1', 'r', encoding='utf-8') as f1, open('db2','w', encoding='utf-8') as f2:
    times = 0
    for line in f1:
        times += 1
        print(line)
        if times <= 10:
            f2.write(line)
        else:
            break










