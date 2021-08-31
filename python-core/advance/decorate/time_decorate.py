# -*- coding:utf-8 -*-
import time
"""
    装饰器:
        运行时间装饰器
"""


def clock_decorate(func):
    """
    运行时间装饰器
    :param func: 被装饰的函数
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        diff_time = time.perf_counter() - start_time
        repr_args = ",".join(str(arg) for arg in args)
        print("[%0.8fs] %s(%s) 0> %s" % (diff_time, func.__name__, repr_args, result))
        return result
    return wrapper
