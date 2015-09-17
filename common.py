# -*- coding: gbk -*-
import sys
import os
import time as t
import re
import threading
import telnetlib
import xlrd as xr
import paramiko as pm
import var as v


class SshClient(object):
    def __init__(self, connection):
        self.connectionType = connection

    def connect(self, host, userid, password=None):
        if self.connectionType == 1: # represent ssh
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
                # sys.exit(1)
        elif self.connectionType == 2: # represent telnet
            self.hostname = host.encode("utf-8")
            self.username = userid.encode("utf-8")
            self.password = password.encode("utf-8")
            try:
                # connect to telnet server
                self.tn = telnetlib.Telnet(self.hostname, port=23, timeout=10)
                # self.tn.set_debuglevel(2)

                #login
                if self.username != "":
                    self.tn.read_until("XiaoQiang login: ", 10)
                    self.tn.write(self.username + "\n")
                    self.tn.read_until("Password: ", 10)
                    self.tn.write(self.password + "\n")

                self.tn.read_until("root@XiaoQiang:", 10)
                return True

            except Exception,e:
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
                except Exception,e:
                    self.out[index] = ""
                    pass
            return self.out
        elif self.connectionType == 2:
            cmd = ";".join(args) # input and output are utf-8
            if checkContainChinese(cmd):
                cmd = cmd.decode("gbk")
                cmd = cmd.encode("utf-8")

            self.tn.write(cmd + "\n")
            self.out = self.tn.read_until("root@XiaoQiang:", 60)
            self.out = self.out.split("\n")
            del self.out[0] # del command and :~#
            del self.out[-1]
            return self.out

    def config(self, arg):
        if self.connectionType == 1:
            cmd = arg
            if checkContainChinese(cmd):
                cmd = unicode(cmd, 'gbk')

            stdin, stdout, stderr = self.client.exec_command(cmd)
            err = stderr.readlines()
            ##        keepGoing = 0
            ##        while keepGoing < 3 and len(err) != 0:
            ##          stdin, stdout, stderr = self.client.exec_command(arg)
            ##          err = stderr.read()
            ##            keepGoing += 1
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
            #     self.out[index] = self.out[index].decode("utf-8").encode("gbk")
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
                           '**********' + c + '**********\n**********' + c + '**********\n'] = self.command(c)
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

class SerialClient(object):
    pass

def connectionCheck(connectiontype, ip=None, port=None, user=None, password=None):
    client = SshClient(connectiontype)
    result = client.connect(ip, user, password)
    client.close()
    return result


def convertStrToBashStr(string):
    if string is not None:
        string = re.sub('`', '\`', string)
        string = re.sub('"', '\\"', string)
        string = '"' + string + '"'
    return string

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
        sys.exit(1)


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
        sys.exit(1)

def setAdbShell(device, command, logname):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        if device != "":
            adb = "adb " + "-s " + device + " shell "
        else:
            adb = "adb shell "
        command = adb + command
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
        sys.exit(1)

def setShell(command, logname):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        ret = os.popen(command).readlines()
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#OS#')
        f.write(command + '\n')
        f.writelines(ret)
        f.write('\n')
        f.close()
        return ret
    except Exception, e:
        sys.exit(1)

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
    command = 'ifconfig ' + intf
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

    command = 'ifconfig ' + intf
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
            result['loss'] = ''
            result['pass'] = ''
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
                      "5g": "wl -i wl0 curpower | grep 'Maximum Power Target among all rates'",}
        command = commandDic.get(intf)
        ret = setGet(terminal, command, logname)
        for line in ret:
            m = re.search('\d*\.\d*.*',line)
            if m:
                power = m.group(0)
                powerList = power.split()
                sum = 0.0
                for c in range(len(powerList)):
                    sum += float(powerList[c])
                result = sum/len(powerList)
                return float(result)
            else:
                result = 0
        return float(result)

    elif dut == "R1CM":
        commandDic = {"2g":"iwconfig wl1 | grep 'Tx-Power='",
                      "5g":"iwconfig wl0 | grep 'Tx-Power='",}
        command = commandDic.get(intf)
        ret = setGet(terminal, command, logname)
        for line in ret:
            m = re.search('(\d*)\sdBm',line)
            if m:
                result = m.group(1)
                return float(result)
            else:
                result = 0
        return float(result)

