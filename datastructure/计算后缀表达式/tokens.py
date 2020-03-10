# -*- coding: utf-8 -*-
"""
File: tokens.py
Tokens for processing expressions.
Created on Tue Mar 12 08:40:05 2019

@author: wangchx
"""

class Token(object):
    
    UNKNOWN = 0 # unknown
    
    INT = 4     # interger
    
    MINUS = 5   # minus operator
    PLUS = 6    # plus operator
    MUL = 7     # multiply operator
    DIV = 8     # divide operator
    
    FIRST_OP = 5  # first operator code
    
    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value
        
    def isOperator(self):
        return self._type >= Token.FIRST_OP
    
    def __str__(self):
        return str(self._value)
    
    def getType(self):
        return self._type
    
    def getValue(self):
        return self._value
    
    def _makeType(self, ch):
        if ch.isdigit():
            return Token.INT
        if ch == '*':
            return Token.MUL
        elif ch == '/':
            return Token.DIV
        elif ch == '+':
            return Token.PLUS
        elif ch == '-':
            return Token.MINUS
        else :
            return Token.UNKNOWN