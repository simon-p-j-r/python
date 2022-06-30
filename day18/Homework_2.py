# 小彭的乱码
# 小彭的乱码
import os
from multiprocessing import Process

num = 10
def test_method(list1: list):
    list1.append(1)
    global num
    num = 0
    print(list1, 'son', num)


if __name__ == '__main__':
    list1 = [0, 1, 2]
    p = Process(target=test_method, args=(list1,))
    p.start()
    p.join()
    print(list1, 'dad', num)
