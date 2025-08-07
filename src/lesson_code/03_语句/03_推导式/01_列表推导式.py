"""
列表推导式 
格式：[exp for子句]
格式：[exp for子句 更多的for子句或者if子句]
"""
lst = [x ** 2 for x in range(4)]
print(lst) # [0, 1, 4, 9]

# 类比
lst = []
for x in range(4):
    lst.append(x ** 2)
print(lst) # [0, 1, 4, 9]



lst = [x + y for x in range(5) if x % 2 for y in (1, 2, 3)]
print(lst) # [2, 3, 4, 4, 5, 6]

# 类比
lst = []
for x in range(5): # [0,1,2,3,4]
    if x % 2:      # 只处理奇数
        for y in (1, 2, 3):
            lst.append(x + y)
print(lst)
