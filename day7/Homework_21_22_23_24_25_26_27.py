# 小彭的乱码
info_dic = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
for num in  info_dic:
    print(num, info_dic[num])
print(info_dic.keys())
print(info_dic.values())
print(info_dic.items())
info_dic['David'] = 19
info_dic['Cecil'] = 17
print(info_dic)
info_dic.pop('Beth')
print(info_dic)
info_dic.clear()
print(info_dic)
print(info_dic.get('David'))
print(info_dic.get('Alice'))
