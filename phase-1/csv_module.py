#-*- coding: utf-8 -*-
import csv
'''
#以普通文件的形式读
users_list = open('users_list.csv', 'r')
users_reader = csv.reader(users_list, delimiter=',')
for row in users_reader:
    print row
'''


#以字典形式读
users_list = open('users_list.csv', 'r')
users_reader = csv.DictReader(users_list, delimiter=',')
print users_reader.fieldnames
for row in users_reader:
    print row


'''
向csv文件中以字典形式写入数据
black_list = open('black_list.csv', 'w')
file_header = ['username', 'password']
black_users_writer = csv.DictWriter(black_list, file_header)
black_users_writer.writeheader()
black_users_writer.writerow({'username': 'blackman', 'password': 888888})
'''

'''
#向csv文件中以字典形式追加写入数据
black_list = open('black_list.csv', 'a')
file_header = ['username', 'password']
black_users_writer = csv.DictWriter(black_list, file_header)
black_users_writer.writerow({'username': 'blackman'})
'''