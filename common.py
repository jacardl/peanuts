# -*- coding: gbk -*-
import os
import time as t
import re
import threading
import telnetlib
from collections import *
import paramiko as pm
import subprocess
import urllib
import var as v


class SshClient(object):
    def __init__(self, connection):
        self.connectionType = connection

    def connect(self, host, userid, password=None):
        if self.connectionType == 1:  # represent ssh
            self.hostname = host
            self.client = pm.SSHClient()
            self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
            try:
                if password is not None:
                    self.client.connect(host, username=userid, password=password)
                else:
                    print 'please input password'
                return True
            except:
                print 'connection is failed. please check your remote settings.'
                return False

        elif self.connectionType == 2:  # represent telnet
            self.hostname = host.encode("utf-8")
            self.username = userid.encode("utf-8")
            self.password = password.encode("utf-8")
            try:
                # connect to telnet server
                self.tn = telnetlib.Telnet(self.hostname, port=23, timeout=10)
                # self.tn.set_debuglevel(2)

                # login
                if self.username != "":
                    self.tn.read_until("XiaoQiang login: ", 10)
                    self.tn.write(self.username + "\n")
                    self.tn.read_until("Password: ", 10)
                    self.tn.write(self.password + "\n")

                self.tn.read_until("root@XiaoQiang:", 10)
                return True

            except Exception, e:
                print 'connection is failed. please check your remote settings.'
                return False

    def command(self, *args):
        if self.connectionType == 1:
            cmd = ";".join(args)
            if checkContainChinese(cmd):
                cmd = unicode(cmd, 'gbk')

            stdin, stdout, stderr = self.client.exec_command(cmd)
            self.out = stdout.readlines()  # input and output are unicode
            for index in range(len(self.out)):
                try:
                    self.out[index] = self.out[index].encode("gbk")
                except Exception, e:
                    self.out[index] = ""
                    pass
            return self.out
        elif self.connectionType == 2:
            cmd = ";".join(args)  # input and output are utf-8
            if checkContainChinese(cmd):
                cmd = cmd.decode("gbk")
                cmd = cmd.encode("utf-8")
            self.tn.write(cmd + "\n")
            self.out = self.tn.read_until("root@XiaoQiang:", 60)
            self.out = self.out.split("\n")
            del self.out[0]  # del command and :~#
            del self.out[-1]
            return self.out

    def config(self, arg):
        if self.connectionType == 1:
            cmd = arg
            if checkContainChinese(cmd):
                cmd = unicode(cmd, 'gbk')

            stdin, stdout, stderr = self.client.exec_command(cmd)
            err = stderr.readlines()
            # keepGoing = 0
            # while keepGoing < 3 and len(err) != 0:
            # stdin, stdout, stderr = self.client.exec_command(arg)
            # err = stderr.read()
            # keepGoing += 1
            return err
        elif self.connectionType == 2:
            cmd = arg
            if checkContainChinese(cmd):
                cmd = cmd.decode("gbk")
                cmd = cmd.encode("utf-8")

            self.tn.write(cmd + "\n")
            self.out = self.tn.read_until("root@XiaoQiang:", 60)
            self.out = self.out.split("\n")
            del self.out[0]
            del self.out[-1]
            # for index in range(len(self.out)):
            # self.out[index] = self.out[index].decode("utf-8").encode("gbk")
            return self.out

    def close(self):
        if self.connectionType == 1:
            self.client.close()
        elif self.connectionType == 2:
            self.tn.close()


