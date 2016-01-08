# coding=utf8
import httplib
import urllib
import hashlib
import time
import random
import re
import time as t
import os
from Crypto.Cipher import AES

import var as v
import common

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
    macStr = 'peanutsclient'
    nonce = '0_' + macStr + '_' + str(timeNum) + '_' + str(randomNum)
    return nonce


def getWebLoginPassword(password=v.WEB_PWD, key=v.WEB_KEY):
    """
    password = sha1(nonce+sha1(pwd+key))
    """
    result = dict()
    nonce = getWebLoginNonce()
    password = str(hashlib.sha1(nonce + str(hashlib.sha1(password + key).hexdigest())).hexdigest())
    result['nonce'] = nonce
    result['password'] = password
    return result


def getWebLoginOldPwd():
    result = dict()
    nonce = getWebLoginNonce()
    oldPwd = str(hashlib.sha1(nonce + v.ACCOUNT_DEFAULT_PWD).hexdigest())
    result['nonce'] = nonce
    result['password'] = oldPwd
    return result


def getWebLoginNewPwdEncryptBase64(password=v.WEB_PWD, key=v.WEB_KEY):

    # AES加密密钥是oldpwdnononce
    oldPwdNoNonce = v.ACCOUNT_DEFAULT_PWD
    aesKey = oldPwdNoNonce.decode('hex')
    # aes-cbc-128 的key 16bytes
    aesKey = aesKey[0:16]
    iv = v.IV.decode('hex')
    newPwdNoNonce = str(hashlib.sha1(password + key).hexdigest())
    text = newPwdNoNonce
    text = PKCSPad(text)

    encryptor = AES.new(aesKey, AES.MODE_CBC, iv)
    cipher = encryptor.encrypt(text)
    cipherbase = cipher.encode('base64')
    return cipherbase


def PKCSPad(data):
    """
    PKCS#5 padding is identical to PKCS#7 padding, except that
    it has only been defined for block ciphers that use a 64 bit (8 byte)
    block size.
    But in AES, there is no block of 8 bit, so PKCS#5 is PKCS#7.
    """
    BS = AES.block_size
    data =  data + (BS - len(data) % BS) * chr(BS - len(data) % BS)
    return data


def PKCSUnpad(data):
    data = data[0:-ord(data[-1])]
    return data


class HttpClient(object):
    def __init__(self):
        self.init = None
        self.token = None
        self.hostname = None
        self.httpClient = None
        self.headers = {"Content-type": "application/x-www-form-urlencoded",
                        "Accept": "text/plain",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
                        }

    def connect(self, init=0, host=v.HOST, port=80, password=v.WEB_PWD):
        self.init = init
        self.token = False
        self.hostname = host

        def connectInLoop(host, password):
            loop2 = 0
            try:
                self.httpClient = httplib.HTTPConnection(host, port, timeout=30)
                while self.token is False and loop2 < 5:
                    t.sleep(1)
                    result = self.getToken(password=password)
                    loop2 += 1
                if result is False:
                    return False
                else:
                    return True
            except:
                print 'connection is failed. please check your network.'
                return False

        loop = 0
        ret = connectInLoop(host, password)
        while ret is False and loop < 5:
            loop += 1
            t.sleep(2)
            ret = connectInLoop(host, password)
        return ret


    def close(self):
        if self.httpClient:
            self.httpClient.close()

    def getToken(self, password):
        self.password = password
        if self.init is 0:
            self.login = getWebLoginPassword(self.password, v.WEB_KEY)
        elif self.init is 1:
            self.login = getWebLoginOldPwd()
        params = urllib.urlencode({'username': v.WEB_USERNAME,
                                   'password': self.login['password'],
                                   'init': self.init,
                                   'nonce': self.login['nonce']})

        self.httpClient.request('POST', '/cgi-bin/luci/api/xqsystem/login', params, self.headers)
        response = self.httpClient.getresponse()
        if response.status is not 200:
            print 'web server has problem'
            return False
        else:
            loginresponse = eval(response.read())
            if loginresponse['code'] is not 0:
                print 'probably use wrong web password or router hasnot been initialized.'
                return False
            self.token = 'stok=' + loginresponse['token']
            return self.token

    def getApi(self, path, **kwargs):
        apipath = re.sub('stok=token', self.token, path)
        if len(kwargs) is 0:
            self.httpClient.request('GET', apipath, headers=self.headers)
            response = self.httpClient.getresponse().read()
            responseDict = eval(response)
            return responseDict
        else:
            for key, value in kwargs.items():
                if type(value) is str and common.checkContainChinese(value):
                    kwargs[key] = value.decode('gbk').encode('utf8')
            params = urllib.urlencode(kwargs)
            self.httpClient.request('POST', apipath, params, self.headers)
            response = self.httpClient.getresponse().read()
            responseDict = eval(response)
            return responseDict


