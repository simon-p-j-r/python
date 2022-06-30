# 小彭的乱码
info_str = '2.72, 5, 7, 3.14'
info_list = info_str.split(',')
for num in info_list:
    if num.find('.') != -1:
        num = float(num)
    else:
        num = int(num)
    print(num, type(num))