# 12
info_list = [3, 0, 8, 5, 7]
print(info_list)
info_list.sort()
print(info_list)
info_list.sort(reverse=True)
print(info_list)


# 13.
tag = 0
for num in info_list:
    if info_list[tag] > 5:
        info_list[tag] = 1
    else:
        info_list[tag] = 0
    tag +=1
print(info_list)