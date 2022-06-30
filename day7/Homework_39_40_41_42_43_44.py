# 小彭的乱码
info_set_one = {'A','D','B'}
info_set_Two = {'D','E','C'}
info_set = info_set_one.difference(info_set_Two)
print(info_set)

info_set = info_set_one.union(info_set_Two)
print(info_set)

info_set = info_set_one.intersection(info_set_Two)
print(info_set)

info_set = info_set_one.symmetric_difference(info_set_Two)
print(info_set)

print(info_set_one.isdisjoint(info_set_Two))

print(info_set_one.issubset(info_set_Two))