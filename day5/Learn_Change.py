# 小彭的乱码
test_int = 1
print(id(test_int))
test_bool = True
print(id(test_bool))
test_float = 1.01
print(id(test_float))
test_str = 'test'
print(id(test_str))
test_list = [1, 2, 3]
print(id(test_list))


def test_change_int(num):
    num = 2;
    print(num, ' ', id(num))


def test_change_bool(num):
    num = False;
    print(num, ' ', id(num))


def test_change_float(num):
    num = 2.0;
    print(num, ' ', id(num))


def test_change_str(num):
    num = 'change';
    print(num, ' ', id(num))


def test_change_list(num):
    num.append(2)
    print(num, id(num))


test_change_int(test_int)
test_change_bool(test_bool)
test_change_float(test_float)
test_change_str(test_str)
test_change_list(test_list)
print(test_int, id(test_int))
print(test_bool, id(test_bool))
print(test_float, id(test_float))
print(test_str, id(test_str))
print(test_list, id(test_list))


