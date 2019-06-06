# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:24:35 2018

@author: Administrator
"""

class Rte():
    def __init__(self):
        self.p1 = [15, 29, 35]
        self.p2 = [10, 25, 35]
        self.p3 = [15, 25, 35]
        self.p4 = [15, 25, 35]
        
        self.p = 2
    def execute(self, T, period):
        if period == 'p1' :
            [Tb, To, Tm] = self.p1
        elif period == 'p2':
            [Tb, To, Tm] = self.p2
        elif period == 'p3':
            [Tb, To, Tm] = self.p3
        elif period == 'p4':
            [Tb, To, Tm] = self.p4
       
        
        if T > Tb and T <= To:
            rte = ((T - Tb)/(To - Tb))**(self.p*((T-To)/Tb)**2)
        elif T > To and T < Tm:
            rte = ((Tm - T)/(Tm - To))**(self.p*((T-To)/Tb)**2)
        else:
            rte = 0
        return rte