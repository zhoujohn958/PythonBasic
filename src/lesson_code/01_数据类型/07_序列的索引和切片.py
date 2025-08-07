"""
六种标准数据类型中是序列的有：字符串、列表、元组。
所以它们都可以通过索引和切片的方式来访问其中的元素
"""

'''
# 序列的索引
''' 
# 字符串索引 
string = "Hello 1牛马3 Python"
print(string[8])  # 马
print(string[-9]) # 马

""" 索引超出范围时, 会报错 """
# IndexError: string index out of range
print(string[17])  
print(string[-18])

# 列表索引 
lst = [567, 'hello', True, False, 456]
print(lst[1])  # hello
print(lst[-4]) # hello

# 元组索引
tup = (567, 'hello', True, False, 456)
print(tup[1])  # hello
print(tup[-4]) # hello

'''
# 序列的切片
seq[start: end: step]
start: 起始索引，闭区间
步长为正数，start没有指定，默认为0
步长为负数，start没有指定，默认为-1
end: 结束索引，开区间
步长为正数，end没有指定，默认为len(seq)
步长为负数，end没有指定，默认为-len(seq)-1
step: 步长，没有指定时，默认为1
步长为正数，表示从左往右取数据
步长为负数，表示从右往左取数据
如果start到end的方向和step的正负性不一致，则得到空序列
索引超出范围会报错，但切片不会
''' 
string = 'Hello 1牛马3 Python'
"""
正向索引和反向索引都可以使用
步长默认为1, 取连续的数据
"""
print(string[7: 11])   # '牛马3'
print(string[-9: -5])  # '马3 P'
print(string[7: -5])   # '牛马3 P'
print(string[-9: 11])  # '马3'

""" 步长为2, 取数据时要隔一个再取 """
print(string[7: 14: 2])  # '牛3Pt'

""" 步长为3, 取数据时要隔两个再取 """
print(string[7: 14: 3]) # '牛 t'

""" 步长为负数, 表示从右往左取数据 """
print(string[10: 6: -1]) # ' 3马牛'

""" 步长为-2, 表示从右往左隔一个取数据 """
print(string[13: 6: -2]) # 'tP3牛'

""" 步长为正数, start没有指定, 默认为0 """
print(string[: 3])  # 'Hel'
print(string[0: 3]) # 'Hel'

""" 步长为负数, start没有指定, 默认为-1 """
print(string[: 12: -1])   # 'noht'
print(string[-1: 12: -1]) # 'noht'

""" 步长为正数, end没有指定, 默认为len(string) """
print(string[13:])            # 'thon'
print(string[13:len(string)]) # 'thon'

""" 步长为负数, end没有指定, 默认为-len(string)-1 """
print(string[2::-1])                # 'leH'
print(string[2:-len(string)-1:-1])  # 'leH'

""" 把该序列复制一份 """
print(string[:])  # 'Hello 1牛马3 Python'

""" 把该序列倒过来 """
print(string[::-1]) # 'nohtyP 3马牛1 olleH'

""" start到end是从左往右，但step表示从右往左 """
print(string[1: 3: -1]) # ''

'''
特点：索引会降维，切片不会降维
'''
""" 类比0维数据 """
item1 = 1
item2 = 2
item3 = 3
item4 = 4
item5 = 5
item6 = 6
item7 = 7
item8 = 8
item9 = 9

""" 类比1维数据 """
lst1 = [item1, item2, item3]
lst2 = [item4, item5, item6]
lst3 = [item7, item8, item9]

# 对1维数据索引，结果为0维数据
print(lst1[0])  # 1
print(lst2[1])  # 5
print(lst3[2])  # 9

# 无论怎么切片，维度保持不变
print(lst1[::2])       # [1, 3]
print(lst2[1:2])       # [5]
print(lst3[::2][1:2])  # [9]
'''
原始列表: lst3 = [7, 8, 9]
索引:            0   1   2

第一步 lst3[::2]:
- 步长为2，取索引0和2的元素
- 结果: [7, 9]

第二步 [7, 9][1:2]:
- 从索引1到索引2（开区间）
- 结果: [9]
'''

""" 类比2维数据 """
lst4 = [lst1, lst2, lst3]
print(lst4) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 对2维数据索引，结果为1维数据
print(lst4[0]) # [1, 2, 3]
print(lst4[1]) # [4, 5, 6]
print(lst4[2]) # [7, 8, 9]

# 并且每索引一次，降低一次维度
print(lst4[0][1]) # 2

# 无论怎么切片，维度保持不变
print(lst4[::2])       # [[1, 2, 3], [7, 8, 9]]
print(lst4[1:2])       # [[4, 5, 6]]
print(lst4[::2][1:2])  # [[7, 8, 9]]

print(lst4[::2][1:2][0]) # [7, 8, 9]
print(lst4[::2][1:2][1]) # IndexError: list index out of range
print(len(lst4[::2][1:2])) # 1

'''
len(s)
s 可以是序列（如 string、tuple、list ...）/ 字典 / 集合等
返回对象的长度（即元素个数）
'''
print(len('abcd'))   # 4 
print(len([1, 2, 3, 4])) # 4 
print(len((1, 2, 3, 4))) # 4 

print(len([[7, 8, 9]]))  # 1

"""
del 语句不是直接删除数据，而是解除对应的引用，当该数据的引用计数为0时，
该数据就变为了一个可回收的对象，然后会被Python自动回收。
"""
lst1 = [567, 'hello', 456, [912, 923], 'world']
lst2 = lst1

print(lst2)     # [567, 'hello', 456, [912, 923], 'world']
print(id(lst1)) # 2387669075008
print(id(lst2)) # 2387669075008

del lst1
print(lst2)   # [567, 'hello', 456, [912, 923], 'world']
print(lst1)   # NameError: name 'lst1' is not defined. Did you mean: 'lst'?

del lst2[1]
print(lst2)   # [567, 456, [912, 923], 'world']

del lst2[0], lst2[2]
print(lst2)   # [456, [912, 923]]

del lst2[:3:2]
print(lst2)   # [[912, 923]]

lst1 = [567, 'hello', 456, [912, 923], 'world']
lst2 = lst1
del lst2[3][0]
print(lst2) #  [567, 'hello', 456, [923], 'world']

del lst2[:]
print(lst2) # []