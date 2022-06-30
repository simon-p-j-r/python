i = 0
j = 0
for j in range(0, 9) :
    j+=1
    for i in range(0, j):
        i+=1
        print('%d*%d=%d  '%(i, j, i*j), end='')
    print('\n')