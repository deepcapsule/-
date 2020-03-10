# -*- coding: utf-8 -*-
"""
File: bstnode.py
Created on Tue Mar 19 15:21:21 2019

@author: wangchx
"""


class BSTNode(object):
    """树节点"""
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right