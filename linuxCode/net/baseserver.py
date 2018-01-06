#!/usr/bin/env python
#!coding:utf-8

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print('Waiting for connections...')
s.listen(1)

while 1:
    clientsock,clientaddr = s.accept()
    print('Got connection from',clientsock.getpeername())
    clientsock.close()

