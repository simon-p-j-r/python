# 小彭的乱码
class MiniIOS():
    def __init__(self, name):
        self.name = name
        self.apps = []

    def __str__(self):
        return '%s 安装了 %s' % (self.name, self.apps)

    def install_app(self, app):
        if app.name in self.apps:
            print('%s已经安装' % app.name)
        else:
            # 这里其实就是app是啥类型就调用那个类型的install方法，
            # 这其实和python不用申明对象类型一样，以此来实现多态
            app.install()
            self.apps.append(app.name)


class App():
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return '%s 的当前版本是 %s -%s' % (self.name, self.version, self.desc)
    
    def install(self):
        print("将 %s [%s] 的执行程序复制到程序目录..." % (self.name, self.version))
        
class QQ(App):
    def install(self):
        print('正在安装')
        super(QQ, self).install()

class Chrom(App):
    def install(self):
        print("正在解压缩安装程序...")
        super().install()

linux = MiniIOS('Linux')
pycharm = QQ('QQ', '2', '实时交流软件')
chrom = Chrom('chrom', '3', 'brows')
linux.install_app(pycharm)
linux.install_app(chrom)
linux.install_app(chrom)
print(linux)