# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 664,467 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Load Temperature...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Load CO2 Concentration...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Load Lightintensity...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Load All...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menu11 = wx.Menu()
		self.m_menuItem11 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Tomato", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem11 )
		
		self.m_menu11.AppendSeparator()
		
		self.m_menuItem12 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem12 )
		
		self.m_menu1.AppendSubMenu( self.m_menu11, u"Select Species" )
		
		self.m_menubar1.Append( self.m_menu1, u"Input" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menu21 = wx.Menu()
		self.m_menuItem13 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Show Overall Changes With Time", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem13 )
		
		self.m_menu21.AppendSeparator()
		
		self.m_menuItem14 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Show Changes of Spatial Distribution With Time ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem14 )
		
		self.m_menu2.AppendSubMenu( self.m_menu21, u"Leaf Area" )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem15 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Show Overall Changes With Time", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem15 )
		
		self.m_menu5.AppendSeparator()
		
		self.m_menuItem16 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Show Changes of Spatial Distribution With Time ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem16 )
		
		self.m_menu2.AppendSubMenu( self.m_menu5, u"Leaf Weight" )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menu6 = wx.Menu()
		self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Show Changes of Fruit Number With Time ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem17 )
		
		self.m_menu6.AppendSeparator()
		
		self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Show Changes of Fruit Spatial Distribution With Time ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem18 )
		
		self.m_menu2.AppendSubMenu( self.m_menu6, u"Fruit" )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem7 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Save All Outputs", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem7 )
		
		self.m_menubar1.Append( self.m_menu2, u"Output" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Execute", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem8 )
		
		self.m_menu3.AppendSeparator()
		
		self.m_menuItem9 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem9 )
		
		self.m_menubar1.Append( self.m_menu3, u"3D Visualization" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem10 )
		
		self.m_menubar1.Append( self.m_menu4, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		fgSizer1 = wx.FlexGridSizer( 5, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Daily Temperayure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.contents1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.contents1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Daily CO2 Concentration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.contents2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.contents2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Daily Lightintensity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.contents3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.contents3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Species", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.contents4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.contents4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Simulation", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 400,-1 ), wx.GA_HORIZONTAL )
		self.gauge1.SetValue( 0 ) 
		fgSizer1.Add( self.gauge1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.contents5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		fgSizer1.Add( self.contents5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.Openfile1, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.Openfile2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.Openfile3, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.Openfile5, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.Openfile4, id = self.m_menuItem11.GetId() )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Openfile1 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.Openfile2 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.Openfile3 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.Openfile4 )
		self.m_button21.Bind( wx.EVT_BUTTON, self.Simulation )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Openfile1( self, event ):
		event.Skip()
	
	def Openfile2( self, event ):
		event.Skip()
	
	def Openfile3( self, event ):
		event.Skip()
	
	def Openfile5( self, event ):
		event.Skip()
	
	def Openfile4( self, event ):
		event.Skip()
	
	
	
	
	
	def Simulation( self, event ):
		event.Skip()
	

