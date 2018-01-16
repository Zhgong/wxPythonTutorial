'''
In this example, we create a submenu and a menu
separator.

'''


import wx

APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shst = None
        self.shst1 = None
        self.toolbar = None
        self.statusbar = None

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar',
                                    'Show Statusbar', kind = wx.ITEM_CHECK)

        self.shst1 = viewMenu.Append(wx.ID_ANY, 'Show toolbar',
                                    'Show Toolbar', kind = wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shst1.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shst1)

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(1, '', wx.Bitmap('texit.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')


        self.SetSize((350, 250))
        self.SetTitle('Check menu item')
        self.Centre()
        self.Show(True)

    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shst1.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()


    def OnQuit(self, e):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
