import wx
import threading
import time
 
def do_stuff(dialog): # put your logic here
 for i in range(101):
  wx.CallAfter(dialog.Update, i)
  time.sleep(0.1)
 wx.CallAfter(dialog.Destroy)
 
def start(func, *args): # helper method to run a function in another thread
 thread = threading.Thread(target=func, args=args)
 thread.setDaemon(True)
 thread.start()
 
def main():
 app = wx.App()
 dialog = wx.ProgressDialog('Doing Stuff', 'Please wait...')
 start(do_stuff, dialog)
 dialog.ShowModal()
 app.MainLoop()
 
if __name__ == '__main__':
 main()

