#x=tuple(1,2,3,4) 错误tuple() takes at most 1 argument(4 given)
#print(x)
y=tuple([1,2,3,4,5])
print(y)
z=tuple((1,2,3,4)) #元组会返回元组自身
print(z)
k=tuple({1:2,3:4}) #针对字典 会返回字典的key组成的tuple
print(k)

aList = [123, 'xyz', 'zara', 'abc'];
aTuple = tuple(aList)
print("Tuple elements : ", aTuple)

tup1 = (12, 34.56,11)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
#元组可以使用下标索引来访问元组中的值
print ("tup1[0]: ", tup3[0])
print ("tup2[1:5]: ", tup3[1:5])

#python中元组和小括号的关系，即元组是由逗号决定的，不是小括号。可以看到，即便没有了小括号，还是元组
a=1,2,3,4
print(a)
b=2, #元组必须跟逗号，就算是一个也要跟逗号
print(b)