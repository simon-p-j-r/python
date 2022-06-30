# 小彭的乱码
info_list = [1,4,7,2,5,8]
info_add = ['x', 'y', 'z']
info_list_tag = 3
info_add_tag = 0
while info_list_tag < 3 + len(info_add):
    info_list.insert(info_list_tag, info_add[info_add_tag])
    info_list_tag += 1
    info_add_tag += 1
print(info_list)