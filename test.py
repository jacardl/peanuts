import os
# file_name = 'ez_setup.py'
# from urllib import urlopen
# data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
# with open(file_name, 'wb') as f:
#     f.write(data.read())
# os.system("D:\\Python\\\new peanuts\\24\\ez_setup.py")
# import numpy as np
# import matplotlib.pyplot as plt
# import multiprocessing
#
#
# class TEST(multiprocessing.Process):
#     def __init__(self, interval):
#         multiprocessing.Process.__init__(self)
#         self.interval = interval
#
#     def run(self):
#         f, ax = plt.subplots(figsize=(12, 6))
#         print 1
#         ax.plot(xrange(len(self.interval)), self.interval)
#         print 2
#         # ax.set_title('Total Memory Used')
#         plt.suptitle("Total Memory Used")
#         print 3
#         plt.xlabel('Counts')
#         print 4
#         plt.ylabel('KB')
#         print 5
#         # plt.show()
#         plt.savefig("test.png")
#         print 6
#         plt.close()
#
# if __name__ == "__main__":
#     t1 = TEST([1,2,3,4,5,6,7,8,9])
#     t1.start()
#     t1.join()
#     t2 = TEST([2,3,4,5,6,7,8,9])
#     t2.start()
#     t2.join()


import time
import multiprocessing as mp
import wx
import threading

def myWorker(a, b):
    time.sleep(10)
    print '{} * {} = {}'.format(a, b, a*b)

def onProcess(event):
    jobs = mp.cpu_count() * 2
    a = 5
    b = 10

    for job in range(jobs):
        mp.Process(target = myWorker, args = (a, b,)).start()

def onGUI(event):
    print 'GUI is not blocked'

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
       wx.Frame.__init__(self, parent, id, title)
       buttons = []
       panel = wx.Panel(self, wx.ID_ANY)
       sizer = wx.BoxSizer(wx.VERTICAL)
       gui_proc_btn = wx.Button(panel, wx.ID_ANY, 'GUI Process')
       other_proc_btn = wx.Button(panel, wx.ID_ANY, 'Other process')

       gui_proc_btn.Bind(wx.EVT_BUTTON, onGUI)
       sizer.Add(gui_proc_btn, 0, wx.ALL, 5)
       other_proc_btn.Bind(wx.EVT_BUTTON, onProcess)
       sizer.Add(other_proc_btn, 0, wx.ALL, 5)
       panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'test.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':

    app = MyApp(0)
    app.MainLoop()