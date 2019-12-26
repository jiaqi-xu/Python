# -*- encoding: utf-8 -*-
'''
作业需求:
模拟实现一个ATM + 购物商城程序
1. 额度15000或者自定义
2. 实现购物商城，买东西加入购物车，调用信用卡接口结账
3. 可以提现，手续费5%
4. 每月22号出账单，每月10号为还款日期，过期未还，按欠款总额万分之5 每日计息
5. 支持多账户登录
6. 支持账户间转账
7. 记录每月日常消费流水
8. 提供还款接口
9. ATM记录操作日志
10. 提供管理接口，包括账户添加，用户额度，冻结账户等。

bin: 执行文件，入口
    atm.py start 每个程序不超过10行
    shopping.py
config:
    user_db
    log_format
module/core: business logic
log
db

分析设计:
    角色:
        管理员
            1. 创建用户
                记录文件夹
                    2018_03_01
                    2018_04_01
                基本信息
            普通用户的增删改查
            额度15000或者自定义
        普通管理员
            可以提现，手续费5%
            支持多账户登录
            支持账户间转账
            记录每月日常消费流水
            提供还款接口
            ATM记录操作日志
'''