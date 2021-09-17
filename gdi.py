from win32gui import *
from win32ui import *
from win32con import *
from win32api import *
from time import *
from tkinter import *
from random import randint
import win32api, win32con, win32gui, win32ui



def ex1():
    for x in range(0,40):
        hwnd = GetDesktopWindow()
        hdc = GetWindowDC(hwnd)
        desk = GetDC(0)
        x = GetSystemMetrics(SM_CXSCREEN)
        y = GetSystemMetrics(SM_CXSCREEN)
        BitBlt(desk,randint(0,x), randint(0,10),randint(0,x),randint(0,y),desk,randint(0,10), randint(0,100), 0x98123c)
        PatBlt(desk,0,0,randint(0,x),randint(0,y),PATINVERT)
        BitBlt(hdc,0x00660046); 

        ReleaseDC(hwnd,hd)
        sleep(.1)

def ex2():
    dc = win32gui.GetDC(0)
    red = win32api.RGB(255, 0, 0)
    win32gui.SetPixel(dc, 0, 400, red)  # draw red at 0,0


def ex3():
    import tkinter, win32api, win32con, pywintypes

    label = tkinter.Label(text='Python is cool!', font=('Times New Roman','80'), fg='black', bg='white')
    label.master.overrideredirect(True)
    label.master.geometry("+250+250")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")
    
    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
    
    label.pack()
    label.mainloop()

def ex4():
    import win32gui, win32ui
    from win32api import GetSystemMetrics
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0,0))
    monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
    
    while True:
        m = win32gui.GetCursorPos()
        dcObj.Rectangle((m[0], m[1], m[0]+30, m[1]+30))
        win32gui.InvalidateRect(hwnd, monitor, True) 

def p3():
    pass



#ex1()
#ex2()
#writer()
#trial()
#p3()
