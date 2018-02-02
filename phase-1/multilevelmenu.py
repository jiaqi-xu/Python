#-*- coding: utf-8 -*-
'''
Requirement：implement a multilevel menu. 实现多级菜单
1. three level menu. 三级菜单
2. can go to sub-menu when choose the chioce. 可依次选择进入各子菜单
3. 用到了字典，列表。

Implemeation 递归实现。
可通过输入相应的菜单目录进入下一级菜单，并且可以随时返回至上一级菜单或者退出菜单系统。
练习了字典，列表的功能。
用temporary_list存储上一级菜单用于返回上一级。
'''



multilevel_menu = {
    'North America': {
        'Canada': ['Ottawa', 'Toronto', 'Montreal', 'Vancouver'],
        'America': ['New York', 'Washington', 'Los Angeles', 'Chicago']
    },
    'Asian': {
        'China': ['Beijing', 'Shanghai', 'Shenzheng', 'Zhejiang'],
        'Japan': ['Tokyo', 'Kyoto', 'Osaka'],
        'korea': ['Seoul', 'Busan', 'Incheon']
    }
}

print 'Welcome To Cities Map'.center(50, '*')

temporary_list = [multilevel_menu]


def run_mutiplevel_menu(current_level_menu, n):
    if n > 0:
        while True:
            current_level_menu_item_num = 0
            for index, item in enumerate(current_level_menu, 1):
                current_level_menu_item_num += 1
                print str(index) + '.' + item

            print 'WARM PROMPT:\n1.choose area number go to check count' \
                  'ries\n2.choose B or b return previous menu\n3.choose Q or q to quit'

            choice = raw_input('please enter your choice:').strip()

            if choice.isdigit():  # do not need to convert to int
                if int(choice) in range(1, current_level_menu_item_num+1):
                    if type(current_level_menu) != list: # 如果不是最后一级菜单
                        choices_list = current_level_menu.keys()
                        item_name = choices_list[int(choice) - 1]
                        next_level_menu = current_level_menu.get(item_name)
                        temporary_list.append(current_level_menu) #存储当前菜单
                        return run_mutiplevel_menu(next_level_menu, n+1) # print out next level menu recursively
                    else:
                        print 'Congratulation, you get the city: '.format(
                            current_level_menu[int(choice)-1]
                        )
                        b_or_q = raw_input(
                            'It is the last level menu, '
                            'please return to previously menu or exit:'
                        )

                        if b_or_q == 'B' or b_or_q == 'b':
                            print 'returned to previous menu.'
                            return run_mutiplevel_menu(temporary_list.pop(), n-1)

                            # print last menue
                        elif b_or_q == 'Q' or b_or_q == 'q':
                            print 'exit to menu system'
                            break

                else:
                    print 'area number does not exist, please enter again'
                    continue
            else:
                if choice == 'B' or choice == 'b':
                    if n == 1:
                        print 'it is already the main menu!'
                    else:
                        print 'returned to previous menu.'
                        return run_mutiplevel_menu(temporary_list.pop(), n-1)

                    # print last menue
                elif choice == 'Q' or choice == 'q':
                    print 'exit to menu system'
                    break

                else:
                    print 'the command you enter is not correct!'
                    continue

run_mutiplevel_menu(multilevel_menu, 1)