class SshCommand(SshClient):
    def getPidList(self):
        self.outPidList = []
        out = self.command('ps w | grep -v [[]')
        del out[0]
        for index in range(len(out)):
            self.outPidList.append(self.out[index][:5])

    def getPidNameDic(self):
        self.outPidNameDic = {}
        out = self.command('ps w | grep -v [[]')
        del out[0]
        for index in range(len(out)):
            keypid = self.out[index][:5]
            value = self.out[index][26:]
            self.outPidNameDic[keypid] = value

    def getPidNameVSZDic(self):
        self.outPidNameVSZDic = {}
        out = self.command('ps w | grep -v [[]')
        del out[0]
        for index in range(len(out)):
            pid = out[index][:5].strip()
            name = out[index][26:].strip()
            vsz = out[index][14:20].strip()
            try:
                vsz = int(vsz)
                self.outPidNameVSZDic['#'.join([name, pid])] = vsz
            except:
                result = self.getDaemonMemStatus(pid)
                vsz = result["vmsize"]
                vsz = int(vsz)
                self.outPidNameVSZDic['#'.join([name, pid])] = vsz

    def getDaemonMemStatus(self, pid):
        cmd = "cat /proc/" + pid + "/status"
        ret = self.command(cmd)
        result = {}
        for line in ret:
            m = re.search('VmSize:\s*(\d+)', line)
            if m:
                result["vmsize"] = m.group(1)
                return result
            else:
                result["vmsize"] = ""
        return result

    def getTotalMemInfo(self):
        cmd = "free"
        ret = self.command(cmd)
        result = {}
        for line in ret:
            m = re.search('-/\+ buffers/cache:\s+(\d+)\s+(\d+)', line)
            if m:
                result["used"] = int(m.group(1))
                result["free"] = int(m.group(2))
                return result
            else:
                result["used"] = ""
                result["free"] = ""
        return result

    def getTimeStr(self):
        date = self.command('date')
        time = date[0][4:19]
        return time

    def getTitleResDic(self, *args):
        cmd = args
        outTitleResDic = {}
        for c in cmd:
            outTitleResDic['**********' + c + '**********\n' \
                                              '**********' + c + '**********\n**********' + c + '**********\n' \
                                                                                                '**********' + c + '**********\n**********' + c + '**********\n'] = self.command(
                c)
        return outTitleResDic

    def getHardware(self):
        cmd = "bootinfo"
        ret = self.command(cmd)
        for line in ret:
            m = re.search('option HARDWARE \'([A-Z0-9]{3,})\'', line)
            if m:
                result = m.group(1)
                return result
            else:
                result = ""
        return result

    def getRomVersion(self):
        cmd = "bootinfo"
        ret = self.command(cmd)
        result = {"version": "", "channel": ""}
        for line in ret:
            m = re.search('option ROM \'(\d+\.\d+.\d+)\'', line)
            n = re.search('option CHANNEL \'(\w+)\'', line)
            if m:
                result["version"] = m.group(1)
            if n:
                result["channel"] = n.group(1)
        channelDic = {"current": " daily build ",
                      "stable": " 开发版OTA ",
                      "release": " 稳定版OTA "}
        result["channel"] = channelDic.get(result["channel"])
        return result

    def setMailTitle(self):
        hardware = self.getHardware()
        Rom = self.getRomVersion()
        title = "【" + hardware + Rom["channel"] + Rom["version"] + "】自动化测试报告"
        return title

    def setReportName(self):
        hardware = self.getHardware()
        Rom = self.getRomVersion()
        name = hardware + Rom["channel"] + Rom["version"]
        return name

class SerialClient(object):
    pass


def connectionCheck(connectiontype, ip=None, port=None, user=None, password=None):
    client = SshCommand(connectiontype)
    result = client.connect(ip, user, password)
    if result is True:
        hardware = client.getHardware()
        if hardware == "":
            return False, ""
        client.close()
        return result, hardware
    elif result is False:
        return result, ""


def convertStrToBashStr(string):
    if string is not None:
        string = re.sub('`', '\`', string)
        string = re.sub('"', '\\"', string)
        string = '"' + string + '"'
    return string



def convertStrToURL(string):
    if string is not None:
        return urllib.quote(string)


def checkContainChinese(string):
    checkstr = unicode(string, 'gbk')
    for ch in checkstr:
        if u'\u4e00' <= ch <= u'\u9ffff':
            return True
    return False


def setConfig(terminal, command, logname):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        err = terminal.config(command)
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#Config to ' + terminal.hostname + '#')
        f.write(command + '\n')
        f.writelines(err)
        f.write('\n')
        f.close()

    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#Config to ' + terminal.hostname + ' failed#')
        f.write(command + '\n')
        f.write(str(e))
        f.write('\n')
        terminal.close()
        f.close()


def setGet(terminal, command, logname):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        ret = terminal.command(command)
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#Get from ' + terminal.hostname + '#')
        f.write(command + '\n')
        f.writelines(ret)
        f.write('\n')
        f.close()
        return ret

    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#Get from ' + terminal.hostname + ' failed#')
        f.write(command + '\n')
        f.write(str(e))
        f.write('\n')
        terminal.close()
        f.close()


def setAdbShell(device, command, logname):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)
    if device != "":
        adb = "adb " + "-s " + device + " shell "
    else:
        adb = "adb shell "
    command = adb + command
    try:
        ret = os.popen(command).readlines()
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#ADB#')
        f.write(command + '\n')
        f.writelines(ret)
        f.write('\n')
        f.close()
        return ret
    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#ADB failed#')
        f.write(command + '\n')
        f.writelines(str(e))
        f.write('\n')
        f.close()


def setShell(command, cwd=None, timeout=30, logname=None):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        if cwd is not None:
            pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=cwd)
        else:
            pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        def killproc(p1, p2):
            p1.kill()
            subprocess.call('taskkill /F /IM ' + p2)

        timer = threading.Timer(timeout, killproc, [pipe, command.split()[0]])
        try:
            timer.start()
            ret = pipe.stdout.readlines()
        finally:
            timer.cancel()
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#OS#')
        f.write(command + '\n')
        f.writelines(ret)
        f.write('\n')
        f.close()
        return ret
    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#OS failed#')
        f.write(command + '\n')
        f.writelines(str(e))
        f.write('\n')
        f.close()


