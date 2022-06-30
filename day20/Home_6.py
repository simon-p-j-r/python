# 小彭的乱码
import re

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'


def substitute(temp):
    string = temp.group()
    info_list = list(string)
    target = ''
    tag = 0
    while tag < len(info_list):
        num = info_list[tag]
        if num == '年' or num == '月':
            info_list[tag] = '/'
        elif num == '日':
            info_list[tag] = ' '
        elif num == '时':
            info_list[tag] = ':'
        elif num == '分':
            info_list[tag] = ''
        tag += 1
    for num in info_list:
        target += num
    return target

ret_one = re.sub(r'.*', substitute, s)
ret_two = re.findall(r'\d{4}/(?:\d|1\d)?/(?:[0-2]?[0-9]|30|31)?\s(?:[01]?[0-9]|2[0-4]?)\:[0-5]?[0-9]?', ret_one)
if ret_two:
    print(ret_two)
