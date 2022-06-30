# 小彭的乱码
def test(list1, dic1):
    list1.insert(0, 0)
    dic1.clear()


info_list = [1, 2, 3]
info_dic = {"name":'pengjiaren'}
test(info_list, info_dic)
print(info_list)
print(info_dic)