#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsTclnt.py
Author: wangchx
Created Time: 2019年06月20日 星期四 19时13分16秒
"""
 
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
