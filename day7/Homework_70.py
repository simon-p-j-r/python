# 小彭的乱码
info_list = [3,'a',5.2,4,{},9,[]]
tag = 0
len_tag = len(info_list)
str_info = type(info_list[0])
while tag < len_tag:
    if (isinstance(info_list[tag],int))  | (isinstance(info_list[tag], float)):
        if info_list[tag] > 3.0:
            info_list[tag] = 1
        else:
            info_list[tag] = 0
    else:
        info_list[tag] = 0
    tag += 1
print(info_list)