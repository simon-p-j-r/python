# 小彭的乱码
info_tuple_one = (1, 2)
info_tuple_Two = (3, 4)
info_list = list(info_tuple_one)
info_list.extend(list(info_tuple_Two))
print(tuple(info_list))
info_tuple_Three = info_tuple_one + info_tuple_Two
print(info_tuple_Three)