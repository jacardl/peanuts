# -*- coding: utf8 -*-
from unittest import *

import api
from common import *
import data


class AP_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_LOW(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'min',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_MID(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_HIGH(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'max',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_LOW_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = ShellClient(v.CONNECTION_TYPE)
        self.dut2 = api.HttpClient()
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_CLEAR_MID_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = ShellClient(v.CONNECTION_TYPE)
        self.dut2 = api.HttpClient()
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'mid',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_CLEAR_HIGH_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = ShellClient(v.CONNECTION_TYPE)
        self.dut2 = api.HttpClient()
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_CLEAR_CHANSELECTION(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Http connection is failed. please check your remote settings.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def chanselection_2g(self):
        count = 0
        chan2g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option2g)
            channel = api.getWifiChannel(self.dut, '2g', self.__class__.__name__)
            if channel not in chan2g:
                self.fail("Current auto-selected channel isnot between 1 and 11.")
            else:
                count += 1

    def chanselection_5g(self):
        count = 0
        chan5g = [149, 153, 157, 161]
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option5g)
            channel = api.getWifiChannel(self.dut, '5g', self.__class__.__name__)
            if channel not in chan5g:
                self.fail("Current auto-selected channel isnot between 149 and 161.")
            else:
                count += 1


class AP_CLEAR_CHAN_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 0
        }
        api.setEditDevice(self.dut, self.__name__, **option)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

    @classmethod
    def tearDownClass(self):

        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 1
        }
        api.setEditDevice(self.dut, self.__name__, **option)
        api.setWifiMacFilter(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_clear_sta_in_whitelist_2g(self):

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if res2gConn is False:
            self.fail("Association wasnot successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")
        # connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
        # if self.staMac in connType.keys():
        #     self.fail(msg='STA should be kicked off.'

    def assoc_clear_sta_in_whitelist_5g(self):

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }

        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if res5gConn is False:
            self.fail("Association wasnot successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")
        # connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
        # if self.staMac in connType.keys():
        #     self.fail(msg='STA should be kicked off.')

    def assoc_clear_sta_outof_whitelist_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        # 鍒犻櫎鎵�鏈墂hitelist鍒欑櫧鍚嶅崟涓嶅啀鐢熸晥
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        # self.assertTrue(res2gConn, "Association should be successful when no sta in whitelist at all.")
        #
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 0
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)

    def assoc_clear_sta_outof_whitelist_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        self.assertFalse(res5gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        # 鍒犻櫎鎵�鏈墂hitelist鍒欑櫧鍚嶅崟涓嶅啀鐢熸晥
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        # self.assertTrue(res5gConn, "Association should be successful when no sta in whitelist at all.")
        #
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 0
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)


