# 小彭的乱码
def test_1(a=3, b=4):
    def test_2(x):
        return a * x + b

    return test_2


info = test_1(1, 2)
print(info(1))


def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start

    return incr


c1 = counter(5)
print(c1())
print(c1())
