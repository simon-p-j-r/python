# 小彭的乱码
info_file = open('The_Holy_Bible_Two.txt', 'r+', encoding='utf-8')
char_num = 0
line_num = 0
word_num = {}
tag_end = 0
tag_output = 0
while True:
    text = info_file.readline()
    info_list = list(text)
    # 统计行数
    line_num += 1
    # 去除换行符
    if len(info_list) > 0:
        if info_list[len(info_list) - 1] == '\n':
            info_list.pop()
    # 统计字符数
    char_num += len(info_list)
    info_list_word = text.split()
    # 统计单词数
    for i in info_list_word:
        if not word_num.__contains__(i):
            word_num[i] = 0
        word_num[i] += 1
    # 推出循环标记
    if text == 'gENESIS 1\n':
        tag_end += 1
    if tag_end == 2:
        break
while True:
    max_num = max(word_num.values())
    for num in word_num:
        if word_num[num] == max_num:
            print('%s :%d' % (num, max_num))
            tag_output += 1
            word_num[num] = -1
            if tag_output == 10:
                break
    if tag_output == 10:
        break
print(line_num)
print(char_num)
