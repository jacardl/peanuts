import matplotlib.pyplot as plt
import xlwt as x
from openpyxl import Workbook

from common import *
import var as v


class memMonitor(threading.Thread):
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
                res = self.terminal.getTotalMemInfo()
                memUsed = res["used"]
                self.plot.append(memUsed)
                if self.callback is not None:
                    self.callback.after_read_res(res, t)
            t.sleep(self.period)

    def stop(self):
        # draw a chart
        f, ax = plt.subplots(figsize=(12, 6))
        # f, ax = plt.subplots()
        ax.plot(range(len(self.plot)), self.plot)
        # ax.set_title('Total Memory Used')
        plt.suptitle("Total Memory Used")
        plt.xlabel('Counts')
        plt.ylabel('KB')
        # plt.show()
        plt.savefig(v.MAIL_PIC1)
        plt.close()

        self.terminal.close()
        self.running = False


class memMonitorXls(threading.Thread):
    def __init__(self, interval, count, file="temp.xls"):
        threading.Thread.__init__(self)
        self.interval = interval
        self.count = count
        self.running = False
        self.callback = None
        self.curr_count = 1
        self.file = file

        self.terminal = SshCommand(v.CONNECTION_TYPE)
        self.ret = self.terminal.connect(v.HOST, v.USR, v.PASSWD)

    def run(self):
        self.running = True
        last_time = t.time()
        self.book = x.Workbook()
        self.memSheet = self.book.add_sheet('memery tracking')
        row0 = self.memSheet.row(0)
        col0 = self.memSheet.col(0)
        col0.width = v.WIDTH2
        keys = []
        row0Col = 2  # col 0 write time, col 1 write total mem, so vsz begin with 2
        vszRow = 1
        style1 = x.easyxf(num_format_str='h:mm:ss')
        self.memSheet.write(0, 1, "Total used")  # write Total used title

        while self.running and self.curr_count <= self.count:
            curr_time = t.time()
            if curr_time - last_time >= self.interval:
                last_time = curr_time
                self.terminal.getPidNameVSZDic()
                totalmem = self.terminal.getTotalMemInfo()
                time = self.terminal.getTimeStr()
                newDic = self.terminal.outPidNameVSZDic
                newKeys = newDic.keys()

                self.memSheet.write(vszRow, 0, time, style1)  # write time
                self.memSheet.write(vszRow, 1, totalmem["used"])
                for i in newKeys:
                    try:
                        vszCol = keys.index(i) + 2  # begin from col 2
                        self.memSheet.write(vszRow, vszCol, newDic[i])  # write daemon vsz

                    except:
                        flag = 0
                        for e in v.EXCEPTIONS:  # exclude some daemons
                            if e not in i:
                                pass
                            else:
                                flag = 1
                                break
                        if flag == 0:
                            row0.write(row0Col, i)  # write new daemon title
                            self.memSheet.col(row0Col).width = v.WIDTH
                            self.memSheet.write(vszRow, row0Col, newDic[i])  # write new daemon vsz
                            keys.append(i)
                            row0Col += 1
                vszRow += 1
                self.curr_count += 1
                try:
                    self.book.save(self.file)
                except:
                    self.terminal.close()
                    break
            t.sleep(1)
        self.stop()

    def stop(self):
        memData = xr.open_workbook(self.file)
        memTable = memData.sheet_by_name('memery tracking')
        maxRow = memTable.nrows
        maxCol = memTable.ncols
        stylePercent = x.easyxf('font: name Calibri, bold on, height 250, underline on;', num_format_str="0.00%")
        for col in range(1, maxCol):
            rowStart = ""
            rowEnd = ""
            for row in range(1, maxRow):
                if rowStart == "":
                    rowStart = memTable.cell(row, col).value
                else:
                    break
            for row in reversed(range(1, maxRow)):
                if rowEnd == "":
                    rowEnd = memTable.cell(row, col).value
                else:
                    break
            diff = (rowEnd - rowStart) / rowStart
            if diff != 0:
                self.memSheet.write(maxRow, col, diff, stylePercent)
            else:
                self.memSheet.write(maxRow, col, diff)
        self.book.save(self.file)

        self.terminal.close()
        self.running = False


