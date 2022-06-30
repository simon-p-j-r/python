# 小彭的乱码
import time


def tes_module(func):
    def test_core():
        print(time.time())
        func()
        print(time.time())
    return test_core

@tes_module
def test_over():
    for i in range(1000000):
        pass

test_over()