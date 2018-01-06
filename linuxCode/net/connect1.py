#!/usr/bin/env python
#!coding:utf-8

import socket

print('Creating socket...')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Done!')

print('Connecting to remote host...')
s.connect(('192.168.0.100',51423))
print('Done!')