class memMonitorExcelXlsx(threading.Thread):
    def __init__(self, interval, count, file="temp.xlsx"):
        threading.Thread.__init__(self)
        self.interval = interval
        self.count = count
        self.running = False
        self.callback = None
        self.curr_count = 1
        self.file = file

        self.terminal = SshCommand(v.CONNECTION_TYPE)
        self.ret = self.terminal.connect(v.HOST, v.USR, v.PASSWD)

    def run(self):
        self.running = True
        last_time = t.time()
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = "Mem tracking"
        # col0.width = v.WIDTH2
        keys = []
        row1Col = 3  # col 1 write time, col 2 write total mem, so vsz begin with 3
        vszRow = 2  # Row 1 write title, value begin with Row 2
        style1 = x.easyxf(num_format_str='h:mm:ss')
        self.ws.cell(row=1, column=2).value = "Total used"  # write Total used title

        while self.running and self.curr_count <= self.count:
            curr_time = t.time()
            if curr_time - last_time >= self.interval:
                last_time = curr_time
                self.terminal.getPidNameVSZDic()
                totalmem = self.terminal.getTotalMemInfo()
                time = self.terminal.getTimeStr()
                newDic = self.terminal.outPidNameVSZDic
                newKeys = newDic.keys()

                self.ws.cell(row=vszRow, column=1).value = time  # write time
                self.ws.cell(row=vszRow, column=2).value = totalmem["used"]  # write total mem
                for i in newKeys:
                    try:
                        vszCol = keys.index(i) + 3  # begin from col 3
                        self.ws.cell(row=vszRow, column=vszCol).value = newDic[i]  # write daemon vsz

                    except:
                        flag = 0
                        for e in v.EXCEPTIONS:  # exclude some daemons
                            if e not in i:
                                pass
                            else:
                                flag = 1
                                break
                        if flag == 0:
                            self.ws.cell(row=1, column=row1Col).value = i  # write new daemon title
                            # self.ws.col(row0Col).width = v.WIDTH
                            self.ws.cell(row=vszRow, column=row1Col).value = newDic[i]  # write new daemon vsz
                            keys.append(i)
                            row1Col += 1
                vszRow += 1
                self.curr_count += 1
                try:
                    self.wb.save(self.file)
                except:
                    self.terminal.close()
                    break
            t.sleep(1)
        self.stop()

    def stop(self):
        maxRow = self.ws.get_highest_row()
        maxCol = self.ws.get_highest_column()

        for col in range(2, maxCol + 1):
            rowStart = None
            rowEnd = None
            for row in range(2, maxRow+1):
                if rowStart is None:
                    rowStart = self.ws.cell(row=row, column=col).value
                else:
                    rowStart = float(rowStart)
                    break
            for row in reversed(range(2, maxRow+1)):
                if rowEnd is None:
                    rowEnd = self.ws.cell(row=row, column=col).value
                else:
                    rowEnd = float(rowEnd)
                    break
            try:
                diff = (rowEnd - rowStart) / rowStart
            except Exception, e:
                print e, "rowStart=%s, rowEnd=%s"%rowStart,rowEnd

            if diff != 0:
                # self.ws.write(maxRow, col, diff, stylePercent)
                sum = self.ws.cell(row=maxRow + 1, column=col)
                diff = "{:.1%}".format(diff)
                sum.value = diff
                # else:
                # # self.ws.write(maxRow, col, diff)
                # sum = self.ws.cell(row=maxRow+1, column=col)
                # sum.value = diff

        self.wb.save(self.file)
        self.terminal.close()
        self.running = False


if __name__ == "__main__":
    interval = 1
    memMon = memMonitorExcelXlsx(interval, 5)
    memMon.setDaemon(True)
    memMon.start()
    c = 0
    while c <= 7:
        print memMon.curr_count
        c += 1
        t.sleep(1.2)
