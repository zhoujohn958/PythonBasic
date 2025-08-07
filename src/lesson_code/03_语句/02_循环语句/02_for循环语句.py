"""
for 循环 
for 变量 in 可迭代对象:
    循环体
"""
"""
第1次循环: i = lst[0], 执行循环体 print(i)
第2次循环: i = lst[1], 执行循环体 print(i)
第3次循环: i = lst[2], 执行循环体 print(i)
第4次循环: i = lst[3], 执行循环体 print(i)
当取不到lst中元素时，for循环自动停止。
"""
lst = ['d', 'c', 'k', 'a']
# 获取元素
for i in lst:
    print(i)

# 获取索引
for i in range(len(lst)):
    print(i)

# 获取索引和元素
for index, item in enumerate(lst):
    print(index, item)

""" for 循环嵌套 """ 
# 实现九九乘法表
for right in range(1, 10):
    for left in range(1, right+1):
        print(f'{left}x{right}={left*right}', end='\t')
    print()

''' 
range([start], stop[, step])
按照 step 生成从 start 到 stop 的整数序列（不可变）
start：起始值，闭区间，默认为 0
stop：结束值，开区间
step：步长，默认为 1
'''
print(list(range(4)))         # [0, 1, 2, 3]
print(list(range(1, 5)))      # [1, 2, 3, 4]
print(list(range(1, 8, 2)))   # [1, 3, 5, 7]
print(list(range(8, 1, -2)))  # [8, 6, 4, 2]
rg = range(1, 8, 2)
print(len(rg))  # 4
print(rg[2])  # 5
print(rg[::2])  # range(1, 9, 4)

'''
enumerate(iterable, start=0)
返回一个迭代器对象。迭代它会得到一个个的元组，每个元组是由索引和对应元素构成的。
start决定索引的起始值。
'''
lst = ['d', 'c', 'k', 'a']
print(list(enumerate(lst)))
print(tuple(enumerate(lst)))
for i in enumerate(lst):
    print(i)

""" 循环控制语句 """
''' break 终止所在的循环 '''
for _ in range(3):
    for _ in range(4):
        print('hello')
        break

for _ in range(3):
    for _ in range(4):
        print('hello')
    break

for _ in range(3):
    for _ in range(4):
        print('hello')
        break
    break

'''
continue 跳过当前这次循环，继续到下一次循环
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 == 0:
        continue  # 如果数字是偶数，跳过当前循环
    print(number)