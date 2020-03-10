#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsTserv.py
Author: wangchx
Created Time: 2019年06月20日 星期四 17时50分41秒
"""
 
 
from socket import *
from time import ctime,sleep

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected form:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode('utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
