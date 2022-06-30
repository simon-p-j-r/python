# 小彭的乱码
import os

file_one = open('readme', 'a+', encoding='UTF-8')
file_one.write('人生苦短，我用python\n')
file_two = open('readme1', 'a+', encoding='UTF-8')
file_one.seek(0)
while True:
    text = file_one.readline()
    if not text:
        break
    file_two.write(text)

file_one.seek(0,os.SEEK_CUR)
file_one.seek(6)
text = file_one.read()
print(text)

file_three = open('homework_1', 'w+', encoding='utf_8')
text = file_three.read()
print(text)

file_one.close()
file_two.close()
file_three.close()