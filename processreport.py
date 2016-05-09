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
        self.dut2g = {
            '20tx': [],
            '20rx': [],
            '40tx': [],
            '40rx': [],
        }
        self.dut5g = {
            '20tx': [],
            '40tx': [],
            '80tx': [],
            '20rx': [],
            '40rx': [],
            '80rx': [],
        }
        self.lan2g = {
            '20tx': [],
            '20rx': [],
            '40tx': [],
            '40rx': [],
        }
        self.lan5g = {
            '20tx': [],
            '40tx': [],
            '80tx': [],
            '20rx': [],
            '40rx': [],
            '80rx': [],
        }
        self.dut = {
            'CH1 20M': "self.dut2g['20tx'].append(speedDict['tx']), self.dut2g['20rx'].append(speedDict['rx'])",
            'CH6 20M': "self.dut2g['20tx'].append(speedDict['tx']), self.dut2g['20rx'].append(speedDict['rx'])",
            'CH11 20M': "self.dut2g['20tx'].append(speedDict['tx']), self.dut2g['20rx'].append(speedDict['rx'])",
            'CH13 20M': "self.dut2g['20tx'].append(speedDict['tx']), self.dut2g['20rx'].append(speedDict['rx'])",
            'CH1 40M': "self.dut2g['40tx'].append(speedDict['tx']), self.dut2g['40rx'].append(speedDict['rx'])",
            'CH6 40M': "self.dut2g['40tx'].append(speedDict['tx']), self.dut2g['40rx'].append(speedDict['rx'])",
            'CH11 40M': "self.dut2g['40tx'].append(speedDict['tx']), self.dut2g['40rx'].append(speedDict['rx'])",
            'CH13 40M': "self.dut2g['40tx'].append(speedDict['tx']), self.dut2g['40rx'].append(speedDict['rx'])",
            'CH36 20M': "self.dut5g['20tx'].append(speedDict['tx']), self.dut5g['20rx'].append(speedDict['rx'])",
            'CH52 20M': "self.dut5g['20tx'].append(speedDict['tx']), self.dut5g['20rx'].append(speedDict['rx'])",
            'CH149 20M': "self.dut5g['20tx'].append(speedDict['tx']), self.dut5g['20rx'].append(speedDict['rx'])",
            'CH165 20M': "self.dut5g['20tx'].append(speedDict['tx']), self.dut5g['20rx'].append(speedDict['rx'])",
            'CH36 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH44 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH52 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH60 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH149 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH157 40M': "self.dut5g['40tx'].append(speedDict['tx']), self.dut5g['40rx'].append(speedDict['rx'])",
            'CH36 80M': "self.dut5g['80tx'].append(speedDict['tx']), self.dut5g['80rx'].append(speedDict['rx'])",
            'CH52 80M': "self.dut5g['80tx'].append(speedDict['tx']), self.dut5g['80rx'].append(speedDict['rx'])",
            'CH149 80M': "self.dut5g['80tx'].append(speedDict['tx']), self.dut5g['80rx'].append(speedDict['rx'])",
        }
        self.lan = {
            'CH1 20M': "self.lan2g['20tx'].append(speedDict['tx']), self.lan2g['20rx'].append(speedDict['rx'])",
            'CH6 20M': "self.lan2g['20tx'].append(speedDict['tx']), self.lan2g['20rx'].append(speedDict['rx'])",
            'CH11 20M': "self.lan2g['20tx'].append(speedDict['tx']), self.lan2g['20rx'].append(speedDict['rx'])",
            'CH13 20M': "self.lan2g['20tx'].append(speedDict['tx']), self.lan2g['20rx'].append(speedDict['rx'])",
            'CH1 40M': "self.lan2g['40tx'].append(speedDict['tx']), self.lan2g['40rx'].append(speedDict['rx'])",
            'CH6 40M': "self.lan2g['40tx'].append(speedDict['tx']), self.lan2g['40rx'].append(speedDict['rx'])",
            'CH11 40M': "self.lan2g['40tx'].append(speedDict['tx']), self.lan2g['40rx'].append(speedDict['rx'])",
            'CH13 40M': "self.lan2g['40tx'].append(speedDict['tx']), self.lan2g['40rx'].append(speedDict['rx'])",
            'CH36 20M': "self.lan5g['20tx'].append(speedDict['tx']), self.lan5g['20rx'].append(speedDict['rx'])",
            'CH52 20M': "self.lan5g['20tx'].append(speedDict['tx']), self.lan5g['20rx'].append(speedDict['rx'])",
            'CH149 20M': "self.lan5g['20tx'].append(speedDict['tx']), self.lan5g['20rx'].append(speedDict['rx'])",
            'CH165 20M': "self.lan5g['20tx'].append(speedDict['tx']), self.lan5g['20rx'].append(speedDict['rx'])",
            'CH36 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH44 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH52 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH60 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH149 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH157 40M': "self.lan5g['40tx'].append(speedDict['tx']), self.lan5g['40rx'].append(speedDict['rx'])",
            'CH36 80M': "self.lan5g['80tx'].append(speedDict['tx']), self.lan5g['80rx'].append(speedDict['rx'])",
            'CH52 80M': "self.lan5g['80tx'].append(speedDict['tx']), self.lan5g['80rx'].append(speedDict['rx'])",
            'CH149 80M': "self.lan5g['80tx'].append(speedDict['tx']), self.lan5g['80rx'].append(speedDict['rx'])",
        }

    def run(self):
        indexList = list()
        report = open(self.reportName)
        for line in report:
            if not line.isspace():
                m = re.search('AP_(.*)_CHAN(\d{1,3})_BW(\d{2})_((.*)_)?THROUGHPUT', line)
                if m:
                    logFile = self.logPath + m.group(0) + ".log"
                    chanBW = "CH" + m.group(2) + " " + m.group(3) + "M" # CH36 20M
                    encrypto = m.group(1) # CLEAR or PSK2
                    sheet = m.group(5) # infoTuple[3] is sheet name
                    infoTuple = (logFile, chanBW, encrypto, sheet)
                    if infoTuple not in indexList:
                        indexList.append(infoTuple)
        report.close()
        if len(indexList) is not 0:
            try:
                wb = load_workbook(v.MAIL_THROUGHPUT_XLSX_ORIGINAL)
            except:
                print "specified file no exists!"
                return
            for tu in indexList:
                speedDict = getThroughputLogVerbose(tu[0])
                # collect draw chart data
                if tu[3] == "DUT":
                    eval(self.dut.get(tu[1]))
                elif tu[3] == "LAN":
                    eval(self.lan.get(tu[1]))

                for cell in wb[tu[3]].get_cell_collection():
                    if tu[1] == cell.value:
                        x = cell.row
                        y = column_index_from_string(cell.column)
                        if tu[2] == "PSK2":
                            x += 3
                            y += 1
                            while wb[tu[3]].cell(row=x, column=y).value is not None:
                                x += 1
                            wb[tu[3]].cell(row=x, column=y).value = speedDict["tx"]
                        elif tu[2] == "CLEAR":
                            x += 3
                            y += 2
                            while wb[tu[3]].cell(row=x, column=y).value is not None:
                                x += 1
                            wb[tu[3]].cell(row=x, column=y).value = speedDict["tx"]
                        y += 2
                        wb[tu[3]].cell(row=x, column=y).value = speedDict['rx']
                        break
            wb.save(v.MAIL_THROUGHPUT_XLSX)

            for key, value in self.dut2g.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.dut2g[key] = ave
                else:
                    self.dut2g[key] = 0

            for key, value in self.dut5g.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.dut5g[key] = ave
                else:
                    self.dut5g[key] = 0

            # draw chart
            for value in self.dut2g.values():
                if isinstance(value, float):
                    drawThroughput2g(self.dut2g, v.MAIL_PIC2)
                    break
            for value in self.dut5g.values():
                if isinstance(value, float):
                    drawThroughput5g(self.dut5g, v.MAIL_PIC3)
                    break

            for key, value in self.lan2g.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.lan2g[key] = ave
                else:
                    self.lan2g[key] = 0

            for key, value in self.lan5g.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.lan5g[key] = ave
                else:
                    self.lan5g[key] = 0

            # draw chart
            for value in self.lan2g.values():
                if isinstance(value, float):
                    drawThroughput2g(self.lan2g, v.MAIL_PIC5)
                    break
            for value in self.lan5g.values():
                if isinstance(value, float):
                    drawThroughput5g(self.lan5g, v.MAIL_PIC6)
                    break


