# -*- coding: utf-8 -*-
import chardet
import codecs

# 场景:
# 在mac上用文本编辑器打开的csv文件一般编码方式是utf-8
# 但是用execl打开的时候默认用的是gbk，所以出现了乱码，可以使用以下代码进行转换，
# 乱码问题可以得到解决。

#fcsvs = ['测试集.csv', '训练集样本.csv', 'stopwords(1).csv']
#fcsvfixs = ['测试集（修复）.csv', '训练集样本（修复）.csv', 'stopwords(1)（修复）.csv']

#fcsvs = ['训练集样本修改结果.csv', '测试集修改结果.csv']
#fcsvfixs = ['训练集样本修改结果（修复）.csv', '测试集修改结果（修复）.csv']

fcsvs = ["test.csv"]
fcsvfixs = ['test（修复）.csv']
def detect_source_encoding(fin):
    with open(fin, 'rb') as f:
        content_byte = f.read()
    print(chardet.detect(content_byte))
#   source_encoding = chardet.detect(content_byte)['encoding']

def convert_to_uft_8_sig(fin, fout):
    with open(fin, 'r') as f:
        content_str = f.read()
    codecs.open(fout, 'w', encoding='UTF-8-SIG').write(content_str)


for i in range(len(fcsvs)):
    fcsv, fcsvfix = fcsvs[i], fcsvfixs[i]
    detect_source_encoding(fcsv)
    convert_to_uft_8_sig(fcsv, fcsvfix)
