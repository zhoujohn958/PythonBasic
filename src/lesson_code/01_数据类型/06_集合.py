"""
# 集合（Set） 
特性：可变，不是序列
集合也用花括号定义，但其中的元素不是键值对
集合中不能存在可变的数据
集合是无序的
集合的元素如果重复，会自动去重
创建空集合必须用 set()，因为 {} 已用来创建空字典
"""
# 空集合
s = set()
print(s)    # set()

# 空字典
d = {}
print(d)
print(type(d))  # <class 'dict'>

s = {789, 456, "hello", (135,), 'world'}
print(s) # {(135,), 789, 456, 'world', 'hello'}

'''
set([iterable])
将一个iterable对象转化为集合并返回，如果没有实参，则返回空集合
'''
print(set())
print(set("hello"))      # {'e', 'o', 'l', 'h'}
print(set([1, 2, 3]))    # {1, 2, 3}
print(set((1, 2, 3)))    # {1, 2, 3}
# 字典作为一个iterable, 只有键参与迭代
print(set({1: 2, 3: 4})) # {1, 3}

"""
## 集合方法
"""
'''
① set.update(*iterables)
更新集合，添加来自 iterables 中的所有元素
'''
s = '12'
lst = [1, '2']
d = {1: '1', 2: '2'}
set1 = {'1', '2', 1, 3}
set1.update(s, lst, d)
print(set1)  # {1, '1', 3, 2, '2'}

'''
② set.add(elem)
将指定元素添加到集合中。如果元素已经存在，则不做任何操作
'''
s = {1, 2, 3}
s.add(2) 
print(s) # {1, 2, 3} 

s.add("hello world")
print(s)  # {'hello world', 1, 2, 3}

'''
③ set.remove(elem)
从集合中移除指定元素。 如果指定元素不存在，则报错
'''
s = {1, 2, 3, 4}
s.remove(3)
print(s)  # {1, 2, 4}
s.remove(5) # KeyError: 5

'''
④ set.discard(elem)
从集合中移除指定元素。 如果指定元素不存在，则不做任何操作
'''
s = {1, 2, 3, 4}
s.discard(3)
print(s)     # {1, 2, 4}
s.discard(3)
print(s)     # {1, 2, 4}

'''
⑤ set.pop()
从集合中移除并返回任意一个元素。如果集合为空，则报错
'''
s = {'1', 'hello', 789}
print(s.pop()) # 1
print(s)       # {789, 'hello'}
print(s.pop()) # 789
print(s.pop()) # hello
print(s.pop()) # KeyError: 'pop from an empty set'

'''
⑥ set.copy()
返回该集合的一个副本
''' 
set1 = {'1', '2', 1, 3}
set2 = set1.copy()
print(set2) # {'2', '1', 3, 1}

''' 
⑦ set.clear()
从集合中移除所有元素
''' 
s = {'1', '2', 'hello', 789}
s.clear()
print(s) # set()
