# 小彭的乱码
import os
from multiprocessing import Process
def test_method():
    print(os.getpid())
    while True:
        pass

if __name__ == '__main__':
    p = Process(target=test_method)
    p.start()
    print(os.getpid())