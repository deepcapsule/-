#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsUserv.py
Author: wangchx
Created Time: 2019年06月20日 星期四 19时31分35秒
"""
 
from socket import *
from time import ctime,sleep

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode('utf-8'), addr)
    print('...received from and returned to:', addr)

updSerSock.close()