def getWlanInfo(terminal, intf, logname):
    commandDic = {"2g": "iwinfo wl1 info",
                  "5g": "iwinfo wl0 info",
                  "guest": "iwinfo wl1.2 info",}

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

def getAdbDevices():
    """
    C:\Users\Jac>adb devices
    List of devices attached
    01808409        device
    87eae3b5        device
    """
    command = "adb devices"
    ret = os.popen(command).readlines()
    del ret[0]
    m = re.findall('.+\s+device', ''.join(ret))
    count = 0
    result = []
    for dev in m:
        result.append(dev[:-7])
        count = count + 1
    return result

def getAdbShellWlan(device, logname):
    """
    D:\Python\new peanuts\22\iperf-2.0.5-3-win32>adb shell netcfg
lo       UP                                   127.0.0.1/8   0x00000049 00:00:00:
00:00:00
mhi0     DOWN                                   0.0.0.0/0   0x00000090 26:00:00:
00:00:00
p2p0     UP                                     0.0.0.0/0   0x00001003 16:f6:5a:
8f:c7:c1
sit0     DOWN                                   0.0.0.0/0   0x00000080 00:00:00:
00:00:00
wlan0    UP                              192.168.31.103/24  0x00001043 14:f6:5a:
8f:c7:c1
rmnetctl DOWN                                   0.0.0.0/0   0x00000080 00:00:00:
00:00:00
dummy0   DOWN                                   0.0.0.0/0   0x00000082 a2:ef:9e:
78:79:f2
usbnet0  DOWN                                 10.0.2.15/24  0x00001002 0e:f7:11:
b7:75:b6
ip6tnl0  DOWN                                   0.0.0.0/0   0x00000080 00:00:00:
00:00:00
    """
    command = "netcfg"
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



def chkAdbDevicesCount(count):
    ret = getAdbDevices()
    if len(ret) >= count:
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

def setUCIWirelessIntf(terminal, intf, type, name, value, logname):
    """
    :param intf: wl1/wl0/wl1.2
    :param type: add/add_list/del_list_delete/set/del
    :param name: macfilter/maclist/key/mode...etc
    """
    commandDic = {v.INTF_2G: 'uci ' + type + ' wireless.@wifi-iface[1].' + name + '=' + value,
                  v.INTF_5G: 'uci ' + type + ' wireless.@wifi-iface[0].' + name + '=' + value,
                  v.INTF_GUEST: 'uci ' + type + ' wireless.guest_2G.' + name + '=' + value}

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
        commandDic = {"2g": 'uci ' + type + ' wireless.wl1.' + name + '=' + value,
                      "5g": 'uci ' + type + ' wireless.wl0.' + name + '=' + value,}
    elif dut == "R1CM":
        commandDic = {"2g": 'uci ' + type + ' wireless.mt7620.' + name + '=' + value,
                      "5g": 'uci ' + type + ' wireless.mt7612.' + name + '=' + value,}

    command = commandDic.get(intf)
    setConfig(terminal, command, logname)
    setConfig(terminal, "uci commit wireless", logname)

def setWifiRestart(terminal, logname):
    command = 'wifi; sleep 10'
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
        elif v.DUT_MODULE == 'R1CM':
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
        elif v.DUT_MODULE == 'R1CM':
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

