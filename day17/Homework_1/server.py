# 小彭的乱码
import sys
from socket import *

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_addr = (sys.argv[1], 2000)
tcp_server.bind(tcp_addr)
tcp_server.listen(50)
tcp_server.setblocking(False)
client = None
tag = 0

while True:
    try:
        client, _ = tcp_server.accept()
    except Exception:
        pass
    if client:
        client.setblocking(False)
        try:
            data = client.recv(20)
            if not data:
                tag = 1
                print(886)
                break
            print(data.decode('utf-8'))
        except Exception:
            pass
    if tag == 1:
        break
client.close()
tcp_server.close()