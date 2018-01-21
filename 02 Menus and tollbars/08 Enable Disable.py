'''

In this example, we create two horizontal
toolbars.

'''

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.count = 5
        self.toolbar = self.CreateToolBar()

        self.InitUI()


    def InitUI(self):

        tundo = self.toolbar.AddLabelTool(wx.ID_UNDO, '', wx.Bitmap('tundo.png'))
        tredo = self.toolbar.AddLabelTool(wx.ID_REDO, '', wx.Bitmap('tredo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('texit.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit,texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo,tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo,tredo)

        self.SetSize((300, 250))
        self.SetTitle('Undo redo')
        self.Center()
        self.Show(True)

    def OnUndo(self, e):
        if 1< self.count <= 5:
            self.count = self.count -1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if 1<= self.count < 5:
            self.count = self.count +1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, e):
        self.Close()



def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
