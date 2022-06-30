# 小彭的乱码
import os
import string

str_punctuation = string.punctuation
file_bible = open('The_Holy_Bible.txt', 'r+', encoding='utf-8')
file_bible_two = open('The_Holy_Bible_Two.txt', 'a+', encoding='utf-8')
text = ''  # 用来接收从文件中取出的一行
str_list = []  # 用来接收一行转化成的list
list_len = 0  # 用来记录一行中字符个数
tag = 0  # 用来做标记循环
tag_end = 0  # 结束标记，读到两次Genesis 1的时候结束
str_output = ''  # 用来重组list中的字符使之成为完整的字符串
# tag_tell_ing = 0
# tag_tell_ed = 0
while True:
    # file_bible.seek(tag_tell_ing)
    text = file_bible.readline()
    # tag_tell_ed = tag_tell_ing
    # file_bible.seek(0, os.SEEK_CUR)
    # tag_tell_ing = file_bible.tell()
    str_list = list(text)
    if len(str_list) > 0:  # 把换行符丢掉
        if str_list[len(str_list) - 1] == '\n':
            str_list.pop()
    list_len = len(str_list)
    tag = 0
    str_output = ''
    while tag < list_len:
        for j in str_punctuation:
            if str_list[tag] == j:
                str_list[tag] = ' '
        tag += 1
    for i in str_list:
        str_output = str_output + i
    str_output = str_output + '\n'  # \n是把换行符再加回去
    # file_bible.seek(tag_tell_ed)
    file_bible_two.write(str_output.swapcase())
    if str_output == 'Genesis 1\n':
        tag_end += 1
    if tag_end == 2:
        break
file_bible.close()
