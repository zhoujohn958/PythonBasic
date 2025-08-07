"""
# 参数传递 :对象引用的传递
传不可变对象 & 传可变对象
不可变对象（如int、float、str、tuple）：在函数内部修改参数，不会影响外部变量。
可变对象（如list、dict、set）：在函数内部修改对象内容，会影响外部变量。
""" 
# 不可变对象： int 
def change_num(a):
    a = 10  # 重新赋值，不影响外部变量

x = 5
change_num(x)
print(x)  # 输出5

# 可变对象，列表list 
def change_list(lst):
    print(lst)
    lst.append(100)  # 修改内容，会影响外部变量

y = [1, 2, 3]
change_list(y)
print(y)  # 输出[1, 2, 3, 100]

"""
# 参数类型
Python函数支持多种参数类型：
位置参数：按顺序传递
关键字参数：通过参数名传递
默认参数：有默认值的参数
可变参数：*args（接收任意数量的位置参数，类型为元组）
关键字可变参数：**kwargs（接收任意数量的关键字参数，类型为字典）
"""
def func(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

func(1, 3, 4, 5, x=6, y=7)  # 输出: 1 3 (4, 5) {'x': 6, 'y': 7}

'''
参数传递的注意事项
默认参数：默认参数最好使用不可变对象（如None、数字、字符串），避免可变对象带来的副作用。
可变对象作为参数：如果不想影响外部变量，可以在函数内部使用对象的副本（如lst[:]或copy.copy()）
'''
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  # 不是[2]，因为lst默认值只初始化一次

# 正确写法
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

'''
关键字参数
按照指定的名称将实参传递给对应的形参，与位置顺序无关
关键字参数必须放在位置参数的后面
'''
def func(a, b):
    print(a - b)
# 按照指定的名称将实参传递给对应的形参，与位置顺序无关
func(a=3, b=4)  # -1
func(b=4, a=3)  # -1
# 关键字参数必须放在位置参数的后面
func(3, b=4)    # -1

'''
默认参数
有接收到实参，使用实参，没有接收到实参时，才会使用默认值 
'''
def func(a, b=4):
    print(a - b)
func(3)     # -1
func(3, 5)  # -2

'''
不定长参数
*args：接收[0, +∞)个位置参数，贪婪的，将它们打包成一个元组，如果没有接收到实参，则为空元组。
**kwargs：接收[0, +∞)个关键字参数，贪婪的，将它们打包成一个字典，如果没有接收到实参，则为空字典。必须放在所有形参的最后。
'''
def func(*args):
    print(args)
func()            #  () 如果没有接收到实参，则为空元组
func(3, 1, 4, 6)  #  (3, 1, 4, 6) 接收[0, +∞)个位置参数，贪婪的，将它们打包成一个元组

def func(**kwargs):
    print(kwargs)
func()              # {}  如果没有接收到实参，则为空字典
func(a=3, b=2, c=4) # {'a': 3, 'b': 2, 'c': 4} 将它们打包成一个字典

def func(*args, **kwargs):
    print(args)
    print(kwargs)
func()
func(1, 2, a=3, b=4)

'''
特殊参数
默认情况下，实参的传递形式可以是位置参数或关键字参数
可以用 / 和 * 来限制参数的传递形式
'''
'''
 /：仅限位置参数（Positional-only Parameters）
作用：在 / 之前的参数，只能通过“位置”传递，不能用关键字传递。
用法：放在参数列表中，表示其左侧的参数必须用位置传递。
'''
# a 和 b 只能用位置传递，c 可以用位置或关键字。
def func(a, b, /, c):
    print(a, b, c)

func(1, 2, 3)        # 正确
func(1, 2, c=3)      # 正确
func(a=1, b=2, c=3)  # 错误，a 和 b 不能用关键字

'''
*：仅限关键字参数（Keyword-only Parameters）
作用：在 * 之后的参数，只能通过“关键字”传递，不能用位置传递。
用法：放在参数列表中，表示其右侧的参数必须用关键字传递。
'''
# c 和 d 只能用关键字传递
def func(a, b, *, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)    # 正确
func(1, 2, 3, 4)        # 错误，c 和 d 必须用关键字


def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

func(1, 2, 3, kwd1=4, kwd2=5)  # 正确
func(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5)
func(pos1=1, pos2=2, 3, kwd1=4, kwd2=5) # 错误，pos1 和 pos2 不能用关键字
# SyntaxError: positional argument follows keyword argument



