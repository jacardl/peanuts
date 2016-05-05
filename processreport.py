# -*- coding: utf8 -*-
import multiprocessing as mp
import threading
import re
from collections import *
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook
from openpyxl.cell import column_index_from_string

import var as v
import data

class ProcessReport(mp.Process):
    def __init__(self, report, q):
        mp.Process.__init__(self)
        self.running = False
        self.report = report
        self.result = OrderedDict()
        self.qu = q

    def run(self):
        self.running = True
        time = GetTimeUsed(self.report)
        test = GetTestResult(self.report)
        # flow = GetFlowLog(self.report)
        throughput = GetThroughputLog(self.report)
        online = GetOnlineLog(self.report)
        module = GetTestModule(self.report)
        time.start()
        test.start()
        throughput.start()
        online.start()
        module.start()
        while time.is_alive() or test.is_alive() or throughput.is_alive() \
                or online.is_alive() or module.is_alive():
            pass
        self.result.update(error=test.result['error'])
        self.result.update(ranpass=test.result["ranpass"])
        self.result.update(sum=test.result["ransum"])
        if self.result['sum'] == 0:
            self.result.update(percent=0)
        else:
            self.result.update(percent=self.result["ranpass"]/float(self.result['sum'])*100)
        self.result.update(time=time.timeUsed)
        self.result.update(onlinesum=online.result["pass"]+online.result["fail"])
        self.result.update(onlinepass=online.result["pass"])
        onlineSum = online.result["pass"]+online.result["fail"]
        if onlineSum == 0:
            self.result.update(onlinepercent=0)
        else:
            self.result.update(onlinepercent=online.result["pass"]/float(onlineSum)*100)
        self.result.update(module=module.result)
        self.qu.put(self.result)
        self.stop()

    def stop(self):
        self.running = False


