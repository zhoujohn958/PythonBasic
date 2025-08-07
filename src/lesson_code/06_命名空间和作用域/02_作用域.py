"""
作用域（Scope）指的是变量可以被访问的范围
"""
'''
1. 作用域的分类
Python 中的作用域主要分为四种，通常用“LEGB”规则来记忆：
L（Local）本地作用域：函数内部定义的变量，只能在该函数内部访问。
E（Enclosing）嵌套作用域：嵌套函数（函数内部再定义函数）中，内层函数可以访问外层（非全局）函数的变量。
G（Global）全局作用域：模块级别定义的变量，可以在整个模块中访问。
B（Built-in）内置作用域：Python 解释器内置的名字，比如 len、range 等。
'''
'''
2. 作用域查找顺序（LEGB规则）
当你在代码中引用一个变量名时，Python 会按照以下顺序查找：
Local：当前函数内部
Enclosing：所有外层函数的作用域（如果有嵌套函数）
Global：当前模块的全局作用域
Built-in：Python 内置作用域
一旦在某一层找到了变量名，就不会再往外层查找。
'''
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # 输出 local
    inner()
    print(x)      # 输出 enclosing

outer()
print(x)          # 输出 global

'''
4. global 和 nonlocal 关键字
global：在函数内部声明变量为全局变量，可以修改全局变量的值。
nonlocal：在嵌套函数中声明变量为外层（非全局）变量，可以修改外层函数的变量。
'''
x = 10

def func():
    global x
    x = 20  # 修改全局变量

def outer():
    y = 5
    def inner():
        nonlocal y
        y = 15  # 修改外层函数的变量
    inner()
    print(y)  # 输出 15



def outer():
    global a, b
    a, b, c, d = 3, 4, 5, 6
    print(a, b)      # 3 4
    def inner():
        global a, b
        nonlocal c, d
        a, b, c, d = 7, 8, 9, 0
    inner()
    print(c, d)     # 9 0
a, b = 1, 2
outer()
print(a, b)  # 7 8