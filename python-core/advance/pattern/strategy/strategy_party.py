# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractclassmethod
"""
    策略模式之一:
        场景: 小明离职，同事选择交通工具去聚餐
"""


class Vehicle(metaclass=ABCMeta):
    """
    策略抽象基类
    """

    @abstractclassmethod
    def running(cls):
        pass


class Walk(Vehicle):
    """
    步行策略类
    """
    def running(cls):
        print("I am Walking!!!")


class Subway(Vehicle):
    """
    火车策略类
    """
    def running(cls):
        print("I am drive Subway!!!")


class Bicycle(Vehicle):
    """
    自行车策略类
    """
    def running(cls):
        print("I am drive Bicycle!!!")


class Classmate:
    """
    """
    def __init__(self, name, vehicle):
        self.__name = name
        self.__vehicle = vehicle

    def party(self):
        self.__vehicle.running()
        print("我做了其他额外的封装任务")


# 使用了走路策略，并且通过上下文类的封装方法来实现具体的封装行为
walk = Walk()
person1 = Classmate("person1", walk)
person1.party()

person2 = Classmate("person2", Subway())
person2.party()