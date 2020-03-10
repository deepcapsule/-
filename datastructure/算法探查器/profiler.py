# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 08:48:39 2019

@author: wangchx
"""

"""
File : profiler.py

Defines a class for profiling sort algorithms.
A Profiler object tracks the list,the number of comparisons
and exchanges,and the running time.The Profiler can also print 
a trace and can create a list of unique or duplicate numbers.
"""

import time
import random

class Profiler(object):
    
    def test(self,function,lyst=None,size=10,
             unique=True,comp=True,exch=True,trace=False):
        self._comp = comp
        self._exch = exch
        self._trace = trace
        if lyst != None:
            self._lyst = lyst
        elif unique:
            self._lyst = [i for i in range(1,size+1)]
            random.shuffle(self._lyst)
        else:
            self._lyst = []
            for count in range(size):
                self._lyst.append(random.randint(1,size+1))
        self._exchCount = 0
        self._cmpCount = 0
        self._startClock()
        function(self._lyst,self)
        self._stopClock()
        print(self)
        
    def exchange(self):
        "Counts exchanges if on"
        if self._exch:
            self._exchCount += 1
        if self._trace:
            print(self._lyst)
        
    def comparision(self):
        "Counts comparisions if on"
        if self._comp:
            self._cmpCount += 1
            
    def _startClock(self):
        "Record the starting time."
        self._start = time.time()
        
    def _stopClock(self):
        "Stops the clock and computes the elapsed time in seconds."
        self._elapsedTime = round(time.time()-self._start,3)
        
    def __str__(self):
        "returns the results as a string."
        result = "Problem size: "
        result += str(len(self._lyst)) + '\n'
        result += "Elapsed time: "
        result += str(self._elapsedTime) + '\n'
        if self._comp:
            result += "Comparisions: "
            result += str(self._cmpCount) + "\n"
        if self._exch:
            result += "Exchangs: "
            result += str(self._exchCount) + '\n'
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            