# -*- coding: gbk -*-
import threading
from unittest import *
import os
import time as t

import wx
import wx.lib.agw.customtreectrl as CT
import wx.lib.delayedresult as delayedresult

import var as v
import common as co
import images
import data
import testcase as tc
import sendmail as sm
import memmonitor as mm
# ----------------------------------------------------------------------------


def getNextImageID(count):
    imID = 0
    while True:
        yield imID
        imID += 1
        if imID == count:
            imID = 0


class ToolBook(wx.Toolbook):
    def __init__(self, parent, id):
        wx.Toolbook.__init__(self, parent, id, style=
        wx.BK_DEFAULT
                             ####                             | wx.BK_TOP
                             ####                             | wx.BK_BOTTOM
                             ####                             | wx.BK_LEFT
                             ####                             | wx.BK_RIGHT
                             )

        # make an image list using the LBXX images
        il = wx.ImageList(120, 50)
        for x in range(4):
            obj = getattr(images, 'LB%02d' % (x + 1))
            bmp = obj.GetBitmap()
            il.Add(bmp)
        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())

        # Now make a bunch of panels for the list book        
        for tool in v.TOOL_LIST:
            if tool == v.TOOL_LIST[0]:
                page1 = GeneralPage(self)
                self.AddPage(page1, tool, imageId=imageIdGenerator.next())

            elif tool == v.TOOL_LIST[1]:
                page2 = MemoryTrackPage(self)
                self.AddPage(page2, tool, imageId=imageIdGenerator.next())

            elif tool == v.TOOL_LIST[2]:
                page3 = LogCollectionPage(self)
                self.AddPage(page3, tool, imageId=imageIdGenerator.next())

            elif tool == v.TOOL_LIST[3]:
                page4 = TestSuitePage(self)
                self.AddPage(page4, tool, imageId=imageIdGenerator.next())

        self.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGING, self.OnPageChanging)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()


class GeneralPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.BORDER_STATIC)

        # change text event
        self.Bind(wx.EVT_TEXT, self.EvtTextChange)

        # btn ctrl n box
        self.saveBtn = wx.Button(self, -1, 'Save')
        self.cancelBtn = wx.Button(self, -1, 'Cancel')

        self.Bind(wx.EVT_BUTTON, self.EvtSave, self.saveBtn)
        self.Bind(wx.EVT_BUTTON, self.EvtClose, self.cancelBtn)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(self.saveBtn, 0, wx.LEFT, 400)
        btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)

        # DUT connection ctrl
        typeLbl = wx.StaticText(self, -1, 'Device:')
        self.type = wx.Choice(self, -1, choices=['R1D', 'R2D', 'R1CM'])
        self.type.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.type)

        connLbl = wx.StaticText(self, -1, "Connection type:")
        self.conn = wx.Choice(self, -1, choices=["SSH", "Telnet", "fac"])
        self.conn.SetSelection(1)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice3, self.conn)

        ipLbl = wx.StaticText(self, -1, 'IP:')
        self.ip = wx.TextCtrl(self, -1, '')
        self.ip.SetValue(v.HOST)

        sshUsrLbl = wx.StaticText(self, -1, 'User:')
        self.sshUsr = wx.TextCtrl(self, -1, '')
        self.sshUsr.SetValue(v.USR)

        sshPasswdLbl = wx.StaticText(self, -1, 'Password:')
        self.sshPasswd = wx.TextCtrl(self, -1, '')
        self.sshPasswd.SetValue(v.PASSWD)

        # DUT connection box
        connBox = wx.StaticBox(self, -1, 'DUT', size=(580, -1))
        connSizer = wx.StaticBoxSizer(connBox, wx.HORIZONTAL)
        # left column
        connSizer2 = wx.BoxSizer(wx.VERTICAL)
        connSizer2.Add(typeLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        connSizer2.Add(ipLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        connSizer2.Add(sshUsrLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        connSizer2.Add(sshPasswdLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT | wx.BOTTOM, 10)

        connSizer3 = wx.BoxSizer(wx.VERTICAL)
        connSizer3.Add(self.type, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 2)
        connSizer3.Add(self.ip, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        connSizer3.Add(self.sshUsr, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        connSizer3.Add(self.sshPasswd, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)

        # right column
        connSizer4 = wx.BoxSizer(wx.VERTICAL)
        connSizer4.Add(connLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)

        connSizer5 = wx.BoxSizer(wx.VERTICAL)
        connSizer5.Add(self.conn, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 2)

        connSizer.Add(connSizer2, 0, wx.LEFT, 5)
        connSizer.Add(connSizer3, 0, wx.LEFT, 2)
        connSizer.Add(connSizer4, 0, wx.LEFT, 10)
        connSizer.Add(connSizer5, 0, wx.LEFT, 2)

        # sta connection ctrl
        staTypeLbl = wx.StaticText(self, -1, 'Device:')
        self.staType = wx.Choice(self, -1, choices=['Android', 'R1CM & Android'])
        self.staType.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.staType)

        staIpLbl = wx.StaticText(self, -1, 'IP:')
        self.staIp = wx.TextCtrl(self, -1, '')
        self.staIp.Enable(False)
        self.staIp.SetValue(v.STA_IP)

        staSshUsrLbl = wx.StaticText(self, -1, 'User:')
        self.staSshUsr = wx.TextCtrl(self, -1, '')
        self.staSshUsr.Enable(False)
        self.staSshUsr.SetValue(v.STA_USR)

        staSshPasswdLbl = wx.StaticText(self, -1, 'Password:')
        self.staSshPasswd = wx.TextCtrl(self, -1, '')
        self.staSshPasswd.Enable(False)
        self.staSshPasswd.SetValue(v.STA_PASSWD)

        # sta connection box
        staConnBox = wx.StaticBox(self, -1, 'STA', size=(580, -1))
        staConnSizer = wx.StaticBoxSizer(staConnBox, wx.HORIZONTAL)

        staConnSizer2 = wx.BoxSizer(wx.VERTICAL)
        staConnSizer2.Add(staTypeLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        staConnSizer2.Add(staIpLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        staConnSizer2.Add(staSshUsrLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        staConnSizer2.Add(staSshPasswdLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT | wx.BOTTOM, 10)

        staConnSizer3 = wx.BoxSizer(wx.VERTICAL)
        staConnSizer3.Add(self.staType, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 2)
        staConnSizer3.Add(self.staIp, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        staConnSizer3.Add(self.staSshUsr, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        staConnSizer3.Add(self.staSshPasswd, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)

        staConnSizer.Add(staConnSizer2, 0, wx.LEFT, 5)
        staConnSizer.Add(staConnSizer3, 0, wx.LEFT, 2)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(connSizer, 0, wx.ALL, 10)
        mainSizer.Add(staConnSizer, 0, wx.ALL, 10)
        mainSizer.Add(btnSizer, 0, wx.TOP, 40)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    def EvtChoice(self, event):
        v.DUT_MODULE = event.GetString()

    def EvtChoice2(self, event):
        v.STA_MODULE = event.GetString()
        if v.STA_MODULE == "Android":
            self.staIp.Enable(False)
            self.staSshUsr.Enable(False)
            self.staSshPasswd.Enable(False)
        elif v.STA_MODULE == "R1CM & Android":
            self.staIp.Enable(True)
            self.staSshUsr.Enable(True)
            self.staSshPasswd.Enable(True)

    def EvtChoice3(self, event):
        type = event.GetString()
        self.sshUsr.Enable(True)
        self.sshPasswd.Enable(True)
        if type == "Telnet":
            v.CONNECTION_TYPE = 2
        elif type == "SSH":
            v.CONNECTION_TYPE = 1
        elif type == "fac":
            v.CONNECTION_TYPE = 2
            self.sshUsr.Enable(False)
            self.sshUsr.SetValue("")
            self.sshPasswd.Enable(False)
            self.sshPasswd.SetValue("")

    def connectionCheckThread(self, connectiontype, ip=None, port=None, user=None, password=None):
        result = co.connectionCheck(connectiontype, ip=ip, user=user, password=password)
        if result:
            self.flag += 1
        else:
            return

    def EvtSave(self, event):
        deviceNum = 0
        self.flag = 0

        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D" or v.DUT_MODULE == "R1CM":
            deviceNum += 1
            v.HOST = self.ip.GetValue()
            v.USR = self.sshUsr.GetValue()
            v.PASSWD = self.sshPasswd.GetValue()
            dutConn = threading.Thread(target=self.connectionCheckThread, kwargs={'connectiontype': v.CONNECTION_TYPE,
                                                                                  'ip': v.HOST, 'user': v.USR,
                                                                                  'password': v.PASSWD})
            dutConn.start()
            dutConn.join()

        if v.STA_MODULE == "R1CM":
            deviceNum += 1
            v.STA_IP = self.staIp.GetValue()
            v.STA_USR = self.staSshUsr.GetValue()
            v.STA_PASSWD = self.staSshPasswd.GetValue()
            staConn = threading.Thread(target=self.connectionCheckThread,
                                       kwargs={'connectiontype': v.STA_CONNECTION_TYPE,
                                               'ip': v.STA_IP, 'user': v.STA_USR,
                                               'password': v.STA_PASSWD})
            staConn.start()
            staConn.join()

        if self.flag < deviceNum:
            dlgErr = wx.MessageDialog(self, 'Connection is failed, please check your network!',
                                      'Info',
                                      wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                      )

            dlgErr.ShowModal()
            dlgErr.Destroy()
        elif self.flag == deviceNum:
            self.saveBtn.Enable(False)
            v.SAVE_BTN_FLAG = True
            dlgOk = wx.MessageDialog(self, 'Connection is OK!',
                                     'Info',
                                     wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                     )

            dlgOk.ShowModal()
            dlgOk.Destroy()

    def EvtTextChange(self, event):
        self.saveBtn.Enable(True)
        v.SAVE_BTN_FLAG = False

    def EvtClose(self, event):
        frame.Close(True)


class MemoryTrackPage(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1, style=wx.BORDER_STATIC)
        wx.StaticText(self, -1, "Memory Tracking", wx.Point(10, 10))

        self.applyBtn = wx.Button(self, -1, 'Apply')
        self.cancelBtn = wx.Button(self, -1, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.EvtTrackDaemonMemInfo, self.applyBtn)
        self.Bind(wx.EVT_BUTTON, self.EvtClose, self.cancelBtn)

        intervalLbl = wx.StaticText(self, -1, "Interval(1-3600s):")
        self.interval = wx.SpinCtrl(self, -1, "", size=(75, -1))
        self.interval.SetRange(1, 3600)
        self.interval.SetValue(10)

        countLbl = wx.StaticText(self, -1, 'Count(1-10000):')
        self.count = wx.SpinCtrl(self, -1, "", size=(75, -1))
        self.count.SetRange(1, 10000)
        self.count.SetValue(360)

        optionalSizer2 = wx.BoxSizer(wx.VERTICAL)
        optionalSizer2.Add(intervalLbl, 0,
                           wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        optionalSizer2.Add(countLbl, 0,
                           wx.ALIGN_RIGHT | wx.TOP | wx.LEFT | wx.BOTTOM, 10)

        optionalSizer3 = wx.BoxSizer(wx.VERTICAL)
        optionalSizer3.Add(self.interval, 0,
                           wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        optionalSizer3.Add(self.count, 0,
                           wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)

        optionalBox = wx.StaticBox(self, -1, 'Memory Tracking', size=(580, -1))
        optionalSizer = wx.StaticBoxSizer(optionalBox, wx.HORIZONTAL)
        optionalSizer.Add(optionalSizer2, 0, wx.LEFT, 5)
        optionalSizer.Add(optionalSizer3, 0, wx.LEFT, 2)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(self.applyBtn, 0, wx.LEFT, 400)
        btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(optionalSizer, 0, wx.ALL, 10)
        mainSizer.Add(btnSizer, 0, wx.TOP, 265)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    def EvtTrackDaemonMemInfo(self, event):

        if not v.SAVE_BTN_FLAG:
            dlg5 = wx.MessageDialog(self, 'General page settings have not been saved yet!',
                                    'Info',
                                    wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                    # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                    )
            dlg5.ShowModal()
            dlg5.Destroy()
            return

        v.INTERVAL = self.interval.GetValue()
        v.COUNT = self.count.GetValue()
        keepGoing = True
        fileCreateTime = t.strftime('_%Y.%m.%d %H.%M.%S', t.localtime())
        memMon = mm.memMonitorExcelXlsx(v.INTERVAL, v.COUNT, 'MEM' + fileCreateTime + '.xlsx')

        if memMon.ret:

            self.dlg = wx.ProgressDialog('Memory tracking progress',
                                         'Starting...',
                                         maximum=v.COUNT,
                                         parent=self,
                                         style=0
                                               | wx.PD_APP_MODAL
                                               | wx.PD_CAN_ABORT
                                               ##                                | wx.PD_CAN_SKIP
                                               | wx.PD_ELAPSED_TIME
                                               | wx.PD_REMAINING_TIME
                                               | wx.PD_AUTO_HIDE
                                         )

            memMon.setDaemon(True)
            memMon.start()

            while keepGoing and memMon.curr_count <= v.COUNT:
                wx.Yield()  # refresh progress
                (keepGoing, skip) = self.dlg.Update(memMon.curr_count, str(memMon.curr_count) + '/' + str(v.COUNT))
                t.sleep(1)

            self.dlg.Destroy()

        elif not memMon.ret:
            dlg3 = wx.MessageDialog(self, 'Connection is failed, please check your remote settings!',
                                    'Info',
                                    wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                    # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                    )
            dlg3.ShowModal()
            dlg3.Destroy()

    def EvtClose(self, event):
        frame.Close(True)


class LogCollectionPage(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1, style=wx.BORDER_STATIC)
        wx.StaticText(self, -1, "Log Collection", wx.Point(10, 10))

        self.applyBtn = wx.Button(self, -1, 'Apply')
        self.cancelBtn = wx.Button(self, -1, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.EvtLogCollection, self.applyBtn)
        self.Bind(wx.EVT_BUTTON, self.EvtClose, self.cancelBtn)
        self.systemCheck = wx.CheckBox(self, -1, 'Collect system log information')
        self.networkCheck = wx.CheckBox(self, -1, 'Collect network log information')
        self.wifiCheck = wx.CheckBox(self, -1, 'Collect wifi log information')
        self.cfgCheck = wx.CheckBox(self, -1, 'Collect UCI config information')
        self.statCheck = wx.CheckBox(self, -1, 'Collect forwarding statistic log information')

        logBox = wx.StaticBox(self, -1, 'Log Collection', size=(580, -1))
        logSizer = wx.StaticBoxSizer(logBox, wx.VERTICAL)
        logSizer.Add(self.systemCheck, 0, wx.LEFT | wx.TOP, 10)
        logSizer.Add(self.networkCheck, 0, wx.LEFT | wx.TOP, 10)
        logSizer.Add(self.wifiCheck, 0, wx.LEFT | wx.TOP, 10)
        logSizer.Add(self.cfgCheck, 0, wx.LEFT | wx.TOP, 10)
        logSizer.Add(self.statCheck, 0, wx.LEFT | wx.TOP | wx.BOTTOM, 10)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(self.applyBtn, 0, wx.LEFT, 400)
        btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(logSizer, 0, wx.ALL, 10)
        mainSizer.Add(btnSizer, 0, wx.TOP, 186)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    def EvtLogCollection(self, event):

        if not v.SAVE_BTN_FLAG:
            dlg5 = wx.MessageDialog(self, 'General page settings have not been saved yet!',
                                    'Info',
                                    wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                    # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                    )
            dlg5.ShowModal()
            dlg5.Destroy()
            return

        # if v.CONNECTION_TYPE == 1:
        ssh = co.SshCommand(v.CONNECTION_TYPE)
        ret = ssh.connect(v.HOST, v.USR, v.PASSWD)

        if ret:
            logList = []
            # model = ssh.command(v.GET_MODEL)
            # model = model[0].strip('\n')

            if self.systemCheck.IsChecked() is True:
                # collect system info
                logList.append('system_log')

            if self.networkCheck.IsChecked() is True:
                # collect network info
                logList.append('network_log')

            if self.wifiCheck.IsChecked() is True:
                # collect wifi info
                if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
                    logList.append('r1d_wifi2G_log')
                    logList.append('r1d_wifi5G_log')

                elif v.DUT_MODULE == 'R1CM':
                    logList.append('r1c_wifi2G_log')
                    logList.append('r1c_wifi5G_log')

            if self.cfgCheck.IsChecked() is True:
                # collect cfg
                logList.append('uci_config')

            if self.statCheck.IsChecked() is True:

                if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
                    logList.append('r1d_forward_statistic_log')

                elif v.DUT_MODULE == 'R1CM':
                    logList.append('r1c_forward_statistic_log')

            if len(logList) == 0:  # all checkboxs arenot selected
                dlg4 = wx.MessageDialog(self, 'One item should be selected at least!',
                                        'Info',
                                        wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                        # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                        )
                dlg4.ShowModal()
                dlg4.Destroy()
                ssh.close()
                return

            self.dlg = wx.ProgressDialog('Log collecting progress',
                                         'Starting...',
                                         maximum=len(logList),
                                         parent=self,
                                         style=0
                                               | wx.PD_APP_MODAL
                                               | wx.PD_CAN_ABORT
                                               ##                        | wx.PD_CAN_SKIP
                                               | wx.PD_ELAPSED_TIME
                                               | wx.PD_REMAINING_TIME
                                               | wx.PD_AUTO_HIDE
                                         )

            c = 0
            keepGoing = True
            fileCreateTime = t.strftime('_%Y.%m.%d %H.%M.%S', t.localtime())
            saveLogPath = os.getcwd() + os.sep + 'LOG_COLLECTION' + fileCreateTime + os.sep
            if not os.path.exists(saveLogPath):
                os.makedirs(saveLogPath)

            while keepGoing and c < len(logList):
                retDic = {}
                ll = logList[c]
                wx.Yield()  # refresh progress
                (keepGoing, skip) = self.dlg.Update(c + 1, ll)

                commands = getattr(data, ll)

                for command in commands:
                    try:
                        retDic.update(ssh.getTitleResDic(command))
                    except Exception, e:
                        dlg4 = wx.MessageDialog(self.dlg, 'Connection is failed, please check your network!',
                                                'Info',
                                                wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                                )

                        dlg4.ShowModal()
                        dlg4.Destroy()
                        ssh.close()
                        self.dlg.Destroy()
                        return

                f = open(saveLogPath + ll + '.txt', 'a')
                for index in retDic:
                    f.write(index)
                    f.writelines(retDic[index])
                c += 1
                ##                        f.flush()
                ##                        os.fsync(f)
                f.close()

            ssh.close()
            self.dlg.Destroy()

        elif not ret:
            dlg3 = wx.MessageDialog(self, 'Connection is failed. please check your remote settings!',
                                    'Info',
                                    wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                    # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                    )
            dlg3.ShowModal()
            dlg3.Destroy()
            return

            # elif v.CONNECTION_TYPE == 2:
            # self.dlg2 = wx.MessageDialog(self, 'Serial-port is not supported now!',
            # 'Info',
            # wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
            # # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
            # )
            # self.dlg2.ShowModal()
            #     self.dlg2.Destroy()
            #     return

    def EvtClose(self, event):
        frame.Close(True)


class TestSuitePage(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1, style=wx.BORDER_STATIC)
        ##        wx.StaticText(self, -1, "Test suite", wx.Point(10, 10))
        ##        self.tree = wx.TreeCtrl(self, size = (340,330))
        self.tree = CT.CustomTreeCtrl(self, size=(340, 330),
                                      style=
                                      wx.BORDER_SIMPLE
                                      | wx.WANTS_CHARS,
                                      agwStyle=
                                      CT.TR_HAS_BUTTONS
                                      | CT.TR_MULTIPLE
                                      | CT.TR_AUTO_CHECK_CHILD

                                      )
        self.tree.SetBackgroundColour(wx.WHITE)

        self.root = self.tree.AddRoot('Test Cases', ct_type=1)
        self.rootAndroid = self.tree.AppendItem(self.root, 'Android-STA', ct_type=1)
        self.rootR1CM = self.tree.AppendItem(self.root, 'R1CM-STA', ct_type=1)
        self.rootNone = self.tree.AppendItem(self.root, 'None-STA', ct_type=1)

        self.AddTreeNodes(self.rootAndroid, data.treeAndroid)
        self.AddTreeNodes(self.rootR1CM, data.treeR1CM)
        self.AddTreeNodes(self.rootNone, data.treeNone)

        self.tree.Expand(self.root)

        # self.Bind(CT.EVT_TREE_ITEM_CHECKED, self.EvtAddRemoveCase, self.tree)

        treeLbl = wx.StaticText(self, -1, 'Select cases supposed to excute:')

        self.applyBtn = wx.Button(self, -1, 'Apply')
        self.cancelBtn = wx.Button(self, -1, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.EvtTestExcute, self.applyBtn)
        self.Bind(wx.EVT_BUTTON, self.EvtClose, self.cancelBtn)

        retryLbl = wx.StaticText(self, -1, "If test case failed, try ")
        retryLbl2 = wx.StaticText(self, -1, " more times.")
        self.retry = wx.SpinCtrl(self, -1, "", size=(45, -1))
        self.retry.SetRange(0, 100)
        self.retry.SetValue(v.FAIL_RETRY)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(retryLbl, 0, wx.LEFT, 10)
        btnSizer.Add(self.retry, 0, wx.LEFT, 2)
        btnSizer.Add(retryLbl2, 0, wx.LEFT, 2)
        btnSizer.Add(self.applyBtn, 0, wx.LEFT, 143)
        btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)

        mainSizer.Add(treeLbl, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT | wx.BOTTOM, 10)
        mainSizer.Add(self.tree, 0, wx.ALIGN_LEFT | wx.LEFT, 20)
        mainSizer.Add(btnSizer, 0, wx.TOP, 10)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    def AddTreeNodes(self, parent, children):
        for child in children:
            if type(child) is str:
                newParent = self.tree.AppendItem(parent, child, ct_type=1)
            else:
                # self.tree.AppendItem(newParent, child[0], ct_type=1)
                self.AddTreeNodes(newParent, child)

    def TestCaseGenerator(self):

        cases = {}
        for child in self.root.GetChildren():
            for child2 in child.GetChildren():
                child2Name = self.tree.GetItemText(child2)
                cases[child2Name] = []
                if child2.HasChildren():
                    for child3 in child2.GetChildren():
                        if child3.IsChecked():
                            child3Name = self.tree.GetItemText(child3)
                            cases[child2Name].append(child3Name)
                else:
                    if child2.IsChecked():
                        cases[child2Name].append(child2Name)
        for (i, j) in cases.items():
            if len(j) == 0:
                del cases[i]

        return cases

    def TextTestRunnerFailCheck(self, jobID, abortEvent, testcase, count):
        # process testcases tend to find error or failed cases,
        # then add them to suitefailed and process it until count times
        ssh = co.SshCommand(v.CONNECTION_TYPE)
        ssh.connect(v.HOST, v.USR, v.PASSWD)
        hardware = ssh.getHardware()
        rom = ssh.getRomVersion()
        self.report = hardware + rom["channel"] + rom["version"] + ".log"
        self.mailTitle = ssh.setMailTitle()

        # curTime = t.strftime('%Y.%m.%d %H.%M.%S', t.localtime())
        f = open(self.report, 'a')
        runner = TextTestRunner(f, verbosity=2)
        res = runner.run(testcase)
        errors = res.errors
        failures = res.failures
        c = 0

        while (len(errors) != 0 or len(failures) != 0) and c < count and not abortEvent():
            suitefailed = TestSuite()
            for testcase in failures:
                suitefailed.addTest(testcase[0])

            res = runner.run(suitefailed)
            errors = res.errors
            failures = res.failures
            c += 1

        f.close()
        return jobID

    def TestCaseRunDialog(self, testcase):

        self.abortEvent = delayedresult.AbortEvent()
        self.abortEvent.clear()
        self.jobID = 1
        self.runFlag = True  # testcases were completed, destory dlg
        testKeepGoing = True

        self.dlg = wx.ProgressDialog('Executing test suite progress',
                                     'Running......please wait.',
                                     maximum=50,
                                     parent=self,
                                     style=0
                                           | wx.PD_APP_MODAL
                                           | wx.PD_CAN_ABORT
                                           ##                        | wx.PD_CAN_SKIP
                                           | wx.PD_ELAPSED_TIME
                                           | wx.PD_REMAINING_TIME
                                     ##                        | wx.PD_AUTO_HIDE
                                     )

        delayedresult.startWorker(self.DestoryTestCaseRunDialog, self.TextTestRunnerFailCheck,
                                  wargs=(self.jobID, self.abortEvent, testcase, v.FAIL_RETRY),
                                  jobID=self.jobID)

        # start memory monitor
        self.memMon = mm.memMonitor(v.MEM_MONITOR_INTERVAL)
        self.memMon.setDaemon(True)
        self.memMon.start()

        while testKeepGoing and self.runFlag:
            wx.Yield()  # refresh progress
            (testKeepGoing, skip) = self.dlg.Pulse()
            t.sleep(0.1)

        # t.sleep(1.0)
        if v.SEND_MAIL == 1 and testKeepGoing:
            content = """<html><body><img src="cid:Total_memory_used.png" alt="Total_memory_used.png"></body></html><small>此为系统自动发送，请勿回复，详情查看附件。</small>"""
            sm.sendMail(v.MAILTO_LIST, self.mailTitle, content, self.report, ["Total_memory_used.png"])

        self.abortEvent.set()
        self.dlg.Destroy()

    def DestoryTestCaseRunDialog(self, delayedResult):

        jobID = delayedResult.getJobID()
        assert jobID == self.jobID
        try:
            result = delayedResult.get()
            self.runFlag = False
            self.memMon.stop()  # stop memory monitor

        except Exception:
            return

    def EvtTestExcute(self, event):

        if not v.SAVE_BTN_FLAG:
            dlg2 = wx.MessageDialog(self, 'General page settings have not been saved yet!',
                                    'Info',
                                    wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                    # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                    )
            dlg2.ShowModal()
            dlg2.Destroy()
            return

        v.FAIL_RETRY = self.retry.GetValue()
        allSuiteTuple = ()
        selCasesDic = self.TestCaseGenerator()
        for i in selCasesDic:
            testCaseClass = getattr(tc, i)
            maptc = map(testCaseClass, selCasesDic[i])
            allSuiteTuple += tuple(maptc)

        allTestSuite = TestSuite(allSuiteTuple)
        self.TestCaseRunDialog(allTestSuite)

    def EvtClose(self, event):
        frame.Close(True)


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Peanuts " + v.VER, pos=(300, 200), size=(610, 530), style=
        wx.CAPTION
        | wx.CLOSE_BOX
        | wx.MINIMIZE_BOX
        | wx.SYSTEM_MENU
                          )
        self.Center()
        self.SetIcon(images.logo.GetIcon())
        bookFrame = ToolBook(self, -1)

##        wx.StaticBitmap(bookFrame, -1, images.logo.GetBitmap(), (520,5))

app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()
