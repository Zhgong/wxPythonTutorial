import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, 'Exit', (10, 10))
        runButton = wx.Button(pnl, wx.ID_ANY, 'Run', (100, 10))

        self.Bind(wx.EVT_BUTTON, self.OnExit, id=exitButton.GetId())
        # self.Bind(wx.EVT_BUTTON, self.OnExit)

        self.SetTitle("Automatic id")
        self.Centre()
        self.Show(True)

    def OnExit(self, event):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()