def getThroughputLogVerbose(logfile):
    result = {
        'tx': 0,
        'rx': 0,
    }
    try:
        log = open(logfile)
        for line in log:
            if not line.isspace():
                m = re.search('0\.0-\d{1,4}.*\s(\d{1,3}\.?\d{1,2})?\sMbits/sec', line)
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


def drawThroughput2g(data, picname):
    bar_width = 0.2
    opacity = 0.4
    index = np.arange(2)
    ret = data

    tx = list()
    rx = list()

    tx.append(ret.get("20tx"))
    tx.append(ret.get("40tx"))
    rx.append(ret.get("20rx"))
    rx.append(ret.get("40rx"))

    fig, ax = plt.subplots(figsize=(6, 4))
    print "draw %s chart" % picname
    # plt.subplots_adjust(left=0.08, right=0.95)
    rects1 = plt.bar(index, tx, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Tx',
                     )

    rects2 = plt.bar(index + bar_width, rx, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Rx',
                     )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 0.75*height, '%.1f'%float(height),
                    ha='center', va='bottom', fontsize=10)

    autolabel(rects1)
    autolabel(rects2)

    plt.xlabel('Bandwidth', fontsize=10)
    plt.ylabel('Mbps', fontsize=10)
    plt.suptitle(picname.split(".")[0].split('\\')[-1].title(), fontsize=10)
    plt.xticks(index + bar_width, ('20MHz', '40MHz',), fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(prop={'size': 10})

    # plt.show()
    plt.savefig(picname)
    plt.close()


def drawThroughput5g(data, picname):
    bar_width = 0.2
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

    fig, ax = plt.subplots(figsize=(6, 4))
    print "draw %s chart" % picname
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
                    ha='center', va='bottom', fontsize=10)

    autolabel(rects1)
    autolabel(rects2)

    plt.xlabel('Bandwidth', fontsize=10)
    plt.ylabel('Mbps', fontsize=10)
    plt.suptitle(picname.split(".")[0].split('\\')[-1].title(), fontsize=10)
    plt.xticks(index + bar_width, ('20MHz', '40MHz', '80MHz'), fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(prop={'size': 10})

    # plt.show()
    plt.savefig(picname)
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
    # info = GetThroughputLog("report.log".decode("utf8").encode("gbk"))
    # info.start()
    # info.join()
    print getThroughputLogVerbose('ttt.log'.decode("utf8").encode("gbk"))
    # f = open('test.log')
    # ret = f.readlines()
    # f.close()
    # f2 = open('ttt.log', 'a')
    # for l in xrange(len(ret)):
    #     ret[l] = re.sub('\r', '\n', ret[l])
    # a = ret
    # f2.writelines(ret)
    # f2.close()




