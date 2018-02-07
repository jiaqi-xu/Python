#-*- coding: utf-8 -*-

'''
Homework requirement:
1. optimize shopping program, allow user choose number of goods to buy when shopping
   优化购物程序，购买时允许用户选择购买多少件商品
2. 允许多用户登陆，下一次登陆后，继续按上次的余额继续购买 （可以充值）
3. 允许用户查看之前的购买记录（记录要显示商品购买时间）
4. 商品列表分级显示，比如：
    第一层菜单：
    1. 家电类
    2. 衣服
    3. 手机类
    4. 车类
    ...
    选择类型，比如车类，进入第二层菜单：
    1. BMW 33333
    2. Audi 33355
    3. Pasate 33335
    4. Tesla Model_3 430000
    5. Tesla Model S 888888
5. 显示已购买的商品时，如果有重复的商品，不打印多行，而是在一行展示
  id     p_name    num  total_price
  1.  TeslaModel    2     xxx
  2.  Coffee        2     60
  3.  Bike          1     100

Stuff will be used: File operation, datatime模块， json 序列化
'''