def getApcli0Conn(terminal, logname):
    """apcli0    Connstatus:
    ApCli0 Connected AP : 00:90:4C:23:45:A0   SSID:R2D-JAC"""

    command = 'iwpriv apcli0 Connstatus'
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('(([\da-fA-F]{2}:){5}[\da-fA-F]{2}).*SSID:(.{1,33})', line)

        if m:
            result['bssid'] = m.group(1)
            result['ssid'] = m.group(3).strip()
            return result
        else:
            result['bssid'] = ''
            result['ssid'] = ''
    return result


def getApclii0Conn(terminal, logname):
    """apclii0   Connstatus:
    =============================================================
    ApCli0 Connected AP : 12:34:56:78:00:1B   SSID:R2D-JAC_5G
    ============================================================="""

    command = 'iwpriv apclii0 Connstatus'
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('(([\da-fA-F]{2}:){5}[\da-fA-F]{2}).*SSID:(.{1,33})', line)

        if m:
            result['bssid'] = m.group(1)
            result['ssid'] = m.group(3).strip()
            return result

        else:
            result['bssid'] = ''
            result['ssid'] = ''
    return result


def getIntfHWAddr(terminal, intf, logname):
    if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
        commandDic = {
            v.INTF_2G: "ifconfig wl1",
            v.INTF_5G: "ifconfig wl0",
            v.INTF_GUEST: "ifconfig wl1.2"
        }
    elif v.DUT_MODULE == "R1CM" or v.DUT_MODULE == "R1CL":
        commandDic = {
            v.INTF_2G: "ifconfig wl1",
            v.INTF_5G: "ifconfig wl0",
            v.INTF_GUEST: "ifconfig wl3"
        }

    command = commandDic.get(intf)
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('HWaddr\s(([\da-fA-F]{2}:){5}[\da-fA-F]{2})', line)
        if m:
            result['mac'] = m.group(1)
            return result
        else:
            result['mac'] = ''
    return result


def getIntfIpAddr(terminal, intf, logname):
    """apclii0   Link encap:Ethernet  HWaddr 8E:BE:BE:40:0A:35
              inet addr:192.168.32.125  Bcast:192.168.32.255  Mask:255.255.255.0
              inet6 addr: fe80::8cbe:beff:fe40:a35/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)"""

    if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
        commandDic = {
            v.INTF_2G: "ifconfig wl1",
            v.INTF_5G: "ifconfig wl0",
            v.INTF_GUEST: "ifconfig wl1.2"
        }
    elif v.DUT_MODULE == "R1CM" or v.DUT_MODULE == "R1CL":
        commandDic = {
            v.INTF_2G: "ifconfig wl1",
            v.INTF_5G: "ifconfig wl0",
            v.INTF_GUEST: "ifconfig wl3"
        }
    command = commandDic.get(intf)
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('inet addr:((\d{1,3}\.){3}\d{1,3})', line)

        if m:
            result['ip'] = m.group(1)
            return result
        else:
            result['ip'] = ''
    return result


def getPingStatus(terminal, target, count, logname):
    """
    root@XiaoQiang:~# ping 192.168.31.1 -c 5
    PING 192.168.31.1 (192.168.31.1) 56(84) bytes of data.
    64 bytes from 192.168.31.1: icmp_req=1 ttl=64 time=0.197 ms
    64 bytes from 192.168.31.1: icmp_req=2 ttl=64 time=0.097 ms
    64 bytes from 192.168.31.1: icmp_req=3 ttl=64 time=0.104 ms
    64 bytes from 192.168.31.1: icmp_req=4 ttl=64 time=0.111 ms
    64 bytes from 192.168.31.1: icmp_req=5 ttl=64 time=0.106 ms

    --- 192.168.31.1 ping statistics ---
    5 packets transmitted, 5 received, 0% packet loss, time 3997ms
    rtt min/avg/max/mdev = 0.097/0.123/0.197/0.037 ms
    """
    command = 'ping -c ' + str(count) + ' ' + target
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('(\d{1,3})%\spacket\sloss', line)

        if m:
            result['loss'] = int(m.group(1))
            result['pass'] = 100 - int(m.group(1))
            return result
        else:
            result['loss'] = 100
            result['pass'] = 0
    return result


def getSiteSurvey(terminal, intf, logname):
    command = 'iwpriv ' + intf + ' get_site_survey'
    setIwpriv(terminal, intf, 'SiteSurvey', '1', logname)
    t.sleep(1)
    ret = setGet(terminal, command, logname)
    result = {'channel': [], 'ssid': [], 'bssid': [], 'sec': []}
    for line in ret:
        m = re.search('(^\d{1,3})\s*(.{1,33})\s+(([\da-fA-F]{2}:){5}[\da-fA-F]{2})[\s]*([\S]*)', line)
        try:
            result['channel'].append(m.group(1))
            result['ssid'].append(m.group(2).strip())
            result['bssid'].append(m.group(3))
            result['sec'].append(m.group(5))
        except Exception:
            pass
    return result


