# -*- coding: utf-8 -*-
"""
File: customer.py
Created on Wed Mar 13 16:52:43 2019

@author: wangchx
"""

import random


class Customer(object):
    
    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime, averageTimePerCustomer):
        """Returns a Customer object if the probability
        of arrival is greater than of equal to a random number.
        Otherwise, return None, indicating no new customer."""
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None
        
    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded
        
    def arrivalTime(self):
        return self._arrivalTime
    
    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded
    
    def serve(self):
        """Accepts a unit of service from the cashier."""
        self._amountOfServiceNeeded -= 1