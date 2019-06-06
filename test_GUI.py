# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:52:23 2018

@author: Administrator
"""
import wx
import gui_demo

class CalcFrame(gui_demo.MyFrame1):
    def __init__(self, parent):
        gui_demo.MyFrame1.__init__(self,parent)
        
    def FindSquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num**2))

	
app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 

app.MainLoop() 