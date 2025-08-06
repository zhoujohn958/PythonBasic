"""
# 数字（Number） 
特性：不可变，不是序列
分类：整数、浮点数、布尔型、复数

## 整数（int）
包括正整数，负整数和零，如：789，-789，0

## 浮点数（float）
和数学中的小数类似，如：7.89，8.0
科学计数法认定为浮点数，如：3e4，3E4

## 布尔型（bool）
True 和 False 定义成了关键字，它们被当成数字时，大小分别为1和0

## 复数（complex）
实部+虚部，和数学中 a+bi 是类似的，只不过这里的虚部是以 j 或者 J 结尾，
如：a = 3 + 4j 、 b = 1J（注意：j 或 J 前面的系数不能省略）

## type(object)
返回 object 的类型

"""

"""
### int([x]) 
x：接收数字或特定字符串
将 x 转换为十进制整数并返回，如果没有指定 x，则返回 0
""" 
print(int())       # 0
print(int(3))      # 3
print(int(-3))     # -3
print(int(3.99))   # 3
print(int(-3.99))  # -3
print(int(True))   # 1
print(int(False))  # 0
print(int('12'))   # 12
print(int('-12'))  # -12


# 当传的是字符串时, 必须是整数形式的
# int('12.1')  # ValueError

"""
### float([x])
x：接收数字或特定字符串
将 x 转换为浮点数并返回，如果没有指定 x，则返回 0.0
"""
print(float())        # 0.0
print(float(3))       # 3.0
print(float(-3))      # -3.0
print(float(3.99))    # 3.99
print(float(-3.99))   # -3.99
print(float(True))    # 1.0
print(float(False))   # 0.0
print(float('12'))    # 12.0
print(float('-12'))   # -12.0
print(float('12.1'))  # 12.1

"""
### bool([x]) 
根据指定的 x，返回布尔值
如果没有指定 x，则返回 False
...
数字0, 0.0, 0j, False,
空字符串, 空列表, 空元组,
空字典, 空集合, 关键字None
...
以上这些数据bool判定为False,
其它通常判定为True
"""
print(bool())
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(False))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool(None))

print(bool(' '))      # True
print(bool('None'))   # True
print(bool('False'))  # True

"""
### complex([real[, imag]])
返回一个 real + imag * 1j 的复数
如果第一个参数是字符串，它将被解释为复数，此时不能传第二个参数
如果没有指定实参，则返回 0j
"""
print(complex())          # 0j
print(complex(3.2, 4))    # (3.2+4j)
print(complex(3.2))       # (3.2+0j)
print(complex('3.2'))     # (3.2+0j)
print(complex("3.2+4j"))  # (3.2+4j)