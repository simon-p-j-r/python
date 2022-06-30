# 小彭的乱码
import re
test_liest = ['http://www.yahoo.com', 'https://www.xju.edu.cn']
for num in test_liest:
    ret = re.match(r'\w+', num)
    if ret:
        print(ret.group())