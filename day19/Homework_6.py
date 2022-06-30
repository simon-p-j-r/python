# 小彭的乱码
import re

ret = re.match('[a-z]{3}','bat')
print(ret.group())
ret = re.match('[a-z]{3}','bit')
print(ret.group())
ret = re.match('[a-z]{3}','but')
print(ret.group())
ret = re.match('[a-z]{3}','hat')
print(ret.group())
ret = re.match('[a-z]{3}','hit')
print(ret.group())
ret = re.match('[a-z]{3}','hut')
print(ret.group())

