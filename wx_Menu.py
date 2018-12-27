import wx  

class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title, size = (400,300))  
      self.InitUI() 
         
   def InitUI(self):    
      menubar = wx.MenuBar() 
            
      fileMenu = wx.Menu() 
      newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "New",kind = wx.ITEM_NORMAL) 
      newitem.SetBitmap(wx.Bitmap("new.bmp")) 
      fileMenu.Append(newitem) 
            
      fileMenu.AppendSeparator()
            
      editMenu = wx.Menu() 
      copyItem = wx.MenuItem(editMenu, 100,text = "copy",kind = wx.ITEM_NORMAL)
      copyItem.SetBitmap(wx.Bitmap("copy.bmp")) 
            
      editMenu.Append(copyItem) 
      cutItem = wx.MenuItem(editMenu, 101,text = "cut",kind = wx.ITEM_NORMAL) 
      cutItem.SetBitmap(wx.Bitmap("cut.bmp")) 
            
      editMenu.Append(cutItem) 
      pasteItem = wx.MenuItem(editMenu, 102,text = "paste",kind = wx.ITEM_NORMAL) 
      pasteItem.SetBitmap(wx.Bitmap("paste.bmp")) 
            
      editMenu.Append(pasteItem) 
      fileMenu.Append(wx.ID_EDIT, "Edit", editMenu) 
      fileMenu.AppendSeparator() 
         
      radio1 = wx.MenuItem(fileMenu, 200,text = "Radio1",kind = wx.ITEM_RADIO) 
      radio2 = wx.MenuItem(fileMenu, 300,text = "radio2",kind = wx.ITEM_RADIO) 
            
      fileMenu.Append(radio1) 
      fileMenu.Append(radio2) 
      fileMenu.AppendSeparator() 
         
      fileMenu.AppendCheckItem(103,"Checkable") 
      quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
            
      fileMenu.Append(quit) 
      menubar.Append(fileMenu, '&File') 
            
      self.SetMenuBar(menubar) 
      self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
      self.Bind(wx.EVT_MENU, self.menuhandler) 
      self.SetSize((350, 250)) 
      self.Centre() 
      self.Show(True)
            
   def menuhandler(self, event): 
      id = event.GetId() 
      if id == wx.ID_NEW: 
         self.text.AppendText("new"+"\n")
                  
ex = wx.App() 
Mywin(None,'MenuBar Demo - yiibai.com') 
ex.MainLoop() 