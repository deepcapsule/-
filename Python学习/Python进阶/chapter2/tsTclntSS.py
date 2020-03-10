#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsTclntSS.py
Author: wangchx
Created Time: 2019年06月20日 星期四 20时05分22秒
"""
 
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(b'%s\r\n' % data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8').strip())
    tcpCliSock.close()
