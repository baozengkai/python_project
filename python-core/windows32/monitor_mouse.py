#-*- coding:utf-8
import pyHook
import pythoncom
import win32gui
import win32con
import win32com.client
import win32api

import win32process
import win32clipboard
import win32gui_struct
import winnt
import shutil
import struct
import platform

"""
    例子:
        1.监控鼠标点击事件
        2.遍历控件内容
        3.遍历窗口子窗口，并获取Edit中内容
        4.更新Edit中内容
        5.获取子窗体的位置信息
        6.获取菜单栏的子菜单栏个数
        7.获取菜单栏的子菜单栏信息
"""
# 例7 获取某个子菜单 某个菜单项的内容
def GetMenuItemString(id):
    pHandle = win32gui.FindWindow(None, u"test - 记事本")
    menuHandle = win32gui.GetMenu(pHandle)
    menuSubHandle = win32gui.GetSubMenu(menuHandle, 0)

    buf, extra = win32gui_struct.EmptyMENUITEMINFO()
    win32gui.GetMenuItemInfo(menuSubHandle, id, True, buf)
    fType,fState, wID, hSubMenu, hbmpChecked, hbmpUnchecked, dwItemData, text, hbmpItem = win32gui_struct.UnpackMENUITEMINFO(buf)
    print text.decode("gbk").encode("UTF-8")
    print fType
    print fState
    return text

# 例1
def onMouseEvent(event):
    """
    监控鼠标点击事件,并判断此时的菜单项状态
    """
    left, top, right, bottom = win32gui.GetWindowRect(event.Window)
    if event.MessageName == "mouse left down":
        print "MessageName:", event.MessageName
        print "window", event.Window
        if event.WindowName:
            print "WindowName", event.WindowName.decode("gbk").encode("UTF-8")
        else:
            print "WindowName", event.WindowName
        print "Position", event.Position
        print "Left", left
        print "Wheel", event.Wheel  #当滑轮使用的时候
        print "Injected", event.Injected #当该事件是编程产生的时候
        print "---------------------------------------------------"

        GetMenuItemString(0)
    return True

if __name__ == '__main__':
    hookmanager = pyHook.HookManager()
    hookmanager.MouseAllButtonsDown = onMouseEvent
    hookmanager.HookMouse()
    pythoncom.PumpMessages()


# 例子2:
#   遍历控件内容
# def findWindow(pHandle):
#     handle = win32gui.FindWindowEx(pHandle, 0, None, None)
#     while handle !=0:
#         print(handle,win32gui.GetClassName(handle), win32gui.GetDlgCtrlID(handle))
#         handle = win32gui.FindWindowEx(pHandle,handle,None,None)
#
#         print(handle,win32gui.GetClassName(handle), win32gui.GetDlgCtrlID(handle))
#         buffer = '0' * 50
#         len = win32gui.SendMessage(handle, win32con.WM_GETTEXTLENGTH) + 1  # 获取edit控件文本长度
#         win32gui.SendMessage(handle, win32con.WM_GETTEXT, len, buffer)  # 读取文本
#         print buffer[:len - 1]
#         handle = win32gui.FindWindowEx(pHandle,handle,None,None)
#
# findWindow(win32gui.FindWindow(None, u"test - 记事本"))

# 例子3:
#     更新Edit控件内容
# def set_message(pHandle):
#     handle = win32gui.FindWindowEx(pHandle,0,'Edit',None)
#     while handle != 0:
#         print(handle, win32gui.GetClassName(handle), win32gui.GetDlgCtrlID(handle))
#         win32gui.SendMessage(handle, win32con.WM_SETTEXT,None,"666")
#         win32gui.SendMessage(win32con.HEIGHT)
# set_message(win32gui.FindWindow(None, u"test - 记事本"))

# 例4 获取子窗体位置信息
# def childWindow(pHandle):
#     left,top,right,bottom = win32gui.GetWindowRect(pHandle)
#     print("main left: ", left)
#     print("main left: ", top)
#     print("main left: ", right)
#     print("main left: ", bottom)
#     print
#     handle = win32gui.FindWindowEx(pHandle,0,'Edit',None)
#     cleft, ctop, cright, cbottom = win32gui.GetWindowRect(handle)
#     print("edit left: ", cleft)
#     print("edit left: ", left)
#     print("edit left: ", left)
#     print("edit left: ", left)
#     print
#
#     handle = win32gui.FindWindowEx(pHandle,0,'msctls_statusbar32',None)
#     cleft, ctop, cright, cbottom = win32gui.GetWindowRect(handle)
#     print("bar left: ", cleft)
#     print("bar left: ", left)
#     print("bar left: ", left)
#     print("bar left: ", left)
#
#
#
# childWindow(win32gui.FindWindow(None, u"无标题 - 记事本"))

# 例6 获取菜单栏元素
#   6.1 获取子菜单栏 菜单项的个数
# def GetMenuCount(pHandle):
#     menuHandle = win32gui.GetMenu(pHandle)
#     menuSubHandle = win32gui.GetSubMenu(menuHandle,0)
#
#     count = win32gui.GetMenuItemCount(menuSubHandle)
#     print count
#     # GetMenuItemString(0)
#     if menuHandle != 0:
#         print(menuHandle)
#
# GetMenuCount(win32gui.FindWindow(None, u"python-core - [C:\\baozengkai\git\python_project\python-core] - ...\windows32\monitor_mouse.py - PyCharm 2017.2"))

