# 小彭的乱码
import re
test_liest = ['123http://www.yahoo.com', '2https://www.xju.edu.cn']
for num in test_liest:
    ret = re.match(r'\d+', num)
    if ret:
        print(ret.group())