# -*- coding:utf-8 -*-
from collections import defaultdict
"""
    1.可调用对象
        1.1) 什么是可调用对象
            如果一个类的实例，也就是对象，可以被当做函数来使用，p = Person() p(),相当于重载括号运算符，那么我们就称这个对象是可被调用的。
        1.2) 可调用对象有哪些
            用户自定义函数
            内置函数，比如len
            内置方法，比如dict.get
            类
            对象(前提是该对象实现了__call__方法)
            生成器函数(使用yield的函数)
        1.3) 实现包含__call__方法的类
"""


# 1.3 自定义__call__方法
class Foo:
  def __call__(self):
    print('called')


foo_instance = Foo()
foo_instance()
