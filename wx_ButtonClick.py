#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import gSizerDemo
# 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
class MianWindow(gSizerDemo.gSizerDemo):
    # 咱们给个初始化函数，将文本框初始填有‘主窗口测试’几个字
    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        self.m_textCtrl2.SetValue('world')
        self.Bind(wx.EVT_BUTTON,self.m_button1OnButtonClick,self.m_button1)
        self.Title= "my wx test哈哈"
    # 将点击按钮清空文本框的,功能写成函数
    def m_button1OnButtonClick(self,event):
        self.m_textCtrl2.Clear()
if __name__ == '__main__':
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = MianWindow(None)
    main_win.init_main_window()
    
    main_win.Show()
    app.MainLoop()