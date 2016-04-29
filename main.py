# -*- coding: utf8 -*-
import threading
from unittest import *
import os
import time as t
from collections import *
import wx
import wx.lib.agw.customtreectrl as CT
import wx.lib.delayedresult as delayedresult
import shutil
import random
import multiprocessing as mp
import var as v
import common as co
import images
import data
import testcase2 as tc
import sendmail as sm
import memmonitor as mm
import processreport as pr
import api
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

            # elif tool == v.TOOL_LIST[2]:
            #     page3 = LogCollectionPage(self)
            #     self.AddPage(page3, tool, imageId=imageIdGenerator.next())

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
        self.type = wx.Choice(self, -1, choices=['R1D', 'R2D', 'R1CM', "R1CL", "R3"])
        self.type.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.type)

        connLbl = wx.StaticText(self, -1, "Connection type:")
        self.conn = wx.Choice(self, -1, choices=["SSH", "Telnet", "Serial", "fac" ])
        self.conn.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice3, self.conn)

        ipLbl = wx.StaticText(self, -1, 'Host IP:')
        self.ip = wx.TextCtrl(self, -1, '')
        self.ip.SetValue(v.HOST)

        sshUsrLbl = wx.StaticText(self, -1, 'User name:')
        self.sshUsr = wx.TextCtrl(self, -1, '')
        self.sshUsr.SetValue(v.USR)

        sshPasswdLbl = wx.StaticText(self, -1, 'Password:')
        self.sshPasswd = wx.TextCtrl(self, -1, '')
        self.sshPasswd.SetValue(v.PASSWD)

        webPasswdLbl = wx.StaticText(self, -1, 'Web password:')
        self.webPasswd = wx.TextCtrl(self, -1, '')
        self.webPasswd.SetValue(v.WEB_PWD)

        serialPortLbl = wx.StaticText(self, -1, 'Serial port:')
        self.serialNum = []
        if len(co.getSerialPort()) is 0:
            self.serialNum.append("None")
        else:
            self.serialNum = co.getSerialPort()
        self.serialNum.append("None")
        self.serialPort = wx.Choice(self, -1, choices=self.serialNum)
        v.SERIAL_PORT = self.serialNum[0]

        self.serialPort.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice4, self.serialPort)
        self.serialPort.Enable(False)

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
        connSizer4.Add(webPasswdLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        connSizer4.Add(serialPortLbl, 0,
                       wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)

        connSizer5 = wx.BoxSizer(wx.VERTICAL)
        connSizer5.Add(self.conn, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 2)
        connSizer5.Add(self.webPasswd, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)
        connSizer5.Add(self.serialPort, 0,
                       wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)

        connSizer.Add(connSizer2, 0, wx.LEFT, 5)
        connSizer.Add(connSizer3, 0, wx.LEFT, 2)
        connSizer.Add(connSizer4, 0, wx.LEFT, 10)
        connSizer.Add(connSizer5, 0, wx.LEFT, 2)

        # sta connection ctrl
        staTypeLbl = wx.StaticText(self, -1, 'Device:')
        self.staType = wx.Choice(self, -1, choices=['Android'])
        self.staType.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.staType)

        staCountLbl = wx.StaticText(self, -1, 'Count:')
        self.staCount = wx.TextCtrl(self, -1, '')
        self.staCount.SetValue(v.STA_COUNT)

        # sta connection box
        staConnBox = wx.StaticBox(self, -1, 'STA', size=(580, -1))
        staConnSizer = wx.StaticBoxSizer(staConnBox, wx.HORIZONTAL)

        staConnSizer2 = wx.BoxSizer(wx.VERTICAL)
        staConnSizer2.Add(staTypeLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)
        staConnSizer2.Add(staCountLbl, 0,
                          wx.ALIGN_RIGHT | wx.TOP | wx.LEFT, 10)


        staConnSizer3 = wx.BoxSizer(wx.VERTICAL)
        staConnSizer3.Add(self.staType, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 2)
        staConnSizer3.Add(self.staCount, 0,
                          wx.ALIGN_LEFT | wx.TOP | wx.LEFT, 4)

        staConnSizer.Add(staConnSizer2, 0, wx.LEFT, 5)
        staConnSizer.Add(staConnSizer3, 0, wx.LEFT, 2)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(connSizer, 0, wx.ALL, 10)
        mainSizer.Add(staConnSizer, 0, wx.ALL, 10)
        mainSizer.Add(btnSizer, 0, wx.TOP, 106)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    def EvtChoice(self, event):
        self.saveBtn.Enable(True)
        v.SAVE_BTN_FLAG = False
        v.DUT_MODULE = event.GetString()

    def EvtChoice2(self, event):
        self.saveBtn.Enable(True)
        v.SAVE_BTN_FLAG = False
        v.STA_MODULE = event.GetString()
        if v.STA_MODULE == "Android":
            self.staIp.Enable(False)
            self.staSshUsr.Enable(False)
            self.staSshPasswd.Enable(False)
        # elif v.STA_MODULE == "R1CM & Android":
        #     self.staIp.Enable(True)
        #     self.staSshUsr.Enable(True)
        #     self.staSshPasswd.Enable(True)

    def EvtChoice3(self, event):
        self.saveBtn.Enable(True)
        v.SAVE_BTN_FLAG = False
        type = event.GetString()
        self.sshUsr.Enable(True)
        self.sshPasswd.Enable(True)
        self.serialPort.Enable(False)
        if type == "Telnet":
            v.CONNECTION_TYPE = 2
        elif type == "SSH":
            v.CONNECTION_TYPE = 1
        elif type == "fac":
            v.CONNECTION_TYPE = 2
            self.sshUsr.Enable(False)
            self.sshPasswd.Enable(False)
        elif type == "Serial":
            v.CONNECTION_TYPE = 3
            self.sshUsr.Enable(False)
            self.sshPasswd.Enable(False)
            self.serialPort.Enable(True)

    def EvtChoice4(self, event):
        self.saveBtn.Enable(True)
        v.SAVE_BTN_FLAG = False
        v.SERIAL_PORT = event.GetString()


    def connectionCheckThread(self, connectiontype, ip=None, port=None, user=None, password=None):
        result, self.hardware = co.connectionCheck(connectiontype, ip=ip, user=user, password=password)
        if result:
            v.SAVE_BTN_FLAG = True
            dlgOk = wx.MessageDialog(self, 'Connection is OK ! \n'
                                           'DUT is %s !'%self.hardware,
                                     'Info',
                                     wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                     )

            dlgOk.ShowModal()
            dlgOk.Destroy()
        else:
            self.saveBtn.Enable(True)
            dlgErr = wx.MessageDialog(self, 'Connection is failed, please check your network!',
                                      'Info',
                                      wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                      )

            dlgErr.ShowModal()
            dlgErr.Destroy()

    def adbDeviceCheckThread(self, count):
        result = co.chkAdbDevicesCount(count)
        if result is False:
            dlgErr = wx.MessageDialog(self, 'Some Android devices are offline!',
                                      'Info',
                                      wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
                                      )

            dlgErr.ShowModal()
            dlgErr.Destroy()

    def EvtSave(self, event):
        self.saveBtn.Enable(False)
        if v.DUT_MODULE is not None:
            v.HOST = self.ip.GetValue()
            v.USR = self.sshUsr.GetValue()
            v.PASSWD = self.sshPasswd.GetValue()
            v.WEB_PWD = self.webPasswd.GetValue()
            dutConn = threading.Thread(target=self.connectionCheckThread, kwargs={'connectiontype': v.CONNECTION_TYPE,
                                                                                  'ip': v.HOST, 'user': v.USR,
                                                                                  'password': v.PASSWD})
            dutConn.start()

        if v.STA_MODULE is 'Android':
            v.STA_COUNT = self.staCount.GetValue()
            dutConn = threading.Thread(target=self.adbDeviceCheckThread, args=(v.STA_COUNT,))
            dutConn.start()


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
        memMon = mm.MemMonitorXlsx(v.INTERVAL, v.COUNT, 'MEM' + fileCreateTime + '.xlsx')

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

            # while keepGoing and memMon.curr_count <= v.COUNT:
            while keepGoing and memMon.isAlive():
                # wx.Yield()  # refresh progress
                # (keepGoing, skip) = self.dlg.Update(memMon.curr_count, str(memMon.curr_count) + '/' + str(v.COUNT))
                # t.sleep(1)
                wx.Yield()  # refresh progress
                (testKeepGoing, skip) = self.dlg.Pulse()
                t.sleep(0.1)

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


