"""
格式一 
if 判断条件:
    执行代码块
"""
age = float(input('请问你今年多少岁? '))
if age >= 18:
    print('你已经成年了!')


"""
格式二 
if 判断条件:
    执行代码块1
else:
    执行代码块2
"""
age = float(input('请问你今年多少岁? '))
if age >= 18:
    print('你已经成年了!')
else:
    print('你还未成年!')

"""
格式三 
if 判断条件1:
    执行代码块1
elif 判断条件2:
    执行代码块2
elif 判断条件3:
    执行代码块3
...
else:
    执行代码块n
"""
score = float(input('你这次考试考了多少分? '))
if score >= 90:
    print('厉害!')
elif score >= 80:
    print('优秀!')
elif score >= 70:
    print('良好!')
elif score >= 60:
    print('及格!')
else:
    print('不及格!')

"""
三元表达式 
三元表达式用来实现一些简单的条件语句，会比结构化的代码块更灵活
"""
age = float(input('请问你今年多少岁? '))
print('你已经成年了!') if age >= 18 else print('你还未成年!')

score = float(input('你这次考试考了多少分? '))
print('厉害!') if score >= 90 else \
print('优秀!') if score >= 80 else \
print('良好!') if score >= 70 else \
print('及格!') if score >= 60 else \
print('不及格!')

