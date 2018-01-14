# size.py

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(250, 200))

        self.Move((800, 250))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')

    app.MainLoop()


