# -*- coding:utf-8 -*-
import contextlib
"""
    协议和抽象基类
        1.协议
        2.抽象基类
"""

# 2.1 抽象基类
import abc


class C(abc.ABC):
    @property
    @abc.abstractmethod
    def a(self): pass

    @classmethod
    @abc.abstractmethod
    def clsa(cls): pass

    @staticmethod
    @abc.abstractmethod
    def stca(): pass


class D(C):
    @property
    def a(self):
        print('property: a')

    @classmethod
    def clsa(cls):
        print('classmethod clsa')

    @staticmethod
    def stca():
        print('staticmethod stca')


@C.register
class R:
    def a(self):
        print("虚拟子类:")


d = D()
d.a
d.clsa()
d.stca()

r = R()
r.a()
print(issubclass(R, C))