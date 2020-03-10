# -*- coding: utf-8 -*-
"""
File: abstrackstack.py
Created on Mon Mar 11 14:50:43 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection


class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""
    
    # Construcor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contends of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)
        
    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        self.push(item)