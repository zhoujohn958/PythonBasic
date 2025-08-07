"""
# 赋值运算符 
= 简单的赋值运算符
+= 加法赋值运算符
-= 减法赋值运算符
*= 乘法赋值运算符
/= 除法赋值运算符，返回完整的商（可能包含小数）
%= 取模赋值运算符，返回余数
**= 幂赋值运算符
//= 取整赋值运算符，返回整数商（向下取整）
"""
a = 3
c = a + 2

print(c)  # 5
c += a
print(c)  # 8   结果等于 c = c + a
c -= a
print(c)  # 5   结果等于 c = c - a
c *= a
print(c)  # 15   结果等于 c = c * a
c /= a
print(c)  # 5.0   结果等于 c = c / a
c %= a
print(c)  # 2.0   结果等于 c = c % a
c **= a
print(c)  # 8.0   结果等于 c = c ** a
c //= a
print(c)  # 2.0   结果等于 c = c // a


'''
## 增强赋值
增强赋值在条件符合的情况下（如：操作数是一个可变数据）
会以inplace的方式来进行处理，而普通赋值则会以新建的方式进行处理。
'''
lst1 = [1, 2]
lst2 = [3, 4, 5]
print(id(lst1))  # 1467247038976
lst1 += lst2
print(id(lst1))  # 1467247038976
print(lst1)      # [1, 2, 3, 4, 5]

lst1 = [1, 2]
lst2 = [3, 4, 5]
print(id(lst1))    # 1467250177280
lst1 = lst1 + lst2
print(id(lst1))    # 1467247038784
print(lst1)        # [1, 2, 3, 4, 5]

'''
id(object)
返回 object 的唯一标识符（内存地址）
两个对象具有相同的id值，说明它们为同一对象
'''
a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
c = a
print(id(a))       # 1467250177280
print(id(b))       # 1467248848448
print(id(c))       # 1467250177280

'''
+、* 的拼接操作
+、+=、*、*= 还支持字符串、列表、元组的拼接操作
'''
# 字符串拼接
str1 = 'hello '
str2 = 'world'
print(str1 + str2) # 'hello world'
str1 += str2
print(str1)        # 'hello world'

str1 = 'hello '
print(id(str1))    # 1467250256912
print(str1 * 3)    # 'hello hello hello '

str1 *= 3
print(id(str1))    # 1467248427248
print(str1)        # hello hello hello 

# 列表拼接
lst1 = [1, 2]
lst2 = [3, 4, 5]
print(lst1 + lst2) # [1, 2, 3, 4, 5] 
print(id(lst1))    # 2860158554624

lst1 += lst2       # [1, 2, 3, 4, 5] 
print(lst1)        # [1, 2, 3, 4, 5] 
print(id(lst1))    # 2860158554624

lst1 = [1, 2]
print(lst1)        # [1, 2]
print(id(lst1))    # 2860160364096

print(lst1 * 3)    # [1, 2, 1, 2, 1, 2]
lst1 *= 3
print(id(lst1))    # 2860160364096
print(lst1)        # [1, 2, 1, 2, 1, 2]

# 元组拼接
tup1 = (1, 2)
tup2 = (3, 4, 5)
print(tup1 + tup2) # (1, 2, 3, 4, 5)
tup1 += tup2
print(tup1)        # (1, 2, 3, 4, 5)

tup1 = (1, 2)
print(tup1 * 3)    # (1, 2, 1, 2, 1, 2)
tup1 *= 3
print(tup1)        # (1, 2, 1, 2, 1, 2)

'''
基本序列赋值: 
格式： a, b, c, ... = iterable
将iterable的元素分别赋值给对应变量，元素和变量个数需要一致
'''
a, b = 3, 4
print(a, b)        # 3 4
a, b, c = [3, 4, 5]
print(a, b, c)     # 3 4 5
a, b, c, d = '你好吗?'
print(a, b, c, d)  # 你 好 吗 ?

'''
多目标赋值
将一个对象同时赋值给多个变量。
'''
a = b = c = 999
print(id(a))   # 2860157940272
print(id(b))   # 2860157940272
print(id(c))   # 2860157940272

a = b = c = [1, 2, 3]
print(id(a))  # 2860158554624
print(id(b))  # 2860158554624
print(id(c))  # 2860158554624

b.append(4)
print(a)   # [1, 2, 3, 4]
print(b)   # [1, 2, 3, 4]
print(c)   # [1, 2, 3, 4]


