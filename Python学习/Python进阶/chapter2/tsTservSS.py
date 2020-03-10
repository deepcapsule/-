#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
File Name: tsTservSS.py
Author: wangchx
Created Time: 2019年06月20日 星期四 19时56分31秒
"""
 
from socketserver import (TCPServer as TCP, 
        StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):

    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(b'[%s] %s' % (ctime().encode('utf-8'), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

