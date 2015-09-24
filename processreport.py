# -*- coding: gbk -*-
import threading
import re
import time
import common
import var


class ProcessReport(threading.Thread):
    def __init__(self):
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

if __name__ == '__main__':
    t = GetTestResult("R1CM 开发版OTA 2.5.48.log")
    t.start()
    while t.isAlive():
        print time.time()
    print t.testSum, t.testFail, t.testPass





