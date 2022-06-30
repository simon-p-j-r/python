# 小彭的乱码
import gevent

num = 0
def add_num():
    global num
    tag = 0
    while tag < 10000:
        num += 1
        tag += 1
        gevent.sleep(0.01)

if __name__ == '__main__':
    ti = gevent.spawn(add_num)
    t2 = gevent.spawn(add_num)
    ti.join()
    t2.join()
    print(num)