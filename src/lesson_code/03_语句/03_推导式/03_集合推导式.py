"""
集合推导式 
格式：{exp for子句}
格式：{exp for子句 更多的for子句或者if子句}
"""
s = {x ** 2 for x in range(4)}
print(s) # {0, 1, 4, 9}

# 类比
s = set()
for x in range(4):
    s.add(x ** 2)
print(s) # {0, 1, 4, 9}


s = {x + y for x in range(5) if x % 2 for y in (1, 2, 3)}
print(s)

# 类比
s = set()
for x in range(5):   # [0,1,2,3,4]
    if x % 2:        # 只处理奇数
        for y in (1, 2, 3):
            s.add(x + y)
print(s) # {2,3,4,5,6} 自动去重，相同值只保留一个


"""
pass 是一个关键字，表示一个空语句，当它被执行时，不做任何操作，
通常用作占位语句，在语法上需要语句但实际上不需要执行任何操作的情况下使用。
"""
score = float(input('你这次考试考了多少分? '))
if score >= 90:
    print('厉害!')
elif score >= 80:
    pass
elif score >= 70:
    print('良好!')
elif score >= 60:
    print('及格!')
else:
    print('不及格!')