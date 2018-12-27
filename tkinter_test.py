import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("tkinter test")

sw = root.winfo_screenwidth()
#得到屏幕宽度
sh = root.winfo_screenheight()
#得到屏幕高度
ww = 600
wh = 400
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))


def callback():
	print('click!')
	tk.messagebox._show("you clicked!","hello")
	#最普通的返回操作，按钮返回一个值（通过一个函数传递）

labelHello = tk.Label(root, text = "Hello Tkinter!")
button1 = tk.Button(root,text ="this is a button")
b=tk.Button(root,text='OK',command=callback)



labelHello.pack()
button1.pack()
b.pack()


root.mainloop()