class AP_CLEAR_CHAN_BLACKLIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

    @classmethod
    def tearDownClass(self):
        api.setWifiMacFilter(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_clear_sta_outof_blacklist_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_outof_blacklist_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_in_blacklist_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if self.staMac in connType.keys():
            self.fail(msg='STA should be kicked off.')

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta in blacklist.")

    def assoc_clear_sta_in_blacklist_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        self.assertTrue(res5gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if self.staMac in connType.keys():
            self.fail(msg='STA should be kicked off.')

        self.assertFalse(res5gConn, "Association wasnot supposed to be successful which sta in blacklist.")


class AP_CLEAR_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_repeat_clear_sta_2g(self):

        res2gConn = setAdbClearStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_clear_sta_5g(self):

        res5gConn = setAdbClearStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_PSK2_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_PSK2_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_repeat_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_MIXEDPSK_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW80(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '80',
        }

        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW40(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW20(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SPECIAL_SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SPECIAL_SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_ssidspec_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidspec_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_2g(self):
        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_keyspec_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_keyspec_5g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_5g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.CHINESE_SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.CHINESE_SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidchinese_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_repeat_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_2g(self):

        res2gConn = setAdbPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_5g(self):

        res5gConn = setAdbPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_MIXEDPSK_BSD(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_MIXEDPSK_BSD_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'bsd': 1,
            'ssid1': v.SPECIAL_SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SPECIAL_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SPECIAL_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SPECIAL_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SPECIAL_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_MIXEDPSK_BSD_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.SPECIAL_KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.SPECIAL_KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.SPECIAL_KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.SPECIAL_KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.SPECIAL_KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_MIXEDPSK_BSD_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'bsd': 1,
            'ssid1': v.CHINESE_SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.CHINESE_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.CHINESE_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.CHINESE_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.CHINESE_SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_MIXEDPSK_BSD_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 0
        }
        api.setEditDevice(self.dut, self.__name__, **option)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo['mac'].upper()

    @classmethod
    def tearDownClass(self):
        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 1
        }
        api.setEditDevice(self.dut, self.__name__, **option)
        api.setWifiMacFilter(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta_in_whitelist(self):

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if res2gConn is False:
            self.fail("Association wasnot successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk2_near_field_sta_outof_whitelist(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta outof whitelist.")


class AP_MIXEDPSK_BSD_BLACKLIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo['mac'].upper()

    @classmethod
    def tearDownClass(self):
        api.setWifiMacFilter(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta_outof_blacklist(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

    def assoc_psk2_near_field_sta_in_blacklist(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if self.staMac in connType.keys():
            self.fail(msg='STA should be kicked off.')

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta in blacklist.")


class AP_MIXEDPSK_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo['mac'].upper()

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_GUEST_CLEAR(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_guest(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_PSK2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_guest(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_guest(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_guest(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_CLEAR_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 0
        }
        api.setEditDevice(self.dut, self.__name__, **option)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

    @classmethod
    def tearDownClass(self):
        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 1
        }
        api.setEditDevice(self.dut, self.__name__, **option)
        api.setWifiMacFilter(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_in_whitelist_guest(self):
        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if res2gConn is False:
            self.fail("Association wasnot successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

        # connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
        # if self.staMac in connType.keys():
        #     self.fail(msg='STA should be kicked off.')

    def assoc_clear_sta_outof_whitelist_guest(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        # self.assertTrue(res2gConn, "Association should be successful when no sta in whitelist at all.")
        #
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 0
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)


class AP_GUEST_CLEAR_BLACKLIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

    @classmethod
    def tearDownClass(self):
        api.setWifiMacFilter(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_outof_blacklist_guest(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_in_blacklist_guest(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)
        self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0,
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 1,
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if self.staMac in connType.keys():
            self.fail(msg='STA should be kicked off.')

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta in blacklist.")


class AP_GUEST_CLEAR_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_clear_sta_guest(self):

        res2gConn = setAdbClearStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_GUEST_MIXEDPSK_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_guest(self):

        res2gConn = setAdbPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_guest(self):

        res2gConn = setAdbTkipPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_guest(self):

        res2gConn = setAdbTkipPskStaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_GUEST_PSK2_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConnRepeat(v.ANDROID_SERIAL_NUM, "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

    @classmethod
    def tearDownClass(self):
        self.dut.close()

    def ap_clear_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_clear_ssidhide_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'hidden': 1
        }

        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_psk2_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_psk2_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')


class AP_MIXEDPSK_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def ap_clear_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'none',
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_psk2_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'psk2',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_mixedpsk_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')


class AP_RELAY_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_LOW(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'min',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_MID(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_HIGH(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'max',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_LOW_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut2 = api.HttpClient()
        ret2 = self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret2 is False:
            raise Exception('Connection is failed for httpclient. please check your remote settings.')

        api.setLanAp(self.dut2, self.__name__)

        self.dut = ShellClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed for shell after setLanAp.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)

        api.setDisableLanAp(self.dut2, self.__name__)

        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[0] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_RELAY_CLEAR_MID_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut2 = api.HttpClient()
        ret2 = self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret2 is False:
            raise Exception('Connection is failed for httpclient. please check your remote settings.')

        api.setLanAp(self.dut2, self.__name__)

        self.dut = ShellClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed for shell after setLanAp.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)

        api.setDisableLanAp(self.dut2, self.__name__)
        
        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'mid',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[1] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_RELAY_CLEAR_HIGH_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut2 = api.HttpClient()
        ret2 = self.dut2.connect(host=v.HOST, password=v.WEB_PWD)
        if ret2 is False:
            raise Exception('Connection is failed for httpclient. please check your remote settings.')

        api.setLanAp(self.dut2, self.__name__)

        self.dut = ShellClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed for shell after setLanAp.')

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)

        api.setDisableLanAp(self.dut2, self.__name__)

        self.dut.close()
        self.dut2.close()

    def autochan_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL1,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL6,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL11,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL13,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, "2g", self.__class__.__name__)

        minPower = data.txPower2G.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower2G.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL36,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL52,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GL.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL165,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

        minPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 0.985
        maxPower = data.txPower5GH.get(v.DUT_MODULE)[2] * 1.015

        if minPower <= power <= maxPower:
            pass
        else:
            self.fail("Txpower isnot correct.")


class AP_RELAY_CLEAR_CHANSELECTION(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Http connection is failed. please check your remote settings.')

        api.setLanAp(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def chanselection_2g(self):
        count = 0
        chan2g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option2g)
            channel = api.getWifiChannel(self.dut, '2g', self.__class__.__name__)
            if channel not in chan2g:
                self.fail("Current auto-selected channel isnot between 1 and 11.")
            else:
                count += 1

    def chanselection_5g(self):
        count = 0
        chan5g = [149, 153, 157, 161]
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option5g)
            channel = api.getWifiChannel(self.dut, '5g', self.__class__.__name__)
            if channel not in chan5g:
                self.fail("Current auto-selected channel isnot between 149 and 161.")
            else:
                count += 1


class AP_RELAY_PSK2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_CHAN_BW80(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '80',
        }

        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_CHAN_BW40(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_CHAN_BW20(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SPECIAL_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SPECIAL_SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_ssidspec_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidspec_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_2g(self):
        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_keyspec_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_keyspec_5g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_5g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.CHINESE_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.CHINESE_SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidchinese_5g(self):

        res5gConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_2g(self):

        res2gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_5g(self):

        res5gConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        res2gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_MIXEDPSK_BSD(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_RELAY_MIXEDPSK_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2StaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskStaConn(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_RELAY_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def ap_clear_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_clear_ssidhide_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'hidden': 1
        }

        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_psk2_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_psk2_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')


class AP_RELAY_MIXEDPSK_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_RELAY_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):

        api.setDisableLanAp(self.dut, self.__name__)

        self.dut.close()

    def ap_clear_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'none',
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_psk2_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'psk2',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_mixedpsk_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')


class AP_RELAY_CONFIG_CHECK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        self.option2g = {
            'wifiIndex': 1,
            'on': "1",
            'ssid': v.SSID,
            'pwd': v.KEY,
            'encryption': 'mixed-psk',
            'channel': v.CHANNEL11,
            'bandwidth': '20',
            'hidden': "0",
            'txpwr': 'max'
        }

        self.option5g = {
            'wifiIndex': 2,
            'on': "1",
            'ssid': v.SSID_5G,
            'pwd': v.KEY,
            'encryption': 'psk2',
            'channel': v.CHANNEL149,
            'bandwidth': '40',
            'hidden': "0",
            'txpwr': 'min'
        }

        self.optionGuest = {
            'wifiIndex': 3,
            'on': "1",
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **self.option2g)
        api.setWifi(self.dut, self.__name__, **self.option5g)
        api.setWifi(self.dut, self.__name__, **self.optionGuest)
        api.setLanAp(self.dut, self.__name__)

        self.relay2g = api.getWifiDetailDic(self.dut, self.__name__, "2g")
        self.relay5g = api.getWifiDetailDic(self.dut, self.__name__, "5g")
        self.relayGuest = api.getWifiDetailDic(self.dut, self.__name__, "guest")

        api.setDisableLanAp(self.dut, self.__name__)

        self.router2g = api.getWifiDetailDic(self.dut, self.__name__, "2g")
        self.router5g = api.getWifiDetailDic(self.dut, self.__name__, "5g")
        self.routerGuest = api.getWifiDetailDic(self.dut, self.__name__, "guest")

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def config_check_2g(self):

        self.assertDictEqual(self.relay2g, self.option2g,
                             msg="Normal router module switch over to wire relay module, wifi config should not be changed.")
        self.assertDictEqual(self.router2g, self.option2g,
                             msg="Wire relay module switch back to normal router module, wifi config should not be changed.")

    def config_check_5g(self):

        self.assertDictEqual(self.relay5g, self.option5g,
                             msg="Normal router module switch over to wire relay module, wifi config should not be changed.")
        self.assertDictEqual(self.router5g, self.option5g,
                             msg="Wire relay module switch back to normal router module, wifi config should not be changed.")

    def config_check_guest(self):

        # when wire relay module switch back to normal router module, guest wifi is turned off
        self.optionGuest["on"] = "0"
        self.assertDictEqual(self.relayGuest, {}, msg="Wire relay module should not support guest wifi")
        self.assertDictEqual(self.routerGuest, self.optionGuest,
                             msg="Wire relay switch back to normal router module, guest wifi should be turned off.")


class AP_QOS_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

        optionQos = {
            'mac': self.staMac,
            'upload': v.QOS_MAXUP,
            'download': v.QOS_MAXDOWN,
        }

        api.setQosSwitch(self.dut, self.__name__)
        api.setMACQoSInfo(self.dut, self.__name__, **optionQos)

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        optionQosSwitch = {
            'on': 0,
        }
        api.setQosSwitch(self.dut, self.__name__, **optionQosSwitch)

        self.dut.close()

    def assoc_psk2_sta_speedtest_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_speedtest_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_speedtest_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_speedtest_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_speedtest_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_speedtest_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_speedtest_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_speedtest_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_QOS_CLEAR(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

        optionQos = {
            'mac': self.staMac,
            'upload': v.QOS_MAXUP,
            'download': v.QOS_MAXDOWN,
        }

        api.setQosSwitch(self.dut, self.__name__)
        api.setMACQoSInfo(self.dut, self.__name__, **optionQos)

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        optionQosSwitch = {
            'on': 0,
        }
        api.setQosSwitch(self.dut, self.__name__, **optionQosSwitch)

        self.dut.close()

    def assoc_clear_sta_speedtest_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_speedtest_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_QOS_PSK2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

        optionQos = {
            'mac': self.staMac,
            'upload': v.QOS_MAXUP,
            'download': v.QOS_MAXDOWN,
        }

        api.setQosSwitch(self.dut, self.__name__)
        api.setMACQoSInfo(self.dut, self.__name__, **optionQos)

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        optionQosSwitch = {
            'on': 0,
        }
        api.setQosSwitch(self.dut, self.__name__, **optionQosSwitch)

        self.dut.close()

    def assoc_psk2_sta_speedtest_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_speedtest_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], v.QOS_MAXDOWN * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], v.QOS_MAXDOWN))
                self.assertLessEqual(speedTestRes['up'], v.QOS_MAXUP * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (speedTestRes['up'], v.QOS_MAXUP))
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_QOS_GUEST_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

        api.setQosSwitch(self.dut, self.__name__)

        optionGuest = {
            'percent': 0.15,
            'percent_up': 0.1,
        }

        self.guestQos = api.setQosGuest2(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):

        optionQosSwitch = {
            'on': 0
        }

        api.setQosSwitch(self.dut, self.__name__, **optionQosSwitch)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_speedtest_guest(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, v.KEY, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], self.guestQos['guest']['down'] * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], self.guestQos['guest']['down']))
                self.assertLessEqual(speedTestRes['up'], self.guestQos['guest']['up'] * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (
                                         speedTestRes['up'], self.guestQos['guest']['up']))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_speedtest_guest(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, v.KEY, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], self.guestQos['guest']['down'] * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], self.guestQos['guest']['down']))
                self.assertLessEqual(speedTestRes['up'], self.guestQos['guest']['up'] * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (
                                         speedTestRes['up'], self.guestQos['guest']['up']))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_speedtest_guest(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, v.KEY, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], self.guestQos['guest']['down'] * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], self.guestQos['guest']['down']))
                self.assertLessEqual(speedTestRes['up'], self.guestQos['guest']['up'] * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (
                                         speedTestRes['up'], self.guestQos['guest']['up']))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_speedtest_guest(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, v.KEY, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speedTestRes = getAdbOoklaSpeedTestResult(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
                self.assertLessEqual(speedTestRes['down'], self.guestQos['guest']['down'] * 1.1,
                                     "Downlink rate %s KB/s exceed maxdown %s KB/s" % (
                                         speedTestRes['down'], self.guestQos['guest']['down']))
                self.assertLessEqual(speedTestRes['up'], self.guestQos['guest']['up'] * 1.1,
                                     "Uplink rate %s KB/s exceed maxup %s KB/s" % (
                                         speedTestRes['up'], self.guestQos['guest']['up']))
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'none',
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)
        
        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_PSK2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'psk2',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'mixed-psk',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g",
                                      self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g",
                                     self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'mixed-psk',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1,
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SPECIAL_SSID,
            'nencryption': 'mixed-psk',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_ssidspec_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID, v.KEY, "2g",
                                  self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidspec_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID_5G, v.KEY, "5g",
                                  self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID, v.KEY, "2g",
                                 self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID_5G, v.KEY, "5g",
                                 self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID, v.KEY, "2g",
                                      self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID_5G, v.KEY, "5g",
                                      self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_2g(self):
        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID, v.KEY, "2g",
                                     self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SPECIAL_SSID_5G, v.KEY, "5g",
                                     self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'mixed-psk',
            'npassword': v.SPECIAL_KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_keyspec_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.SPECIAL_KEY, "2g",
                                  self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_keyspec_5g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.SPECIAL_KEY, "5g",
                                  self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.SPECIAL_KEY, "2g",
                                 self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_5g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.SPECIAL_KEY, "5g",
                                 self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.SPECIAL_KEY, "2g",
                                      self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.SPECIAL_KEY, "5g",
                                      self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.SPECIAL_KEY, "2g",
                                     self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.SPECIAL_KEY, "5g",
                                     self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_CHINESE_SSID,
            'nencryption': 'mixed-psk',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID, v.KEY, "2g",
                                  self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidchinese_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID_5G, v.KEY, "5g",
                                  self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID, v.KEY, "2g",
                                 self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID_5G, v.KEY, "5g",
                                 self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID, v.KEY, "2g",
                                      self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID_5G, v.KEY, "5g",
                                      self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID, v.KEY, "2g",
                                     self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_CHINESE_SSID_5G, v.KEY, "5g",
                                     self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_LOW(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'min',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_MID(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_HIGH(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'txpwr': 'max',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_CHANSELECTION(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception('Http connection is failed. please check your remote settings.')

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def chanselection_2g(self):
        count = 0
        chan2g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option2g)
            channel = api.getWifiChannel(self.dut, '2g', self.__class__.__name__)
            if channel not in chan2g:
                self.fail("Current auto-selected channel isnot between 1 and 11.")
            else:
                count += 1

    def chanselection_5g(self):
        count = 0
        chan5g = [149, 153, 157, 161]
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        while count < 10:
            api.setWifi(self.dut, self.__class__.__name__, **option5g)
            channel = api.getWifiChannel(self.dut, '5g', self.__class__.__name__)
            if channel not in chan5g:
                self.fail("Current auto-selected channel isnot between 149 and 161.")
            else:
                count += 1


class AP_WIRELESS_RELAY_MIXEDPSK_CHAN_BW80(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '80',
        }

        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_CHAN_BW40(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)
        
        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_CHAN_BW20(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT,
                                                  self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_MIXEDPSK_BSD(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_WIRELESS_RELAY_MIXEDPSK_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        api.setAllWifi(self.dut, self.__name__)
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
            resConn2 = chkAdb5gFreq(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if resConn and resConn2:
                break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(v.ANDROID_SERIAL_NUM, v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_WIRELESS_RELAY_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def ap_clear_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID, self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_clear_ssidhide_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'hidden': 1
        }

        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID_5G, self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_psk2_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID, self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_psk2_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'psk2',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID_5G, self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_2g(self):
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        ret2g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID, self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

    def ap_mixedpsk_ssidhide_5g(self):
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'hidden': 1
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        ret5g = chkAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, v.SSID_5G, self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')


class AP_WIRELESS_RELAY_BSD_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        api.setDisableAp(self.dut, self.__name__)

        self.dut.close()

    def ap_clear_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'none',
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_psk2_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'psk2',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')

    def ap_mixedpsk_ssidhide(self):
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd': v.KEY,
            'hidden1': 1,
        }
        api.setAllWifi(self.dut, self.__class__.__name__, **option)

        ret = setAdbScanSsidNoExist(v.ANDROID_SERIAL_NUM, "normal", "2g", self.__class__.__name__)

        api.setAllWifi(self.dut, self.__class__.__name__)

        if ret is False:
            self.fail(msg='ssid should be hidden when bsd is on')


class AP_WIRELESS_RELAY_CONFIG_CHECK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        self.option2g = {
            'wifiIndex': 1,
            'on': "1",
            'ssid': v.SSID,
            'pwd': v.KEY,
            'encryption': 'mixed-psk',
            'channel': v.CHANNEL11,
            'bandwidth': '20',
            'hidden': "0",
            'txpwr': 'max'
        }

        self.option5g = {
            'wifiIndex': 2,
            'on': "1",
            'ssid': v.SSID_5G,
            'pwd': v.KEY,
            'encryption': 'psk2',
            'channel': v.CHANNEL149,
            'bandwidth': '40',
            'hidden': "0",
            'txpwr': 'min'
        }

        self.optionGuest = {
            'wifiIndex': 3,
            'on': "1",
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **self.option2g)
        api.setWifi(self.dut, self.__name__, **self.option5g)
        api.setWifi(self.dut, self.__name__, **self.optionGuest)

        option = {
            'ssid': v.ROOT_AP_SSID,
            # 'encryption': 'WPA2PSK',
            # 'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            # 'channel': v.ROOT_AP_CHANNEL,
            # 'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'WPA2PSK',
            'npassword': v.ROOT_AP_PWD,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

        self.relayConfGuest = api.getWifiDetailDic(self.dut, self.__name__, "guest")

        api.setDisableAp(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def config_check_2g(self):
        routerConf2g = api.getWifiDetailDic(self.dut, self.__class__.__name__, "2g")

        self.assertDictEqual(routerConf2g, self.option2g,
                             msg="Wireless relay module switch back to normal router module, wifi config should not be changed.")

    def config_check_5g(self):
        routerConf5g = api.getWifiDetailDic(self.dut, self.__class__.__name__, "5g")

        self.assertDictEqual(routerConf5g, self.option5g,
                             msg="Wireless relay module switch back to normal router module, wifi config should not be changed.")

    def config_check_guest(self):
        routerConfGuest = api.getWifiDetailDic(self.dut, self.__class__.__name__, "guest")

        self.optionGuest["on"] = "0"
        self.assertDictEqual(self.relayConfGuest, {}, msg="Wireless relay module should not support guest wifi")
        self.assertDictEqual(routerConfGuest, self.optionGuest,
                             msg="Wireless relay switch back to normal router module, guest wifi should be turned off.")


class AP_WIRELESS_RELAY_SCAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        if ret is False:
            raise Exception("Http connection is failed. please check your remote settings.")

    @classmethod
    def tearDownClass(self):

        self.dut.close()
        

    def scan_radio_on_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        option = {
            'ssid': v.ROOT_AP_SSID,
        }

        res, wifiInfo = api.chkWifiInfo(self.dut, self.__class__.__name__, **option)

        if res is False:
            self.fail(msg="Scan wifi list should be successful when 2.4g radio on.")

        result = api.setWifiAp(self.dut, self.__class__.__name__, **wifiInfo)

        self.assertEqual(result['code'], 0,
                         msg='Switching to wireless relay module should be successful using wifi info scaned')

        api.setDisableAp(self.dut, self.__class__.__name__)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

    def scan_radio_off_2g(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__class__.__name__, **option2g)

        option = {
            'ssid': v.ROOT_AP_SSID,
        }

        res, wifiInfo = api.chkWifiInfo(self.dut, self.__class__.__name__, **option)

        if res is False:
            self.fail(msg="Scan wifi list should be successful when 2.4g radio off.")

        result = api.setWifiAp(self.dut, self.__class__.__name__, **wifiInfo)

        self.assertEqual(result['code'], 0,
                         msg='Switching to wireless relay module should be successful using wifi info scaned')

        api.setDisableAp(self.dut, self.__class__.__name__)


class AP_MIXEDPSK_WEB_ACCESS(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()

        option = {
            'open': 1,
            'opt': 0,
            'mac': self.staMac,
        }

        api.setWebAccessOpt(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        option = {
            'open': 0,
        }

        api.setWebAccessOpt(self.dut, self.__name__, **option)

        self.dut.close()

    def assoc_psk2_sta_access_web_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_access_web_2g(self):
        res2gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_access_web_2g(self):
        res2gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_access_web_2g(self):
        res2gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_access_web_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_access_web_5g(self):
        res5gConn = setAdbPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_access_web_5g(self):
        res5gConn = setAdbTkipPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_access_web_5g(self):
        res5gConn = setAdbTkipPskSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res5gConn:
            ret1 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 1,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)

            ret2 = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL, self.__class__.__name__)

            option = {
                'open': 1,
                'opt': 0,
                'mac': self.staMac,
            }

            api.setWebAccessOpt(self.dut, self.__class__.__name__, **option)
            if ret1 is False:
                self.fail("STA in whitelist should be allowed access web")
            self.assertFalse(ret2, "STA out of whitelist should not be allowed access web")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_CHAN1_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN1_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN165_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN44_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN60_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN157_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN165_BW20_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN44_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN60_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN157_BW40_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW80_DUT_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        self.dut2 = ShellClient(v.CONNECTION_TYPE)
        ret3 = self.dut2.connect(v.HOST, v.USR, v.PASSWD)

        if ret3 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.dut2.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(4.0)
            ret = setIperfFlow2(self.dut2, result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN1_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN1_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN165_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN44_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN60_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN157_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN165_BW20_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN44_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN60_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN157_BW40_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW80_LAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN1_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN1_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN1_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL1,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL6,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL13,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.wanStatus = api.getPppoeStatus(self.dut, self.__name__)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN165_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN44_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN60_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN157_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN36_BW80_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN52_BW80_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN149_BW80_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80'
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN165_BW20_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL165,
            'bandwidth': '20',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN44_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL44,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN60_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL60,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN157_BW40_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL157,
            'bandwidth': '40',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN36_BW80_WLAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL36,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN52_BW80_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL52,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN149_BW80_WAN_THROUGHPUT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        self.pc = ShellClient(4)
        ret3 = self.pc.connect(host=v.PC_HOST, userid=v.PC_USERNAME, password=v.PC_PWD)

        if ret3 is False:
            raise Exception("PC telnet connection is failed, please check network.")

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'bandwidth': '80',
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()
        self.pc.close()

    def assoc_sta_throughput_5g(self):
        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn is True:
            staStatus = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            optionRedirect = {
                "name": "iperf",
                "proto": 1,
                "sport": v.IPERF_PORT,
                "ip": staStatus.get('ip'),
                "dport": v.IPERF_PORT,
            }
            api.setAddRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            iperfOn = SetAdbIperfOn(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow3(self.pc, self.wanStatus.get('ip'), v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)

            optionRedirect = {
                'port': v.IPERF_PORT
            }
            api.setDelRedirect(self.dut, self.__class__.__name__, **optionRedirect)
            api.setRedirectApply(self.dut, self.__class__.__name__)

            self.assertTrue(ret, "Excute iperf flow error, connection refused.")
        else:
            self.assertTrue(res5gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_speedtest_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_CLEAR_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_speedtest_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_PSK2_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_speedtest_5g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_CLEAR_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_clear_sta_speedtest_5g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_PSK2_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_speedtest_guest(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, v.KEY, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_CLEAR_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_speedtest_guest(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.GUEST_SSID, "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_PSK2_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_psk2_sta_speedtest_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL11,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_speedtest_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_PSK2_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_psk2_sta_speedtest_5g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_RELAY_CLEAR_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        api.setLanAp(self.dut, self.__name__)

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL149,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        api.setDisableLanAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_speedtest_5g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_PSK2_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'psk2',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setDisableAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_psk2_sta_speedtest_2g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, v.KEY, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_CHAN11_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'none',
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setDisableAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_speedtest_2g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID, "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_PSK2_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'psk2',
            'npassword': v.KEY,
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setDisableAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_psk2_sta_speedtest_5g(self):
        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, v.KEY, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WIRELESS_RELAY_CLEAR_CHAN149_OOKLA(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)

        option = {
            'ssid': v.ROOT_AP_SSID,
            'encryption': 'WPA2PSK',
            'enctype': 'TKIPAES',
            'password': v.ROOT_AP_PWD,
            'channel': v.ROOT_AP_CHANNEL,
            'bandwidth': '20',
            'nssid': v.WIRELESS_RELAY_SSID,
            'nencryption': 'none',
        }
        api.setWifiAp(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):
        api.setDisableAp(self.dut, self.__name__)
        self.dut.close()

    def assoc_clear_sta_speedtest_5g(self):
        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.WIRELESS_RELAY_SSID_5G, "5g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                speed = getAdbOoklaSpeedTestShot(v.ANDROID_SERIAL_NUM, self.__class__.__name__, self.__class__.__name__)
                self.assertTrue(speed, "Ookla speedtest run for wrong.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_WAN_BANDWIDTH(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

    @classmethod
    def tearDownClass(self):
        self.dut.close()

    def test_wan_bandwidth(self):
        ret, speedDict= api.getWanBandwidth(self.dut, self.__class__.__name__)
        self.assertTrue(ret, "WAN port bandwidth test run for wrong.")


class AP_MIXEDPSK_NET_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'white'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_in_whitelist_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                    }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                    }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website in whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_in_whitelist_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                    }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website in whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")



    def assoc_psk2_sta_outof_whitelist_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertFalse(ret, msg='STA should not browser website outof whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_outof_whitelist_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertFalse(ret, msg='STA should not browser website outof whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_CLEAR_NET_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'white'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_clear_sta_in_whitelist_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website in whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_in_whitelist_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'white',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website in whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


    def assoc_clear_sta_outof_whitelist_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertFalse(ret, msg='STA should not browser website outof whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_outof_whitelist_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertFalse(ret, msg='STA should not browser website outof whitelist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_MIXEDPSK_NET_BLACKLIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'black'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_in_blacklist_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertFalse(ret, msg='STA should not browser website in blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_in_blacklist_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertFalse(ret, msg='STA should not browser website in blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")



    def assoc_psk2_sta_outof_blacklist_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertTrue(ret, msg='STA should browser website outof blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_outof_blacklist_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertTrue(ret, msg='STA should browser website outof blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_CLEAR_NET_BLACKLIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'black'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none'
        }
        api.setParentCtrlFilter(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_clear_sta_in_blacklist_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertFalse(ret, msg='STA should not browser website in blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_in_blacklist_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '0',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)

                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)

                option = {
                    'mac': self.staMac,
                    'mode': 'black',
                    'opt': '1',
                    'url': v.CHECK_ACCESS_URL2.split("//")[1],
                }
                api.setParentCtrlUrl(self.dut, self.__class__.__name__, **option)
                self.assertFalse(ret, msg='STA should not browser website in blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_outof_blacklist_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertTrue(ret, msg='STA should browser website outof blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_outof_blacklist_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, v.CHECK_ACCESS_URL2, self.__class__.__name__)
                self.assertTrue(ret, msg='STA should browser website outof blacklist')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_MIXEDPSK_NET_CUTOFF_LIMITED(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'limited',
            'enable': '1',
        }
        api.setNetAccessCtrl(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none',
            'enable': '1',
        }
        api.setNetAccessCtrl(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    self.assertFalse(ret, msg='STA should not browser website when net cutoff.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_ctrloff_2g(self):

        res2gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID, v.KEY, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'enable': '0',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)

                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    if ret is False:
                        break
                option = {
                    'mac': self.staMac,
                    'mode': 'limited',
                    'enable': '1',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website when net control off.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    self.assertFalse(ret, msg='STA should not browser website when net cutoff.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_psk2_sta_ctrloff_5g(self):

        res5gConn = setAdbPsk2Sta(v.ANDROID_SERIAL_NUM, v.SSID_5G, v.KEY, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'enable': '0',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)

                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    if ret is False:
                        break
                option = {
                    'mac': self.staMac,
                    'mode': 'limited',
                    'enable': '1',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website when net control off.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_CLEAR_NET_CUTOFF_LIMITED(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevice(v.ANDROID_SERIAL_NUM)

        if ret1 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Device %s is not ready!" % v.ANDROID_SERIAL_NUM)
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        wlanInfo = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__name__)
        self.staMac = wlanInfo["mac"].upper()
        option = {
            'mac': self.staMac,
            'mode': 'limited',
            'enable': '1',
        }
        api.setNetAccessCtrl(self.dut, self.__name__, **option)

    @classmethod
    def tearDownClass(self):

        option = {
            'mac': self.staMac,
            'mode': 'none',
            'enable': '1',
        }
        api.setNetAccessCtrl(self.dut, self.__name__, **option)

        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    self.assertFalse(ret, msg='STA should not browser website when net cutoff.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_ctrloff_2g(self):

        res2gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID, "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'enable': '0',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)

                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    if ret is False:
                        break
                option = {
                    'mac': self.staMac,
                    'mode': 'limited',
                    'enable': '1',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website when net control off.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    self.assertFalse(ret, msg='STA should not browser website when net cutoff.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")

    def assoc_clear_sta_ctrloff_5g(self):

        res5gConn = setAdbClearSta(v.ANDROID_SERIAL_NUM, v.SSID_5G, "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(v.ANDROID_SERIAL_NUM, self.__class__.__name__)
            if result['ip'] != '':
                option = {
                    'mac': self.staMac,
                    'enable': '0',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)

                for url in iter((v.CHECK_ACCESS_URL2, v.CHECK_ACCESS_URL3, v.CHECK_ACCESS_URL4)):
                    ret = chkAdbBrowserWebsite(v.ANDROID_SERIAL_NUM, url, self.__class__.__name__)
                    if ret is False:
                        break
                option = {
                    'mac': self.staMac,
                    'mode': 'limited',
                    'enable': '1',
                }
                api.setNetAccessCtrl(self.dut, self.__class__.__name__, **option)
                self.assertTrue(ret, msg='STA should browser website when net control off.')
            else:
                self.fail("STA should get IP address.")
        else:
            self.fail("Association should be successful.")


class AP_CHECK(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = ShellClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        self.dut2 = api.HttpClient()
        ret2 = self.dut2.connect(host=v.HOST, password=v.WEB_PWD)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("Http connection is failed. please check your remote settings.")

        option2g = {
            'wifiIndex': 1,
            'ssid': 'peanuts_check',
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'channel': v.CHANNEL11,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': 'peanuts_check',
            'encryption': 'mixed',
            'pwd': v.KEY,
            'channel': v.CHANNEL149,
        }
        api.setWifi(self.dut2, self.__name__, **option2g)
        api.setWifi(self.dut2, self.__name__, **option5g)

    @classmethod
    def tearDownClass(self):
        pass

    def check_ap_reboot_lastestpower(self):
        count = 0
        while count <= 800:
            setMvFile(self.dut, self.__class__.__name__, src='/tmp/messages', dst='/tmp/message1')
            setReboot(self.dut, self.__class__.__name__)
            t.sleep(60)
            while 1:
                try:
                    self.dut = ShellClient(v.CONNECTION_TYPE)
                    ret = self.dut.connect(v.HOST, v.USR, v.PASSWD)
                    if ret is True:
                        chkCount = 0
                        while 1:
                            if chkCount < 20:
                                result = chkBootingUpFinished(self.dut, self.__class__.__name__)
                                if result is True:
                                    break
                                else:
                                    chkCount += 1
                                    t.sleep(10)
                            else:
                                self.fail(msg='reboot is failed')
                        break
                    else:
                        t.sleep(10)
                except Exception, e:
                    raise e

            power2g = 0
            power5g = 0
            while power2g == 0 or power5g == 0:
                power2g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                txPower2g = getWlanTxPower(self.dut, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, "5g", self.__class__.__name__)
                t.sleep(1)

            if power2g <= (txPower2g - 5) or power5g <= (txPower5g - 5):
                loop = 0
                while loop < 120:
                    getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                    getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                    loop += 1
                    t.sleep(300)
                self.fail(msg='last est power check is failed')
            count += 1

    def check_ap_upgrade_lastestpower(self):
        count = 0
        while count <= 800:
            upgradefile = getFilePath(self.dut, self.__class__.__name__, path='/extdisks', pattern='brcm4709*')
            if len(upgradefile) is not 0:
                setCopyFile(self.dut, self.__class__.__name__, src=upgradefile, dst='/tmp/upgrade.bin')
                while not getFilePath(self.dut, self.__class__.__name__, path='/tmp', pattern='upgrade.bin'):
                    t.sleep(1)
                setMvFile(self.dut, self.__class__.__name__, src='/tmp/messages', dst='/tmp/message1')
                setUpgradeSystem(self.dut, '/tmp/upgrade.bin', self.__class__.__name__)
                t.sleep(60)
                while 1:
                    try:
                        self.dut = ShellClient(v.CONNECTION_TYPE)
                        ret = self.dut.connect(v.HOST, v.USR, v.PASSWD)
                        if ret is True:
                            chkCount = 0
                            while 1:
                                if chkCount < 20:
                                    result = chkBootingUpFinished(self.dut, self.__class__.__name__)
                                    if result is True:
                                        break
                                    else:
                                        chkCount += 1
                                        t.sleep(10)
                                else:
                                    self.fail(msg='upgrade is failed')
                            break
                        else:
                            t.sleep(10)
                    except Exception, e:
                        raise e

            power2g = 0
            power5g = 0
            while power2g == 0 or power5g == 0:
                power2g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                txPower2g = getWlanTxPower(self.dut, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, "5g", self.__class__.__name__)
                t.sleep(1)

            if power2g <= (txPower2g - 5) or power5g <= (txPower5g - 5):
                loop = 0
                while loop < 120:
                    getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                    getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                    loop += 1
                    t.sleep(300)
                self.fail(msg='last est power check is failed')
            else:
                self.fail(msg='fail to find upgrade file!')
            count += 1

    def check_ap_reset_lastestpower(self):
        count = 0
        while count <= 800:
            setMvFile(self.dut, self.__class__.__name__, src='/tmp/messages', dst='/tmp/message1')
            api.setReset(self.dut2, self.__class__.__name__)
            t.sleep(60)
            while 1:
                try:
                    self.dut = ShellClient(v.CONNECTION_TYPE)
                    ret = self.dut.connect(v.HOST, v.USR, v.PASSWD)
                    if ret is True:
                        chkCount = 0
                        while 1:
                            if chkCount < 20:
                                result = chkBootingUpFinished(self.dut, self.__class__.__name__)
                                if result is True:
                                    break
                                else:
                                    chkCount += 1
                                    t.sleep(10)
                            else:
                                self.fail(msg='reboot is failed')
                        break
                    else:
                        t.sleep(10)
                except Exception, e:
                    raise e

            # router_init
            option = {
                'name': 'peanuts',
                'locale': '公司',
                'ssid': 'peanuts_check',
                'encryption': 'mixed-psk',
                'password': v.KEY,
                'txpwr': 1,
            }
            webclient = api.HttpClient()
            webclient.connect(host=v.HOST, password=v.WEB_PWD, init=1)
            api.setRouterNormal(webclient, self.__class__.__name__, **option)
            webclient.close()

            txPower2g = 0
            txPower5g = 0
            while txPower2g == 0 or txPower5g == 0:
                power2g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                txPower2g = getWlanTxPower(self.dut, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, "5g", self.__class__.__name__)
                t.sleep(1)

            loop = 0
            while power2g <= (txPower2g - 5) or power5g <= (txPower5g - 5):
                t.sleep(10)
                power2g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                txPower2g = getWlanTxPower(self.dut, "2g", self.__class__.__name__)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, "5g", self.__class__.__name__)

                loop += 1
                if loop >= 360:
                    self.fail(msg='last est power check is failed')
            count += 1
            self.dut2.connect(host=v.HOST, password=v.WEB_PWD)


if __name__ == '__main__':
    v.HOST = "192.168.31.1"
    v.WEB_PWD = "12345678"
    v.ANDROID_SERIAL_NUM = "4ea65416"
    cases = [
        'assoc_sta_throughput_2g',
    ]

    suite = TestSuite(map(AP_CLEAR_CHAN1_BW20_WAN_THROUGHPUT, cases))
    curTime = t.strftime('%Y.%m.%d %H.%M.%S', t.localtime())
    f = open(curTime + '_RESULT.log', 'a')
    runner = TextTestRunner(f, verbosity=2)
    runner.run(suite)
    f.close()
