# 小彭的乱码
def verification(funk):
    def verify():
        print('verification')
        funk()

    return verify


@verification
def entry():
    print('entry')

entry()
