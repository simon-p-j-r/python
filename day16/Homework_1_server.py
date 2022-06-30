# 小彭的乱码
import sys
from socket import *

tcp_server = socket(AF_INET, SOCK_STREAM)
addr = (sys.argv[1], 2000)
tcp_server.bind(addr)
tcp_server.listen(20)
client, _ = tcp_server.accept()
data = client.recv(5)
print(data)
client.send(b'hi too')
client.close()
tcp_server.close()