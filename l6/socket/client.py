import socket

sk=socket.socket()

sk.connect(('127.0.0.1',3000))

while True:
    data = sk.recv(1024)
    if not data:pass
    print('>>>>', data.decode('utf-8'))
    inp=input('please send message:')
    sk.send(bytes(inp,'utf-8'))

sk.close()