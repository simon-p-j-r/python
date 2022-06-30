# 小彭的乱码
info_list = [True,1,0,'x',None,'x',False,2,True]
print(info_list)
num = 1
print(len(info_list)//2)
while num <= len(info_list)//2:
    info_list.pop(num)
    num += 1
info_list.pop(num)
print(info_list)

info_list.clear()
print(info_list)