def getWlanTxPower(terminal, dut, intf, logname):
    if dut == "R1D" or dut == "R2D":
        commandDic = {"2g": "wl -i wl1 curpower | grep 'Maximum Power Target among all rates'",
                      "5g": "wl -i wl0 curpower | grep 'Maximum Power Target among all rates'", }
        command = commandDic.get(intf)
        ret = setGet(terminal, command, logname)
        for line in ret:
            m = re.search('(\d{1,3}\.\d{1,2}\s*){2,3}', line)
            if m:
                power = m.group(0)
                powerList = power.split()
                sum = 0.0
                for c in range(len(powerList)):
                    sum += float(powerList[c])
                result = sum / len(powerList)
                return float(result)
            else:
                result = 0
        return float(result)

    elif dut == "R1CM" or dut == "R1CL":
        commandDic = {"2g": "iwconfig wl1 | grep 'Tx-Power='",
                      "5g": "iwconfig wl0 | grep 'Tx-Power='", }
        command = commandDic.get(intf)
        ret = setGet(terminal, command, logname)
        for line in ret:
            m = re.search('(\d*)\sdBm', line)
            if m:
                result = m.group(1)
                return float(result)
            else:
                result = 0
        return float(result)


def  getWlanLastEstPower(terminal, dut, intf, logname):

    if dut == "R1D" or dut == "R2D":
        commandDic = {"2g": "wl -i wl1 curpower | grep 'Last est. power'",
                      "5g": "wl -i wl0 curpower | grep 'Last est. power'", }
        command = commandDic.get(intf)
        ret = setGet(terminal, command, logname)
        for line in ret:
            m = re.search('\d*\.\d*.*', line)
            if m:
                power = m.group(0)
                powerList = power.split(":")
                powerList = powerList[1].split()
                for i in xrange(len(powerList)):
                    powerList[i] = float(powerList[i])
                for j in powerList:
                    if j == 0:
                        powerList.remove(0)
                if len(powerList) != 0:
                    result = reduce(lambda i, j: i + j, powerList)/len(powerList)
                else:
                    result = 0
            else:
                result = 0
        return float(result)

    elif dut == "R1CM" or dut == "R1CL":
        return 0


