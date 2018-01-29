import wx


class MyWindow(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.color = '#b3b3b3'

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

        self.count = 0

    def OnPaint(self, e):
        self.count += 1
        print(str(id(self)) + " paint ... " + str(self.count))

        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, e):
        self.Refresh()

    def OnSetFocus(self, e):
        self.color = '#0099f7'
        self.Refresh()

    def OnKillFocus(self, e):
        self.color = '#b3b3b3'
        self.Refresh()


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.LEFT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.RIGHT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.LEFT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 9)])

        self.SetSizer(grid)

        self.SetSize((350, 250))
        self.SetTitle('Focus event')
        self.Centre()
        self.Show(True)


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()