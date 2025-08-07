"""
while 判断条件:
    循环体
"""
# 输出1-100之间的整数
from turtle import left, right


num = 1
while num <= 100:
    print(num)
    num += 1

"""
while True
无限循环（俗称：死循环），通常配合 break 使用
"""
# 输出1-100之间的整数
num = 1
while True:
    print(num)
    num += 1
    if num > 100:
        break

""" while 循环嵌套 """
right = 1 
while right <=9 :
    left = 1
    while left <= right :
        total = left * right
        print(f"{left} X {right} = {total}",end='\t')
        left +=1
    print()
    right += 1