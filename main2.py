import wx

import images


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="peanuts", pos=(500,200), size=(330,630))
        panel = wx.Panel(self)
        topLbl = wx.StaticText(panel, -1, "PEANUTS")


    def EvtOnClickClose(self, event):
        self.Close(True)

    def EvtOnClickCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