def setGet(terminal, logname, apipath, **kwargs):

    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    def setGetInLoop(terminal, logname, apipath, **kwargs):
        try:
            ret = terminal.getApi(apipath, **kwargs)
            curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
            f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
            f.write(curTime + '~#API request to ' + terminal.hostname + '#')
            f.write(apipath + '?' + str(kwargs) + '\n')
            f.writelines(str(ret))
            f.write('\n\n')
            if ret['code'] == 401:
                f.write('token timeout, renew token.\n\n')
                f.close()
                terminal.getToken(password=v.WEB_PWD)
                setGet(terminal, logname, apipath, **kwargs)
            f.close()
            return ret
        except Exception, e:
            curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
            f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
            f.write(curTime + '~#API request to ' + terminal.hostname + ' failed#')
            f.write(apipath + '?' + str(kwargs) + '\n')
            f.write(str(e))
            f.write('\n\n')
            terminal.close()
            f.close()
            return None

    loop = 0
    ret = setGetInLoop(terminal, logname, apipath, **kwargs)
    while  (ret is None or ret['code'] != 0) and loop < 5:
        loop += 1
        t.sleep(2)
        ret = setGetInLoop(terminal, logname, apipath, **kwargs)

    return ret


def setCheck(terminal, logname, apipath, **kwargs):
    if not os.path.exists(v.TEST_SUITE_LOG_PATH):
        os.makedirs(v.TEST_SUITE_LOG_PATH)

    def setCheckInLoop(terminal, logname, apipath, **kwargs):
        try:
            ret = terminal.getApi(apipath, **kwargs)
            curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
            f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
            f.write(curTime + '~#API request to ' + terminal.hostname + '#')
            f.write(apipath + '?' + str(kwargs) + '\n')
            f.writelines(str(ret))
            f.write('\n')
            if ret['code'] == 0:
                f.write('api processes PASS.\n\n')
                f.close()
                return True
            elif ret['code'] == 401:
                f.write('token timeout, renew token.\n\n')
                f.close()
                terminal.getToken(password=v.WEB_PWD)
                setCheck(terminal, logname, apipath, **kwargs)
            else:
                f.write('api processes FAIL.\n\n')
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

    loop = 0
    ret = setCheckInLoop(terminal, logname, apipath, **kwargs)
    while ret is False and loop < 5:
        loop += 1
        t.sleep(2)
        ret = setCheckInLoop(terminal, logname, apipath, **kwargs)

    return ret


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
        'wifiIndex': 1,
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
    if ret:
        lastTime = int(t.time())
        curTime = int(t.time())
        status = getWifiStatus(terminal, logname)
        index = option['wifiIndex']
        if index == 3:
            # getWifiStatus can't get guest wifi status, check 2g instead of
            while str(status['status'][0]['up']) != str(option.get('on')) or curTime - lastTime <= 20:
                t.sleep(5)
                status = getWifiStatus(terminal, logname)
                curTime = int(t.time())
        else:
            while str(status['status'][index-1]['up']) != str(option.get('on')) or curTime - lastTime <= 20:
                t.sleep(5)
                status = getWifiStatus(terminal, logname)
                curTime = int(t.time())
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
    if ret:
        lastTime = int(t.time())
        curTime = int(t.time())
        status = getWifiStatus(terminal, logname)
        while str(status['status'][0]['up']) != str(option.get('on1')) or curTime - lastTime <= 20:
            t.sleep(5)
            status = getWifiStatus(terminal, logname)
            curTime = int(t.time())
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
    t.sleep(5)
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
    return setCheck(terminal, logname, api, **option)


