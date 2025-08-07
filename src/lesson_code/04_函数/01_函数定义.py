"""
# 定义函数 
def func_name([arg1 [, arg2, ... argN]]):
func_body
形参： 函数定义时声明的参数。
实参： 函数调用时传入的参数。
函数只需要定义一次，就可以被多次使用。
当函数被调用时，才执行函数体，定义时不执行。
"""
def plus(num):
    print(num + 1)

""" 调用函数 """
plus(2)  # 3
plus(5)  # 6

f = plus
print(plus) # <function plus at 0x000001454A9C9760>
print(f)    # <function plus at 0x000001454A9C9760>
f(2)  # 3
f(5)  # 6

'''
## return 用法
把后面跟着的对象返回给函数调用方，并结束所在的函数
return 后面可以跟一个对象，多个对象，甚至不跟任何对象
return 后面什么都不跟，等价于 return None
函数执行时，没有遇到 return，也等价于 return None
'''
# 返回一个对象
def add1(left, right):
    res = left + right
    return res

print(add1(2, 3))

def add2(left, right):
    return left + right

print(add2(2, 3))

# 返回多个对象, 自动打包成一个元组
def add3(left, right):
    res1 = left + right
    res2 = left * right
    return res1, res2

print(add2(2, 3))

def add4(left, right):
    return left + right, left * right

print(add4(2,3))  # (5, 6)

# return None
def add5(left, right):
    print(left + right)  # 5
    return

print(add5(2,3))  # None

# return None
def add6(left, right):
    pass

print(add6(2, 3)) # None
