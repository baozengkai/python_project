# -*- coding:utf-8 -*-

"""
    遍历字典
    求list的长度\
    取tuple数据(支持下标访问)
"""

# 1.遍历字典
fdict = dict(x=1, y=2)

for item in fdict.items():
    print(item)


# 2.求tuple的长度
li = ['1','2','3']
print(len(li))

# 3.取tuple数据
tp = ((1,),)
tp2 = (('{"logGroup": "fedsf", "dataSet": "20180522"}',),)
print(tp[0])
print(tp2[0][0])