def getWlanInfo(terminal, intf, logname):
    commandDic = {"2g": "iwinfo wl1 info",
                  "5g": "iwinfo wl0 info",
                  "guest": "iwinfo wl1.2 info", }

    command = commandDic.get(intf)
    ret = setGet(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('Channel: (\d+)', line)
        if m:
            result["channel"] = m.group(1)
            return result
        else:
            result["channel"] = ""
    return result


def getFilePath(terminal, logname, **kargs):
    command = "find %s -name %s"%(kargs["path"], kargs["pattern"])
    ret = setGet(terminal, command, logname)
    for line in ret:
        if len(line) is not 0:
            return line[:-1]
    return ""


def getUptime(terminal, logname):
    command = 'uptime'
    ret = setGet(terminal, command, logname)
    for line in ret:
        m = re.search('up\s(\d{1,})[\s:](\w*),', line)
        if m:
            if m.group(2) == 'min':
                return int(m.group(1))
            elif m.group(2).isdigit():
                time = int(m.group(1)) * 60 + int(m.group(2))
                return time


def getDaemonRss(terminal):
    pidNameRss = OrderedDict()
    ret = terminal.command('ps w | grep -v [[]')
    del ret[0]
    for line in ret:
        pid = line[:5].strip()
        name = line[26:].strip()
        rss = getDaemonPidRss(terminal, pid)
        pidNameRss['#'.join([name, pid])] = rss
    return pidNameRss


def getDaemonPidRss(terminal, pid):
    cmd = "cat /proc/%s/status"%pid
    ret = terminal.command(cmd)
    for line in ret:
        if not line.isspace():
            m = re.search('VmRSS:\s*(\d+)\D*', line)
            if m:
                return int(m.group(1))


def getKernelSlab(terminal):
    result = OrderedDict()
    cmd = 'cat /proc/slabinfo'
    ret = terminal.command(cmd)
    for line in ret[2:]:
        cacheList = line.split()
        result[cacheList[0]] = round(float(cacheList[2]) * float(cacheList[3])/1024, 2)
    result["Total Cache"] = reduce(lambda x, y: x + y, result.itervalues())
    return result


def getAdbDevices():
    """
    C:\Users\Jac>adb devices
    List of devices attached
    01808409        device
    87eae3b5        device
    """
    command = "adb devices"
    ret = os.popen(command).readlines()
    result = []
    for line in ret:
        if not line.isspace():
            m = re.search('(^[0-9a-zA-Z]*)\s*device$', line)
            if m:
                result.append(m.group(1))
    return result


def getAdbAndroidVersion(device, logname):
    """
    127|shell@cancro:/system/bin $ getprop ro.build.version.release
    getprop ro.build.version.release
    6.0
    """
    command = "getprop ro.build.version.release"
    ret = setAdbShell(device, command, logname)
    return str(ret[0])


def getAdbWlanMac(device, logname):
    """
    127|shell@cancro:/ $  cat /sys/class/net/wlan0/address
    cat /sys/class/net/wlan0/address
    """
    command = "cat /sys/class/net/wlan0/address"
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('([\da-fA-F]{2}:){5}[\da-fA-F]{2}', line)
        if m:
            result = m.group(0)
            return result


def getAdbShellWlan(device, logname):
    verStr = getAdbAndroidVersion(device, logname)
    verInt = 1
    o = re.search('^(\d{1,})\.', verStr)
    if o:
        verInt = int(o.group(1))
    if verInt < 6:
        command = "netcfg"
        """
        D:\>adb shell netcfg
        wlan0    UP                              192.168.31.103/24  0x00001043 14:f6:5a:8f:c7:c1
        """
        ret = setAdbShell(device, command, logname)
        result = {}
        for line in ret:
            m = re.search('wlan.*[UPDOWN]\s*((\d{1,3}\.){3}\d{1,3}).*(([\da-fA-F]{2}:){5}[\da-fA-F]{2})', line)
            if m:
                if m.group(1) == "0.0.0.0":
                    result['ip'] = ""
                    result['mac'] = m.group(3)
                    return result
                else:
                    result['ip'] = m.group(1)
                    result['mac'] = m.group(3)
                    return result
            else:
                result['mac'] = ""
                result['ip'] = ""
        return result
    else:
        command = "ifconfig wlan0"
        """
        ifconfig
        wlan0     Link encap:Ethernet  HWaddr 0C:1D:AF:46:80:23
                  inet addr:192.168.110.211  Bcast:192.168.110.255  Mask:255.255.255.0
                  inet6 addr: fe80::e1d:afff:fe46:8023/64 Scope: Link
                  UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                  RX packets:1488 errors:0 dropped:0 overruns:0 frame:0
                  TX packets:197 errors:0 dropped:0 overruns:0 carrier:0
                  collisions:0 txqueuelen:1000
                  RX bytes:585548 TX bytes:22543
        """
        ret = setAdbShell(device, command, logname)
        result = {"mac": "",
                  "ip": "",}
        for line in ret:
            m = re.search('Ethernet  HWaddr (([\da-fA-F]{2}:){5}[\da-fA-F]{2})', line)
            n = re.search('inet addr:((\d{1,3}\.){3}\d{1,3})', line)
            if m:
                result['mac'] = m.group(1)
            if n:
                result['ip'] = n.group(1)
        return result


def getAdbPingStatus(terminal, target, count, logname):
    """
    C:\Users\Administrator>adb shell ping -c 5 www.baidu.com
    PING www.a.shifen.com (61.135.169.125) 56(84) bytes of data.
    64 bytes from 61.135.169.125: icmp_seq=1 ttl=54 time=19.7 ms
    64 bytes from 61.135.169.125: icmp_seq=2 ttl=54 time=16.1 ms
    64 bytes from 61.135.169.125: icmp_seq=3 ttl=54 time=16.6 ms
    64 bytes from 61.135.169.125: icmp_seq=4 ttl=54 time=18.6 ms
    64 bytes from 61.135.169.125: icmp_seq=5 ttl=54 time=15.6 ms

    --- www.a.shifen.com ping statistics ---
    5 packets transmitted, 5 received, 0% packet loss, time 4006ms
    rtt min/avg/max/mdev = 15.669/17.374/19.774/1.563 ms
    """
    command = 'ping -c ' + str(count) + ' ' + target
    ret = setAdbShell(terminal, command, logname)
    result = {}
    for line in ret:
        m = re.search('(\d{1,3})%\spacket\sloss', line)

        if m:
            result['loss'] = int(m.group(1))
            result['pass'] = 100 - int(m.group(1))
            return result
        else:
            result['loss'] = 100
            result['pass'] = 0
    return result


def chkAdbDevicesCount(count):
    ret = getAdbDevices()
    if len(ret) >= int(count):
        return True
    else:
        return False


def chkSiteSurvey(terminal, intf, chkbssid, logname):
    ret = getSiteSurvey(terminal, intf, logname)
    try:
        index = ret['bssid'].index(chkbssid)
    except Exception:
        resultAll = (False, {})
        return resultAll

    result = {'channel': ret['channel'][index], 'ssid': ret['ssid'][index].lstrip('<').rstrip('>'),
              'bssid': ret['bssid'][index], 'sec': ret['sec'][index]}
    resultAll = (True, result)
    return resultAll


def chkBootingUpFinished(terminal, logname):
    precmd = "touch /tmp/messages"
    command = "cat /tmp/messages | grep 'Booting up finished'"
    setGet(terminal, precmd, logname)
    ret = setGet(terminal, command, logname)
    if len(ret) is not 0:
        return True
    else:
        return False


def chkStaOnline(terminal, intf, stamac, logname):
    commandDic = {"2g": "iwinfo wl1 assoclist | grep -i " + stamac,
                  "5g": "iwinfo wl0 assoclist | grep -i " + stamac,}
    command = commandDic.get(intf)
    ret = setGet(terminal, command, logname)
    if len(ret) is not 0:
        return True
    else:
        return False


def setUCIWirelessIntf(terminal, intf, type, name, value, logname):
    """
    :param intf: wl1/wl0/wl1.2
    :param type: add/add_list/del_list_delete/set/del
    :param name: macfilter/maclist/key/mode...etc
    """
    if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D" or v.DUT_MODULE == "R1CM":
        commandDic = {
            v.INTF_2G: 'uci ' + type + ' wireless.@wifi-iface[1].' + name + '=' + value,
            v.INTF_5G: 'uci ' + type + ' wireless.@wifi-iface[0].' + name + '=' + value,
            v.INTF_GUEST: 'uci ' + type + ' wireless.guest_2G.' + name + '=' + value
        }
    elif v.DUT_MODULE == "R1CL":
        commandDic = {
            v.INTF_2G: "uci " + type + " wireless.@wifi-iface[0]." + name + "=" + value,
            v.INTF_GUEST: "uci " + type + " wireless.guest_2G." + name + "=" + value
        }
    command = commandDic.get(intf)
    setConfig(terminal, command, logname)
    setConfig(terminal, "uci commit wireless", logname)


def setUCIWirelessDev(terminal, dut, intf, type, name, value, logname):
    """
    :param intf: 2g/5g
    :param dut: R1D/R2D/R1CM
    :param type: add/add_list/del_list_delete/set/del
    :param name: txpwr/hwmode/bw/channel/autoch
    """
    if dut == "R1D" or dut == "R2D":
        commandDic = {
            "2g": 'uci ' + type + ' wireless.wl1.' + name + '=' + value,
            "5g": 'uci ' + type + ' wireless.wl0.' + name + '=' + value,
            }
    elif dut == "R1CM":
        commandDic = {
            "2g": 'uci ' + type + ' wireless.mt7620.' + name + '=' + value,
            "5g": 'uci ' + type + ' wireless.mt7612.' + name + '=' + value,
            }
    elif dut == "R1CL":
        commandDic = {
            "2g": "uci " + type + " wireless.mt7628." + name + "=" + value,
            }

    command = commandDic.get(intf)
    setConfig(terminal, command, logname)
    setConfig(terminal, "uci commit wireless", logname)


def setWifiRestart(terminal, logname):
    command = 'miio_notify -t 5 -u;' \
              '/sbin/notice_tbus_device.sh; ' \
              '/sbin/wifi >/dev/null 2>/dev/null; ' \
              '/etc/init.d/minidlna restart; ' \
              '/etc/init.d/samba restart; ' \
              '/usr/bin/gettraffic flush_wl_dev >/dev/null 2>/dev/null'
    setConfig(terminal, command, logname)


def setIwpriv(terminal, intf, arg, value, logname):
    command = 'iwpriv ' + intf + ' set ' + arg + '=' + value
    setConfig(terminal, command, logname)


def setWl(terminal, intf, arg, value, logname):
    command = 'wl -i ' + intf + ' ' + arg + ' ' + value
    setConfig(terminal, command, logname)


def setWifiMacfilterModel(terminal, enable, model=0, mac='none', logname=None):
    if enable == 0:
        if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
            setWl(terminal, 'wl0', 'mac', 'none', logname)
            setWl(terminal, 'wl1', 'mac', 'none', logname)
            setWl(terminal, 'wl1.2', 'mac', 'none', logname)
            setWl(terminal, 'wl0', 'macmode', '0', logname)
            setWl(terminal, 'wl1', 'macmode', '0', logname)
            setWl(terminal, 'wl1.2', 'macmode', '0', logname)
        elif v.DUT_MODULE == 'R1CM' or v.DUT_MODULE == "R1CL":
            setIwpriv(terminal, 'wl0', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl1', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl3', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl0', 'AccessPolicy', '0', logname)
            setIwpriv(terminal, 'wl1', 'AccessPolicy', '0', logname)
            setIwpriv(terminal, 'wl3', 'AccessPolicy', '0', logname)
    else:
        if v.DUT_MODULE == 'R1D' or v.DUT_MODULE == 'R2D':
            setWl(terminal, 'wl0', 'mac', 'none', logname)
            setWl(terminal, 'wl1', 'mac', 'none', logname)
            setWl(terminal, 'wl1.2', 'mac', 'none', logname)
            setWl(terminal, 'wl0', 'mac', mac, logname)
            setWl(terminal, 'wl1', 'mac', mac, logname)
            setWl(terminal, 'wl1.2', 'mac', mac, logname)
            # blacklist
            if model == 0:
                setWl(terminal, 'wl0', 'macmode', '1', logname)
                setWl(terminal, 'wl1', 'macmode', '1', logname)
                setWl(terminal, 'wl1.2', 'macmode', '1', logname)
                setWl(terminal, 'wl0', 'deauthenticate', mac, logname)
                setWl(terminal, 'wl1', 'deauthenticate', mac, logname)
                setWl(terminal, 'wl1.2', 'deauthenticate', mac, logname)
            # whitelist
            elif model == 1:
                setWl(terminal, 'wl0', 'macmode', '2', logname)
                setWl(terminal, 'wl1', 'macmode', '2', logname)
                setWl(terminal, 'wl1.2', 'macmode', '2', logname)
        elif v.DUT_MODULE == 'R1CM' or v.DUT_MODULE == "R1CL":
            setIwpriv(terminal, 'wl0', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl1', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl3', 'ACLClearAll', '1', logname)
            setIwpriv(terminal, 'wl0', 'ACLAddEntry', mac, logname)
            setIwpriv(terminal, 'wl1', 'ACLAddEntry', mac, logname)
            setIwpriv(terminal, 'wl3', 'ACLAddEntry', mac, logname)
            # blacklist
            if model == 0:
                setIwpriv(terminal, 'wl0', 'AccessPolicy', '2', logname)
                setIwpriv(terminal, 'wl1', 'AccessPolicy', '2', logname)
                setIwpriv(terminal, 'wl3', 'AccessPolicy', '2', logname)
                setIwpriv(terminal, 'wl0', 'DisConnectSta', mac, logname)
                setIwpriv(terminal, 'wl1', 'DisConnectSta', mac, logname)
                setIwpriv(terminal, 'wl3', 'DisConnectSta', mac, logname)
            # whitelist
            elif model == 1:
                setIwpriv(terminal, 'wl0', 'AccessPolicy', '1', logname)
                setIwpriv(terminal, 'wl1', 'AccessPolicy', '1', logname)
                setIwpriv(terminal, 'wl3', 'AccessPolicy', '1', logname)


def setReboot(terminal, logname):
    command = 'reboot'
    setConfig(terminal, command, logname)


def setUpgradeSystem(terminal, file, logname):
    command = "flash.sh " + file
    setGet(terminal, command, logname)


def setReset(terminal, logname):
    command = "env -i sleep 4 && nvram set restore_defaults=1 && nvram commit && reboot & >/dev/null 2>/dev/null"
    setConfig(terminal, command, logname)

def setCopyFile(terminal, logname, **kargs):
    command = 'cp %s %s'%(kargs['src'], kargs['dst'])
    setConfig(terminal, command, logname)


def setMvFile(terminal, logname, **kargs):
    command = 'mv %s %s'%(kargs['src'], kargs['dst'])
    setConfig(terminal, command, logname)


def setAdbClearStaConn(device, ssid, radio, logname):
    if radio is "2g":
        if ssid is "normal":
            option = {
                "ssid": v.SSID,
            }
    elif radio is "5g":
        if ssid is "normal":
            option = {
                "ssid": v.SSID_5G,
            }
    elif radio is "guest":
        if ssid is "normal":
            option = {
                "ssid": v.GUEST_SSID,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbClearStaConnRepeat(device, ssid, radio, logname):
    if radio is "2g":
        if ssid is "normal":
            option = {
                "ssid": v.SSID,
                "repeat": 1,
            }
    elif radio is "5g":
        if ssid is "normal":
            option = {
                "ssid": v.SSID_5G,
                "repeat": 1,
            }
    elif radio is "guest":
        if ssid is "normal":
            option = {
                "ssid": v.GUEST_SSID,
                "repeat": 1,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbPsk2StaConn(device, ssid, radio, logname, key=None):
    if radio is "2g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID,
                "encryption": "psk2",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "5g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID_5G,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID_5G,
                "encryption": "psk2",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk2",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "guest":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "psk2",
                "key": v.KEY,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbPsk2StaConnRepeat(device, ssid, radio, logname):
    if radio is "2g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID,
                "encryption": "psk2",
                "key": v.KEY,
                "repeat": 1,
            }
    elif radio is "5g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk2",
                "key": v.KEY,
                "repeat": 1,
            }
    elif radio is "guest":
        if ssid == "normal":
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "psk2",
                "key": v.KEY,
                "repeat": 1,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbPskStaConn(device, ssid, radio, logname, key=None):
    if radio is "2g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID,
                "encryption": "psk",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "5g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID_5G,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID_5G,
                "encryption": "psk",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "guest":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "psk",
                "key": v.KEY,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbPskStaConnRepeat(device, ssid, radio, logname):
    if radio is "2g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID,
                "encryption": "psk",
                "key": v.KEY,
                "repeat": 1,
            }
    if radio is "5g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "psk",
                "key": v.KEY,
                "repeat": 1,
            }
    if radio is "guest":
        if ssid == "normal":
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "psk",
                "key": v.KEY,
                "repeat": 1,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbTkipPsk2StaConn(device, ssid, radio, logname, key=None):
    if radio is "2g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk2",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "5g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID_5G,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID_5G,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk2",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "guest":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbTkipPsk2StaConnRepeat(device, ssid, radio, logname):
    if radio is "2g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
                "repeat": 1,
            }
    if radio is "5g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk2",
                "key": v.KEY,
                "repeat": 1,
            }
    if radio is "guest":
        if ssid == "normal":
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "tkippsk2",
                "key": v.KEY,
                "repeat": 1,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbTkipPskStaConn(device, ssid, radio, logname, key=None):
    if radio is "2g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "5g":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "chinese" and key is None:
            option = {
                "ssid": v.CHINESE_SSID_5G,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "spec" and key is None:
            option = {
                "ssid": v.SPECIAL_SSID_5G,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
        elif ssid == "normal" and key == "spec":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk",
                "key": v.SPECIAL_KEY,
            }
    elif radio is "guest":
        if ssid == "normal" and key is None:
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbTkipPskStaConnRepeat(device, ssid, radio, logname):
    if radio is "2g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
                "repeat": 1,
            }
    elif radio is "5g":
        if ssid == "normal":
            option = {
                "ssid": v.SSID_5G,
                "encryption": "tkippsk",
                "key": v.KEY,
                "repeat": 1,
            }
    elif radio is "guest":
        if ssid == "normal":
            option = {
                "ssid": v.GUEST_SSID,
                "encryption": "tkippsk",
                "key": v.KEY,
                "repeat": 1,
            }
    ret = setAdbStaConn(device, logname, **option)
    return ret


