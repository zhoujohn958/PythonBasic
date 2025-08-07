"""
# 成员运算符 
判断某个对象是否为指定 iterable 的元素
返回布尔值：True，False
in 在其中
not in 不在其中
"""
# 字符串
string = 'hello world'
print('e' in string)      # True
print('lo' in string)     # True
print('ol' not in string) # True
'''
在 Python 中，True 和 False 实际上是整数类型：
True 等于 1
False 等于 0
'''
lst = [True, False, [2, 3], 4]
print(1 in lst)
print(0 in lst)
print(4 in lst)
print(2 not in lst)
print(3 not in lst)

# 字典中，值不参与成员运算
d = {1: 2, 0: 4}
print(True in d)
print(False in d)
print(2 not in d)
print(4 not in d)