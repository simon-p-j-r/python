# 小彭的乱码
import copy

a = [1, 2]
b = a
print(id(a))
print(id(b))
b[0] = 0
print(a,b)
b = a.copy()
print(id(b))
b[0] = 1
print(a, b)
b = [3, 4]
c = [a,b]
d = c.copy()
print(id(c), id(d))
print(c,d)
d[0][0] = 100
print(c, d, a)
d = copy.deepcopy(c)
print(id(c), id(d))
print(c,d)
d[0][0] = 1000
print(c, d, a)