def setAdbStaConn(device, logname, **kwargs):
    option = {
        "ssid": "",
        "encryption": "clear",
        "key": "",
        "repeat": 0,
        }
    option.update(kwargs)
    if option["repeat"] is 1:
        option["repeat"] = "repeat_"
    elif option["repeat"] is 0:
        option["repeat"] = ""

    if option["ssid"] is not "":
        option["ssid"] = " -e ssid " + convertStrToURL(option["ssid"])

    if option["key"] is not "":
        option["key"] = " -e key " + convertStrToURL(option["key"])

    command = "am instrument%(ssid)s%(key)s -e class com.peanutswifi.ApplicationTest#test_%(repeat)sassoc_%(encryption)s_sta " \
              "-w com.peanutswifi.test/com.peanutswifi.MyTestRunner"%option

    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False


def setAdbScanSsidNoExist(device, ssid, radio, logname):
    if radio is "2g":
        if ssid is "normal":
            option = {
                "ssid": convertStrToURL(v.SSID)
            }

    elif radio is "5g":
        if ssid is "normal":
            option = {
                "ssid": convertStrToURL(v.SSID_5G)
            }
    command = "am instrument -e ssid %(ssid)s -e class com.peanutswifi.ApplicationTest#test_ssidhide " \
              "-w com.peanutswifi.test/com.peanutswifi.MyTestRunner"%option

    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK', line)
        if m:
            return True
    return False


