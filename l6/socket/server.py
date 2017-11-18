import socket

address=('127.0.0.1',3000)
sk=socket.socket()
sk.bind(address)
sk.listen(3)


while True:
    print('waiting for connecting')
    conn,addr=sk.accept()
    print('connect from ',addr)
    conn.send(bytes('hello','utf-8'))

    while True:
        data=conn.recv(1024)
        print('-----',data.decode('utf-8'))
        inp=input('>>>')
        conn.send(bytes(inp, 'utf-8'))
sk.close()

