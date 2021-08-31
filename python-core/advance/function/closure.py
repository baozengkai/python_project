# -*- coding:utf-8 -*-
from collections import defaultdict
"""
    1.变量作用域规则
        变量作用域包含四个范围，分别是内部函数作用域、嵌套函数的内部作用域、全局作用域、内置作用域
        1.1) 变量范围
    2.闭包
        2.1) 闭包示例: 实现历史平均值计数的函数
    3.nonlocal声明    
"""

# # 1.1 全局变量
# b = 6
#
#
# def foo(a):
#     print(a)
#     print(b)
#
#
# foo(1)
#
#
# # 1.2 python在编译函数的时候确定变量的作用域范围
# def foo2(a):
#     print(a)
#     print(b)  # python在编译函数的定义体的时候，判断b是局部变量，尝试获取b的值的时候，发生错误
#     b = 9
#
#
# foo2(1)
#
#
# # 1.3 要想明确使用全局变量，使用global关键字
# def foo3(a):
#     global b
#     print(a)
#     print(b)
#     b = 9
#
#
# foo3(1)
# b = 9
# foo3(1)


# 2.1 闭包实现访问可存储历史平均值
def make_average():
    series = []

    def average(value):
        series.append(value)
        total = sum(series)
        return total/len(series)

    return average


avg = make_average()
print(avg(1))
print(avg(2))
print(avg(3))


# 3.1 改进闭包，实现高效率计算历史平均值
def make_average_2():
    count = 0
    total = 0

    def average(value):
        # nonlocal count, total
        count = count + 1  # 不可变类型会导致局部变量count的产生，从而导致错误，需要使用nonlocal将其声明为自由变量
        total = total + value
        return total/count

    return average()
