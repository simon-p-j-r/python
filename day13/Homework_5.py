# 小彭的乱码
def top_k(k, list1, list2):
    if k <= 0:
        return -1
    tag = 1
    list1_tag = 0
    list2_tag = 0
    while tag < k:
        if list1[list1_tag] < list2[list2_tag]:
            list1_tag += 1
        else:
            list2_tag += 1
        tag += 1
    num = min(list1[list1_tag],list2[list2_tag])
    print(num)


list1 = [1, 2, 5, 8, 9, 13]
list2 = [3, 4, 7, 11, 15, 16]
top_k(2, list1, list2)