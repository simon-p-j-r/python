# 小彭的乱码
info_str = 'abc'
info_list = list(info_str)
tag = 0
len_str = len(info_str)
while tag <= len_str * 2:
    info_list.insert(tag, ',')
    tag += 2
info_str = ''
for num in info_list:
    info_str = info_str + num
print(info_str)