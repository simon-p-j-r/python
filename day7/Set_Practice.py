# 小彭的乱码
info_str = "pengjiaren"
info_set = set(info_str)
print(info_set)

info_set.add(12)
print(info_set)

info_set_2 = {"wangdao", '123'}
print(type(info_set_2))
info_set_2.add('p')

print(info_set.difference(info_set_2))
# info_set.difference_update(info_set_2)
# print(info_set)

print(info_set.isdisjoint(info_set_2))

info_set.symmetric_difference_update(info_set_2)
print(info_set)

print(info_set - info_set_2)