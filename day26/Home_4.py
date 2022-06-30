# 小彭的乱码
def verification(funk):
    print('verifying')
    def verify():
        print('verification')
        funk()

    return verify


def passwd(func):
    print('inputing')
    def input_passwd():
        print('input passwd')
        func()
    return input_passwd

@passwd
@verification
def entry():
    print('entry')


entry()
