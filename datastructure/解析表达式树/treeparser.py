# -*- coding: utf-8 -*-
"""
File: treeparser.py
Created on Thu Mar 21 09:38:09 2019

@author: wangchx
"""

from scanner import Scanner
from treetoken import Token
from expressiontree import LeafNode,InteriorNode


class TreeParser(object):
    
    def __init__(self, expr):
        self.scanner = Scanner(expr)
        
    def parser(self):
        return self.expression()
    
    def factor(self):
        token = self.scanner.get()
        if token is None:
            return
        if token.getType() == Token.INT:
            tree = LeafNode(token.getValue())
            self.scanner.tonext()
        elif token.getType() == Token.L_PAR:
            self.scanner.tonext()
            tree = self.expression()
            self.accept(self.scanner.get(),
                        Token.R_PAR,
                        "')' expected")
            self.scanner.tonext()
        else:
            tree = None
            self.fatalError(token, "bad factor")
        return tree
    
    def term(self):
        tree = self.factor()
        token = self.scanner.get()
        if token is None:
            return tree
        while token.getType() in (Token.MUL, Token.DIV):
            op = str(token)
            self.scanner.tonext()
            tree = InteriorNode(op, tree, self.factor())
            token = self.scanner.get()
            if token is None:
                break
        return tree
    
    def expression(self):
        tree = self.term()
        token = self.scanner.get()
        if token is None:
            return tree
        while token.getType() in (Token.PLUS, Token.MINUS):
            op = str(token)
            self.scanner.tonext()
            tree = InteriorNode(op, tree, self.term())
            token = self.scanner.get()
            if token is None:
                break
        return tree
        
    def accept(self, token, expctedType, strings):
        if token.getType() == expctedType:
            return
        else:
            self.fatalError(token, strings)
        
    def fatalError(self, token, strings):
        raise ValueError(str(token) + ': ' + strings)