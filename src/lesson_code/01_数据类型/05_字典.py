"""
# 字典（Dictionary） 
特性：可变，不是序列
字典用花括号定义，每个元素都是键值对的形式 key: value
字典的键不能存在可变的数据；值没有限制。
字典的键如果重复，会自动去重，保留第一个重复键，并且
其它重复的键对应的值还会对第一个重复键对应的值进行修改；值可以重复。
当字典作为一个iterable对象参与操作时，只有键参与迭代。
"""

"""
## 创建字典的多种方式
"""
'''
① 直接在空字典里面写键值对
'''
from cgi import print_arguments
from typing import type_check_only


d = {'name': 'Tom', 'age': 28}
print(d) # {'name': 'Tom', 'age': 28}

'''
② 定义一个空字典，再往里面添加键值对
'''
d = {}
d['name'] = 'Tom'
d['age'] = 28
print(d)

'''
③ 把键值对作为关键字参数传入
'''
d = dict(name='Tom', age=28)
print(d)

'''
④ 用可迭代对象来构建字典
'''
d = dict([('name', 'Tom'), ('age', 28)])  
print(d)

'''
⑤ 用映射结构来构建字典
'''
d = dict(zip(['name', 'age'], ['Tom', 28]))
print(d) 

'''
dict(**kwargs) / dict(mapping) / dict(iterable)
'''
print(dict())
print(dict(one=1, two=2, three=3)) # {'one': 1, 'two': 2, 'three': 3}
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))

'''
zip(*iterables)
返回一个迭代器，在迭代操作时，其中的第 i 个元组包含来自每个可迭代对象的第 i 个元素
当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代
不带参数时，它将返回一个空迭代器
'''
# 迭代器一定是iterable
# 迭代器如果耗尽, 则无法继续迭代
res = zip('abcd', [4, 5, 7, 1])
# print(dict(res))   # {'a': 4, 'b': 5, 'c': 7, 'd': 1}
print(list(res))   # [('a', 4), ('b', 5), ('c', 7), ('d', 1)]
print(tuple(res))  # ()

res = zip('abcd', [4, 5, 7])
print(tuple(res))  # (('a', 4), ('b', 5), ('c', 7))

res = zip('abcd', [4, 5, 7])
# next(iterator) 内置函数, 返回迭代器的下一个元素
print(next(res)) # ('a', 4) 
print(next(res)) # ('b', 5)
print(next(res)) # ('c', 7)

res = zip('abcd')
print(type(res)) # <class 'zip'>
print(list(res)) # [('a',), ('b',), ('c',), ('d',)]

res = zip()
print(list(res)) # []
print(type(res)) # <class 'zip'>

"""
## 访问和修改字典
"""
'''
访问字典的值 
'''
d = {'Name': 'Tom', 'Age': 7, 'Class': 'First'}
print(d['Name']) # Tom
print(d['Age'])  # 7 
# 如果指定的键不存在, 则报错
d['Gender']  # KeyError: 'Gender'

'''
修改字典
'''
d = {'Name': 'Tom', 'Age': 7, 'Class': 'First'}
# 修改指定键所对应的值
d['Name'] = 'Tony'
d['Age'] = 8
print(d)     # {'Name': 'Tony', 'Age': 8, 'Class': 'First'}
# 如果指定的键不存在, 则新增该键值对
d['Gender'] = 'male'
print(d)     # {'Name': 'Tony', 'Age': 8, 'Class': 'First', 'Gender': 'male'}

""" 
## 字典方法 
"""

''' 
① dict.keys()
返回由字典所有键组成的一个新视图
返回的对象是视图对象，这意味着当原字典改变时，视图也会相应改变
''' 
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_keys = d.keys()
print(type(view_keys)) # <class 'dict_keys'>
print(view_keys)       # dict_keys(['name', 'age', 'height'])

# 修改字典
d['weight'] = 59
print(view_keys)       # dict_keys(['name', 'age', 'height', 'weight'])

'''
② dict.values()
返回由字典所有值组成的一个新视图
返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_values = d.values()
print(view_values)   # dict_values(['Tom', 15, 162])
# 修改字典
d['weight'] = 59
print(view_values)   # dict_values(['Tom', 15, 162, 59])

'''
③ dict.items()
返回由字典所有键和值组成的一个新视图
返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
''' 
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_items = d.items()
print(view_items) # dict_items([('name', 'Tom'), ('age', 15), ('height', 162)])
# 修改字典
d['weight'] = 59
print(view_items) # dict_items([('name', 'Tom'), ('age', 15), ('height', 162), ('weight', 59)])

'''
④ dict.get(key, default=None)
key：键
default：如果指定的键不存在时，返回该值，默认为 None
返回指定的键对应的值，如果 key 不在字典中，则返回default
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
print(d.get('age'))     # 15
print(d.get('weight'))  # None
print(d.get('weight', '该键不存在')) # 该键不存在

'''
⑤ dict.setdefault(key, default=None)
如果字典存在指定的键，则返回它的值
如果不存在，则返回 default 指定的值，并且新增该键值对
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
print(d.setdefault('age'))    # 15
print(d.setdefault('weight')) # None
print(d)                      # {'name': 'Tom', 'age': 15, 'height': 162, 'weight': None}
print(d.setdefault('gender', 'male')) # male
print(d)                      # {'name': 'Tom', 'age': 15, 'height': 162, 'weight': None, 'gender': 'male'}

'''
⑥ dict.update([other])
用 other 来更新原字典，没有返回值
other 可以像 dict() 那样传参
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
d.update(age=18, weight=59)
print(d)  # {'name': 'Tom', 'age': 18, 'height': 162, 'weight': 59} 
d.update({'age': 18, 'weight': 59})
print(d)  # {'name': 'Tom', 'age': 18, 'height': 162, 'weight': 59}
d.update(zip(['age', 'weight'], [18, 59]))
print(d)  # {'name': 'Tom', 'age': 18, 'height': 162, 'weight': 59} 
d.update([('age', 18), ('weight', 59)])
print(d)  # {'name': 'Tom', 'age': 18, 'height': 162, 'weight': 59} 

'''
⑦ dict.pop(key[, default])
key：键
default：指定当键不存在时应该返回的值
移除 key 所对应的键值对，并返回 key 对应的值；如果 key 不在字典中，则返回 default 指定的值，
此时如果 default 未指定值，则报错
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
print(d.pop('height')) # 162
print(d) # {'name': 'Tom', 'age': 15}
print(d.pop('weight', None)) # None
print(d.pop('weight')) # KeyError: 'weight'

''' 
⑧ dict.popitem()
从字典中移除最后一个键值对，并返回它们构成的元组 (key, value)
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
print(d.popitem()) # ('height', 162)
print(d)           # {'name': 'Tom', 'age': 15}
print(d.popitem()) # ('age', 15)
print(d)           # {'name': 'Tom'}
print(d.popitem()) # {'name': 'Tom'}
print(d)           # {}
print(d.popitem()) # KeyError: 'popitem(): dictionary is empty'

'''
⑨ dict.clear()
移除字典中的所有元素，无返回值
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
d.clear()
print(d)

''' 
⑩ dict.copy()
返回该字典的一个副本
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
new_d = d.copy()
print(new_d)

