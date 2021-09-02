# -*- coding:utf-8 -*-
import contextlib
"""
    1.上下文管理器
      1.1) 概念
        上下文表达式: with open('file.path') as f
        上下文管理器: open('file.path')
        资源对象: f
      1.2) 如何实现一个上下文管理器
        open()函数返回的是TextIOWrapper类的实例，该类实现了__enter__和__exit__方法
        实现__enter__()方法
        实现___exit__()方法
        关于异常处理: 如果有异常出现，会传入到__exit__方法中，若__exit__方法返回True，表示异常已经处理；若__exit__方法
            未返回True，则异常向上抛出
      1.3) 基于@contextmanager装饰器实现上下文管理器
        使用标准库中的装饰器可以简化上下文管理器的操作，不用单独创建一个上下文管理器的类
        @contextmanager
        该装饰器将自定义生成器函数包装成__enter__和___exit__方法
      1.4) 类上下文管理器和@contextmanager装饰的上下文管理器区别
        引发异常时,__exit__方法正常进行
        引发异常时,异常传递给生成器，如果生成器无法处理异常，那么yield之后的代码无法执行。通常yield代码需要在try...except块中    
"""
#
# # 1.1 经典的上下文管理文件打开代码
# with open("text.txt") as f:
#     print(f.readline(1))
#
#
# # 1.2 自定义上下文管理器类
# class ResourceManager:
#     def __init__(self, resource_name):
#         self.resource_name = resource_name
#         self.file = None
#
#     def __enter__(self):
#         print("__enter__")
#         self.file = open(self.resource_name)
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if self.file:
#             self.file.close()
#
#
# with ResourceManager("text.txt") as f:
#     print(f.readlines())


# 1.3 使用@contextmanager
@contextlib.contextmanager
def open_file(file_name):
    file = open(file_name)
    try:
        yield file
    except Exception:
        print(123)
    finally:
        if file:
            file.close()


with open_file("text.txt") as f:
    print(f.readlines)
