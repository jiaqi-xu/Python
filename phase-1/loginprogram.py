#-*- coding: utf-8 -*-
import csv
import json

try_times = 0
# a dict of which the key is username
# and value is times of wrong input within a period
wrong_input_dict = {}
while True:
    # just check the wrong input dict in file
    wrong_times_log = open('wrong_input_count_log.txt', 'w')
    json.dump(wrong_input_dict, wrong_times_log)
    wrong_times_log.close()

    print '**********************Welcome To Login Page**********************'
    black_user_list = []

    username = raw_input('please enter your username:')
    password = raw_input('please enter your password:')

    # get black user list
    black_list = open('black_list.csv', 'r')
    black_reader = csv.DictReader(black_list, delimiter=',')
    for row in black_reader:
        black_user_list.append(row.get('blackuser'))
    black_list.close()

    # open the file contains existing users
    users_list = open('users_list.csv', 'r')
    users_reader = csv.DictReader(users_list, delimiter=',')

    # banned flag
    banned_flag = False

    for row in users_reader:
        if username in black_user_list:
            banned_flag = True
            break


        if row.get('username') == username:
            if row.get('password') == password:
                print 'You Login Successfully!'
                exit()

            else:
                # if type a wrong password
                users_list.close()
                # log the times of wrong input 记录输入错误次数
                wrong_time_curr_user = int(wrong_input_dict.get(username,0))

                total_wrong_times_now = wrong_time_curr_user + 1

                wrong_input_dict.update({username: total_wrong_times_now})

                if total_wrong_times_now == 3:
                    print 'Too many times, your account ' \
                          'is banned at present, please try later'
                    black_list = open('black_list.csv', 'a')
                    black_list_header = ['blackuser', 'password']
                    black_writer = csv.DictWriter(black_list, black_list_header)
                    black_writer.writerow({'blackuser': username})
                    black_list.close()
                else:
                    print 'username or password is not ' \
                          'correct, please try again.'

                break
        else:
            continue

    # if it is a banned account
    if banned_flag:
        print 'Your account is banned'
    else:
        print 'username or password is not correct, please try again.'

    print '**************************End of Login Page***********************'







