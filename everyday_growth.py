# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:38:46 2018

@author: Administrator
"""

import numpy as np
import functions as fun
class Everyday_growth():
    def __init__(self):
        self.t = np.array([0, 0, 0, 0, 0], dtype = int)                         # count
        self.dis = np.array([[0.084, 0.251, 0.665, 0], [0.063, 0.204, 0.654, 0.079], 
               [0.034, 0.15, 0.409, 0.407], [0.01, 0.089, 0.305, 0.596]])       # distribution
        self.yt = np.array([0, 0, 0, 0], dtype = float)                         #[yroot, ystem, yleaf, yfruit]
        self.area = np.zeros((200,1))
        self.area[0] = 0.05                                                       #m2
        self.weight2area = np.array([31.3, 32.2, 34.5, 35.7])                   #g m-2
        self.weight = np.zeros((200,4))
        self.weight[0] = [1, 1, 1.57, 0]
        self.count = 0
    def growth(self, tp, Tp, PND, i):
        if tp >= Tp[0,0] and tp < Tp[0,1]: #发芽期
            p = 'p1'
            self.t[0] += 1
            self.count = 3 
        if tp >= Tp[0,1] and tp < Tp[0,2]: #苗期
            p = 'p2'  
            Yield = fun.TDRW(PND, p)
            self.yt = self.dis[0] * Yield
            self.weight[i] = self.yt * self.area[i-1] + self.weight[i-1]
            self.area[i] = self.weight[i, 2]/ self.weight2area[0]
            self.t[1] += 1
            self.count = 35
        if tp >= Tp[0,2] and tp < Tp[0,3]: #开花坐果期
            p = 'p3'    
            Yield = fun.TDRW(PND, p)
            self.yt = self.dis[1] * Yield
            self.weight[i] = self.yt * self.area[i-1] + self.weight[i-1]
            self.area[i] = self.weight[i, 2]/ self.weight2area[1]
            self.t[2] += 1
            self.count = 43
        if tp >= Tp[0,3] and tp < Tp[0,4]: #结果期
            p = 'p4'
            Yield = fun.TDRW(PND, p)
            self.yt = self.dis[2] * Yield
            self.weight[i] = self.yt * self.area[i-1] + self.weight[i-1]
            self.area[i] = self.weight[i, 2]/ self.weight2area[2]
            self.t[3] += 1
            self.count =  89
        if tp >= Tp[0,4]:                #采收期
            p = 'p5'
            Yield = fun.TDRW(PND, p)
            self.yt = self.dis[3] * Yield
            self.weight[i] = self.yt * self.area[i-1] + self.weight[i-1]
            self.area[i] = self.weight[i, 2]/ self.weight2area[3]
            self.t[4] += 1
            self.count = 100
        
        return [self.yt, self.t, self.area, self.weight, p, self.count]