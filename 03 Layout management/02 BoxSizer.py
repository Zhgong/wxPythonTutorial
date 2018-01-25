# absolute.py

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title,
                         size=(260, 180))

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self, -1)

        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)


if __name__ == '__main__':

    app = wx.App()
    Example(None, title='Absolute')
    app.MainLoop()
