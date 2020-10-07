import wx
import sqlite3
import loginPanel
import BasicalInfo

conn = sqlite3.connect('F:\sqlitedb\studydb.db')
cursor = conn.cursor()

class reg(wx.Frame):
    def __init__(self, parent, id, title="INTERVIEW SYSTEM", pos=(100, 100), size=(400, 400)):
        frame = wx.Frame.__init__(self, parent, id, title="REGISTER SYSTEM", pos=(500, 250), size=(400, 300))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="New user register", pos=(130, 20))
        self.label_user = wx.StaticText(panel, label="Username:", pos=(35, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label="Password:", pos=(35, 90))
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)
        self.bt_regist = wx.Button(panel, label='regist', pos=(105, 130))
        self.bt_cancel = wx.Button(panel, label='cancel', pos=(195, 130))
        self.bt_regist.Bind(wx.EVT_BUTTON, self.OnclickReg)
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)

    def OnclickReg(self, event):
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        if username == "" or password == "":
            message = "Can not process empty"
        else:
            try:
                cursor.execute("INSERT INTO user(user,password) VALUES('%s','%s');" % (username, password))
            except:
                message = "error"
            else:
                conn.commit()
                cursor.close()
                conn.close()
                self.Close()
                BasicalInfo.open()
                message = "successful"
        wx.MessageBox(message)
        self.Close()
        loginPanel.reOpen()

    def OnclickCancel(self, event):
        self.Close()
        loginPanel.reOpen()


def re():
    app = wx.App()
    re = reg(parent=None, id=5)
    re.Show()
    app.MainLoop()
    print(re.text_user.GetValue())
if __name__ == '__main__':
    re()