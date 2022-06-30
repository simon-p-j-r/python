# 小彭的乱码
num = input('请输入手机号')
info_list = list(num)
info_list.insert(3, '.')
info_list.insert(8, '.')
num = ''
for i in info_list:
    num = num + i
print("Mobile:" + num)