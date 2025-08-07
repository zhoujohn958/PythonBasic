"""
身份运算符 
判断两个标识符是不是引用自同一个对象
返回布尔值：True，False
is 类似于判断 id(a) == id(b)
is not 类似于判断 id(a) != id(b)
"""
'''
Python 对象缓存机制（整数缓存）
Python 对小整数（-5 到 256）进行了缓存优化
这些数字在内存中只存储一份，所有引用都指向同一个对象
所以 a 和 b 实际上是同一个对象，id(a) == id(b) 为 True
'''
a = 256
b = 256
print(a == b)          # True
print(a is b)          # True
print(id(a) == id(b))  # True

'''
257 超出了 Python 的整数缓存范围（-5 到 256）
每次创建 257 时，都会在内存中分配新的对象
所以 a 和 b 虽然值相同，但是不同的对象
id(a) != id(b)，因此 a is b 为 False
'''
a = 257
b = 257
print(a == b)          # True
print(a is b)          # False
print(id(a) == id(b))  # False

a = [257]
b = [257]
print(a == b)          # True
print(a is b)          # False
print(id(a) == id(b))  # False