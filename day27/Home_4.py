# 小彭的乱码
import time


# def tes_module(func):
#     def test_core():
#         print('core')
#         func()
#     return test_core
#
# @tes_module
# def test_over():
#     return 'test'
#
# print(test_over())


def tes_module(func):
    def test_core():
        print('core')
        return func()
    return test_core

@tes_module
def test_over():
    return 'test'

print(test_over())