# class LogCollectionPage(wx.Panel):
#     def __init__(self, parent):
#         wx.Window.__init__(self, parent, -1, style=wx.BORDER_STATIC)
#         wx.StaticText(self, -1, "Log Collection", wx.Point(10, 10))
#
#         self.applyBtn = wx.Button(self, -1, 'Apply')
#         self.cancelBtn = wx.Button(self, -1, 'Cancel')
#         self.Bind(wx.EVT_BUTTON, self.EvtLogCollection, self.applyBtn)
#         self.Bind(wx.EVT_BUTTON, self.EvtClose, self.cancelBtn)
#         self.systemCheck = wx.CheckBox(self, -1, 'Collect system log information')
#         self.networkCheck = wx.CheckBox(self, -1, 'Collect network log information')
#         self.wifiCheck = wx.CheckBox(self, -1, 'Collect wifi log information')
#         self.cfgCheck = wx.CheckBox(self, -1, 'Collect UCI config information')
#         self.statCheck = wx.CheckBox(self, -1, 'Collect forwarding statistic log information')
#
#         logBox = wx.StaticBox(self, -1, 'Log Collection', size=(580, -1))
#         logSizer = wx.StaticBoxSizer(logBox, wx.VERTICAL)
#         logSizer.Add(self.systemCheck, 0, wx.LEFT | wx.TOP, 10)
#         logSizer.Add(self.networkCheck, 0, wx.LEFT | wx.TOP, 10)
#         logSizer.Add(self.wifiCheck, 0, wx.LEFT | wx.TOP, 10)
#         logSizer.Add(self.cfgCheck, 0, wx.LEFT | wx.TOP, 10)
#         logSizer.Add(self.statCheck, 0, wx.LEFT | wx.TOP | wx.BOTTOM, 10)
#
#         btnSizer = wx.BoxSizer(wx.HORIZONTAL)
#         btnSizer.Add(self.applyBtn, 0, wx.LEFT, 400)
#         btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)
#
#         mainSizer = wx.BoxSizer(wx.VERTICAL)
#         mainSizer.Add(logSizer, 0, wx.ALL, 10)
#         mainSizer.Add(btnSizer, 0, wx.TOP, 186)
#
#         self.SetSizer(mainSizer)
#         mainSizer.Fit(self)
#         mainSizer.SetSizeHints(self)
#
#     def EvtLogCollection(self, event):
#
#         if not v.SAVE_BTN_FLAG:
#             dlg5 = wx.MessageDialog(self, 'General page settings have not been saved yet!',
#                                     'Info',
#                                     wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
#                                     # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
#                                     )
#             dlg5.ShowModal()
#             dlg5.Destroy()
#             return
#
#         # if v.CONNECTION_TYPE == 1:
#         ssh = co.SshCommand(v.CONNECTION_TYPE)
#         ret = ssh.connect(v.HOST, v.USR, v.PASSWD)
#
#         if ret:
#             logList = []
#             # model = ssh.command(v.GET_MODEL)
#             # model = model[0].strip('\n')
#
#             if self.systemCheck.IsChecked() is True:
#                 # collect system info
#                 logList.append('system_log')
#
#             if self.networkCheck.IsChecked() is True:
#                 # collect network info
#                 logList.append('network_log')
#
#             if self.wifiCheck.IsChecked() is True:
#                 # collect wifi info
#                 if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
#                     logList.append('r1d_wifi2G_log')
#                     logList.append('r1d_wifi5G_log')
#
#                 elif v.DUT_MODULE == "R1CM":
#                     logList.append('r1c_wifi2G_log')
#                     logList.append('r1c_wifi5G_log')
#
#                 elif v.DUT_MODULE == "R3":
#                     logList.append('r3_wifi2G_log')
#                     logList.append('r3_wifi5G_log')
#
#                 elif v.DUT_MODULE == "R1CL":
#                     logList.append("r1cl_wifi2G_log")
#
#
#             if self.cfgCheck.IsChecked() is True:
#                 # collect cfg
#                 logList.append('uci_config')
#
#             if self.statCheck.IsChecked() is True:
#
#                 if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
#                     logList.append('r1d_forward_statistic_log')
#
#                 elif v.DUT_MODULE == "R1CM":
#                     logList.append('r1c_forward_statistic_log')
#
#                 elif v.DUT_MODULE == "R3":
#                     logList.append('r3_forward_statistic_log')
#
#                 elif v.DUT_MODULE == "R1CL":
#                     logList.append("r1cl_forward_statistic_log")
#
#             if len(logList) == 0:  # all checkboxs arenot selected
#                 dlg4 = wx.MessageDialog(self, 'One item should be selected at least!',
#                                         'Info',
#                                         wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
#                                         # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
#                                         )
#                 dlg4.ShowModal()
#                 dlg4.Destroy()
#                 ssh.close()
#                 return
#
#             self.dlg = wx.ProgressDialog('Log collecting progress',
#                                          'Starting...',
#                                          maximum=len(logList),
#                                          parent=self,
#                                          style=0
#                                                | wx.PD_APP_MODAL
#                                                | wx.PD_CAN_ABORT
#                                                ##                        | wx.PD_CAN_SKIP
#                                                | wx.PD_ELAPSED_TIME
#                                                | wx.PD_REMAINING_TIME
#                                                | wx.PD_AUTO_HIDE
#                                          )
#
#             c = 0
#             keepGoing = True
#             fileCreateTime = t.strftime('_%Y.%m.%d %H.%M.%S', t.localtime())
#             saveLogPath = os.getcwd() + os.sep + 'LOG_COLLECTION' + fileCreateTime + os.sep
#             if not os.path.exists(saveLogPath):
#                 os.makedirs(saveLogPath)
#
#             while keepGoing and c < len(logList):
#                 retDic = OrderedDict()
#                 ll = logList[c]
#                 wx.Yield()  # refresh progress
#                 (keepGoing, skip) = self.dlg.Update(c + 1, ll)
#
#                 commands = getattr(data_old, ll)
#
#                 for command in commands:
#                     try:
#                         retDic.update(ssh.getTitleResDic(command))
#                     except Exception, e:
#                         dlg4 = wx.MessageDialog(self.dlg, 'Connection is failed, please check your network!',
#                                                 'Info',
#                                                 wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
#                                                 )
#
#                         dlg4.ShowModal()
#                         dlg4.Destroy()
#                         ssh.close()
#                         self.dlg.Destroy()
#                         return
#
#                 f = open(saveLogPath + ll + '.txt', 'a')
#                 for index in retDic:
#                     f.write(index)
#                     f.writelines(retDic[index])
#                 c += 1
#                 ##                        f.flush()
#                 ##                        os.fsync(f)
#                 f.close()
#
#             ssh.close()
#             self.dlg.Destroy()
#
#         elif not ret:
#             dlg3 = wx.MessageDialog(self, 'Connection is failed. please check your remote settings!',
#                                     'Info',
#                                     wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
#                                     # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
#                                     )
#             dlg3.ShowModal()
#             dlg3.Destroy()
#             return
#
#             # elif v.CONNECTION_TYPE == 2:
#             # self.dlg2 = wx.MessageDialog(self, 'Serial-port is not supported now!',
#             # 'Info',
#             # wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP
#             # # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
#             # )
#             # self.dlg2.ShowModal()
#             #     self.dlg2.Destroy()
#             #     return
#
#     def EvtClose(self, event):
#         frame.Close(True)


