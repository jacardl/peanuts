# -*- coding: gbk -*-
import threading
import re
from collections import *
import time
import os
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
                    self.testSum = m.group(1)
                    break
        for line in f:
            if not line.isspace():
                m = re.search('FAILED \(failures=(\d+)\)', line)
                n = re.search('OK', line)
                if m:
                    self.testFail = m.group(1)
                if n:
                    self.testFail = 0
                    break
        f.close()
        self.testSum = int(self.testSum)
        self.testFail = int(self.testFail)
        self.testPass = self.testSum - self.testFail
        self.stop()

    def stop(self):
        self.running = False


class GetFlowLog(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.reportName = report
        self.logPath = v.TEST_SUITE_LOG_PATH
        self.tx2gAes = []
        self.rx2gAes = []
        self.tx2gTkip = []
        self.rx2gTkip = []
        self.tx2gClear = []
        self.rx2gClear = []
        self.tx5gAes = []
        self.rx5gAes = []
        self.tx5gTkip = []
        self.rx5gTkip = []
        self.tx5gClear = []
        self.rx5gClear = []

    def run(self):
        self.running = True
        logFile = None
        logName = None
        report = open(self.reportName)
        for line in report:
            if not line.isspace():
                m = re.search('testcase\.(AP_.*_FLOW\d)', line)
                if m:
                    logName = m.group(1) + ".log"
                    logName = self.logPath + logName
                    if logName is not logFile:
                        logFile = logName
                        log = open(logFile)



        report.close()
        self.stop()

    def stop(self):
        self.running = False

def getFlowLogVerbose(logfile):
    count1 = 0
    count2 = 0
    result = OrderedDict()
    try:
        log = open(logfile)
        for line in log:
            if not line.isspace():
                m = re.search('#test_assoc_(.*)_sta_(\dg)', line)
                if m:
                    rfEncrpto = m.group(2) + m.group(1)
                    count1 += 2
                n = re.search('\s0.0-\d{4}.*\s(\d{1,3}\.\d)\sMbits/sec', line)
                if n:
                    count2 += 1
                    if count1 - count2 == 1:
                        tx = n.group(1)
                        if rfEncrpto + "tx" in result:
                            result[rfEncrpto + "tx"].append(tx)
                        else:
                            result[rfEncrpto + "tx"] = [tx]
                    elif count2 == count1:
                        rx = n.group(1)
                        if rfEncrpto + "rx" in result:
                            result[rfEncrpto + "rx"].append(rx)
                        else:
                            result[rfEncrpto + "rx"] = [rx]
        log.close()
    except IOError as e:
        raise e

    return result




if __name__ == '__main__':
    # t = GetTestResult("R1CM 开发版OTA 2.5.48.log")
    # t.start()
    # while t.isAlive():
    #     print time.time()
    # print t.testSum, t.testFail, t.testPass
    print getFlowLogVerbose("D:\python\peanuts\R1CM 开发版OTA 2.5.48\AP_MIXEDPSK_CHAN_FLOW2.log")