class GetTimeUsed(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.timeUsed = 0

    def run(self):
        self.running = True
        f = open(self.reportName)
        for line in f:
            if not line.isspace():
                m = re.search('Ran\s+\d+\s+[tes]+\s+in\s+(\d+)', line)
                if m:
                    self.timeUsed += int(m.group(1))
        f.close()
        self.timeUsed = float(self.timeUsed/3600.0)
        self.timeUsed = round(self.timeUsed, 2)
        self.stop()

    def stop(self):
        self.running = False


class GetTestResult(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.result = {
            'error': 0,
            'ranfail': 0,
            'ranpass': 0,
            'ransum': 0,
            }

    def run(self):
        self.running = True
        f = open(self.reportName)
        for line in f:
            if not line.isspace():
                m = re.search('Ran\s+(\d+)\s+[tes]+\s+in.*', line)
                if m:
                    if self.result['ransum'] is 0:
                        self.result['ransum'] = int(m.group(1))
                    next(f)
                    line2 = next(f)
                    m2 = re.search('(FAILED \((failures=(\d+))?(, )?(errors=(\d+))?\))?(OK)?', line2)
                    if m2:
                        if m.group(1) and m2.group(3) and m2.group(6):
                            self.result["ranpass"] += (int(m.group(1)) - int(m2.group(3)))
                            self.result['ranfail'] = int(m2.group(3))
                            self.result['error'] += int(m2.group(6))
                        elif m.group(1) and m2.group(3):
                            self.result["ranpass"] += (int(m.group(1)) - int(m2.group(3)))
                            self.result['ranfail'] = int(m2.group(3))
                        elif m.group(1) and m2.group(6):
                            self.result["ranpass"] += int(m.group(1))
                            self.result['error'] += int(m2.group(6))
                            self.result['ranfail'] = 0
                        elif m.group(1) and m2.group(7):
                            self.result['ranpass'] += int(m.group(1))
                            self.result['ranfail'] = 0

        f.close()
        self.stop()

    def stop(self):
        self.running = False


class GetThroughputLog(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.reportName = report
        self.logPath = v.TEST_SUITE_LOG_PATH
        self.result2g = {
            '20tx': [],
            '20rx': [],
            '40tx': [],
            '40rx': [],
        }
        self.result5g = {
            '20tx': [],
            '40tx': [],
            '80tx': [],
            '20rx': [],
            '40rx': [],
            '80rx': [],
        }
        self.sw = {
            'CH1 20M': "self.result2g['20tx'].append(speedDict['tx']), self.result2g['20rx'].append(speedDict['rx'])",
            'CH6 20M': "self.result2g['20tx'].append(speedDict['tx']), self.result2g['20rx'].append(speedDict['rx'])",
            'CH11 20M': "self.result2g['20tx'].append(speedDict['tx']), self.result2g['20rx'].append(speedDict['rx'])",
            'CH13 20M': "self.result2g['20tx'].append(speedDict['tx']), self.result2g['20rx'].append(speedDict['rx'])",
            'CH1 40M': "self.result2g['40tx'].append(speedDict['tx']), self.result2g['40rx'].append(speedDict['rx'])",
            'CH6 40M': "self.result2g['40tx'].append(speedDict['tx']), self.result2g['40rx'].append(speedDict['rx'])",
            'CH11 40M': "self.result2g['40tx'].append(speedDict['tx']), self.result2g['40rx'].append(speedDict['rx'])",
            'CH13 40M': "self.result2g['40tx'].append(speedDict['tx']), self.result2g['40rx'].append(speedDict['rx'])",
            'CH36 20M': "self.result5g['20tx'].append(speedDict['tx']), self.result5g['20rx'].append(speedDict['rx'])",
            'CH52 20M': "self.result5g['20tx'].append(speedDict['tx']), self.result5g['20rx'].append(speedDict['rx'])",
            'CH149 20M': "self.result5g['20tx'].append(speedDict['tx']), self.result5g['20rx'].append(speedDict['rx'])",
            'CH165 20M': "self.result5g['20tx'].append(speedDict['tx']), self.result5g['20rx'].append(speedDict['rx'])",
            'CH36 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH44 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH52 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH60 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH149 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH157 40M': "self.result5g['40tx'].append(speedDict['tx']), self.result5g['40rx'].append(speedDict['rx'])",
            'CH36 80M': "self.result5g['80tx'].append(speedDict['tx']), self.result5g['80rx'].append(speedDict['rx'])",
            'CH52 80M': "self.result5g['80tx'].append(speedDict['tx']), self.result5g['80rx'].append(speedDict['rx'])",
            'CH149 80M': "self.result5g['80tx'].append(speedDict['tx']), self.result5g['80rx'].append(speedDict['rx'])",
        }

    def run(self):
        indexList = list()
        report = open(self.reportName)
        for line in report:
            if not line.isspace():
                m = re.search('AP_(.*)_CHAN(\d{1,3})_BW(\d{2})_THROUGHPUT', line)
                if m:
                    logFile = self.logPath + m.group(0) + ".log"
                    chanBW = "CH" + m.group(2) + " " + m.group(3) + "M" # CH36 20M
                    encrypto = m.group(1) # CLEAR or PSK2
                    infoTuple = (logFile, chanBW, encrypto)
                    if infoTuple not in indexList:
                        indexList.append(infoTuple)
        report.close()
        try:
            wb = load_workbook(v.MAIL_THROUGHPUT_XLSX)
        except:
            print "specified file no exists!"
            return
        ws = wb["Sheet1"]
        for tu in indexList:
            speedDict = getThroughputLogVerbose(tu[0])
            eval(self.sw.get(tu[1]))
            for cell in ws.get_cell_collection():
                if tu[1] == cell.value:
                    x = cell.row
                    y = column_index_from_string(cell.column)
                    if tu[2] == "PSK2":
                        x += 3
                        y += 1
                        while ws.cell(row=x, column=y).value is not None:
                            x += 1
                        ws.cell(row=x, column=y).value = speedDict["tx"]
                    elif tu[2] == "CLEAR":
                        x += 3
                        y += 2
                        while ws.cell(row=x, column=y).value is not None:
                            x += 1
                        ws.cell(row=x, column=y).value = speedDict["tx"]
                    y += 2
                    ws.cell(row=x, column=y).value = speedDict['rx']
                    break
        wb.save(self.logPath + v.MAIL_THROUGHPUT_XLSX)

        for key, value in self.result2g.iteritems():
            if len(value) is not 0:
                ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                self.result2g[key] = ave
            else:
                self.result2g[key] = 0

        for key, value in self.result5g.iteritems():
            if len(value) is not 0:
                ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                self.result5g[key] = ave
            else:
                self.result5g[key] = 0

        drawThroughput2g(self.result2g)
        drawThroughput5g(self.result5g)


def getThroughputLogVerbose(logfile):
    result = {
        'tx': 0,
        'rx': 0,
    }
    try:
        log = open(logfile)
        for line in log:
            if not line.isspace():
                m = re.search('\s0.0-\d{1,4}.*\s(\d{1,3}\.?\d{1,2})?\sMbits/sec', line)
                if m:
                    if result['tx'] is 0:
                        result['tx'] = m.group(1)
                        continue
                    else:
                        result['rx'] = m.group(1)
                        break
        log.close()
    except IOError as e:
        raise e
    return result


def drawThroughput2g(data):
    bar_width = 0.42
    opacity = 0.4
    index = np.arange(2)
    ret = data

    tx = list()
    rx = list()

    tx.append(ret.get("20tx"))
    tx.append(ret.get("40tx"))
    rx.append(ret.get("20rx"))
    rx.append(ret.get("40rx"))

    fig, ax = plt.subplots(figsize=(8, 6))
    print "draw 2.4g throughput chart"
    # plt.subplots_adjust(left=0.08, right=0.95)
    rects1 = plt.bar(index, tx, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Tx'
                     )

    rects2 = plt.bar(index + bar_width, rx, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Rx'
                     )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 0.75*height, '%.1f'%float(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.xlabel('Bandwidth')
    plt.ylabel('Mbps')
    plt.suptitle(v.MAIL_PIC2.split(".")[0].title())
    plt.xticks(index + bar_width, ('20MHz', '40MHz',))
    plt.legend()

    # plt.show()
    plt.savefig(v.MAIL_PIC2)
    plt.close()


def drawThroughput5g(data):
    bar_width = 0.42
    opacity = 0.4
    index = np.arange(3)
    ret = data

    tx = list()
    rx = list()

    tx.append(ret.get("20tx"))
    tx.append(ret.get("40tx"))
    tx.append(ret.get("80tx"))
    rx.append(ret.get("20rx"))
    rx.append(ret.get("40rx"))
    rx.append(ret.get("80rx"))

    fig, ax = plt.subplots(figsize=(8, 6))
    print "draw 5g throughputchart"
    # plt.subplots_adjust(left=0.08, right=0.95)
    rects1 = plt.bar(index, tx, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Tx'
                     )

    rects2 = plt.bar(index + bar_width, rx, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Rx'
                     )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 0.75*height, '%.1f'%float(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.xlabel('Bandwidth')
    plt.ylabel('Mbps')
    plt.suptitle(v.MAIL_PIC3.split(".")[0].title())
    plt.xticks(index + bar_width, ('20MHz', '40MHz', '80MHz'))
    plt.legend()

    # plt.show()
    plt.savefig(v.MAIL_PIC3)
    plt.close()


class GetOnlineLog(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.logPath = v.TEST_SUITE_LOG_PATH
        self.result = {
            "pass": 0,
            "fail": 0,
            }

    def run(self):
        self.running = True
        logFileList = list()
        report = open(self.reportName)
        for line in report:
            if not line.isspace():
                m = re.search('assoc_repeat.*testcase.*\.(.*)\)', line)
                if m:
                    if line.endswith("ok\n"):
                        self.result["pass"] += 100
                    elif line.endswith("FAIL\n"):
                        logFile = m.group(1) + ".log"
                        logFile = self.logPath + logFile
                        if logFile not in logFileList:
                            logFileList.append(logFile)
                else:
                    n = re.search('assoc', line)
                    if n:
                        if line.endswith("ok\n"):
                            self.result["pass"] += 1
                        elif line.endswith("FAIL\n"):
                            self.result["fail"] += 1
        report.close()
        for lf in logFileList:
            log = open(lf)
            for line in log:
                if not line.isspace():
                    m = re.search('Not all association were successful.*but was:<(\d+)>', line)
                    if m:
                        self.result["pass"] += int(m.group(1))
                        self.result["fail"] += (100 - int(m.group(1)))
            log.close()
        self.stop()

    def stop(self):
        self.running = False


class GetTestModule(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.logPath = v.TEST_SUITE_LOG_PATH
        self.moduleDict = {
            'treeBasicApi': '基础功能',
            'treeBSDApi': '双频合一',
            'treeWireRelayApi':'有线中继',
            'treeWirelessRelayApi':'无线中继',
            'treeAccessControlApi':'接入控制',
            'treeQosApi':'智能限速',
            'treeThroughputApi':'WiFi吞吐',
            'treeStressApi':'压力测试',
            'treeOthersApi':'其他',
        }
        self.result = list()

    def run(self):
        self.running = True
        f = open(self.reportName)
        for line in f:
            if not line.isspace():
                m = re.search('\(testcase.*\.(.*)\)', line)
                if m:
                    testCase = m.group(1)
                    for module in self.moduleDict.iterkeys():
                        if chkTestCaseModule(testCase, module):
                            if self.moduleDict.get(module) not in self.result:
                                self.result.append(self.moduleDict.get(module))
                                self.result.append('，')
        if len(self.result) > 0:
            del self.result[-1]
        f.close()
        self.stop()

    def stop(self):
        self.running = False


def chkTestCaseModule(tcName, module):
    for i in getattr(data, module):
        if isinstance(i, str):
            if tcName == i:
                return True
    return False


if __name__ == '__main__':
    # t.start()
    # while t.isAlive():
    #     print time.time()
    # print getFlowLogVerbose("E:\peanuts\AP_MIXEDPSK_CHAN1_36_FLOW.log")
    # print getChannelFlowLogVerbose("E:\peanuts\AP_MIXEDPSK_CHAN1_36_FLOW.log")
    info = GetThroughputLog("report.log".decode("utf8").encode("gbk"))
    info.start()
    info.join()



