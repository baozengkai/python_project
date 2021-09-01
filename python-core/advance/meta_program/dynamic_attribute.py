# -*- coding:utf-8 -*-
"""
    1.动态属性
      1.1 用户可以使用__getattr__方法来实现虚拟属性，当属性不存在的时候，根据自己类维护的数据来进行定制化的返回
"""
from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


feed = FrozenJSON({'Schedule': {'inner': '123'}})
print(feed.Schedule.keys())
print(feed.Schedule.inner)