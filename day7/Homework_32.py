# 小彭的乱码
info_tuple = (1, 2, 3)
info_list = list(info_tuple)
info_dir = {}
info_list_tow = ['x', 'y', 'z']
tag = 0
for num in info_list:
    info_dir[info_list_tow[tag]] = num
    tag += 1
print(info_dir)