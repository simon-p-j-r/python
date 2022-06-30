# 小彭的乱码
import re

test_liest = ['L,smith', 'L smith']
for num in test_liest:
    ret = re.match(r'\w.\w+', num)
    if ret:
        print(ret.group())