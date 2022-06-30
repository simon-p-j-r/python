# 小彭的乱码
from functools import wraps


def tes_module(func):
    @wraps(func)
    def test_core():
        '''
        core
        :return:
        '''
        return func()
    return test_core


@tes_module
def test_over():
    '''
    over
    :return:
    '''
    return 'test'


print(test_over.__name__, test_over.__doc__)
print(test_over())
