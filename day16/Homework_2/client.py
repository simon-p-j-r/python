# 小彭的乱码
import select
import sys
from socket import *

tag = 0
tcp_client = socket(AF_INET, SOCK_STREAM)
addr = (sys.argv[1], 2000)
tcp_client.connect(addr)
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(tcp_client.fileno(), select.EPOLLIN)
while True:
    events = epoll.poll(-1, 2)
    for file, _ in events:
        if file == sys.stdin.fileno():
            data = input('赶紧输')
            tcp_client.send(data.encode('utf-8'))
        elif file == tcp_client.fileno():
            data = tcp_client.recv(50)
            if not data:
                print('over')
                tag = 1
                break
            print(data.decode('utf-8'))
    if tag == 1:
        break
tcp_client.close()
