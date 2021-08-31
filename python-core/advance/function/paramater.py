# -*- coding:utf-8 -*-
from collections import defaultdict
"""
    1.参数
        1.1) 位置参数
        1.2) 关键参数
            关键参数可以不考虑参数的顺序，让函数的使用更加容易，同时给与一些参数默认值
        1.3) 可变参数
            一个星和两个星捕获任意数量的参数
        1.4) 混合参数场景
        1.5) 单独星号和强制关键性参数
            (*,arg1, arg2): 注意单独星号和带*args这种是不一样的，一个是不让输入任意参数，一个是捕获所有非关键性参数                  
            __defaults__: 形式参数默认值      
            __kwdefaults__: 强制关键性参数默认值
        1.6) 获取函数的参数信息
            Signature类获取函数的参数信息        
"""


# 1.2 关键参数
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(c=20, a=10)
func(1, c=20)
print(func.__defaults__)
print(func.__kwdefaults__)


# 1.3 可变参数
def func2(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中所有的项目
    for value in numbers:
        print('value', value)

    for key, value in phonebook.items():
        print(key, value)


func2(10, 1, 2, 3, xiaobao=20, xiaoya=20)
print(func2.__defaults__)
print(func2.__kwdefaults__)


# 1.4 混合参数场景
def tag(name, *content, cls=1, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(my_tag))
print(tag(*my_tag))
print(tag(**my_tag))
print(tag.__defaults__)
print(tag.__kwdefaults__)


# 1.5 强制关键性参数
# 1.5.1 单独的星号意味着参数的终结，不能传参数，同时使后面的参数变成强制关键性参数，后面的参数必须要以关键字参数传递
# def add(*, x, y):
#     print(x, y)
#
#
# print(add(1, 2, 3))  # 报错，提示多余参数，不能传递位置参数
# print(add(1, x=2, y=3))  # 报错，提示多余参数，不能传递位置参数
# print(add(x=2, y=3))  # 正确，未传递位置参数


# 1.5.2 单独的星号变种
def add(x, *, y, z):
    print(x, y, z)


# print(add(1, 2, y=3, z=4))  # 错误
add(1, y=2, z=3)  # 正确
print(add.__defaults__)
print(add.__kwdefaults__)

# 1.6 获取函数参数的信息
from inspect import signature


def foo(value1, value2='word'):
    return value1


foo2 = signature(foo)
for name, param in foo2.parameters.items():
    print(name, '=', param.default)

foo2.bind(1)
#foo2.bind()




