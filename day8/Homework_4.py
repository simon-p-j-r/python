# 小彭的乱码
def test(num, *args,**kwargs):
    print(num)
    print('*' *50)
    print(args)
    print('*' *50)
    print(kwargs)
    print('-' *50)


num = 10
info_tuple = (1, "wangdao")
info_dic = {"name":'pengjiaren'}
test(num,info_tuple,info_dic)
test(info_tuple,info_dic)
test(info_dic,info_tuple)
test(num,*info_tuple,**info_dic)