import wx 
 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (400,300))  
      self.InitUI() 
         
   def InitUI(self):    
      pnl = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
		
      self.sld = wx.Slider(pnl, value = 10, minValue = 1, maxValue = 100,
         style = wx.SL_HORIZONTAL|wx.SL_LABELS) 
			
      vbox.Add(self.sld,1,flag = wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border = 20) 
      self.sld.Bind(wx.EVT_SLIDER, self.OnSliderScroll) 
      self.txt = wx.StaticText(pnl, label = 'Yiibai.com',style = wx.ALIGN_CENTER)                
      vbox.Add(self.txt,1,wx.ALIGN_CENTRE_HORIZONTAL) 
		
      pnl.SetSizer(vbox) 
      self.Centre() 
      self.Show(True)      
		
   def OnSliderScroll(self, e): 
      obj = e.GetEventObject() 
      val = obj.GetValue() 
      font = self.GetFont() 
      #font.SetTutorialsSize(self.sld.GetValue()) 
      self.txt.SetFont(font) 
		
ex = wx.App() 
Mywin(None,'Slider Demo - www.yiibai.com') 
ex.MainLoop() 