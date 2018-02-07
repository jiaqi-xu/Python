#-*- coding: utf-8 -*-

'''
购物小程序：
用户启动时先输入工资

用户启动程序后打印商品列表
允许用户选择购买商品
允许用户不断的购买各种商品

购买时，检测余额是否足够，如果足够，直接扣款，否则打印余额不足
允许用户主动退出程序，退出时打印已购商品列表
'''

salary = raw_input('Input your salary:')
if salary.isdigit():
    salary = int(salary)
else:
    exit('Invalid data tpye....')

welcome_msg = 'Welcome to Alex Shopping mall'.center(50, '-')
print welcome_msg

exit_flag = False

product_list = [
    ('Cloth', 200),
    ('Bike', 700),
    ('Iphone', 5888),
    ('Mac Air', 8000),
    ('XiaoMi 2', 19.9),
    ('Coffee', 30),
    ('Tesla', 820000)
]

shopping_car = []
while not exit_flag:
    print 'Product List'.center(50, '-')
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print index, '.', p_name, p_price

    user_choice = raw_input('[q=quit, c=check]What do you want to buy?')
    if user_choice.isdigit(): # 肯定是选商品
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
                shopping_car.append(p_item)  # 添加进购物车
                salary -= p_item[1] # 减去商品的价格
                print 'Added [%s] into shopping car, ' \
                      'your current balance is \033[31;1m[%s]\033[0m' % (p_item, salary) #31红色，32绿色 改变字体颜色
            else:
                print 'Your balance is [%s], can not afford this..' % salary

    else:
        if user_choice == 'q' or user_choice == 'quit':
            print 'Your shopping list as below:'.center(40, '*')
            for item in shopping_car:
                print item
            print 'End shopping system'.center(40, '*')
            print 'Your balance is [%s]' % salary
            print 'Bye...'
            exit_flag = True
        elif user_choice == 'c' or user_choice =='check':
            print 'Your shopping list as below:'.center(40, '*')
            for item in shopping_car:
                print item
            print 'End shopping system'.center(40, '*')
            print 'Your balance is \033[41;1m[%s]\033[0m' % salary  # 改变字体背景颜色（41红色， 42绿色）
        else:
            print 'Please enter correct command.'







