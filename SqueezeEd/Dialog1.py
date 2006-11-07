#Boa:Dialog:newRoomDialog

import wx
import Frame1
def create(parent):
    return newRoomDialog(parent)

[wxID_NEWROOMDIALOG, wxID_NEWROOMDIALOGNEWROOMDONEBTN, 
 wxID_NEWROOMDIALOGROOMDESCLBL, wxID_NEWROOMDIALOGROOMNAMELBL, 
 wxID_NEWROOMDIALOGROOMNAMETXT, wxID_NEWROOMDIALOGTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class newRoomDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_NEWROOMDIALOG, name='newRoomDialog',
              parent=prnt, pos=wx.Point(273, 105), size=wx.Size(509, 472),
              style=wx.DEFAULT_DIALOG_STYLE, title='New Room')
        self.SetClientSize(wx.Size(501, 438))
        self.Show(True)

        self.roomNameLbl = wx.StaticText(id=wxID_NEWROOMDIALOGROOMNAMELBL,
              label='Room Name:', name='roomNameLbl', parent=self,
              pos=wx.Point(8, 16), size=wx.Size(70, 14), style=0)
        self.roomNameLbl.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.roomNametxt = wx.TextCtrl(id=wxID_NEWROOMDIALOGROOMNAMETXT,
              name='roomNametxt', parent=self, pos=wx.Point(88, 16),
              size=wx.Size(288, 21), style=0, value='')

        self.roomDescLbl = wx.StaticText(id=wxID_NEWROOMDIALOGROOMDESCLBL,
              label='Description', name='roomDescLbl', parent=self,
              pos=wx.Point(16, 64), size=wx.Size(60, 14), style=0)
        self.roomDescLbl.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.textCtrl1 = wx.TextCtrl(id=wxID_NEWROOMDIALOGTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(88, 64),
              size=wx.Size(288, 200), style=0, value='')

        self.newRoomDoneBtn = wx.Button(id=wxID_NEWROOMDIALOGNEWROOMDONEBTN,
              label='Done', name='newRoomDoneBtn', parent=self,
              pos=wx.Point(192, 280), size=wx.Size(75, 23), style=0)
        self.newRoomDoneBtn.Bind(wx.EVT_LEFT_UP, self.OnNewRoomDoneBtnLeftUp)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnNewRoomDoneBtnLeftUp(self, event):
        event.Skip()
