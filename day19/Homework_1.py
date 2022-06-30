# 小彭的乱码
import threading

num = 0
def add_num():
    global num
    tag = 0
    while tag < 10000000:
        num += 1
        tag += 1

if __name__ == '__main__':
    ti = threading.Thread(target=add_num)
    t2 = threading.Thread(target=add_num)
    ti.start()
    t2.start()
    ti.join()
    t2.join()
    print(num)