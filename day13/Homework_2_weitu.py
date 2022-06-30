# 小彭的乱码
info_list = [1, 2, 1, 3, 4, 4, 5, 5, 2, 9, 57]
list1 = []
bitnum = 0
for i in info_list:
    if not bitnum & 1 << i:
        list1.append(i)
        bitnum |= 1 << i
print(list1)
