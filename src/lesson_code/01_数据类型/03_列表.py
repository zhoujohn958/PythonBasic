"""
# 列表（List） 
特性：可变，是序列
列表用方括号定义，元素没有类型限制
"""
list0 = []
list1 = ['China', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow','white', 'black']

"""
## 修改列表
列表是可变的，可以通过索引和切片的方式来对列表的元素重新赋值
"""

lst = [567, 'hello', 78.9, 'world', False]
"""
### 针对一个元素:
格式: lst[index] = object
"""
lst[2] = 9.87
lst[3] = 'dlrow'
print(lst)

"""
### 针对多个元素:
格式: lst[start: end: step] = iterable
"""
# 1 vs 1
lst[2:3] = [9.87]
# n vs n
lst[2:4] = [9.87, 'dlrow']
# step为1, 可以 1 vs n
lst[2:3] = [7, 8, 9]
# step为1, 可以 n vs m
lst[2:4] = [1, 2, 3]
lst[1:4] = [1, 2]
# step为1, 可以 1 vs 0
lst[2:3] = []
# step为1, 可以 n vs 0
lst[1:4] = []
# step不为1, 只能 n vs n
lst[1::2] = ['a', 'b']
# 插入一个元素
lst[0:0] = ['a']
lst[1:1] = ['b']
lst[len(lst):] = ['c']

# 插入多个元素
lst[0:0] = ['a', 'b', 'c']
lst[1:1] = ['d', 'f']
lst[len(lst):] = ['x', 'y', 'z']
print(lst)

"""
list([iterable])
将一个iterable对象转化为列表并返回，如果没有实参，则返回空列表
"""
print(list())
print(list("hello"))
print(list((1, 2, 3)))

# 字典作为一个iterable, 只有键参与迭代
print(list({1: 2, 3: 4}))
print(list({'a', 'b', 'c', 789, 456}))

"""
## 列表方法
"""

'''
① list.append(object)
往列表中追加一个元素，无返回值，相当于 lst[len(lst):] = [object] 
'''
lst = [1, 2, 3]
lst.append(4)      # [1, 2, 3, 4]
print(lst)
lst.append([5, 6]) # [1, 2, 3, 4, [5, 6]]
print(lst)

'''
② list.extend(iterable)
使用 iterable 中的所有元素来扩展列表，无返回值，相当于 
lst[len(lst):] = iterable
'''
lst = [1, 2, 3]
lst.extend([5, 6])
print(lst) # [1, 2, 3, 5, 6]

'''
③ list.insert(index, object)
index：要插入元素的位置
object：要插入的元素
在指定位置插入一个元素，无返回值
'''
lst = [1, 2, 3, 4]
lst.insert(1, ['a', 'b'])
print(lst)

'''
④ list.sort( [key], reverse=False)
key：指定一个函数，在排序之前，列表每个元素先应用这个函数，再根据函数的返回值对原数据进行排序
reverse：默认为 False，代表升序，指定为 True 则为降序，对原列表进行排序，无返回值
'''
lst = [1, 2, -5, -3]
# 升序排序
lst.sort()
print(lst)  # [-5, -3, 1, 2]


lst = [1, 2, -5, -3]
# 降序排序
lst.sort(reverse=True)
print(lst)  # [2, 1, -3, -5]

'''
⑤ Unicode码位和字符的转换 
# chr(i) 返回Unicode码位为指定整数的字符
# ord(c) 返回指定字符对应的Unicode码位
''' 
print(chr(97))   # 'a'
print(ord('a'))  # 97

# 字符串在大小比较时是逐个字符进行比较的
# 根据字符在编码表里的位置
lst = ['10', '2', '1', '-3', '101']
lst.sort()
print(lst.sort()) # None
print(lst)        # ['-3', '1', '10', '101', '2']

lst.sort(key=int)
print(lst)        # ['-3', '1', '2', '10', '101']

'''
# abs(number) 内置函数，返回number的绝对值

'''
print(abs(9))      # 9
print(abs(9.87))   # 9.87
print(abs(0))      # 0
print(abs(-9))     # 9
print(abs(-9.87))  # 9.87
print(abs(True))   # 1
print(abs(False))  # 0
print(abs(3+4j))   # 求模, 5.0   勾三股四弦五

'''
对lst中的元素按照绝对值的大小降序排序
把lst中的每个元素依次作为实参传递给key所指定的函数去调用, 
即:
abs(1), abs(2), abs(-5), abs(-3)
返回值分别为: 1, 2, 5, 3
根据返回值的大小对原数据进行排序
'''
lst = [1, 2, -5, -3]
lst.sort(key=abs, reverse=True)
print(lst)

'''
⑥ sorted(iterable, [key], reverse=False)
iterable：要排序的可迭代对象
key：指定一个函数，在排序之前，每个元素都先应用这个函数之后再排序
reverse：默认为 False，代表升序，指定为 True 则为降序
对可迭代对象进行排序，以列表形式返回排序之后的结果
'''
lst = [1, 2, -5, -3]
# 升序排序
print(sorted(lst))                          # 升序 [-5, -3, 1, 2]
# 降序排序
print(sorted(lst, reverse=True))            # 降序 [2, 1, -3, -5]
# 对lst中的元素按照绝对值的大小降序排序
print(sorted(lst, key=abs, reverse=True))   # 处理为绝对值降序 [-5, -3, 2, 1]
# 对字符串排序
print(sorted('hello world'))                # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

'''
⑦ list.reverse()
把列表中的元素倒过来，无返回值
'''
lst = [1, 3, 5, 2]
lst.reverse()  
print(lst)    # [2, 5, 3, 1]

'''
⑧ list.count(x)
返回元素 x 在列表中出现的次数
'''
lst = [1, 2, 3, '23', [2, 4]]
print(lst.count(3)) # 1

'''
⑨ list.index(x[, start[, end]])
x：要找的值
start：起始索引，默认为 0
end：结束索引（开区间），默认为 len(lst)
返回从左边开始第一次找到指定值时的正向索引，找不到报错
'''
lst = [1, 2, 3, 2, '23', [2, 4]]
print(lst.index(2)) # 1
lst.index(2, 4)     # ValueError: 2 is not in list

'''
⑩ list.pop(i=-1)
i：要删除并返回的元素的索引
删除列表中指定索引的元素并返回该元素，默认最后一个
索引超出范围，则报错
'''
lst = [567, 'hello', True, False, 456]
print(lst.pop())   # 456
print(lst.pop(1))  # 'hello'
print(lst)         # [567, True, False]

'''
⑩① list.remove(x)
删除列表中从左往右遇到的第一个x元素，无返回值
如果没有这样的元素，则报错
'''
lst = [1, 2, 4, 2, 3, 3]
# lst.remove()   # TypeError: list.remove() takes exactly one argument (0 given)
lst.remove(3)    
print(lst)       # [1, 2, 4, 2, 3]
lst.remove(3)
print(lst)       # [1, 2, 4, 2]
lst.remove(3)    # ValueError: list.remove(x): x not in list

'''
⑩② list.copy()
返回该列表的一个副本，等价于 lst[:]
'''
lst = [567, 'hello', True, False, 456]
new_lst = lst.copy()
print(id(lst))
print(id(new_lst))
print(lst)
print(new_lst)

'''
⑩③ list.clear()
移除列表中的所有元素，无返回值，等价于 del lst[:]
'''
lst = [567, 'hello', True, False, 456]
lst.clear()
print(lst)  # []
