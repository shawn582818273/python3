import wx 
import time 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (300,200))  
      self.InitUI() 
         
   def InitUI(self):    
      self.count = 0 
      pnl = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL)
		
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		
      self.gauge = wx.Gauge(pnl, range = 20, size = (250, 25), style =  wx.GA_HORIZONTAL) 
      self.btn1 = wx.Button(pnl, label = "Start") 
      self.Bind(wx.EVT_BUTTON, self.OnStart, self.btn1) 
		
      hbox1.Add(self.gauge, proportion = 1, flag = wx.ALIGN_CENTRE) 
      hbox2.Add(self.btn1, proportion = 1, flag = wx.RIGHT, border = 10) 
         
      vbox.Add((0, 30)) 
      vbox.Add(hbox1, flag = wx.ALIGN_CENTRE) 
      vbox.Add((0, 20)) 
      vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_CENTRE) 
      pnl.SetSizer(vbox) 
         
      self.SetSize((300, 200)) 
      self.Centre() 
      self.Show(True)   
		
   def OnStart(self, e): 
      while True: 
         time.sleep(0.5); 
         self.count = self.count + 1 
         self.gauge.SetValue(self.count) 
			
         if self.count >= 20: 
            print ("end")
            return 
				
ex = wx.App() 
Mywin(None,'wx.Gauge - www.yiibai.com') 
ex.MainLoop()