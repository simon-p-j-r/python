# 小彭的乱码
list1 = [1, 2, 3, 4, 4, 4, 4]
tag = 0
storage_num = None
for num in list1:
    if tag == 0:
        storage_num = num
    if num == storage_num:
        tag += 1
    else:
        tag -= 1
if tag > 0:
    print(storage_num)
