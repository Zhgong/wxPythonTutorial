import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        wx.StaticText(self, label='Convert Fahrenheit temperature to Celsius',
                      pos=(20, 20))
        wx.StaticText(self, label='Fahrenheit: ', pos=(20, 80))
        wx.StaticText(self, label='Celsius: ', pos=(20, 150))

        self.celsius = wx.StaticText(self, label='', pos=(150, 150))
        self.sc = wx.SpinCtrl(self, value='0', pos=(150, 75), size=(60, -1))
        self.sc.SetRange(-459, 1000)

        btn = wx.Button(self, label='Compute', pos=(70, 230))
        btn.SetFocus()
        cbtn = wx.Button(self, label='Close', pos=(185, 230))

        self.sc.Bind(wx.EVT_SPINCTRL, self.OnCompute)
        self.sc.Bind(wx.EVT_TEXT, self.OnCompute)

        btn.Bind(wx.EVT_BUTTON, self.OnCompute)
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((350, 310))
        self.SetTitle('wx.SpinCtrl')
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        self.Close(True)

    def OnCompute(self, e):
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()