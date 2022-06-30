# 小彭的乱码
# 小彭的乱码
import time
from threading import Thread


def test_method():
    while True:
        pass

if __name__ == '__main__':
    for i in range(0, 5):
        t = Thread(target=test_method)
        t.start()
    while True:
        pass
