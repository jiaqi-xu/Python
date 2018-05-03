# -*- encoding: utf-8 -*-
'''
作业：选课系统
思路：
    管理员：
        1. 创建老师（爱好，姓名，年龄， 资产=0）
        class Teacher:
                def __init__(self, favor, name, age):
                        self.favor = favor
                        self.name = name
                        self.age = age
                        self.asset = 0

                def 教学事故(self)：
                        self.asset = self.asset - 1

                def gain(self, value):
                        self.asset += value
        obj_1 = Teacher(...)
        obj_2 = Teacher(...)
        obj_3 = Teacher(...)
        obj_4 = Teacher(...)
        [obj_1, obj_2, obj_3, ...]
        pickle.dump([obj_1, obj_2, obj_3], <file_path>)
        # Teacher类型

        2. 创建课程
            teacher_list = pickle.load(<file_path>)
            课程类:
                1. 课程名
                2. 课时费
                3. 负责老师 = teacher_list[0]

            功能:
                上课
                    返回给学生学习的内容
                    负责老师挣钱 li[0].gain(课时费)
            课程对象()

    学生:
        类:

        学生 -> 选课
        __init__(self):
            选课 =  [课程对象]

        上课:
            选课
            1. 生物课
                课程对象.上课()

本次作业所用的知识： pickle序列化和反序列化任何东西（包括对象）, 面向对象的封装
'''





