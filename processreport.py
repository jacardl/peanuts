# -*- coding: gbk -*-
import threading
import re
from collections import *
import numpy as np
import matplotlib.pyplot as plt

import var as v

class ProcessReport(threading.Thread):
    def __init__(self, report):
        threading.Thread.__init__(self)
        self.running = False
        self.report = report
        self.result = OrderedDict()

    def run(self):
        self.running = True
        time = GetTimeUsed(self.report)
        test = GetTestResult(self.report)
        flow = GetFlowLog(self.report)
        online = GetOnlineLog(self.report)
        time.start()
        test.start()
        flow.start()
        online.start()
        while time.isAlive() or test.isAlive() or flow.isAlive() \
                or online.isAlive():
            pass
        self.result.update(sum=test.result["testsum"])
        self.result.update(pa=test.result["testpass"])
        testSum = test.result["testsum"]
        if testSum == 0:
            self.result.update(percent=0)
        else:
            self.result.update(percent=test.result["testpass"]/float(test.result["testsum"])*100)

        self.result.update(time=time.timeUsed)
        self.result.update(onlinesum=online.result["pass"]+online.result["fail"])
        self.result.update(onlinepa=online.result["pass"])
        onlineSum = online.result["pass"]+online.result["fail"]
        if onlineSum == 0:
            self.result.update(onlinepercent=0)
        else:
            self.result.update(onlinepercent=online.result["pass"]/float(onlineSum)*100)
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
        self.result = {}

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
        self.resultAes = {
            "tx1": [],
            "rx1": [],
            "tx6": [],
            "rx6": [],
            "tx11": [],
            "rx11": [],
            "tx13": [],
            "rx13": [],
            "tx36": [],
            "rx36": [],
            "tx52": [],
            "rx52": [],
            "tx149": [],
            "rx149": [],
            "tx165": [],
            "rx165": [],
            }
        self.resultTkip = {
            "tx1": [],
            "rx1": [],
            "tx6": [],
            "rx6": [],
            "tx11": [],
            "rx11": [],
            "tx13": [],
            "rx13": [],
            "tx36": [],
            "rx36": [],
            "tx52": [],
            "rx52": [],
            "tx149": [],
            "rx149": [],
            "tx165": [],
            "rx165": [],
            }
        self.resultClear = {
            "tx1": [],
            "rx1": [],
            "tx6": [],
            "rx6": [],
            "tx11": [],
            "rx11": [],
            "tx13": [],
            "rx13": [],
            "tx36": [],
            "rx36": [],
            "tx52": [],
            "rx52": [],
            "tx149": [],
            "rx149": [],
            "tx165": [],
            "rx165": [],
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
        if len(logFileList) != 0:
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
            sw2 = {
                "tx1psk2": 'self.resultAes["tx1"].extend(ret2["tx1psk2"])',
                "rx1psk2": 'self.resultAes["rx1"].extend(ret2["rx1psk2"])',
                "tx6psk2": 'self.resultAes["tx6"].extend(ret2["tx6psk2"])',
                "rx6psk2": 'self.resultAes["rx6"].extend(ret2["rx6psk2"])',
                "tx11psk2": 'self.resultAes["tx11"].extend(ret2["tx11psk2"])',
                "rx11psk2": 'self.resultAes["rx11"].extend(ret2["rx11psk2"])',
                "tx13psk2": 'self.resultAes["tx13"].extend(ret2["tx13psk2"])',
                "rx13psk2": 'self.resultAes["rx13"].extend(ret2["rx13psk2"])',
                "tx1psk": 'self.resultAes["tx1"].extend(ret2["tx1psk"])',
                "rx1psk": 'self.resultAes["rx1"].extend(ret2["rx1psk"])',
                "tx6psk": 'self.resultAes["tx6"].extend(ret2["tx6psk"])',
                "rx6psk": 'self.resultAes["rx6"].extend(ret2["rx6psk"])',
                "tx11psk": 'self.resultAes["tx11"].extend(ret2["tx11psk"])',
                "rx11psk": 'self.resultAes["rx11"].extend(ret2["rx11psk"])',
                "tx13psk": 'self.resultAes["tx13"].extend(ret2["tx13psk"])',
                "rx13psk": 'self.resultAes["rx13"].extend(ret2["rx13psk"])',
                "tx1tkippsk2": 'self.resultTkip["tx1"].extend(ret2["tx1tkippsk2"])',
                "rx1tkippsk2": 'self.resultTkip["rx1"].extend(ret2["rx1tkippsk2"])',
                "tx6tkippsk2": 'self.resultTkip["tx6"].extend(ret2["tx6tkippsk2"])',
                "rx6tkippsk2": 'self.resultTkip["rx6"].extend(ret2["rx6tkippsk2"])',
                "tx11tkippsk2": 'self.resultTkip["tx11"].extend(ret2["tx11tkippsk2"])',
                "rx11tkippsk2": 'self.resultTkip["rx11"].extend(ret2["rx11tkippsk2"])',
                "tx13tkippsk2": 'self.resultTkip["tx13"].extend(ret2["tx13tkippsk2"])',
                "rx13tkippsk2": 'self.resultTkip["rx13"].extend(ret2["rx13tkippsk2"])',
                "tx1tkippsk": 'self.resultTkip["tx1"].extend(ret2["tx1tkippsk"])',
                "rx1tkippsk": 'self.resultTkip["rx1"].extend(ret2["rx1tkippsk"])',
                "tx6tkippsk": 'self.resultTkip["tx6"].extend(ret2["tx6tkippsk"])',
                "rx6tkippsk": 'self.resultTkip["rx6"].extend(ret2["rx6tkippsk"])',
                "tx11tkippsk": 'self.resultTkip["tx11"].extend(ret2["tx11tkippsk"])',
                "rx11tkippsk": 'self.resultTkip["rx11"].extend(ret2["rx11tkippsk"])',
                "tx13tkippsk": 'self.resultTkip["tx13"].extend(ret2["tx13tkippsk"])',
                "rx13tkippsk": 'self.resultTkip["rx13"].extend(ret2["rx13tkippsk"])',
                "tx1clear": 'self.resultClear["tx1"].extend(ret2["tx1clear"])',
                "rx1clear": 'self.resultClear["rx1"].extend(ret2["rx1clear"])',
                "tx6clear": 'self.resultClear["tx6"].extend(ret2["tx6clear"])',
                "rx6clear": 'self.resultClear["rx6"].extend(ret2["rx6clear"])',
                "tx11clear": 'self.resultClear["tx11"].extend(ret2["tx11clear"])',
                "rx11clear": 'self.resultClear["rx11"].extend(ret2["rx11clear"])',
                "tx13clear": 'self.resultClear["tx13"].extend(ret2["tx13clear"])',
                "rx13clear": 'self.resultClear["rx13"].extend(ret2["rx13clear"])',

                "tx36psk2": 'self.resultAes["tx36"].extend(ret2["tx36psk2"])',
                "rx36psk2": 'self.resultAes["rx36"].extend(ret2["rx36psk2"])',
                "tx52psk2": 'self.resultAes["tx52"].extend(ret2["tx52psk2"])',
                "rx52psk2": 'self.resultAes["rx52"].extend(ret2["rx52psk2"])',
                "tx149psk2": 'self.resultAes["tx149"].extend(ret2["tx149psk2"])',
                "rx149psk2": 'self.resultAes["rx149"].extend(ret2["rx149psk2"])',
                "tx165psk2": 'self.resultAes["tx165"].extend(ret2["tx165psk2"])',
                "rx165psk2": 'self.resultAes["rx165"].extend(ret2["rx165psk2"])',
                "tx36psk": 'self.resultAes["tx36"].extend(ret2["tx36psk"])',
                "rx36psk": 'self.resultAes["rx36"].extend(ret2["rx36psk"])',
                "tx52psk": 'self.resultAes["tx52"].extend(ret2["tx52psk"])',
                "rx52psk": 'self.resultAes["rx52"].extend(ret2["rx52psk"])',
                "tx149psk": 'self.resultAes["tx149"].extend(ret2["tx149psk"])',
                "rx149psk": 'self.resultAes["rx149"].extend(ret2["rx149psk"])',
                "tx165psk": 'self.resultAes["tx165"].extend(ret2["tx165psk"])',
                "rx165psk": 'self.resultAes["rx165"].extend(ret2["rx165psk"])',
                "tx36tkippsk2": 'self.resultTkip["tx36"].extend(ret2["tx36tkippsk2"])',
                "rx36tkippsk2": 'self.resultTkip["rx36"].extend(ret2["rx36tkippsk2"])',
                "tx52tkippsk2": 'self.resultTkip["tx52"].extend(ret2["tx52tkippsk2"])',
                "rx52tkippsk2": 'self.resultTkip["rx52"].extend(ret2["rx52tkippsk2"])',
                "tx149tkippsk2": 'self.resultTkip["tx149"].extend(ret2["tx149tkippsk2"])',
                "rx149tkippsk2": 'self.resultTkip["rx149"].extend(ret2["rx149tkippsk2"])',
                "tx165tkippsk2": 'self.resultTkip["tx165"].extend(ret2["tx165tkippsk2"])',
                "rx165tkippsk2": 'self.resultTkip["rx165"].extend(ret2["rx165tkippsk2"])',
                "tx36tkippsk": 'self.resultTkip["tx36"].extend(ret2["tx36tkippsk"])',
                "rx36tkippsk": 'self.resultTkip["rx36"].extend(ret2["rx36tkippsk"])',
                "tx52tkippsk": 'self.resultTkip["tx52"].extend(ret2["tx52tkippsk"])',
                "rx52tkippsk": 'self.resultTkip["rx52"].extend(ret2["rx52tkippsk"])',
                "tx149tkippsk": 'self.resultTkip["tx149"].extend(ret2["tx149tkippsk"])',
                "rx149tkippsk": 'self.resultTkip["rx149"].extend(ret2["rx149tkippsk"])',
                "tx165tkippsk": 'self.resultTkip["tx165"].extend(ret2["tx165tkippsk"])',
                "rx165tkippsk": 'self.resultTkip["rx165"].extend(ret2["rx165tkippsk"])',
                "tx36clear": 'self.resultClear["tx36"].extend(ret2["tx36clear"])',
                "rx36clear": 'self.resultClear["rx36"].extend(ret2["rx36clear"])',
                "tx52clear": 'self.resultClear["tx52"].extend(ret2["tx52clear"])',
                "rx52clear": 'self.resultClear["rx52"].extend(ret2["rx52clear"])',
                "tx149clear": 'self.resultClear["tx149"].extend(ret2["tx149clear"])',
                "rx149clear": 'self.resultClear["rx149"].extend(ret2["rx149clear"])',
                "tx165clear": 'self.resultClear["tx165"].extend(ret2["tx165clear"])',
                "rx165clear": 'self.resultClear["rx165"].extend(ret2["rx165clear"])',
            }
            for lf in logFileList:
                ret = getFlowLogVerbose(lf)
                ret2 = getChannelFlowLogVerbose(lf)
                for key in ret.iterkeys():
                    eval(sw.get(key))
                for key in ret2.iterkeys():
                    eval(sw2.get(key))
            for key, value in self.result.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.result[key] = ave
                else:
                    self.result[key] = 0
            drawFlowLog(self.result)

            for key, value in self.resultAes.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.resultAes[key] = ave
                else:
                    self.resultAes[key] = 0
            drawChannelFlowLog(self.resultAes, "AES")

            for key, value in self.resultTkip.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.resultTkip[key] = ave
                else:
                    self.resultTkip[key] = 0
            drawChannelFlowLog(self.resultTkip, "TKIP")

            for key, value in self.resultClear.iteritems():
                if len(value) is not 0:
                    ave = round(float(reduce(lambda i, j: float(i)+float(j), value))/len(value), 2)
                    self.resultClear[key] = ave
                else:
                    self.resultClear[key] = 0
            drawChannelFlowLog(self.resultClear, "Clear")
            self.stop()
        else:
            self.stop()

    def stop(self):
        self.running = False


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
                    rfEncrypto = m.group(2) + m.group(1)  # 2gclear/2gpsk2...
                    key1 = rfEncrypto + "tx"
                    key2 = rfEncrypto + "rx"
                    if not key1 in result:
                        result[key1] = []
                        result[key2] = []
                    count1 = 2
                    count2 = 0
                n = re.search('\s0.0-\d{1,4}.*\s(\d{1,3}\.?\d{1,2})?\sMbits/sec', line)
                if n:
                    count2 += 1
                    if count1 - count2 == 1:
                        tx = n.group(1)
                        result[rfEncrypto + "tx"].append(tx)
                    elif count2 == count1:
                        rx = n.group(1)
                        result[rfEncrypto + "rx"].append(rx)
        log.close()
    except IOError as e:
        raise e
    return result


def getChannelFlowLogVerbose(logfile):
    """
    OrderedDict([('tx1clear', ['28.9']), ('rx1clear', ['2.37']), ('tx36clear', ['126']), ('rx36clear', ['167'])])
    """
    channel2 = None
    channel5 = None
    m = re.search('CHAN(\d{1,3})_(\d{1,3})', logfile)
    if m:
        channel2 = m.group(1)
        channel5 = m.group(2)

    result = OrderedDict()
    try:
        log = open(logfile)
        for line in log:
            if not line.isspace():
                m = re.search('#test_assoc_(.*)_sta_(\dg)', line)
                if m:
                    encrypto = m.group(1)
                    rf = m.group(2)
                    if rf == "2g":
                        key1 = 'tx' + channel2 + encrypto
                        key2 = 'rx' + channel2 + encrypto
                        if not key1 in result:
                            result[key1] = []
                            result[key2] = []
                    elif rf == "5g":
                        key1 = 'tx' + channel5 + encrypto
                        key2 = 'rx' + channel5 + encrypto
                        if not key1 in result:
                            result[key1] = []
                            result[key2] = []
                    count1 = 2
                    count2 = 0
                n = re.search('\s0.0-\d{1,4}.*\s(\d{1,3}\.?\d{1,2})?\sMbits/sec', line)
                if n:
                    count2 += 1
                    if count1 - count2 == 1:
                        tx = n.group(1)
                        sw2 = {
                            "2g": "result['tx' + channel2 + encrypto].append(tx)",
                            "5g": "result['tx' + channel5 + encrypto].append(tx)",
                        }
                        eval(sw2.get(rf))
                    elif count2 == count1:
                        rx = n.group(1)
                        sw3 = {
                            "2g": "result['rx' + channel2 + encrypto].append(rx)",
                            "5g": "result['rx' + channel5 + encrypto].append(rx)",
                        }
                        eval(sw3.get(rf))
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

    tx.append(ret.get("tx5gAes"))
    tx.append(ret.get("tx5gClear"))
    tx.append(ret.get("tx5gTkip"))
    tx.append(ret.get("tx2gAes"))
    tx.append(ret.get("tx2gClear"))
    tx.append(ret.get("tx2gTkip"))

    rx.append(ret.get("rx5gAes"))
    rx.append(ret.get("rx5gClear"))
    rx.append(ret.get("rx5gTkip"))
    rx.append(ret.get("rx2gAes"))
    rx.append(ret.get("rx2gClear"))
    rx.append(ret.get("rx2gTkip"))


    fig, ax = plt.subplots(figsize=(12, 6))
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

    plt.xlabel('Radio & Cipher Suite')
    plt.ylabel('Mbps')
    plt.suptitle(v.MAIL_PIC2.split(".")[0].title())
    plt.xticks(index + bar_width, ('5g_AES', '5g_Clear', '5g_TKIP',  '2.4g_AES', '2.4g_Clear', '2.4g_TKIP',))
    plt.legend()

    # plt.show()
    plt.savefig(v.MAIL_PIC2)
    plt.close()


def drawChannelFlowLog(data, encrypto):
    bar_width = 0.42
    opacity = 0.4
    index = np.arange(8)
    ret = data
    title = v.MAIL_PIC3.split(".")[0]%encrypto
    title = title.replace("_", " ")
    tx = list()
    rx = list()
    tx.append(ret.get("tx36"))
    tx.append(ret.get("tx52"))
    tx.append(ret.get("tx149"))
    tx.append(ret.get("tx165"))
    tx.append(ret.get("tx1"))
    tx.append(ret.get("tx6"))
    tx.append(ret.get("tx11"))
    tx.append(ret.get("tx13"))
    rx.append(ret.get("rx36"))
    rx.append(ret.get("rx52"))
    rx.append(ret.get("rx149"))
    rx.append(ret.get("rx165"))
    rx.append(ret.get("rx1"))
    rx.append(ret.get("rx6"))
    rx.append(ret.get("rx11"))
    rx.append(ret.get("rx13"))

    fig, ax = plt.subplots(figsize=(12, 6))
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

    plt.xlabel('Channel')
    plt.ylabel('Mbps')
    # plt.title(title)
    plt.suptitle(title.title())
    plt.xticks(index + bar_width, ('36', '52', '149', '165', '1', '6', '11', '13'))
    plt.legend()

    # plt.show()
    picName = v.MAIL_PIC3%encrypto
    plt.savefig(picName)
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
    # print getFlowLogVerbose("E:\peanuts\LOG_TEST_SUITE\AP_CLEAR_CHAN_FLOW2.log")
    info = GetFlowLog("R2D 稳定版OTA 2.8.6.log")
    # info = GetOnlineLog("R1CM 开发版OTA 2.5.48.log")
    # info = GetTestResult("R1CM 开发版OTA 2.5.48.log")
    # info = ProcessReport("R2D 稳定版OTA 2.6.12.log")
    info.start()
    info.join()
    print info.result
    print info.resultAes
    print info.resultTkip
    print info.resultClear
    # print getChannelFlowLogVerbose("R2D 稳定版OTA 2.8.6\AP_MIXEDPSK_CHAN11_149_FLOW2.log")
    # print getFlowLogVerbose("R2D 稳定版OTA 2.8.6\AP_MIXEDPSK_CHAN11_149_FLOW2.log")



