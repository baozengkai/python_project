# -*- coding:utf-8 -*-
from collections import defaultdict
from types import MappingProxyType
"""
    1.字典创建
    2.字典函数
        len()
    3.字典访问
        下标访问
    4.字典推导
    5.利用setdefault方法和defaultdict类处理找不到的键
      一般的dict，在获取某个不存在的键的时候，会报错  
      通常使用get方法，给一个默认值，避免出错，但是使用setdefault和defaultdict效率更高以及更优雅
    6.不可变映射类型
"""


# # 1.遍历字典
# fdict = dict(x=1, y=2)
#
# for item in fdict.items():
#     print(item)
#
# # 2.求tuple的长度
# li = ['1', '2', '3']
# print(len(li))
#
# # 3.取tuple数据
# tp = ((1,),)
# tp2 = (('{"logGroup": "fedsf", "dataSet": "20180522"}',),)
# print(tp[0])
# print(tp2[0][0])
#
# # 4.字典推导
# country_list = [("china", 5000), ("USA", 100), ("India", 10000)]
# country_dict = {country: country_history for country, country_history in country_list}
# print(country_dict)
#
# # 5.使用setdefault方法和defaultdict类处理找不到的键
# print(country_dict.setdefault("Japan", "1"))
# print(country_dict["1"])
#
# new_default_dict = defaultdict(str)
# new_default_dict["1"] = 1
# print(new_default_dict)
# print(new_default_dict["2"])
# print(new_default_dict)

# 6.不可变映射类型
dict = {'1': "test"}
stable_dict = MappingProxyType(dict)
stable_dict["1"] = 10
print(stable_dict)
dict["1"] = 10
print(stable_dict)
