fi = open("字符.txt", "r")
fo = open("字符统计.txt", "w")

fi.seek(0, 2)
eof = fi.tell()
fi.seek(0, 0)
#import ipdb; ipdb.set_trace()
ch_dict = {}
while (fi.tell() != eof):

    ch = fi.read(1)
    import ipdb;

 #   ipdb.set_trace()
    if '\u4e00' <= ch < '\u9fa5':
        if ch in ch_dict.keys():
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 1


print(ch_dict)
ls = []
for key in ch_dict.keys():

    item = "%s (%s): %s" % (key, hex(ord(key)), str(ch_dict[key]))
    ls.append(item)

fo.write("\n".join(ls))
fi.close()
fo.close()