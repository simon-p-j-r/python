# 小彭的乱码
info_list = [0,1,2,3.14,'x',None,'',list(),{5}]
tag = 0
len_tag = len(info_list)
while tag < len_tag:
    info_list[tag] = bool(info_list[tag])
    tag += 1
print(info_list)