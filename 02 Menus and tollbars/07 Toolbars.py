'''

In this example, we create two horizontal
toolbars.

'''

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('new.png'))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('open.png'))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('save.png'))
        toolbar1.Realize()


        toolbar2 = wx.ToolBar(self)
        qtool = toolbar2.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('texit.png'))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSizer(vbox)

        self.SetSize((300, 250))
        self.SetTitle('Toolbars')
        self.Center()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()



def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
