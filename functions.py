# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:25:12 2018

@author: Administrator
"""
import numpy as np

def Respiration(T,PGD):
    RmTo = 0.015
    Q10 = 2
    To = 25
    Rg = 0.39
    Rm = PGD*RmTo*Q10**((T-To)/10)
    RG = PGD*Rg
    return [Rm, RG]

def TDRW(PND, period):
    delta = 30/40
    if period == 'p2' :
        (cf, pdm) = ([0.45, 0.45, 0.75], [0.1, 0.17, 0.73])
    elif period == 'p3':
        (cf, pdm) = ([0.45, 0.45, 0.75, 0.75], [0.04, 0.31, 0.62, 0.03])
    elif period == 'p4':
        (cf, pdm) = ([0.45, 0.45, 0.75, 0.75], [0.03, 0.33, 0.44, 0.20])
    elif period == 'p5':
        (cf, pdm) = ([0.45, 0.45, 0.75, 0.75], [0.02, 0.31, 0.41, 0.26])
    Cf = np.dot(cf,pdm)
    
    TDRW = delta * Cf * PND / (1-0.05)
    return TDRW

