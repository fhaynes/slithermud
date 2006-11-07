#Boa:Frame:Frame1

import wx
import sys

import Dialog1

sys.path.append("C:\\Slither\\")
import MudRoom
zone = None
rooms = {}
portals = {}

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1SCROLLEDWINDOW1, wxID_FRAME1STATUSBAR1, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_FRAME1MNUFILENEWZONE, wxID_FRAME1MNUFILEQUIT, 
 wxID_FRAME1MNUFILESAVEZONE, 
] = [wx.NewId() for _init_coll_mnuFile_Items in range(3)]

[wxID_FRAME1MNUHELPHELP] = [wx.NewId() for _init_coll_mnuHelp_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.mnuFile, title='File')
        parent.Append(menu=self.mnuHelp, title='Help')

    def _init_coll_mnuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MNUFILENEWZONE,
              kind=wx.ITEM_NORMAL, text='New Zone')
        parent.Append(help='', id=wxID_FRAME1MNUFILESAVEZONE,
              kind=wx.ITEM_NORMAL, text='Save Zone')
        parent.Append(help='', id=wxID_FRAME1MNUFILEQUIT, kind=wx.ITEM_NORMAL,
              text='Quit')
        self.Bind(wx.EVT_MENU, self.OnMnuFileSavezoneMenu,
              id=wxID_FRAME1MNUFILESAVEZONE)
        self.Bind(wx.EVT_MENU, self.OnMnuFileQuitMenu,
              id=wxID_FRAME1MNUFILEQUIT)
        self.Bind(wx.EVT_MENU, self.OnMnuFileNewzoneMenu,
              id=wxID_FRAME1MNUFILENEWZONE)

    def _init_coll_mnuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MNUHELPHELP, kind=wx.ITEM_NORMAL,
              text='Help')
        self.Bind(wx.EVT_MENU, self.OnMnuHelpHelpMenu,
              id=wxID_FRAME1MNUHELPHELP)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text='Status')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.mnuFile = wx.Menu(title='')

        self.mnuHelp = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_mnuFile_Items(self.mnuFile)
        self._init_coll_mnuHelp_Items(self.mnuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(465, 231), size=wx.Size(288, 272),
              style=wx.DEFAULT_FRAME_STYLE, title='Squeeze Editor')
        self._init_utils()
        self.SetClientSize(wx.Size(280, 238))
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_FRAME1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(280, 195), style=wx.HSCROLL | wx.VSCROLL)
        self.scrolledWindow1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.scrolledWindow1.Bind(wx.EVT_LEFT_DOWN,
              self.OnScrolledWindow1LeftDown)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnMnuHelpHelpMenu(self, event):
        event.Skip()

    def OnMnuFileSavezoneMenu(self, event):
        event.Skip()

    def OnMnuFileQuitMenu(self, event):
        event.Skip()

    def OnMnuFileNewzoneMenu(self, event):
        event.Skip()

    def OnScrolledWindow1LeftDown(self, event):
        Dialog1.newRoomDialog(self).ShowModal
