# 小彭的乱码
list1 = ['x', 'y', 'z']
list2 = [1, 2, 3]
info_list = []
tag = 0
for num in list1:
    info_list.append((num,list2[tag]))
    tag += 1
print(info_list)