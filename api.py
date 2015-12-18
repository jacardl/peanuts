# coding=utf8
import httplib
import urllib
import hashlib
import time
import random
import re
import time as t
import os

import var as v

def getWebLoginNonce():
    """
    type : Client 的类型，0[web] 1[Android] 2[iOS] 3[Mac] 4[PC]
    deviceId : 设备的唯一标识，不能包含字符"_"，web可以传当前mac地址，其它Client端可自行定义
    time : 当前时间，按秒计算
    random : 随机数，没有位数限制
    for example
    nonce:0_08:9e:01:d0:f1:f4_1449649511_9171
    """
    timeNum = int(time.time())
    randomNum = random.randint(1, 9999)
    macStr = 'peanutsWebClient'
    nonce = '0_' + macStr + '_' + str(timeNum) + '_' + str(randomNum)
    return nonce


def getWebLoginPassword(password, key):
    """
    password = sha1(nonce+sha1(pwd+key))
    """
    result = dict()
    nonce = getWebLoginNonce()
    password = str(hashlib.sha1(nonce + str(hashlib.sha1(password + key).hexdigest())).hexdigest())
    result['nonce'] = nonce
    result['password'] = password
    return result


class HttpClient(object):
    def __init__(self, init=0):
        self.init = init
        self.token = None
        self.headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    def connect(self, hostname, port=80):
        self.hostname = hostname
        try:
            self.httpClient = httplib.HTTPConnection(self.hostname, port, timeout=30)
            return True
        except:
            print 'connection is failed. please check your network.'
            return False

    def close(self):
        if self.httpClient:
            self.httpClient.close()

    def getToken(self, password=None):

        login = getWebLoginPassword(password, v.WEB_KEY)
        params = urllib.urlencode({'username': v.WEB_USERNAME,
                                   'password': login['password'],
                                   'init': self.init,
                                   'nonce': login['nonce']})

        self.httpClient.request('POST', '/cgi-bin/luci/api/xqsystem/login', params, self.headers)
        response = self.httpClient.getresponse()
        if response.status is not 200:
            print 'web server has problem'
            return False
        else:
            loginresponse = eval(response.read())
            if loginresponse['code'] is not 0:
                print 'login api process wrong'
                return False
            self.token = 'stok=' + loginresponse['token']
            return self.token

    def getApi(self, path, **kwargs):
        apipath = re.sub('stok=token', self.token, path)
        if len(kwargs) is 0:
            self.httpClient.request('GET', apipath, headers=self.headers)
            response = self.httpClient.getresponse().read()
            responsedict = eval(response)
            return responsedict
        else:
            params = urllib.urlencode(kwargs)
            self.httpClient.request('POST', apipath, params, self.headers)
            response = self.httpClient.getresponse().read()
            responsedict = eval(response)
            return responsedict


def setGet(terminal, logname, apipath, **kwargs):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        token = terminal.getToken(v.WEB_PWD)
        if token is not False:
            ret = terminal.getApi(apipath, **kwargs)
        else:
            ret = 'get token failed!'
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#API request to ' + terminal.hostname + '#')
        f.write(apipath + '?' + str(kwargs) + '\n')
        f.writelines(str(ret))
        f.write('\n\n')
        f.close()
        return ret

    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#API request to ' + terminal.hostname + ' failed#')
        f.write(apipath + '?' + str(kwargs) + '\n')
        print e
        f.write(str(e))
        f.write('\n\n')
        terminal.close()
        f.close()


def setCheck(terminal, logname, apipath, **kwargs):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    try:
        token = terminal.getToken(v.WEB_PWD)
        if token is not False:
            ret = terminal.getApi(apipath, **kwargs)
        else:
            ret = 'get token failed!'
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#API request to ' + terminal.hostname + '#')
        f.write(apipath + '?' + str(kwargs) + '\n')
        f.writelines(str(ret))
        f.write('\n')
        if ret['code'] == 0:
            f.write('api processes PASS\n\n')
            f.close()
            return True
        else:
            f.write('api processes FAIL\n\n')
            f.close()
            return False

    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#API request to ' + terminal.hostname + ' failed#')
        f.write(apipath + '?' + str(kwargs) + '\n')
        f.write(str(e))
        f.write('\n\n')
        terminal.close()
        f.close()
        return False


def setCheckFromFile(terminal, file, logname):
    # ignore lines start with '#' in file
    if os.path.exists(file):
        apifile = open(file)
    else:
        print 'file isnot exists.'
        return
    for line in apifile:
        if not line.isspace() and re.match('^#', line) is None:
            api = line.strip('\n').split('?')
            print api
            if len(api) > 1:
                api[1] = eval(api[1])
                setCheck(terminal, logname, api[0], **api[1])
            elif len(api) == 1:
                setCheck(terminal, logname, api[0])
    apifile.close()


