# 小彭的乱码
file = open('homework_1', 'r+', encoding='utf-8')
while True:
    text = file.readline()
    if not text:
        break
    print(text)
file.close()