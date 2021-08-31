# -*- coding:utf-8 -*-
import time
from advance.decorate.time_decorate import clock_decorate
"""
    装饰器:
        运行时间装饰器装饰的实例
"""


@clock_decorate
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


print("6!=", factorial(6))

