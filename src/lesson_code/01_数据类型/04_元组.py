"""
# 元组（Tuple） 
特性：不可变，是序列
元组用圆括号定义（圆括号可省略），元素没有类型限制
"""
# 空元组
tup = ()
# 元组中只有一个元素时, 逗号不能省略
tup = (789,)
# 这不是元组，仍为数字789
tup = (789)

# 封包
tup = 'China', 1997, 2000
print(type(tup))
print(tup)

tup = ('China', 1997, 2000)
print(tup)

# 元组是不可变的, 但其中的可变成员仍然可以被改变
tup = (456, 'hello', ([789, 'world'],))
tup[-1][0][0] = 987
print(tup)

'''
## tuple([iterable])
将一个iterable对象转化为元组并返回，如果没有实参，则返回空元组
'''
print(tuple())                # ()
print(tuple("hello"))         # ('h', 'e', 'l', 'l', 'o')
print(tuple([1, 2, 3]))       # (1, 2, 3)
print(tuple([1, 2, 3,[4,5]])) # (1, 2, 3, [4, 5])   
# 字典作为一个iterable, 只有键参与迭代
print(tuple({1: 2, 3: 4}))    # (1, 3)
print(tuple({'a', 'b', 'c', 789, 456})) # ('c', 'a', 789, 456, 'b')

"""
## 元组方法
"""

'''
① tuple.count(x)
返回元素 x 在元组中出现的次数
'''
tup = (1, 2, 3, 2, '23', [2, 4])
print(tup.count(2))  # 2

'''
② tuple.index(x[, start[, end]])
x：要找的值
start：起始索引，默认为 0
end：结束索引（开区间），默认为 len(tup)
返回从左边开始第一次找到指定值时的正向索引，找不到报错
'''
tup = (1, 2, 3, 2, '23', [2, 4])
print(tup.index(2)) # 1 

print(tup.index(2, 4))  # ValueError: tuple.index(x): x not in tuple


