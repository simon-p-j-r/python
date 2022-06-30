# 小彭的乱码
info_tuple = (1, 2, 3)
info_set = {4, 5, 6}
list1 = list(info_tuple)
list2 = list(info_set)
list1.extend(list2)
print(list1)
