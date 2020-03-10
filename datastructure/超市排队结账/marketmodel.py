# -*- coding: utf-8 -*-
"""
File: marketmodel.py
Created on Wed Mar 13 15:54:55 2019

@author: wangchx
"""
from cashier import Cashier
from customer import Customer


class MarketMode(object):
    
    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._avarageTimePerCus = averageTimePerCus
        self._cashier = Cashier()
        
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                    self._probabilityOfNewArrival,
                    currentTime,self._avarageTimePerCus)
            
            # Send customer to cashier if successfully
            # generated
            if customer != None:
                self._cashier.addCustomer(customer)
                
            # Tell cashier to provide another unit of service
            self._cashier.serveCustomers(currentTime)
            
    def __str__(self):
        return str(self._cashier)
    
        