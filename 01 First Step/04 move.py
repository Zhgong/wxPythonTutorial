# size.py

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((300,200))
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    window = Example(None, title='Move')
    app.MainLoop()


