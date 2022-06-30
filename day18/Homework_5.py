# 小彭的乱码
import time
from threading import Thread


def test_method():
    print('say_hello')
    time.sleep(1)

if __name__ == '__main__':
    for i in range(0, 5):
        t = Thread(target=test_method)
        t.start()
