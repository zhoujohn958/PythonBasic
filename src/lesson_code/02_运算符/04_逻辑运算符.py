"""
and 布尔"与"（左边bool判定为False，返回左边；否则返回右边）
or 布尔"或"（左边bool判定为True，返回左边；否则返回右边）
not 布尔"非"（判定为False，返回 True；判定为True，返回False）
"""
a = 2
b = 'hello'
c = []
d = 0

print(c and a)  # []
print(a and c)  # []
print(d and c)  # 0
print(c and d)  # []
print(a and b)  # 'hello'
print(b and a)  # 2

print(a or c)  # 2
print(c or a)  # 2
print(b or a)  # 'hello'
print(a or b)  # 2
print(c or d)  # 0
print(d or c)  # []

print(not a)  # False
print(not b)  # False
print(not c)  # True
print(not d)  # True

# 优先级：not > and > or
print(b and not a or c) # []

'''
短路机制
在逻辑表达式中，由于and和or的特点，表达式中的部分内容可能不会执行
'''
a = 0
b = 1
c = ()
print(c and b / c) # ()
print(b or a + c)  # 1
b and a + c        # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

'''
all(iterable)
如果 iterable 的所有元素 bool 判定都为 True，则返回 True
如果 iterable 为空，也返回 True
'''
tup = ('0', ' ', 'None', 'False', '[]')
# print(bool(0))   # False
# print(bool('0')) # True
print(all(tup)) # True
print(all([])) # True

'''
any(iterable)
如果 iterable 中存在至少一个元素 bool 判定为 True，则返回 True
如果 iterable 为空，也返回 False
'''
tup = (0, '', None, False, [])
print(any(tup)) # False
print(any([]))  # False

