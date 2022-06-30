# 小彭的乱码
def test_out(info):
    print(info)
    def tes_module(func):
        def test_core():
            print('core')
            return func()
        return test_core
    return tes_module

@test_out(1)
def test_over():
    return 'test'

print(test_over())