# 小彭的乱码
# 小彭的乱码
import time


def tes_module(func):
    def test_core(a):
        print(time.time())
        print(a)
        func()
        print(time.time())
    return test_core

@tes_module
def test_over():
    for i in range(1000000):
        pass

test_over('begin')