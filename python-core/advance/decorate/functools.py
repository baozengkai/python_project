# -*- coding:utf-8 -*-
import functools
from advance.decorate.time_decorate import clock_decorate
"""
    1.标准库functools: 帮助优雅的写出装饰器
        1.1) functools.wraps(func) 将被装饰的函数的元信息(name、doc等)拷贝到封装的函数wrapper()中
        1.2) functools.lru_cache(maxsize=128, typed=False)
"""
# 1.1 functools.wraps(func)示例
def decorate(func):
    @functools.wraps(func)
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


# 1.2 functools.lru_cache(maxsize=128, typed=True)示例
@clock_decorate
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


fibonacci(6)

print()


@functools.lru_cache()
@clock_decorate
def fibonacci2(n):
    return n if n < 2 else fibonacci2(n-2) + fibonacci2(n-1)


fibonacci2(6)
