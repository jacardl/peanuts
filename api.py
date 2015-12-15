# coding=utf8
import httplib
import urllib
import hashlib
import time
import random
import var as v
import re
import time as t
import os


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
        f.write(apipath + '\n')
        f.writelines(str(ret))
        f.write('\n\n')
        f.close()
        return ret

    except Exception, e:
        curTime = t.strftime('%Y.%m.%d %H:%M:%S', t.localtime())
        f = open(v.TEST_SUITE_LOG_PATH + logname + '.log', 'a')
        f.write(curTime + '~#API request to ' + terminal.hostname + ' failed#')
        f.write(apipath + '\n')
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
        f.write(apipath + '\n')
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
        f.write(apipath + '\n')
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
            api = line.strip('\n').split(',')
            print api
            if len(api) > 1:
                api[1] = eval(api[1])
                setCheck(terminal, logname, api[0], **api[1])
            elif len(api) == 1:
                setCheck(terminal, logname, api[0])
    apifile.close()


if __name__ == '__main__':

    host = '192.168.15.1'
    # api = '/cgi-bin/luci/;stok=token/api/xqnetwork/set_wifi'
    # dictx = {'wifiIndex':1, 'on':1, 'ssid':'peanuts_mu', 'pwd':'12345678','encryption':'mixed-psk', 'channel':'11',
    #         'bandwidth':'20','hidden':'0', 'txpower':'mid'}
    webclient = HttpClient()
    webclient.connect(host)
    setCheckFromFile(webclient, 'api.data', 'aaa')
    webclient.close()



