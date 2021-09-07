# -*- coding:utf-8 -*-
"""
    1.继承
      1.1) 继承内置类型很麻烦
      1.2) 继承的访问控制
           单继承示例
           多重继承示例(一个子类继承多个父类)
           多级继承示例(孙子类继承子类、子类继承父类)
           关于__init__子类和父类调用 
      1.3) 方法重写和super调用父类方法
           super直接在父类中查找方法
      1.4) @classmethod和@staticmethod方法使用和继承
           @classmethod用于多个构造函数
           @staticmethod用于独立于类本身的逻辑
"""


# 1.2.1 单继承示例继承的访问控制
# class Animal:
#     __COUNT = 100
#     HEIGHT = 0
#
#     def __init__(self, age, weight, height):
#         self.__COUNT += 1
#         self.age = age
#         self.__weight = weight
#         self.HEIGHT = height
#
#     def eat(self):
#         print("{} eat".format(self.__class__.__name__))
#
#     def __getweight(self):
#         print(self.__weight)
#
#     @classmethod
#     def showcount1(cls):
#         print(cls)
#         print(cls.__dict__)
#         print(cls.__COUNT)
#
#     @classmethod
#     def __showcount2(cls):
#         print(cls.__COUNT)
#
#     def showcount3(self):
#         print(self.__COUNT)
#
#
# class Cat(Animal):
#     NAME = 'CAT'
#     __COUNT = 200
#
#
#
# c = Cat(3, 5, 15)
# c.eat()
# print(c.showcount1())
# # print(c.showcount2())  # 不可访问，因为是类的私有方法
# print(c.showcount3())
# print(c.NAME)
# print(c.HEIGHT)

# 1.2.2 多重继承示例
class Parent:
    def func1(self):
        print("this is Parent1 function 1")


class Parent2:
    def func2(self):
        print("this is Parent2 function 2")


class Child(Parent, Parent2):
    def func3(self):
        print("this is Child function 3")


child = Child()
child.func1()
child.func2()
child.func3()


# 1.2.3 多级继承示例
class Parent:
    def func1(self):
        print("this is Parent function 1")


class Child(Parent):
    def func2(self):
        print("this is Child func 2")


class GrandSon(Child):
    def fun3(self):
        print("this is GrandSon fun 3")

grandSon = GrandSon()
grandSon.func1()

# 1.3.1 方法重写和super调用父类方法
# class Animal:
#     def shout(self):
#         print("Animal shouts")
#
#
# class Cat(Animal):
#     def shout(self):
#         super().shout()
#         super(Cat, self).shout()
#         self.__class__.__base__.shout(self)
#
#
# animal = Animal()
# animal.shout()
#
# cat = Cat()
# cat.shout()

# 1.4.1 @classmethod用于多个构造函数
# class Book(object):
#
#     def __init__(self, title):
#         self.title = title
#
#     @classmethod
#     def class_instance_init(cls, title):
#         book = cls(title=title)
#         return book
#
#
# book_1 = Book("数学")
# book_2 = Book.class_instance_init("语文")
# print(book_1.title)
# print(book_2.title)


# 1.4.3 关于类方法和静态方法的继承
# class Animal:
#
#     @classmethod
#     def class_method(cls):
#         print("class_method_animal")
#
#     @staticmethod
#     def static_method():
#         print("static_method_animal")
#
#
# class Cat(Animal):
#
#     @classmethod
#     def class_method(cls):
#         print("class_method_cat")
#
#     @staticmethod
#     def static_method():
#         print("static_method_cat")
#
#
# c = Cat()
# c.class_method()
# c.static_method()
