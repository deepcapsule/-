# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:55:20 2019

@author: wangchx
"""


class Node(object):
    """Represents a singly linked node."""
    
    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next
        
        
class TwoWayNode(Node):
    
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous