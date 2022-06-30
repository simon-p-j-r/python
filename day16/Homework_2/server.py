# 小彭的乱码
import select
import sys
from socket import *

tag = 0
tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOCK_STREAM, SO_REUSEADDR, 1)
addr = (sys.argv[1], 2000)
tcp_server.bind(addr)
tcp_server.listen(20)
client, _ = tcp_server.accept()
epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(client.fileno(), select.EPOLLIN)
while True:
    events = epoll.poll(-1, 2)
    for file, _ in events:
        if file == sys.stdin.fileno():
            data = input('赶紧输')
            client.send(data.encode('utf-8'))
        elif file == client.fileno():
            data = client.recv(50)
            if not data:
                print('over')
                tag = 1
                break
            print(data.decode('utf-8'))
    if tag == 1:
        break
client.close()
tcp_server.close()
