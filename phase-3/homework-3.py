#-*- coding: utf-8 -*-
# 材料：http://www.cnblogs.com/wupeiqi/articles/4950799.html

'''
作业实例：
需求：

老板现在给你任务，公司有haproxy配置文件，希望通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作了。

现有ha配置文件如下：
global
        log 127.0.0.1 local2
        daemon
        maxconn 256
        log 127.0.0.1 local2 info
defaults
        log global
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        option  dontlognull

listen stats :8888
        stats enable
        stats uri       /admin
        stats auth      admin:1234

frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.oldboy.org
        use_backend www.oldboy.org if www

backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000

backend buy.oldboy.org
        server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000
'''
import json, os

def fetch(backend):
    flag = False
    fetch_list = []
    with open('config_homework.txt', 'r') as f:
        for line in f:
            if line.strip() == 'backend %s'% backend:
                flag = True
                continue

            if line.strip().startswith('backend'):
                flag = False
                break

            if flag and line.strip():
                fetch_list.append(line.strip())

    return fetch_list


def add(dict_info):
    '''
    {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
    :param dict_info:
    :return:
    '''
    flag = False
    # 用于判断fetch_list的是否都写入新的配置文件中
    has_written = False
    backend = dict_info.get("backend")
    record = dict_info.get('record')
    fetch_list = fetch(backend)

    # 要插入的记录
    record_to_insert = "server %s %s weight %s maxconn %s"%(record['server'], record['server'], record['weight'], record['maxconn'])

    if fetch_list:
        # backend存在，record也已经存在
        if record_to_insert in fetch_list:
            import shutil
            shutil.copy('config_homework.txt', 'new_config_homework.txt' )#再拷贝一份
        else:
            # 将要新加入的记录加入对应backend的list组成新的版本
            fetch_list.append(record_to_insert)
            with open('config_homework.txt', 'r') as read_obj, open("new_config_homework.txt", 'w') as write_obj:
                for line in read_obj:
                    if line.strip() == "backend %s" % backend:
                        write_obj.write(line)
                        flag = True
                        continue

                    if flag and line.strip().startswith("backend"):
                        flag = False

                    if flag:
                        if not has_written:
                            backend_record_count = len(fetch_list)
                            for index in range(backend_record_count):
                                temp = '%s%s' % (' ' * 8, fetch_list[index])
                                if index == backend_record_count - 1:
                                    write_obj.write("\n" + temp + "\n\n")
                                elif index == 0:
                                    write_obj.write(temp + '\n')
                                else:
                                    write_obj.write('\n' + temp + "\n")
                            has_written = True
                    else:
                        write_obj.write(line)
    else: # 如果原来backend不存在，则直接加到配置文件的最后
        with open('config_homework.txt', 'r') as read_obj, open("new_config_homework.txt", 'w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            write_obj.write("\n\nbackend " + backend + "\n")
            write_obj.write(" "*8 + record_to_insert + "\n")

    # 将原文件ha改名备用文件为ha.bak，即将ha下线
    # 将新文件new_config_homework.txt改名为线上文件ha.txt，即将new_config_homework.txt上线
    # os.rename("config_homework.txt", "ha.bak")
    # os.rename("new_config_homework.txt", "ha.txt")


def delete(dict_info):
    flag = False
    # 用于判断fetch_list的是否都写入新的配置文件中
    has_written = False
    del_backend = dict_info.get("backend")
    del_record = dict_info.get("record")
    fetch_list = fetch(del_backend)

    # 要插入的记录
    record_to_delete = "server %s %s weight %s maxconn %s" % (
        del_record['server'], del_record['server'], del_record['weight'], del_record['maxconn'])

    if not fetch_list:# 如果配置文件中没有此backend
        return
    else:
        if record_to_delete not in fetch_list: #用户输入的服务器不在配置文件中
            print("服务器不存在")
            return
        else:
            fetch_list.remove(record_to_delete)

    with open('config_homework.txt', 'r') as read_obj, open(
            "new_config_homework.txt", 'w') as write_obj:
        for line in read_obj:
            if line.strip() == "backend %s" % del_backend:
                if len(fetch_list) != 0:  # 移除后改backend还存在server
                    write_obj.write(line)
                flag = True
                continue

            if flag and line.strip().startswith("backend"):
                flag = False

            if flag:
                if not has_written:
                    backend_record_count = len(fetch_list)
                    for index in range(backend_record_count):
                        temp = '%s%s' % (' ' * 8, fetch_list[index])
                        if index == backend_record_count - 1:
                            write_obj.write("\n" + temp + "\n\n")
                        elif index == 0:
                            write_obj.write(temp + '\n')
                        else:
                            write_obj.write('\n' + temp + "\n")
                    has_written = True
            else:
                write_obj.write(line)


if __name__== "__main__":
    print('1. 获取ha记录\n2. 增加ha记录\n3. 删除ha记录\n')
    select_num = input('请输入操作序号:')

    if select_num == '1':
        backend = input("请输入backend:")
        fetch_list = fetch(backend)
        for i in fetch_list:
            print(i)
    else:
        print("请按以下例子输入:")
        print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
        backend_record_str = input("请输入record:")
        backend_record_dict = json.loads(backend_record_str)
        if select_num == '2':
            add(backend_record_dict)
        elif select_num == '3':
            delete(backend_record_dict)













