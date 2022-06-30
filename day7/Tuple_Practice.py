# 小彭的乱码
info_tuple1 = tuple(i for i in range(10))
info_tuple2 = ('pengjiare', 1, 18)
print(info_tuple1)
print(info_tuple2)

tuple_str = "%s是%d年龄%d" % info_tuple2
print(tuple_str)
list1 = list(info_tuple1)
print(type(list1[1]))
print(list1)
