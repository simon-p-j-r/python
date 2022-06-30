# 小彭的乱码
from collections.abc import Iterable, Iterator

list1 = []
turple1 = (1,)
dic = {1: 2}
print(isinstance(list1, Iterator))
print(isinstance(turple1, Iterator))
print(isinstance(dic, Iterator))
print(isinstance(list1, Iterable))
print(isinstance(turple1, Iterable))
print(isinstance(dic, Iterable))
