import multiprocessing as mp

import matplotlib.pyplot as plt
import xlwt as x
from openpyxl import Workbook, load_workbook

from common import *
import var as v


class MemMonitor(threading.Thread):
    def __init__(self, interval=5, period=1):
        threading.Thread.__init__(self)
        self.interval = interval
        self.period = period
        self.running = False
        self.callback = None
        self.terminal = SshCommand(v.CONNECTION_TYPE)
        self.terminal.connect(v.HOST, v.USR, v.PASSWD)

    def run(self):
        self.running = True
        self.plot = []
        last_time = t.time()
        while self.running:
            curr_time = t.time()
            if curr_time - last_time >= self.interval:
                last_time = curr_time
                try:
                    res = self.terminal.getTotalMemInfo()
                except Exception, e:
                    continue
                    # res = dict()
                    # res["used"] = 0
                memUsed = res["used"]
                self.plot.append(memUsed)
                if self.callback is not None:
                    self.callback.after_read_res(res, t)
            t.sleep(self.period)
        self.terminal.close()
        p = mp.Process(target=drawMem, args=(self.plot,))
        p.start()
        p.join()

    def stop(self):
        self.running = False


def drawMem(data):
    # draw a chart
    fig, ax = plt.subplots(figsize=(12, 6))
    print "draw memory chart"
    ax.plot(xrange(len(data)), data)
    # ax.set_title('Total Memory Used')
    plt.suptitle("Total Memory Used")
    plt.xlabel('Counts')
    plt.ylabel('KB')
    # plt.show()
    plt.savefig(v.MAIL_PIC1)
    plt.close()


class MemMonitorXlsx(threading.Thread):
    def __init__(self, interval, count=0, file="temp.xlsx"):
        threading.Thread.__init__(self)
        self.interval = interval
        self.count = count
        self.running = False
        self.callback = None
        self.file = file
        self.sheetDaemon = "User Mem Tracking"
        self.sheetKernel = "Kernel Mem Tracking"
        self.terminal = SshCommand(v.CONNECTION_TYPE)
        self.ret = self.terminal.connect(v.HOST, v.USR, v.PASSWD)

    def run(self):
        self.running = True
        daemon = threading.Thread(target=daemonMonitor, args=(self.terminal, self.interval, self.count,
                                                                    self.file, self.sheetDaemon))
        daemon.setDaemon(True)
        daemon.start()
        while self.running and daemon.isAlive():
            daemon.join(1)
        # while daemonThread.isAlive():
        #     pass
        memDiffCalc(self.file, self.sheetDaemon)
        self.stop()

    def stop(self):
        self.running = False
        self.terminal.close()


def daemonMonitor(terminal, interval, count, filename, sheetname):
    curr_count = 1
    last_time = t.time()
    wb = Workbook()
    ws = wb.active
    ws.title = sheetname
    # col0.width = v.WIDTH2
    keys = []
    row1Col = 3  # col 1 write time, col 2 write total mem, so vsz begin with 3
    vszRow = 2  # Row 1 write title, value begin with Row 2
    style1 = x.easyxf(num_format_str='h:mm:ss')
    ws.cell(row=1, column=2).value = "Total Used"  # write Total used title

    if count >= 1:
        while curr_count <= count:
            curr_time = t.time()
            if curr_time - last_time >= interval:
                last_time = curr_time
                try:
                    # terminal.getPidNameVSZDic()
                    totalmem = terminal.getTotalMemInfo()
                    time = terminal.getTimeStr()
                    newDic = getDaemonRss(terminal)
                except Exception, e:
                    curr_count += 1
                    continue
                newKeys = newDic.keys()

                ws.cell(row=vszRow, column=1).value = time  # write time
                ws.cell(row=vszRow, column=2).value = totalmem["used"]  # write total mem
                for i in newKeys:
                    try:
                        vszCol = keys.index(i) + 3  # begin from col 3
                        ws.cell(row=vszRow, column=vszCol).value = newDic[i]  # write daemon vsz

                    except:
                        flag = 0
                        for e in v.EXCEPTIONS:  # exclude some daemons
                            if e not in i:
                                pass
                            else:
                                flag = 1
                                break
                        if flag == 0:
                            ws.cell(row=1, column=row1Col).value = i  # write new daemon title
                            # self.ws.col(row0Col).width = v.WIDTH
                            ws.cell(row=vszRow, column=row1Col).value = newDic[i]  # write new daemon vsz
                            keys.append(i)
                            row1Col += 1
                vszRow += 1
                curr_count += 1
                try:
                    wb.save(filename)
                except:
                    terminal.close()
                    break
            t.sleep(1)
    elif count is 0:
        while True:
            curr_time = t.time()
            if curr_time - last_time >= interval:
                last_time = curr_time
                try:
                    totalmem = terminal.getTotalMemInfo()
                    time = terminal.getTimeStr()
                    newDic = getDaemonRss(terminal)
                except Exception, e:
                    curr_count += 1
                    continue
                newKeys = newDic.keys()

                ws.cell(row=vszRow, column=1).value = time  # write time
                ws.cell(row=vszRow, column=2).value = totalmem["used"]  # write total mem
                for i in newKeys:
                    try:
                        vszCol = keys.index(i) + 3  # begin from col 3
                        ws.cell(row=vszRow, column=vszCol).value = newDic[i]  # write daemon vsz

                    except:
                        flag = 0
                        for e in v.EXCEPTIONS:  # exclude some daemons
                            if e not in i:
                                pass
                            else:
                                flag = 1
                                break
                        if flag == 0:
                            ws.cell(row=1, column=row1Col).value = i  # write new daemon title
                            # self.ws.col(row0Col).width = v.WIDTH
                            ws.cell(row=vszRow, column=row1Col).value = newDic[i]  # write new daemon vsz
                            keys.append(i)
                            row1Col += 1
                vszRow += 1
                curr_count += 1
                try:
                    wb.save(filename)
                except:
                    terminal.close()
                    break
            t.sleep(1)


def kernelMonitor():
    pass


def memDiffCalc(filename, sheetname):
    try:
        wb = load_workbook(filename)
    except:
        return
    # ws = wb.active
    ws = wb['User Mem Tracking']
    maxRow = ws.get_highest_row()
    maxCol = ws.get_highest_column()

    for col in range(2, maxCol + 1):
        rowStart = None
        rowEnd = None
        for row in range(2, maxRow+1):
            if rowStart is None:
                rowStart = ws.cell(row=row, column=col).value
            else:
                rowStart = float(rowStart)
                break
        for row in reversed(range(2, maxRow+1)):
            if rowEnd is None:
                rowEnd = ws.cell(row=row, column=col).value
            else:
                rowEnd = float(rowEnd)
                break
        try:
            diff = (rowEnd - rowStart) / rowStart
        except Exception, e:
            print e, "rowStart=%s, rowEnd=%s"%(rowStart, rowEnd)
            diff = 0

        if diff != 0:
            # self.ws.write(maxRow, col, diff, stylePercent)
            sum = ws.cell(row=maxRow + 1, column=col)
            diff = "{:.1%}".format(diff)
            sum.value = diff
    wb.save(filename)

if __name__ == '__main__':

    v.CONNECTION_TYPE = 2
    v.HOST = "192.168.110.1"
    v.USR = ""
    v.PASSWD = ""
    memMon = MemMonitorXlsx(interval=1, count=0, file="temp.xlsx")
    # memDiffCalc("temp.xlsx")
    memMon.start()
    t.sleep(10)
    memMon.stop()