def setAdbClearStaConn(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_clear_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_clear_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_clear_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbClearStaConnRepeat(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_clear_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_clear_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_clear_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbPsk2StaConn(device, ssid, radio, logname, key=None,):

    if ssid == "normal" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    elif ssid == "chinese" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidchinese_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidchinese_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidchinese_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    elif ssid == "spec" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_ssidspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    elif ssid == "normal" and key == "spec":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_keyspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_keyspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk2_sta_keyspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbPsk2StaConnRepeat(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk2_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk2_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk2_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbPskStaConn(device, ssid, radio, logname, key=None):

    if ssid == "normal" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "chinese" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidchinese_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidchinese_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidchinese_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "spec" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_ssidspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    elif ssid == "normal" and key == "spec":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbPskStaConnRepeat(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_psk_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbTkipPsk2StaConn(device, ssid, radio, logname, key=None):

    if ssid == "normal" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "chinese" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidchinese_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidchinese_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidchinese_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "spec" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk2_sta_ssidspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "normal" and key == "spec":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbTkipPsk2StaConnRepeat(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk2_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk2_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk2_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbTkipPskStaConn(device, ssid, radio, logname, key=None):

    if ssid == "normal" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "chinese" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidchinese_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidchinese_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidchinese_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "spec" and key == None:
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_tkippsk_sta_ssidspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}
    elif ssid == "normal" and key == "spec":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_assoc_psk_sta_keyspec_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbTkipPskStaConnRepeat(device, ssid, radio, logname):

    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk_sta_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk_sta_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "guest":"am instrument -e class com.peanutswifi.ApplicationTest#test_repeat_assoc_tkippsk_sta_guest -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK ', line)
        if m is not None:
            return True
    return False

def setAdbScanSsidNoExist(device, ssid, radio, logname):
    if ssid == "normal":
        commandDic = {"2g": "am instrument -e class com.peanutswifi.ApplicationTest#test_ssidhide_2g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",
                      "5g": "am instrument -e class com.peanutswifi.ApplicationTest#test_ssidhide_5g -w com.peanutswifi.test/android.test.InstrumentationTestRunner",}

    command = commandDic.get(radio)
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK', line)
        if m:
            return True
    return False

def setAdbIperfOn(device, logname):
    command = "am instrument -e class com.peanutswifi.ApplicationTest#test_iperf -w com.peanutswifi.test/android.test.InstrumentationTestRunner"
    ret = setAdbShell(device, command, logname)
    for line in ret:
        m = re.search('OK', line)
        if m is not None:
            return True
    return False

class SetAdbIperfOn(threading.Thread):
    def __init__(self,device=None,logname=None):
        threading.Thread.__init__(self)
        self.device = device
        self.logname = logname

    def run(self):
        setAdbIperfOn(self.device, self.logname)


def setIperfFlow(target, interval, time, logname):
    if os.path.exists(v.IPERF_PATH):
        os.chdir(v.IPERF_PATH)
    else:
        raise Exception("iperf doesnot exist! please copy iperf dir to the path same as peanuts.")

    command = "iperf -c " + target
    if interval != "":
        command = command +" -i " + interval
    if time != "":
        command = command + " -t " + time

    command = command + " -r"
    ret = setShell(command, logname)
    if len(ret) == 0:
        return False
    return True



if __name__ == '__main__':
    ssh = SshCommand(2)
    ssh.connect("192.168.110.1", "", "")
    setWifiMacfilterModel(ssh, 1, 1, logname='test')
    setWifiMacfilterModel(ssh, 0, logname='test')
    # print ssh.outPidNameVSZDic
    # ret = setConfig(ssh, "uci set wireless.@wifi-iface[0].ssid='我的10'", "a")
    # ret = setGet(ssh, "uci show wireless", "a")
    # ret = getSiteSurvey(ssh, "apcli0", "a")
    # a = [2,13]
    # ret = getWlanInfo(ssh, "2g", "a")
    # try:
    #     a.index(int(ret["channel"]))
    #     print 1
    # except:
    #     print 2
    # ret = chkSiteSurvey(ssh, "apcli0", "64:09:80:73:75:3d" ,"a")
    # setWifiRestart(ssh,"a")
    # ret =getIntfHWAddr(ssh, "wl1", "a")
    # print ret["mac"]
    ssh.close()
    # setIperfFlow("192.168.31.218", "1", "2", "a")
