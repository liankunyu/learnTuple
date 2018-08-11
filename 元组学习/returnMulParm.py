def F1(x, y):
    a = x % y
    b = (x - a) / y
    return (a, b)  # 也可以写作 return a, b

def F2(x,y):
    x=False
    y=100
    return x,y
(c, d) = F1(9, 4)  # 也可以写作 c , d = F1 ( 9, 4 )
e,f=F2(True,10)
print(c,d)
print(e,f)