# 小彭的乱码
import os
import time
from multiprocessing import *


def writer(q):
    # while not q.full():
        for num in ['A', 'B', 'C']:
            q.put(num)
            print(num, 'write')


def reader(q):
    time.sleep(2)
    while not q.empty():
        print(q.get(), 'read')



if __name__ == '__main__':
    q = Manager().Queue(3)
    p = Pool(2)
    p.apply_async(writer, (q,))
    p.apply_async(reader, (q,))
    p.close()
    print('asd')
    p.join()
    print('123')

