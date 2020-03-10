# -*- coding: utf-8 -*-
"""
File: ermodel.py
Created on Fri Mar 15 08:53:54 2019

@author: wangchx
"""

from linkedpriorityqueue import LinkedPriorityQueue


class ERModel(object):
    """ERmodle"""
    
    def __init__(self):
        self._queue = LinkedPriorityQueue()
        
    def isEmpty(self):
        return self._queue.isEmpty()
        
    def schedule(self, patient):
        self._queue.add(patient)
        
    def treatNext(self):
        patient = self._queue.pop()
        return patient