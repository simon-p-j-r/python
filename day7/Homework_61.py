# 小彭的乱码
info_list = ['a', 'b', 'c']
tag = 1
len_tag = len(info_list)
while tag < len_tag * 2:
    info_list.insert(tag, '|')
    tag += 2
tag_str = ''
for num in info_list:
    tag_str = tag_str + num
print(tag_str)