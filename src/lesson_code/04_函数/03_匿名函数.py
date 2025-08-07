"""
匿名函数 
格式： lambda [arg1 [, arg2, ... argN]] : expression
匿名函数的参数可以有多个，但是后面的 expression 只能有一个
匿名函数返回值就是 expression 的结果，而不需要使用 return
匿名函数可以在需要函数对象的地方使用（如：赋值给变量、作为参数传入其他函数等），
因为匿名函数可以作为一个表达式，而不是一个结构化的代码块
"""
''' 
lambda 参数1, 参数2, ... : 表达式
lambda：声明匿名函数的关键字。
参数1, 参数2, ...：可以有多个参数，参数之间用逗号分隔。
:：冒号分隔参数和表达式。
表达式：只能是一个表达式，不能是复杂的语句。表达式的结果就是函数的返回值。
''' 
add = lambda x, y: x + y
print(add(3, 5))  # 输出 8

''' 
 匿名函数的特点
没有函数名，通常赋值给一个变量或直接作为参数传递。
只能写单个表达式，不能包含多条语句。
返回值就是表达式的结果，不需要写return。
适合用于函数式编程场景，如map、filter、sorted等。
'''
''' 作为参数传递 '''
nums = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, nums)
print(list(squared))  # 输出 [1, 4, 9, 16]

''' 排序时自定义key ''' 
students = [("小明", 18), ("小红", 17), ("小刚", 19)]
students_sorted = sorted(students, key=lambda s: s[1])
print(students_sorted)  # 输出 [('小红', 17), ('小明', 18), ('小刚', 19)]

''' 结合filter筛选 '''
nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # 输出 [2, 4, 6]
