# 小彭的乱码
a = 5
b = 10
def test_global():
    a = 10
    global b
    b = 20
    print(b)
    print(a)


test_global()
print(a)
print(b)