def setWifi(terminal, logname, **kwargs):
    """
    wifiIndex (1/2)
    on (0/1)
    ssid
    pwd
    encryption (none,mixed-psk,psk2)
    channel
    bandwidth
    hidden (0/1)
    txpwr (max/mid/min)

    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'wifiIndex':1,
        'on': 1,
        'ssid': 'peanuts',
        'pwd': '',
        'encryption': 'none',
        'channel': '0',
        'bandwidth': '0',
        'hidden': 0,
        'txpwr': 'mid'
    }

    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_wifi'
    ret = setCheck(terminal, logname, api, **option)
    time.sleep(10)
    return ret


def setAllWifi(terminal, logname, **kwargs):
    """
    bsd (0/1)
    on1 (0/1)
    ssid1
    pwd1
    encryption1 (none,mixed-psk,psk2)
    channel1
    bandwidth1
    hidden1 (0/1)
    txpwr1 (max/mid/min)
    on2 (0/1)
    ssid2
    pwd2
    encryption2 (none,mixed-psk,psk2)
    channel2
    bandwidth2
    hidden2 (0/1)
    txpwr2 (max/mid/min)

    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'bsd': 0,
        'on1': 1,
        'ssid1': 'peanuts',
        'pwd1': '',
        'encryption1': 'none',
        'channel1': '0',
        'bandwidth1': '0',
        'hidden1': 0,
        'txpwr1': 'mid',
        'on2': 1,
        'ssid2': 'peanuts',
        'pwd2': '',
        'encryption2': 'none',
        'channel2': '0',
        'bandwidth2': '0',
        'hidden2': 0,
        'txpwr2': 'mid',
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_all_wifi'
    ret = setCheck(terminal, logname, api, **option)
    time.sleep(10)
    return ret

def setEditDevice(terminal, logname, **kwargs):
    """
    model : (0/1 黑名单/白名单)
    mac: (AA:BB:CC:DD:EE:FF or AA:BB:CC:DD:EE:FF;AA:BB:CC:DD:EE:FF...)
    option: (0/1 添加/删除)

    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    """
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'model': 0,
        'mac': '11:22:33:44:55:66',
        'option': 0
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/edit_device'
    ret = setCheck(terminal, logname, api, **option)
    return ret


def setWifiMacFilter(terminal, logname, **kwargs):
    """
    model: (0/1 黑名单/白名单)
    enable: (0/1 关闭/开启)
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'model' : 0,
        'enable': 0
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_wifi_macfilter'
    return setCheck(terminal, logname, api, **option)


def setReboot(terminal, logname):
    api = '/cgi-bin/luci/;stok=token/api/xqsystem/reboot'
    return setCheck(terminal, logname, api)


def setReset(terminal, logname, **kwargs):
    """
    format (0/1 是否格式化磁盘，默认0 不格式化)
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'format': 0,
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqsystem/reset'
    return setCheck(terminal, logname, **option)


def getWifiDetailAll(terminal, logname):

    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/wifi_detail_all'
    ret = setGet(terminal, logname, api)
    if ret['code'] is 0:
        return ret
    else:
        return None


def getDeviceDetail(terminal, logname, **kwargs):
    """
    mac: '11:22:33:44:55:66'
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'mac': '11:22:33:44:55:66'
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/misystem/device_detail'
    ret = setGet(terminal, logname, api, **option)
    if ret['code'] is 0:
        return ret
    else:
        return None


def getDeviceList(terminal, logname, **kwargs):
    """
    online:0/1 (在线+离线/ 在线)
    withbrlan:0/1 (无线/有线+无线)
    :return
    "isap": 0,       (0/1/2  正常设备/无线中继/有线中继)
    "parent": "",    (当该设备是通过中继路由连入该字段内容为中继路由器的MAC地址)
    "active": 1,             该IP是否活跃
    "type": 0,       (0/1/2/3  有线 / 2.4G wifi / 5G wifi / guest wifi)
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    option = {
        'online': 1,
        'withbrlan': 0
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/misystem/devicelist'
    ret = setGet(terminal, logname, api, **option)
    if ret['code'] is 0:
        return ret
    else:
        return None


def getOnlineDeviceType(terminal, logname):
    result = dict()
    option = {
        'online': 1,
        'withbrlan': 1,
    }
    ret = getDeviceList(terminal, logname, **option)
    for d in ret['list']:
        result[d['mac']] = d['type']
    return result

if __name__ == '__main__':

    host = '192.168.31.1'
    # api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_wifi'
    # dictx = {'wifiIndex':1, 'on':1, 'ssid':'peanuts_mu', 'pwd':'12345678','encryption':'mixed-psk', 'channel':'11',
    #         'bandwidth':'20','hidden':'0', 'txpower':'mid'}
    webclient = HttpClient()
    webclient.connect(host)
    # option = {
    #     'bsd': 0,
    #     'on1': 1,
    #     'ssid1': 'peanuts',
    #     'pwd1': '',
    #     'encryption1': 'none',
    #     'channel1': '0',
    #     'bandwidth1': '0',
    #     'hidden1': 0,
    #     'txpwr1': 'mid',
    # }
    option = {
        'wifiIndex': 1,
        'ssid': v.SSID,
        'encryption': 'psk2',
        'pwd': v.SPECIAL_KEY,
    }
    ret = setWifi(webclient, 'aaa', **option)
    webclient.close()



