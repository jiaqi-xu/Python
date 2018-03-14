# -*- encoding: utf-8 -*-
'''
python日志处理之logging模块
'''

import logging
# logging.warning("user [jqx] attempted wrong password more than 3 times")
# logging.critical("server is down")


# 将日志写入到文件中（比这个level级别相同或者更严重的日志才会写入文件中）
logging.basicConfig(
    filename='example.log', level=logging.INFO,
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
    )  #
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


'''
logger模块进阶
'''
import logging

# create logger
logger = logging.getLogger('TEST-LOG') # 先获取logger对象
logger.setLevel(logging.DEBUG) # 设置全局日志级别(全局优先级别高)

# create console handler and set level to debug
ch = logging.StreamHandler() # print the log on monitor
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler('access.log')
fh.setLevel(logging.WARNING)

# create formatter
formatter_for_console = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_for_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter_for_console)
fh.setFormatter(formatter_for_file)

# add ch and fh to logger
logger.addHandler(ch) # 告诉logger输出日志到某个给定的handler上
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
