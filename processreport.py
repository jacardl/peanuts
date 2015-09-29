# -*- coding: gbk -*-
import threading
import re
from collections import *
import  numpy as np
import matplotlib.pyplot as plt

import common
import var as v


class ProcessReport(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        pass

    def stop(self):
        pass


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
        self.result = {}
        self.testSum = 0
        self.testPass = 0
        self.testFail = 0

    def run(self):
        self.running = True
        f = open(self.reportName)
        for line in f:
            if not line.isspace():
                m = re.search('Ran\s+(\d+)\s+[tes]+\s+in\s+\d+', line)
                if m:
                    self.result["testsum"] = int(m.group(1))
                    break
        for line in f:
            if not line.isspace():
                m = re.search('FAILED \(failures=(\d+)\)', line)
                n = re.search('OK', line)
                if m:
                    self.result["testfail"] = int(m.group(1))
                if n:
                    self.result["testfail"] = 0
                    break
        f.close()
        self.result["testpass"] = self.result["testsum"] - self.result["testfail"]
        self.stop()

    def stop(self):
        self.running = False


class GetFlowLog(threading.Thread):
    """
    {'tx2gClear': 50.9, 'rx2gTkip': 17.7, 'tx5gAes': 93.27, 'rx2gClear': 42.4, 'tx5gTkip': 26.4, 'rx2gAes': 39.1,
    'tx5gClear': 93.6, 'tx2gAes': 47.83, 'rx5gTkip': 19.8, 'rx5gAes': 52.2, 'tx2gTkip': 26.45, 'rx5gClear': 57.4}

    """
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.logPath = v.TEST_SUITE_LOG_PATH
        self.result = {
            "tx2gAes": [],
            "rx2gAes": [],
            "tx2gTkip": [],
            "rx2gTkip": [],
            "tx2gClear": [],
            "rx2gClear": [],
            "tx5gAes": [],
            "rx5gAes": [],
            "tx5gTkip": [],
            "rx5gTkip": [],
            "tx5gClear": [],
            "rx5gClear": [],
            }

    def run(self):
        self.running = True
        logFile = None
        logFileList = list()
        report = open(self.reportName)
        for line in report:
            if not line.isspace():
                m = re.search('testcase\.(AP_.*_FLOW\d?)', line)
                if m:
                    logFile = m.group(1) + ".log"
                    logFile = self.logPath + logFile
                    if logFile not in logFileList:
                        logFileList.append(logFile)
        report.close()
        for lf in logFileList:
            ret = getFlowLogVerbose(lf)
            sw = {
                "2gpsk2tx": 'self.result["tx2gAes"].extend(ret["2gpsk2tx"])',
                "2gpsk2rx": 'self.result["rx2gAes"].extend(ret["2gpsk2rx"])',
                "5gpsk2tx": 'self.result["tx5gAes"].extend(ret["5gpsk2tx"])',
                "5gpsk2rx": 'self.result["rx5gAes"].extend(ret["5gpsk2rx"])',
                "2gpsktx": 'self.result["tx2gAes"].extend(ret["2gpsktx"])',
                "2gpskrx": 'self.result["rx2gAes"].extend(ret["2gpskrx"])',
                "5gpsktx": 'self.result["tx5gAes"].extend(ret["5gpsktx"])',
                "5gpskrx": 'self.result["rx5gAes"].extend(ret["5gpskrx"])',
                "2gtkippsk2tx": 'self.result["tx2gTkip"].extend(ret["2gtkippsk2tx"])',
                "2gtkippsk2rx": 'self.result["rx2gTkip"].extend(ret["2gtkippsk2rx"])',
                "5gtkippsk2tx": 'self.result["tx5gTkip"].extend(ret["5gtkippsk2tx"])',
                "5gtkippsk2rx": 'self.result["rx5gTkip"].extend(ret["5gtkippsk2rx"])',
                "2gtkippsktx": 'self.result["tx2gTkip"].extend(ret["2gtkippsktx"])',
                "2gtkippskrx": 'self.result["rx2gTkip"].extend(ret["2gtkippskrx"])',
                "5gtkippsktx": 'self.result["tx5gTkip"].extend(ret["5gtkippsktx"])',
                "5gtkippskrx": 'self.result["rx5gTkip"].extend(ret["5gtkippskrx"])',
                "2gcleartx": 'self.result["tx2gClear"].extend(ret["2gcleartx"])',
                "2gclearrx": 'self.result["rx2gClear"].extend(ret["2gclearrx"])',
                "5gcleartx": 'self.result["tx5gClear"].extend(ret["5gcleartx"])',
                "5gclearrx": 'self.result["rx5gClear"].extend(ret["5gclearrx"])',
                }
            for key in ret.iterkeys():
                eval(sw.get(key))
        for key, value in self.result.iteritems():
            if len(value) is not 0:
                ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                self.result[key] = ave
            else:
                self.result[key] = 0
        self.stop()

    def stop(self):
        self.running = False
        drawFlowLog(self.result)

def getFlowLogVerbose(logfile):
    """
    OrderedDict([('2gpsk2tx', ['47.7']), ('2gpsk2rx', ['38.8']), ('5gpsk2tx', ['92.8']), ('5gpsk2rx', ['47.0'])])
    :param logfile:
    :return:
    """
    rfEncrypto = None
    result = OrderedDict()
    try:
        log = open(logfile)
        for line in log:
            if not line.isspace():
                m = re.search('#test_assoc_(.*)_sta_(\dg)', line)
                if m:
                    rfEncrypto = m.group(2) + m.group(1)
                    result[rfEncrypto + "tx"] = []
                    result[rfEncrypto + "rx"] = []
                    count1 = 2
                    count2 = 0
                n = re.search('\s0.0-\d{4}.*\s(\d{1,3}\.\d)\sMbits/sec', line)
                if n:
                    count2 += 1
                    if count1 - count2 == 1:
                        tx = n.group(1)
                        if rfEncrypto + "tx" in result:
                            result[rfEncrypto + "tx"].append(tx)
                    elif count2 == count1:
                        rx = n.group(1)
                        if rfEncrypto + "rx" in result:
                            result[rfEncrypto + "rx"].append(rx)
        log.close()
    except IOError as e:
        raise e
    return result

def drawFlowLog(data):
    bar_width = 0.42
    opacity = 0.4
    index = np.arange(6)
    ret = data

    tx = list()
    rx = list()
    tx.append(ret.get("tx2gClear"))
    tx.append(ret.get("tx2gAes"))
    tx.append(ret.get("tx2gTkip"))
    tx.append(ret.get("tx5gClear"))
    tx.append(ret.get("tx5gAes"))
    tx.append(ret.get("tx5gTkip"))
    rx.append(ret.get("rx2gClear"))
    rx.append(ret.get("rx2gAes"))
    rx.append(ret.get("rx2gTkip"))
    rx.append(ret.get("rx5gClear"))
    rx.append(ret.get("rx5gAes"))
    rx.append(ret.get("rx5gTkip"))

    fig, ax = plt.subplots()
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

    plt.xlabel('Radio & cipher suite')
    plt.ylabel('Mbps')
    plt.title('Throughput')
    plt.xticks(index + bar_width, ('2.4g_Clear', '2.4g_AES', '2.4g_TKIP', '5g_Clear', '5g_AES', '5g_TKIP',))
    plt.legend()

    # plt.show()
    plt.savefig("Throughput")
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
                m = re.search('assoc_repeat.*testcase\.(.*)\)', line)
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


if __name__ == '__main__':
    # t = GetTestResult("R1CM 开发版OTA 2.5.48.log")
    # t.start()
    # while t.isAlive():
    #     print time.time()
    # r = getFlowLogVerbose("D:\python\peanuts\R1CM 开发版OTA 2.5.48\AP_CLEAR_CHAN_FLOW2.log")
    info = GetFlowLog("R1CM 开发版OTA 2.5.48.log")
    # info = GetOnlineLog("R1CM 开发版OTA 2.5.48.log")
    # info = GetTestResult("R1CM 开发版OTA 2.5.48.log")
    info.start()
    info.join()
    print info.result



