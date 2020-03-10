#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsUclnt.py
Author: wangchx
Created Time: 2019年06月20日 星期四 19时37分25秒
"""
 
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