class TestSuitePage(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1, style=wx.BORDER_STATIC)
        ##        wx.StaticText(self, -1, "Test suite", wx.Point(10, 10))
        ##        self.tree = wx.TreeCtrl(self, size = (340,330))
        self.tree = CT.CustomTreeCtrl(self, size=(340, 303),
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
        self.rootBasic = self.tree.AppendItem(self.root, 'Basic', ct_type=1)
        self.rootBSD = self.tree.AppendItem(self.root, 'BSD', ct_type=1)
        self.rootQosApi = self.tree.AppendItem(self.root, 'QoS', ct_type=1)
        self.rootAccessControlApi = self.tree.AppendItem(self.root, 'Access Control', ct_type=1)
        self.rootWireRelay = self.tree.AppendItem(self.root, 'Wire Relay', ct_type=1)
        self.rootWirelessRelay = self.tree.AppendItem(self.root, 'Wireless Relay', ct_type=1)
        self.rootFlow = self.tree.AppendItem(self.root, 'Throughput', ct_type=1)
        self.rootStress = self.tree.AppendItem(self.root, 'Stress', ct_type=1)
        self.rootOthers = self.tree.AppendItem(self.root, 'Others', ct_type=1)

        # self.rootAndroid = self.tree.AppendItem(self.root, 'Android', ct_type=1)
        # self.rootCheck = self.tree.AppendItem(self.root, 'Check', ct_type=1)
        # self.AddTreeNodes(self.rootAndroid, data.treeAndroid)
        # self.AddTreeNodes(self.rootCheck, data.treeCheck)

        self.AddTreeNodes(self.rootBasic, data.treeBasicApi)
        self.AddTreeNodes(self.rootBSD, data.treeBSDApi)
        self.AddTreeNodes(self.rootQosApi, data.treeQosApi)
        self.AddTreeNodes(self.rootAccessControlApi, data.treeAccessControlApi)
        self.AddTreeNodes(self.rootWireRelay, data.treeWireRelayApi)
        self.AddTreeNodes(self.rootWirelessRelay, data.treeWirelessRelayApi)
        self.AddTreeNodes(self.rootFlow, data.treeFlowApi)
        self.AddTreeNodes(self.rootStress, data.treeStressApi)
        self.AddTreeNodes(self.rootOthers, data.treeOthersApi)
        self.tree.Expand(self.root)
        treeLbl = wx.StaticText(self, -1, 'Select cases supposed to excute:')

        self.sel2gCheck = wx.CheckBox(self, -1, "2.4G")
        self.sel5gCheck = wx.CheckBox(self, -1, "5G")
        self.selGuestCheck = wx.CheckBox(self, -1, "Guest wifi")
        self.selUploadLog = wx.CheckBox(self, -1, 'Upload Log')
        self.selUploadLog.SetValue(True)
        self.selSendMail = wx.CheckBox(self, -1, 'Send Mail')
        self.selSendMail.SetValue(True)

        self.Bind(wx.EVT_CHECKBOX, self.EvtSel2g, self.sel2gCheck)
        self.Bind(wx.EVT_CHECKBOX, self.EvtSel5g, self.sel5gCheck)
        self.Bind(wx.EVT_CHECKBOX, self.EvtSelGuest, self.selGuestCheck)
        self.Bind(wx.EVT_CHECKBOX, self.EvtSelUploadLog, self.selUploadLog)
        self.Bind(wx.EVT_CHECKBOX, self.EvtSelSendMail, self.selSendMail)

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
        checkBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(retryLbl, 0, wx.LEFT, 10)
        btnSizer.Add(self.retry, 0, wx.LEFT, 2)
        btnSizer.Add(retryLbl2, 0, wx.LEFT, 2)
        btnSizer.Add(self.applyBtn, 0, wx.LEFT, 143)
        btnSizer.Add(self.cancelBtn, 0, wx.LEFT, 15)

        checkBoxSizer.Add(self.sel2gCheck, 0, wx.LEFT, 10)
        checkBoxSizer.Add(self.sel5gCheck, 0, wx.LEFT, 10)
        checkBoxSizer.Add(self.selGuestCheck, 0, wx.LEFT, 10)
        checkBoxSizer.Add(self.selUploadLog, 0, wx.LEFT, 10)
        checkBoxSizer.Add(self.selSendMail, 0, wx.LEFT, 10)

        mainSizer.Add(treeLbl, 0, wx.ALIGN_LEFT | wx.TOP | wx.LEFT | wx.BOTTOM, 10)
        mainSizer.Add(checkBoxSizer, 0, wx.LEFT | wx.BOTTOM, 10)
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
        # save file in windows, default code is gbk
        self.report = ssh.setReportName().decode("utf8").encode("gbk")
        self.reportFile = (ssh.setReportName() + ".log").decode("utf8").encode("gbk")
        self.mailTitle = ssh.setMailTitle()

        # curTime = t.strftime('%Y.%m.%d %H.%M.%S', t.localtime())
        f = open(self.reportFile, 'a')
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
        self.memMon = mm.HttpMemCPUMonitor(v.MEM_MONITOR_INTERVAL)
        self.memMon.start()

        # start upload
        if v.UPLOAD_LOG == 1:
            self.upLoad = api.SetUploadLog(v.DEVICE_STATUS_LOG)
            self.upLoad.start()
            self.upLoad.join()

        if v.CONNECTION_TYPE is not 3:
            self.memMonXlsx = mm.MemMonitorXlsx(v.MEM_MONITOR_INTERVAL, file=v.MAIL_XLSX)
            # self.memMonXlsx.setDaemon(True)
            self.memMonXlsx.start()

        while testKeepGoing and self.runFlag:
            wx.Yield()  # refresh progress
            (testKeepGoing, skip) = self.dlg.Pulse()
            t.sleep(0.1)
            # set testKeepGoing to False when click cancel

        if os.path.exists(v.TEST_SUITE_LOG_PATH):
            if not os.path.exists(self.report):
                os.rename(v.TEST_SUITE_LOG_PATH, self.report)
            else:
                os.rename(v.TEST_SUITE_LOG_PATH, self.report + str(random.random()))
        if testKeepGoing is False:
            os.system("taskkill /F /IM python.exe | taskkill /F /T /IM adb.exe")
        self.abortEvent.set()
        self.dlg.Destroy()

    def DestoryTestCaseRunDialog(self, delayedResult):

        jobID = delayedResult.getJobID()
        assert jobID == self.jobID
        try:
            result = delayedResult.get()
            self.memMon.stop()  # stop memory monitor and draw chart
            # self.memMon.join()

            if v.CONNECTION_TYPE is not 3:
                self.memMonXlsx.stop()  # stop tracing daemon and kernel memory
                self.memMonXlsx.join()

            q = mp.Queue() # tranlate test result to generateMail
            self.procReport = pr.ProcessReport(self.reportFile, q)
            self.procReport.start()
            self.procReport.join()

            while not os.path.exists(v.DEFAULT_PATH + v.MAIL_PIC1) or \
                    not os.path.exists(v.DEFAULT_PATH + v.MAIL_PIC4):
                print "wait for draw memory/cpu chart"
                t.sleep(1)

            if v.SEND_MAIL == 1:
                # add Queue to communicate with processreport process
                sm.generateMail(v.MAILTO_LIST, self.mailTitle, q, self.reportFile, v.MAIL_XLSX)

            # before stoping upload log threading, upload log for the last time
            if v.UPLOAD_LOG is 1:
                self.upLoad.stop()

            files = os.listdir(v.DEFAULT_PATH)
            for file in files:
                if os.path.splitext(file)[1] == ".png":
                    try:
                        shutil.move(file, v.TEST_SUITE_LOG_PATH)
                    except Exception, e:
                        print "shutil.move " + file + str(e)
                elif file == v.MAIL_XLSX:
                    try:
                        shutil.move(file, v.TEST_SUITE_LOG_PATH)
                    except Exception, e:
                        print "shutil.move" + file + str(e)
            # quit execution test dlg
            self.runFlag = False

        except Exception, e:
            raise e

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

    def EvtSel2g(self, event):
        import re
        if self.sel2gCheck.IsChecked() is True:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search("2g", child3Name)
                            if m:
                                self.tree.CheckItem(child3)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search("2g", child2Name)
                        if m:
                            self.tree.SelectItem(child2)
        elif self.sel2gCheck.IsChecked() is False:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            import re
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search('2g', child3Name)
                            if m:
                                self.tree.CheckItem(child3, checked=False)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search('2g', child2Name)
                        if m:
                            self.tree.CheckItem(child2, checked=False)

    def EvtSel5g(self, event):
        import re
        if self.sel5gCheck.IsChecked() is True:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search("5g", child3Name)
                            if m:
                                self.tree.CheckItem(child3)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search("5g", child2Name)
                        if m:
                            self.tree.SelectItem(child2)
        elif self.sel5gCheck.IsChecked() is False:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            import re
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search('5g', child3Name)
                            if m:
                                self.tree.CheckItem(child3, checked=False)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search('5g', child2Name)
                        if m:
                            self.tree.CheckItem(child2, checked=False)

    def EvtSelGuest(self, event):
        import re
        if self.selGuestCheck.IsChecked() is True:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search("guest", child3Name)
                            if m:
                                self.tree.CheckItem(child3)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search("guest", child2Name)
                        if m:
                            self.tree.SelectItem(child2)
        elif self.selGuestCheck.IsChecked() is False:
            for child in self.root.GetChildren():
                for child2 in child.GetChildren():
                    if child2.HasChildren():
                        for child3 in child2.GetChildren():
                            import re
                            child3Name = self.tree.GetItemText(child3)
                            m = re.search('guest', child3Name)
                            if m:
                                self.tree.CheckItem(child3, checked=False)
                    else:
                        child2Name = self.tree.GetItemText(child2)
                        m = re.search('guest', child2Name)
                        if m:
                            self.tree.CheckItem(child2, checked=False)

    def EvtSelUploadLog(self, event):
        if self.selUploadLog.IsChecked() is True:
            v.UPLOAD_LOG = 1
        else:
            v.UPLOAD_LOG = 0

    def EvtSelSendMail(self, event):
        if self.selSendMail.IsChecked() is True:
            v.SEND_MAIL = 1
        else:
            v.SEND_MAIL = 0

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

# when use multiprocess module on windows platform, " 'if __name__ == '__main__' "should be added
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
