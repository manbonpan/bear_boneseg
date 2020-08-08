import socket
import re
import base64
import hashlib
from time import sleep
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',1234))
server.listen(10)
'''
+-+-+-+-+-------+-+-------------+-------------------------------+
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                     Payload Data continued ...                |
+---------------------------------------------------------------+
'''









while True:
    key=''

    connection, addr = server.accept()
    y=connection.recv(1600).decode()
    if 'websocket' in y:
        if 'Sec-WebSocket-Key: ' in y:
            x=re.search('Sec-WebSocket-Key: ',y)
            a,b = x.span()
            baseline=y[b:]
            for i in range(len(baseline)):
                if baseline[i] == '\n':
                    break
                
                
                key = key + baseline[i]
            key = key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
            sha1=hashlib.sha1(key.encode())
            sha1b=sha1.digest()
            aceept=base64.b64encode(sha1b)
            response='''HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {}'''.format(aceept.decode())
            print(response)
            connection.sendall(bytes(response,'utf-8'))
        
            #connection.sendall(bytes('hell','utf-8'))

        
        


