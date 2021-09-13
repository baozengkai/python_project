# -*- coding:utf-8 -*-
from inspect import getgeneratorstate
from functools import wraps
from collections import namedtuple
"""
    1.协程
      1.1 协程的四种状态  
      1.2 基于生成器的协程
      1.3 预激活协程装饰器
      1.4 协程最后返回值
      1.5 yield from      
"""


# 1.2 基于生成器的协程
# def simple_coroutine():
#     print("-->coroutine started")
#     x = yield
#     print("-->coroutine received: ", x)
#
#
# coroutine1 = simple_coroutine()
# print(getgeneratorstate(coroutine1))
# next(coroutine1)
# print(getgeneratorstate(coroutine1))
# next(coroutine1)
#
#
# # 1.3 预激活协程装饰器
# def coroutine(func):
#     @wraps(func)
#     def func(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         next(gen)
#         return gen


# 1.4 协程返回最后一个值(返回最后的平均值)
# Result = namedtuple("Result", "count average")
# def average():
#     total = 0
#     count = 0
#     average = None
#     while True:
#         item = yield
#         if item is None:
#             break
#         total += item
#         count += 1
#         average = total/count
#     return Result(count, average)
#
# coroutine_average = average()
# next(coroutine_average)
# coroutine_average.send(10)
# coroutine_average.send(20)
# # 第一种版本
# # coroutine_average.send(None)
# # 第二种版本 将异常捕获
# try:
#     coroutine_average.send(None)
# except StopIteration as e:
#     print("协程最后一个值为: ", e.value)
#
#
# # 1.5 yield from
# def proxy_coroutine():
#     while True:
#         yield from average()
#
#
# proxy = proxy_coroutine()
# next(proxy)
# proxy.send(10)
# proxy.send(20)
# proxy.send(None)
