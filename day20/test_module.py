# 小彭的乱码
import re

test_liest = ['18:30', '25:20', '18:50']
for num in test_liest:
    ret = re.match(r'\d{4}/(\d|1\d)?/([0-2]?[0-9]|30|31)?\s([01]?[0-9]|2[0-4]?)\:[0-5]?[0-9]?', num)
    if ret:
        print(ret.group())