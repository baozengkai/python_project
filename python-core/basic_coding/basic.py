#!/usr/bin/env python
# -*- coding:utf-8
"""
    基础知识：
        1.raw_input函数获取用户输入
        2.下划线
            单下划线 ：保护成员
            双下划线 ：私有成员，会触发_className_变量名 的机制，目的放置被子类覆盖名称
            前后双下划线：特殊标识
        3.引用计数
            在Python内部，记录了所有使用的对象有多少引用，当对象创建的时候，创建了一个引用计数并设置为1，
            当对象销毁的时候，引用计数变为0，被当做垃圾回收
          3.1 增加引用计数
        4.实战例子
            创建文件 : 提醒用户输入一个(尚不存在)文件名，然后由用户输入该文件的每一行，最后将内容写入到文件文件中

"""
import os

# 1.raw_input函数获取用户输入
# name = raw_input("Please input your Name:")
# print(name)

# 2.下划线的使用
# class LineTest(object):
#     def __init__(self):
#         self.foo = 11
#         self._bar = 23
#         self.__car = 33
#
#     def _func(self):
#         return 123
#
#     def __func2(self):
#         return 456
#
#
# class LineSubTest(LineTest):
#     def __init__(self):
#         super(LineSubTest, self).__init__()
#         self.foo = 12
#         self._LineTest__car = 66
#
# t = LineTest()
# print t.foo
# print t._bar
# print t._func()
# print t._LineTest__car
#
# print dir(t)
#
# tsub = LineSubTest()
# print tsub.foo
# print tsub._bar
# print dir(tsub)
# print tsub._LineTest__car

# 3.引用计数
# 3.1 增加引用计数
# x = 3.14
# y = x

# 4.实战例子
# file_name = raw_input("Please input file name:")

# f = file(file_name)
# while line:
#     line = raw_input()
#     f.write(line)
#
# f.close()

linesep = os.linesep

# 获取要创建的文件名
file_name = raw_input("Please input file name:")
while True:
    # 判断文件是否存在在当前目录
    if os.path.exists(file_name):
        print "Error : file already exists"
    else:
        break

# 循环获取文件内容，符号.代表输入结束
contents = []
while True:
    line = raw_input('>')
    if line == '.':
        break
    else:
        contents.append(line)
# 调用open和writelines方法将列表内容以遍历方式写入到文件中
f = open(file_name, 'w')
f.writelines(['%s%s' % (line,linesep) for line in contents])
f.close()











