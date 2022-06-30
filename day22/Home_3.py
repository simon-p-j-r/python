# 小彭的乱码
class File:
    def __init__(self, filename, method):
        self.filename = filename
        self.method = method

    def __enter__(self):
        self.info_file = open(self.filename, self.method, encoding='utf-8')
        return self.info_file

    def __exit__(self, *args):
        self.info_file.close()


with File('readme', 'w+') as f:
    f.write('hi')
