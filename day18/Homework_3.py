# 小彭的乱码
import os
import time
from multiprocessing import Process, Queue


def writer(q: Queue):
    while not q.full():
        for num in ['A', 'B', 'C']:
            q.put(num)
            print(num, 'write')


def reader(q: Queue):
    time.sleep(2)
    while not q.empty():
        print(q.get(), 'read')



if __name__ == '__main__':
    q = Queue(3)
    p_one = Process(target=writer, args=(q,))
    p_one.start()
    p_two = Process(target=reader, args=(q,))
    p_two.start()
