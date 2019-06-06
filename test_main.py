# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:58:19 2018

@author: Administrator
"""
import xlrd
import gui_main
import wx
import numpy as np
import functions as fun
import matplotlib.pyplot as plt
from rte import Rte
from everyday_growth import Everyday_growth



wildcard1 = "(*.xls; *.xlsx; *.csv); |*.xls;*.xlsx; *.csv"
class Main_test2(gui_main.MyFrame1):
    def __init__(self, parent):
        gui_main.MyFrame1.__init__(self,parent)
        self.a1 = np.array([])
        self.a2 = np.array([])
        self.a3 = np.array([])
        self.a4 = np.array([])
        self.t = np.array([])
        self.area = np.array([])
        self.weight = np.array([])
        
    def Openfile1(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose Temperature",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path
            
            #set the value to the TextCtrl[contents]
            self.a1 = self.readtable(tmp)
            self.contents1.SetValue(str(self.a1))
           
        dlg.Destroy()
        return self.a1
        
    def Openfile2(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose CO2 Concentration",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path

            #set the value to the TextCtrl[contents]
            self.a2 = self.readtable(tmp)
            self.contents2.SetValue(str(self.a2))
           
        dlg.Destroy()
        return self.a2
    def Openfile3(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose Lightintensity",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path
            
            #set the value to the TextCtrl[contents]
            self.a3 = self.readtable(tmp)
            self.contents3.SetValue(str(self.a3))
           
        dlg.Destroy()
        return self.a3   
    def Openfile4(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a Specie",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path
            
            #set the value to the TextCtrl[contents]
            self.a4 = self.readtable(tmp)
            self.contents4.SetValue(str(self.a4))
           
        dlg.Destroy()
        return self.a4
    def Openfile5(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a Specie",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path
            #set the value of TextCtrl[filename]
            
            #set the value to the TextCtrl[contents]
           
            self.aa = self.readtable(tmp)
            self.contents1.SetValue(str(self.aa[0]))
            self.contents2.SetValue(str(self.aa[1]))
            self.contents3.SetValue(str(self.aa[2]))
#            self.contents4.SetValue(str(a[3]))
            
        dlg.Destroy()
        return self.aa
    def readtable(self,tablename):
    
        data = xlrd.open_workbook(tablename)        
        table = data.sheets()[0]        
        nrows = table.nrows #行数        
        ncols = table.ncols #列数
        a = np.zeros((nrows, ncols),dtype = float)
        for i in range(0,nrows):
            rowValues= table.row_values(i) #某一行数据 
            a[i] = rowValues
        return a
    
    def Simulation(self,event):
        self.contents5.SetValue(' ')
        [self.t, self.area, self.weight] = self.main(event)
        
    def Get_a(self,event):
        T = self.a1
        CO2 = self.a2
        Light = self.a3
        Tp = self.a4
        All = self.aa
        if All is None:
            return [T, CO2, Light, Tp]
        else:
            [T, CO2, Light] = [All[0], All[1], All[2]]
            return [T, CO2, Light, Tp] 
    
    


    def main(self,event):
        tp =0
        c = Rte()
        g = Everyday_growth()
        i = 1
        j = 0
        
        while True:
            # one day
            #T = 25 # everage temperature
            # PGD = 10.3360 # g CO2 m-2 d-1
            # Tp = [0, 3, 35, 43, 89] #expected time of period
            
            [T, CO2, Light, Tp] = self.Get_a(event)
            PGD = np.ones((1,len(T))) * 10.3360 
            [Rm, RG] = fun.Respiration(T[j],PGD[0,j])
            PND = PGD[0,j] - Rm - RG # net photosynthesis yield     
            [yt, t, area, weight, p, count] = g.growth(tp, Tp, PND, i)    
            
            if p != 'p5':
                rte_1 = c.execute(T[j], p)
                tp += rte_1
            if p != 'p1':
                i += 1
            
            if t[4] >= 50:
                self.contents5.SetValue('completed !!!')
                break
            j += 1
            self.gauge1.SetValue(count) 
            
        return [t, area, weight]
        
if __name__ == '__main__':
    
    app = wx.App(False)
    frame = Main_test2(None)
    frame.Show(True)
    app.MainLoop()