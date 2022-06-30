# 小彭的乱码
try:
    num_str = input('请输入一个整型数')
    num_int = int(num_str)
    num_list = list(num_str)
    tag = len(num_list) // 2
    tag_to_zero = 0
    if len(num_list) % 2 == 0:
        tag_to_zero = tag - 1
    else:
        tag_to_zero = tag - 1
        tag += 1
    while tag_to_zero >= 0:
        if num_list[tag_to_zero] != num_list[tag]:
            raise Exception('不是回文数')
        tag += 1
        tag_to_zero -= 1
except ValueError:
    print('叫你输整型数')
except Exception as result:
    print(result)
else:
    print('是回文数')
