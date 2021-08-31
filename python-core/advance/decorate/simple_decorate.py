# -*- coding:utf-8 -*-
from advance.decorate.time_decorate import clock_decorate
"""
    1.简单装饰器:
        1.1) 不带参数装饰器
        1.2) 被装饰函数带任意参数的装饰器
        1.3) 装饰器本身带参数
"""


# 1.1 不带参数装饰器
def decorate(func):
    def wrapper():
        print(func.__name__)
        return func()
    return wrapper


@decorate
def say_hello():
    print("hello")


@decorate
def say_hi():
    print("Hi")


hello = say_hello()
hi = say_hi()
print(say_hello.__name__)
print(say_hi.__name__)


# 1.2 带任意参数装饰器
def decorateFuncWithParam(func):
    def wrapper(*args, **kwargs):
        print("decorate func with parameters: %s" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@decorateFuncWithParam
def say_hello_param(value):
    print(value)


@decorateFuncWithParam
def say_hi_parram(value2="2"):
    print(value2)


hello_param = say_hello_param(1)
hi_param = say_hi_parram(value2=3)


# 1.3 装饰器带参数
def decorateWithParam(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("Level is: %s", level)
            print("decorate func with parameters: %s", func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@decorateWithParam(level='Debug')
def say_hello_outer_param(value):
    print(value)


@decorateWithParam(level='Warning')
def say_hi_outer_parram(value2="2"):
    print(value2)


say_hello_outer_param(1)
say_hi_outer_parram()