# 小彭的乱码
import struct
import sys
from socket import *

tcp_file = socket(AF_INET,SOCK_STREAM)
tcp_file.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
addr = ('192.168.3.144', 2000)
tcp_file.bind(addr)
tcp_file.listen(50)
client,_ = tcp_file.accept()
file_name = 'Readme'
b_name = file_name.encode('utf-8')
client.send(struct.pack('I', len(b_name)))
client.send(b_name)
file = open(file_name, 'rb')
text = file.read()
client.send(struct.pack('I', len(text)))
client.send(text)
file.close()
client.close()
tcp_file.close()