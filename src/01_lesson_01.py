# 正确的缩进示例
# if True:
#     print("这是正确的缩进")
#     print("这行代码属于同一个代码块")
# else:
#     print("这是else代码块")
#     print("缩进必须一致")

# 错误的缩进示例
# if True:
# print("这会导致语法错误")  # 错误：缺少缩进
#     print("这行缩进不一致")  # 错误：缩进不一致


# 这是单行注释
# print("Hello World")  # 这也是单行注释

# 多行注释示例

'''
这是多行注释
可以写很多行
用于解释复杂的代码逻辑
'''

"""
这也是多行注释
通常用于函数或类的文档字符串
"""
# def calculate_area(radius):
#     """
#     计算圆的面积
#     参数：radius - 圆的半径
#     返回：圆的面积
#     """
#     return 3.14159 * radius ** 2

# print(calculate_area(3))

# 方法1：使用 + 运算符
# first_name = "张三"
# last_name = "李"
# full_name = first_name + " " + last_name
# print(full_name)  # 输出：张三 李

# 方法2：使用 join() 方法
# words = ["Hello", "World", "Python"]
# sentence = " ".join(words)
# print(sentence)  # 输出：Hello World Python

# 方法3：使用格式化字符串（推荐）
# name = "小明"
# age = 18
# message = f"我叫{name}，今年{age}岁"
# print(message)  # 输出：我叫小明，今年18岁

# # 方法4：使用 format() 方法
# message2 = "我叫{}，今年{}岁".format(name, age)
# print(message2)  # 输出：我叫小明，今年18岁

# # 方法5：使用 % 运算符（旧式格式化）
# message3 = "我叫%s，今年%d岁" % (name, age)
# print(message3)  # 输出：我叫小明，今年18岁