def setRouterNormal(terminal, logname,  **kwargs):
    """
    name 路由器名
    locale 路由器地点
    nonce 加密用
    newPwd 新管理密码
    oldPwd 旧管理密码
    ssid wifi ssid
    encryption (none,mixed-psk,psk2)
    password wifi 密码
    txpwr 1 穿墙
    :param terminal:
    :param logname:
    :param kwargs:
    :return:
    """
    # old = getWebLoginOldPwd()
    # new = getWebLoginNewPwdEncryptBase64()
    t.sleep(1)  # wait 1 sec for nonce check, new nonce > old nonce
    old = getWebLoginOldPwd()
    new = getWebLoginNewPwdEncryptBase64()
    option = {
        'name': 'peanuts',
        'locale': 'com',
        'ssid': 'peanuts_check',
        'encryption': 'mixed-psk',
        'password': '12345678',
        'nonce': old['nonce'],
        'newPwd': new,
        'oldPwd': old['password'],
        'txpwr': 1,
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/misystem/set_router_normal'
    result = setCheck(terminal, logname, api, **option)
    if result:
        lastTime = int(t.time())
        curTime = int(t.time())
        status = getWifiStatus(terminal, logname)
        while int(status['status'][0]['up']) != 1 or curTime - lastTime <= 20:
            t.sleep(2)
            status = getWifiStatus(terminal, logname)
            curTime = int(t.time())
    return result


def setLanAp(terminal, logname, **kwargs):
    option = {
        'ssid': '',
        'password': '',
    }
    option.update(kwargs)
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_lan_ap'
    result = setGet(terminal, logname, api, **option)
    t.sleep(10)
    if result is not None:
        terminal.connect(host=result['ip'], password=v.WEB_PWD)
        return result
    return result
    # if result is not None:
    #     t.sleep(5)
    #     while not terminal.connect(host=result['ip'], password=v.WEB_PWD):
    #         t.sleep(2)
    #     return result
    # return None


def setDisableLanAp(terminal, logname):
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/disable_lan_ap'
    result = setGet(terminal, logname, api)
    t.sleep(10)
    if result is not None:
        terminal.connect(host=result['ip'], password=v.WEB_PWD)
        return result
    return result
    # if result is not None:
    #     t.sleep(5)
    #     while not terminal.connect(host=result['ip'], password=v.WEB_PWD):
    #         t.sleep(2)
    #     return result
    # return None


def getWifiDetailAll(terminal, logname):

    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/wifi_detail_all'
    ret = setGet(terminal, logname, api)
    if ret is not None:
        if ret['code'] is 0:
            return ret
    return None

def getWifiDetailDic(terminal, logname, intf):
    commandDic = {
        "2g": "{ 'wifiIndex': 1,"
              "'on': ret['info'][0]['status'],"
              "'ssid': ret['info'][0]['ssid'],"
              "'pwd': '',"
              "'encryption': ret['info'][0]['encryption'],"
              "'channel': ret['info'][0]['channel'],"
              "'bandwidth': ret['info'][0]['bandwidth'],"
              "'hidden': ret['info'][0]['hidden'],"
              "'txpwr': ret['info'][0]['txpwr']}",

        "5g": "{ 'wifiIndex': 2,"
              "'on': ret['info'][1]['status'],"
              "'ssid': ret['info'][1]['ssid'],"
              "'pwd': '',"
              "'encryption': ret['info'][1]['encryption'],"
              "'channel': ret['info'][1]['channel'],"
              "'bandwidth': ret['info'][1]['bandwidth'],"
              "'hidden': ret['info'][1]['hidden'],"
              "'txpwr': ret['info'][1]['txpwr']}",

        "guest":"{ 'wifiIndex': 3,"
              "'on': ret['info'][-1]['status'],"
              "'ssid': ret['info'][-1]['ssid'],"
              "'pwd': '',"
              "'encryption': ret['info'][-1]['encryption']}",
    }
    infoDic = {
        "2g": "ret['info'][0]",
        "5g": "ret['info'][1]",
        "guest": "ret['info'][-1]",
    }
    ret = getWifiDetailAll(terminal, logname)
    if ret is not None:
        resultDic = eval(commandDic.get(intf))
        for key, value in resultDic.items():
            if key is 'wifiIndex':
                continue
            resultDic[key] = str(value)
        infoDicIntf = eval(infoDic.get(intf))
        if "password"  in infoDicIntf.keys():
            resultDic["pwd"] = infoDicIntf.get("password")
        if intf == "guest":
            if "enabled" in infoDicIntf.keys():
                return resultDic
            else:
                return {}
        return resultDic
    else:
        return {}


def getWifiChannel(terminal, intf, logname):
    """
    channel = wifidetailall['info'][0]['channelInfo']['channel']
    :param terminal:
    :param intf:
    :param logname:
    :return:
    """
    ret = getWifiDetailAll(terminal, logname)
    if ret is None:
        return None
    else:
        commandDic = {
            '2g': "ret['info'][0]['channelInfo']['channel']",
            '5g': "ret['info'][1]['channelInfo']['channel']",
        }
        channel = commandDic.get(intf)
        return int(eval(channel))

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
    if ret is not None:
        if ret['code'] is 0:
            return ret
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
    if ret is not None:
        if ret['code'] is 0:
            return ret
    return None


def getOnlineDeviceType(terminal, logname):
    """
    "type": 0,       (0/1/2/3  有线 / 2.4G wifi / 5G wifi / guest wifi)
    :param terminal:
    :param logname:
    :return:
    """
    result = dict()
    option = {
        'online': 1,
        'withbrlan': 1,
    }
    ret = getDeviceList(terminal, logname, **option)
    if ret is not None:
        for d in ret['list']:
            result[d['mac']] = d['type']
        return result
    return None

def getWifiStatus(terminal, logname):
    """
    {'status': [{'ssid': 'peanuts', 'up': 0}, {'ssid': 'peanuts_automatic_test_suite-5G', 'up': 0}], 'code': 0}
    :param terminal:
    :param logname:
    :return:
    """
    api = '/cgi-bin/luci/;stok=token/api/xqnetwork/wifi_status'
    ret = setGet(terminal, logname, api)
    if ret is not None:
        return ret
    return None


if __name__ == '__main__':

    v.HOST = '192.168.31.1'
    v.WEB_PWD = '12345678'
    webclient = HttpClient()
    webclient.connect(host=v.HOST, password=v.WEB_PWD)
    setLanAp(webclient, 'aaa')

    print getWifiDetailDic(webclient, 'aaa', 'guest')

    setDisableLanAp(webclient, 'aaa')
    print getWifiDetailDic(webclient, 'aaa', 'guest')
    webclient.close()

