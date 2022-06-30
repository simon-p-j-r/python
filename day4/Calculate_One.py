def negative_number(num):
    binary = bin(num)
    list_binary = list(binary)
    list_binary.reverse()
    list_index = list_binary.index('1')
    list_binary[list_index] = '2'
    ind = '0'
    while ind != 'b':
        ind = list_binary.pop()
    list_binary.reverse()
    deposit = 64 - len(list_binary)
    while ind != '2':
        ind = list_binary.pop()
    print(list_binary.count('0') + 1 + deposit)


def positive_number(num):
    binary = bin(num)
    list_binary = list(binary)
    print(list_binary.count('1'))


num = int(input('请输入一个数字'))
if num < 0:
    negative_number(num)
else:
    positive_number(num)



