#!/usr/bin/env python
#!coding:utf-8

import socket
import sys

print('Creating socket...')
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Done!')

print('Connecting to remote host...')
s.connect(('192.168.0.100',51423))
s.sendall('helloworld!')

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

print('Done!')
