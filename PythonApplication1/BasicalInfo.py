import wx
import sqlite3
import loginPanel
import registerPanel

conn = sqlite3.connect('F:\sqlitedb\studydb.db')
cursor = conn.cursor()


class userDetailCollection(wx.Frame):
    def __init__(self, parent, id):
        list1 = ["Male", "Female", "SECRET"]
        frame = wx.Frame.__init__(self, parent, id, title="Set basical detail", pos=(500, 250), size=(600, 500))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="Basical data for new employee", pos=(200, 20))
        self.label_name = wx.StaticText(panel, label="Name:", pos=(50, 50))
        self.text_Name = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_gender = wx.StaticText(panel, label="Gender:", pos=(50, 90))
        self.check_gender = wx.ListBox(panel, -1, choices=list1, style=wx.LB_SINGLE, pos=(100, 90), size=(150, 50))
        self.label_age = wx.StaticText(panel, label="age:", pos=(50, 160))
        self.text_age = wx.TextCtrl(panel, pos=(100, 160), size=(235, 25), style=wx.TE_LEFT)
        self.label_department = wx.StaticText(panel, label="department:", pos=(30, 200))
        self.text_department = wx.TextCtrl(panel, pos=(100, 200), size=(235, 25), style=wx.TE_LEFT)
        self.label_address = wx.StaticText(panel, label="address:", pos=(40, 240))
        self.text_address = wx.TextCtrl(panel, pos=(100, 240), size=(235, 25), style=wx.TE_LEFT)
        self.label_dob = wx.StaticText(panel, label="DOB:", pos=(50, 280))
        self.text_dob = wx.TextCtrl(panel, pos=(100, 280), size=(235, 25), style=wx.TE_LEFT)
        self.bt_submit = wx.Button(panel, label='Submit', pos=(105, 320))
        self.bt_cancel = wx.Button(panel, label='Cancel', pos=(195, 320))
        self.bt_resit = wx.Button(panel, label='Resit', pos=(285, 320))
        self.bt_submit.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        self.bt_resit.Bind(wx.EVT_BUTTON, self.OnclickResit)
        self.check_gender.Bind(wx.EVT_LISTBOX, self.OnclickSubmit, id=34)

    def OnclickCancel(self, event):
        self.Close()

    def OnclickResit(self, event):
        self.text_age.SetValue("")
        self.text_dob.SetValue("")
        self.text_Name.SetValue("")
        self.text_apartment.SetValue("")
        self.text_address.SetValue("")

    def OnclickSubmit(self, event):

        cursor.execute("SELECT user,password from user")

       # username=loginPanel.tem
        name = self.text_Name.GetValue()
        gender = self.check_gender.GetStringSelection()
        age = int(self.text_age.GetValue())
        department = self.text_department.GetValue()
        address = self.text_address.GetValue()
        dob = self.text_dob.GetValue()
        try:
            cursor.execute("INSERT INTO userDetail(userNum,Name,Gender,Age,department,Address,DOB) VALUES('%s','%s','%s','%d','%s','%s',%s);" % (registerPanel.temp,name, gender, age, department, address, dob))
            self.Close()
        except:
            message = "error"
        else:
            conn.commit()
            cursor.close()
            conn.close()
            message = "successful"
        wx.MessageBox(message)

def open():
    app = wx.App()
    t = userDetailCollection(parent=None, id=34)
    t.Show()
    app.MainLoop()



    app = wx.App()
    t = userDetailCollection(parent=None, id=34)
    t.Show()
    app.MainLoop()
