# coding=utf8
import httplib
import urllib
import hashlib
import time
import random
import var as v
import re


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

    def connect(self, host, port=80):
        try:
            self.httpClient = httplib.HTTPConnection(host, port, timeout=30)
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
        subpath = re.sub('stok=token', self.token, path)
        print subpath
        if len(kwargs) is 0:
            self.httpClient.request('GET', subpath, headers=self.headers)
            response = self.httpClient.getresponse().read()
            responsedict = eval(response)
            return responsedict
        else:
            params = urllib.urlencode(kwargs)
            self.httpClient.request('POST', subpath, params, self.headers)
            response = self.httpClient.getresponse().read()
            responsedict = eval(response)
            return responsedict


if __name__ == '__main__':
    webclient = HttpClient()
    webclient.connect('192.168.15.1')
    print webclient.getToken(password=v.WEB_PWD)
    # print webclient.getApi('/cgi-bin/luci/;stok=token/api/xqsystem/main_status_for_app')
    # print webclient.getApi('/cgi-bin/luci/;stok=token/api/xqsystem/detection_ts')
    print webclient.getApi('/cgi-bin/luci/;stok=token/api/xqnetwork/set_wifi', wifiIndex=1, on=1, ssid='peanuts_mu', pwd='12345678',
                                                                                encryption='mixed-psk', channel='11', bandwidth='20',
                                                                                hidden='0', txpower='mid')




