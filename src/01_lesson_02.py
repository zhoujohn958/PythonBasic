# 基本整数
# age = 25
# year = 2024
# negative = -10

# 不同进制的整数
# binary = 0b1010      # 二进制: 10
# print(binary.bit_length())      # 获取二进制位数
# print(binary.to_bytes(4, 'big'))  # 转换为字节
# print(int.from_bytes(b'\x00\x00\x00\n', 'big'))  # 从字节转换

# octal = 0o12         # 八进制: 10
# hexadecimal = 0xA    # 十六进制: 10

# # 大整数 (Python自动处理)
# big_number = 123456789012345678901234567890
# print(big_number)

# 常用方法
# print(age.bit_length())      # 获取二进制位数
# print(age.to_bytes(4, 'big'))  # 转换为字节
# print(int.from_bytes(b'\x00\x00\x00\x19', 'big'))  # 从字节转换



# 基本浮点数
# pi = 3.14159
# e = 2.71828
# scientific = 1.23e-4  # 科学计数法

# # 特殊值
# infinity = float('inf')
# negative_infinity = float('-inf')
# not_a_number = float('nan')

# # 常用方法
# print(pi.is_integer())       # 检查是否为整数
# print(pi.hex())             # 转换为十六进制字符串
# print(float.fromhex('0x1.921fb54442d18p+1'))  # 从十六进制转换


# 基本复数
# z1 = 3 + 4j
# z2 = complex(5, 6)

# # 复数运算
# print(z1.real)      # 实部: 3.0
# print(z1.imag)      # 虚部: 4.0
# print(abs(z2))      # 模: 5.0
# print(z1.conjugate())  # 共轭复数: 3-4j

# bool
'''
根据指定的 x，返回布尔值
如果没有指定 x，则返回 False
'''
# print(bool())
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(False))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(set()))
# print(bool(None))
# print(bool(' '))    # True
# print(bool('None'))  # True
# print(bool('False'))  # True


# str1 = "hello world"
# print(str1.startswith("h"))
# print(str1.startswith("he"))
# print(str1.startswith("wo"))
# print(str1.startswith("wo", 6))
# print(str1.startswith(("wo", "h")))


# string = '1234'
# print(string.isdigit()) # True
# string = '-123'
# print(string.isdigit()) # False
# string = '1.23'
# print(string.isdigit()) # False

# s = '-.'
# s1 = 'hello world'
# print(s.join(s1))
# s2 = ['1', '2', '3', '4']
# print(s.join(s2))
# s3 = ('1', '2', '3', '4')
# print(s.join(s3))
# # 字典作为iterable, 只有键参与迭代
# s4 = {'height': 175, 'weight': 65}
# print(s.join(s4))
# s5 = {'5', 'hello', '789', 'world'}
# print(s.join(s5))

# lst = [567, 'hello', 78.9, 'world', False]
# """
# 针对一个元素:
# 格式: lst[index] = object
# """
# lst[2] = 9.87
# lst[3] = 'dlrow'
# print(lst)

"""
针对多个元素:
格式: lst[start: end: step] = iterable
"""
lst = [567, 'hello', 78.9, 'world', False]
# 1 vs 1
# lst[2:3] = [9.87]
# n vs n
# lst[2:4] = [9.87, 'dlrow']
# # step为1, 可以 1 vs n
# lst[2:3] = [7, 8, 9]
# # step为1, 可以 n vs m
# lst[2:4] = [1, 2, 3]
# lst[1:4] = [1, 2]
# # step为1, 可以 1 vs 0
# lst[2:3] = []
print(lst)
# # step为1, 可以 n vs 0
# lst[1:4] = []
# # step不为1, 只能 n vs n
# lst[1::2] = ['a', 'b']
# # 插入一个元素
# lst[0:0] = ['a']
# lst[1:1] = ['b']
# lst[len(lst):] = ['c']list([iterable])
# 将一个iterable对象转化为列表并返回，如果没有实参，则
# 返回空列表
#  
# 列表方法
# list.append(object)
# 往列表中追加一个元素，无返回值，相当于 lst[len(lst):] = 
# [object] 
# # 插入多个元素
# lst[0:0] = ['a', 'b', 'c']
# lst[1:1] = ['d', 'f']
# lst[len(lst):] = ['x', 'y', 'z']
# print(lst)

# 列表方法
# fruits = ['apple', 'banana', 'orange']

# 添加元素
# fruits.append('grape')           # 在末尾添加
# print(fruits)
# fruits.insert(1, 'pear')        # 在指定位置插入
# fruits.extend(['kiwi', 'mango']) # 扩展列表

# 删除元素
# fruits.remove('banana')          # 删除指定元素
# popped = fruits.pop()            # 删除并返回最后一个元素
# popped = fruits.pop(2)           # 删除并返回指定位置的元素
# del fruits[0]                    # 删除指定位置的元素
