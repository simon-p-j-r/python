# 小彭的乱码
def test(num, name = 'wangdao', put = 'pengjiaren'):
    print(num)
    return name + put


num = 10
info_str = test(num)
print(info_str)
info_str_2 = test(2, 'shenzhen')
print(info_str_2)
info_str_2 = test(3, put = 'wangdao')
print(info_str_2)

