# 小彭的乱码
# 小彭的乱码
# 小彭的乱码
import time


def tes_module(func):
    def test_core(*args, **kwargs):
        print(time.time())
        print(args, kwargs)
        func(*args, **kwargs)
        print(time.time())

    return test_core


@tes_module
def test_over(*args, **kwargs):
    print('func')
    print(args)
    print(kwargs)


test_over('begin', 1, 2, a=2)
