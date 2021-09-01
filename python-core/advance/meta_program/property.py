# -*- coding:utf-8 -*-
"""
    1.@property装饰器
      1.1) 类的getter和setter方法
      1.2) 场景一: 让方法可以像属性一样被访问
           场景二: 设置只读装饰，防止属性被修改
      1.3) property装饰问题
           1.3.1) 当类属性和实例属性同名的时候，通过实例对象读取属性的时候，读取的是实例属性，通过类读取属性的时候，读取是类属性
           1.3.2) 特性可以被覆盖修改
      1.4) 相关内置函数和属性
           1.4.1) __dict__和vars()(PS: 类本身和对象本身都可以调用__dict__)
"""


# 1.1 普通的getter和setter方法
class LineItem:
    """
    """

    def __init__(self, description, weight, price):
        self.descriptionn = description
        self.weight = weight
        self.price = price

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight


line_item = LineItem("book1", 1, 10)
print(line_item.get_weight())


# 1.2 @propert装饰的getter和setter方法
class LineItem2:
    """
    """
    data = "LineItem2"

    def __init__(self, description, weight, price):
        self._description = description
        self._weight = weight
        self._price = price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight


line_item2 = LineItem2("book2", 2, 20)
print(line_item2.weight)
print(vars(line_item2))
print(vars(LineItem2))


# 1.3 类属性、实例属性和特性
class Class:
    data = "the class data str"

    @property
    def prop(self):
        return "the prop value"


# 1.3.1) 当类属性和实例属性同名的时候，通过实例对象读取属性的时候，读取的是实例属性，通过类读取属性的时候，读取是类属性
obj = Class()
# print(vars(obj))
# obj.data = 'object value'
# print(vars(obj))
# print(Class.data)
# print(obj.data)


# 1.3.2) 特性可以被覆盖销毁
print(obj.prop)
print(Class.__dict__)
Class.prop = 'baz'
print(Class.__dict__)
print(obj.__dict__)
print(obj.prop)