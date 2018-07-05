# -*- encoding: utf-8 -*-


'''
Higher-level threading interface
使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
'''
import threading
import time
exit_flag = 0


class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting ' + self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting ' + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            threading.Thread.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新进程
thread_1 = myThread(1, 'Thread-1', 1)
thread_2 = myThread(1, 'Thread-2', 2)

# 开启线程
thread_1.start()
thread_2.start()

print('Existing Main thread')
