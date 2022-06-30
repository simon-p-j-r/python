# 小彭的乱码
import threading

num = 0
def add_num(mutex):
    global num
    tag = 0
    while tag < 10000000:
        mutex.acquire()
        num += 1
        mutex.release()
        tag += 1

if __name__ == '__main__':
    mutex = threading.Lock()
    ti = threading.Thread(target=add_num,args=(mutex,))
    t2 = threading.Thread(target=add_num,args=(mutex,))
    ti.start()
    t2.start()
    ti.join()
    t2.join()
    print(num)