def setAdbIperfOn(device, logname):
    command = "am instrument -e class com.peanutswifi.ApplicationTest#test_iperf2 -w com.peanutswifi.test/android.test.InstrumentationTestRunner"
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK', line)
        if m is not None:
            return True
    return False


class SetAdbIperfOn(threading.Thread):
    def __init__(self, device=None, logname=None):
        threading.Thread.__init__(self)
        self.device = device
        self.logname = logname

    def run(self):
        setAdbIperfOn(self.device, self.logname)


def setIperfFlow(target, interval, time, logname):
    if os.path.exists(v.IPERF_PATH):
        pass
    else:
        raise Exception("iperf doesnot exist! please copy iperf dir to the path same as peanuts.")

    command = "iperf.exe -c " + target
    if interval != "":
        command = command + " -i " + interval
    if time != "":
        command = command + " -t " + time

    command += " -r -w 2m -f m"
    ret = setShell(command, cwd=v.IPERF_PATH, timeout=3*int(time), logname=logname)
    # os.chdir(v.DEFAULT_PATH)
    if len(ret) == 0:
        return False
    return True


if __name__ == '__main__':
    # ssh = SshClient(2)
    # ssh.connect("192.168.140.1", "", "")
    # v.DUT_MODULE = "R1CM"
    # setWifiRestart(ssh, "log")
    # ssh.close()
    dut = getAdbDevices()
    ret = setAdbPsk2StaConn(dut[0], "normal", "2g", 'aaa')
    print ret