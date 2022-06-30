# 小彭的乱码
info_str = 'pengjiaren'
for num in info_str:
    print(num)

info_str_space = ' '
print(info_str_space.isspace())
print(info_str.isspace())

info_str_num_and_str = 'wangdao123'
print(info_str.isalnum())
print(info_str_space.isalnum())
print(info_str_num_and_str.isalnum())

print(info_str_num_and_str.isalpha())
print(info_str.isalpha())

info_str_num = "123"
print(info_str_num.isdecimal())

print(info_str.islower())
print(info_str.isupper())

print(info_str.startswith('peng'))
print(info_str.endswith('ren'))

print(info_str.find('jia'))
print(info_str.find("wang"))

print(info_str_num_and_str.lower())
print(info_str_num_and_str.upper())

print(info_str.ljust(50))
print(info_str.center(50))

print(info_str.strip())

list1 = ['asd', 'asd', 'asd']
print(info_str.join(list1))
print(type(info_str.join(list1)))
print(info_str.join(info_str_num_and_str))

print(info_str[2:-1:2])
print(info_str[::-1])
print(info_str[-1::])
print(info_str[:])

