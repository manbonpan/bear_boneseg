import socket
import sys
import re
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_address = ('localhost', 10000)
matches_positions=[]
sock.bind(('127.0.0.1',8080))
sock.listen(10)
index=open('./index.html','r+')
preprocess=(index.read())
index.close()
origins=[]
substring = ['src="','rel="','href']
#forbidden=['s','r','c','r','e','l','u','r','l','(',')','h','r','e','f','"']
with open('./index.html') as fp:
   for cnt, line in enumerate(fp):
       count=0
       for i in substring:
           if i in line:
               x=re.findall(i,line)
               count=0
               m=re.finditer(i,line)
               for k in m:
                   stri=''
                   a,b = k.span()
                   f= k.group(0)
                   for j in range(len(line)):
                       
                       if f not in line:
                           break
                       print(len(line))
                       if line[b+j] == '"':
                          origins.append(stri)
                          break
                       stri=stri+line[b+j]
                       count=count+1
                   
                   
                   
               
    
               




while True:
    index=open('./index.html','r+')
    preprocess=(index.read())
    index.close()
    connection, addr = sock.accept()
    y=connection.recv(1600).decode()
    connection.sendall(bytes(preprocess,'utf-8'))
    print('conn:',connection,'addr',addr,'recv',y)
    if 'seesion' in y:
        
    
        print(y)
        

    
    

        

    
