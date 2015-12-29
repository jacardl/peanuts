# -*- coding: utf8 -*-
from unittest import *

import api
import var as v
from common import *


class AP_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_LOW(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

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
        self.device = getAdbDevices()

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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_MID(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

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
        self.device = getAdbDevices()

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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_HIGH(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

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
        self.device = getAdbDevices()

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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_CLEAR_LOW_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
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
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if 19.55 <= power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 14
            """
            if 13.8 <= power <= 14.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'min',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 16.25
            """
            if 16.0 <= power <= 16.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL2,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if 19.55 <= power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 14
            """
            if 13.8 <= power <= 14.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL3,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if 19.55 <= power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 14
            """
            if 13.8 <= power <= 14.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if 19.55 <= power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 14
            """
            if 13.8 <= power <= 14.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL4,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if 19.55 <= power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 14
            """
            if 13.8 <= power <= 14.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL2_5G,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 15.5
            """
            if 15.3 <= power <= 15.7:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL3_5G,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 15.5
            """
            if 15.3 <= power <= 15.7:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 16.25
            """
            if 16.0 <= power <= 16.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL4_5G,
            'txpwr': 'min',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 16.25
            """
            if 16.0 <= power <= 16.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if 12.8 <= power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")


class AP_CLEAR_MID_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
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

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1

        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if 23.0 <= power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'mid',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1

        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19
            """
            if 18.8 <= power <= 19.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL2,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if 23.0 <= power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL3,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if 23.0 <= power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if 23.0 <= power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL4,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if 23.0 <= power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

        elif v.DUT_MODULE == "R1CL":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL2_5G,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 18.25
            """
            if 18 <= power <= 18.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL3_5G,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 18.25
            """
            if 18 <= power <= 18.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19
            """
            if 18.8 <= power <= 19.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL4_5G,
            'txpwr': 'mid',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19
            """
            if 18.8 <= power <= 19.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if 14.8 <= power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")


class AP_CLEAR_HIGH_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
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

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if 26.8 <= power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 17
            """
            if 16.8 <= power <= 17.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def autochan_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'txpwr': 'max',
        }

        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 22
            """
            if 21.8 <= power <= 22.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan1_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL2,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if 26.8 <= power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 17
            """
            if 16.8 <= power <= 17.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan6_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL3,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if 26.8 <= power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 17
            """
            if 16.8 <= power <= 17.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan11_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if 26.8 <= power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 17
            """
            if 16.8 <= power <= 17.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan13_txpower_2g(self):

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL4,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option2g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if 26.8 <= power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")
        elif v.DUT_MODULE == "R1CL":
            """
            exactly 17
            """
            if 16.8 <= power <= 17.2:
                pass
            else:
                self.fail("R1CL txpower isnot correct")

    def chan36_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL2_5G,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 21
            """
            if 20.8 <= power <= 21.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan52_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL3_5G,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 21
            """
            if 20.8 <= power <= 21.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan149_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 22
            """
            if 21.8 <= power <= 22.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan165_txpower_5g(self):

        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL4_5G,
            'txpwr': 'max',
        }
        api.setWifi(self.dut2, self.__class__.__name__, **option5g)
        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        loop = 0
        while power == 0 and loop < 5:
            t.sleep(2)
            power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
            loop += 1
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 22
            """
            if 21.8 <= power <= 22.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if 15.8 <= power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")


class AP_CLEAR_CHANSELECTION(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
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
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)

        option = {
            'model': 1,
            'mac': '11:22:33:44:55:66',
            'option': 0
        }
        api.setEditDevice(self.dut, self.__name__, **option)

        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        self.assertTrue(res2gConn, "Association wasnot successful which sta in whitelist.")
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

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }

        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        self.assertTrue(res5gConn, "Association wasnot successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        # connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
        # if self.staMac in connType.keys():
        #     self.fail(msg='STA should be kicked off.')

    def assoc_clear_sta_outof_whitelist_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        #鍒犻櫎鎵�鏈墂hitelist鍒欑櫧鍚嶅崟涓嶅啀鐢熸晥
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        # self.assertTrue(res2gConn, "Association should be successful when no sta in whitelist at all.")
        #
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 0
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)

    def assoc_clear_sta_outof_whitelist_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        self.assertFalse(res5gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        #鍒犻櫎鎵�鏈墂hitelist鍒欑櫧鍚嶅崟涓嶅啀鐢熸晥
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
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
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'encryption': 'none',
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'encryption': 'none',
            'channel': v.CHANNEL_5G,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_outof_blacklist_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_in_blacklist_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

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

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        self.assertTrue(res5gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        if self.staMac in connType.keys():
            self.fail(msg='STA should be kicked off.')

        self.assertFalse(res5gConn, "Association wasnot supposed to be successful which sta in blacklist.")


class AP_CLEAR_CHAN1_36_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL2,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL2_5G
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_clear_sta_flow_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_clear_sta_flow_5g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN6_52_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL3,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL3_5G
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_clear_sta_flow_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_clear_sta_flow_5g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN11_149_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_clear_sta_flow_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_clear_sta_flow_5g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN13_165_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL4,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL4_5G
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_clear_sta_flow_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_clear_sta_flow_5g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_CLEAR_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_clear_sta_5g(self):

        res5gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_PSK2_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_PSK2_CHAN1_36_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL2,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL2_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN6_52_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL3,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL3_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN11_149_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN13_165_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL4,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL4_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_PSK2_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'psk2',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'psk2',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_MIXEDPSK_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW80(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '80',
        }

        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__name__, **option5g)
        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW40(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '40'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_BW20(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'bandwidth': '20'
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SPECIAL_SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SPECIAL_SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidspec_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_2g(self):
        res2gConn = setAdbTkipPskStaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPskStaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.SPECIAL_KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_keyspec_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.CHINESE_SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.CHINESE_SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidchinese_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        res2gConn = setAdbTkipPskStaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPskStaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")


class AP_MIXEDPSK_CHAN1_36_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL2,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL2_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_MIXEDPSK_CHAN6_52_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL3,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL3_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_MIXEDPSK_CHAN11_149_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_MIXEDPSK_CHAN13_165_FLOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL4,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL4_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk2_sta_flow_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_psk_sta_flow_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk2_sta_flow_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

    def assoc_tkippsk_sta_flow_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__)
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")


class AP_MIXEDPSK_CHAN_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option2g = {
            'wifiIndex': 1,
            'ssid': v.SSID,
            'channel': v.CHANNEL,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': v.SSID_5G,
            'channel': v.CHANNEL_5G,
            'encryption': 'mixed-psk',
            'pwd': v.KEY
        }

        api.setWifi(self.dut, self.__name__, **option2g)
        api.setWifi(self.dut, self.__name__, **option5g)
        self.device = getAdbDevices()

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

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_2g(self):

        res2gConn = setAdbPskStaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_5g(self):

        res5gConn = setAdbPskStaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")


class AP_MIXEDPSK_BSD(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        option = {
            'bsd': 1,
            'ssid1': v.SSID,
            'encryption1': 'mixed-psk',
            'pwd1': v.KEY,
        }
        api.setAllWifi(self.dut, self.__name__, **option)
        self.device = getAdbDevices()
        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
        self.staMac = wlanInfo['mac'].upper()

    @classmethod
    def tearDownClass(self):
        api.setAllWifi(self.dut, self.__name__)
        self.dut.close()

    def assoc_psk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
            connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
            if self.staMac in connType.keys():
                resConn2 = int(connType[self.staMac]) == 2
                if resConn and resConn2:
                    break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(self.device[0], self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_psk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
            connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
            if self.staMac in connType.keys():
                resConn2 = int(connType[self.staMac]) == 2
                if resConn and resConn2:
                    break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(self.device[0], self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk2_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
            connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
            if self.staMac in connType.keys():
                resConn2 = int(connType[self.staMac]) == 2
                if resConn and resConn2:
                    break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(self.device[0], self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")

    def assoc_tkippsk_near_field_sta(self):
        count = 0
        while count <= 1:
            resConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
            connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
            if self.staMac in connType.keys():
                resConn2 = int(connType[self.staMac]) == 2
                if resConn and resConn2:
                    break
            else:
                resConn2 = False
            count += 1

        self.assertTrue(resConn, msg="Association wasnot successful.")
        self.assertTrue(resConn2, msg="STA doesnot associate with 5g")
        result = getAdbShellWlan(self.device[0], self.__class__.__name__)
        self.assertIsNot(result['ip'], "", msg='no ip address got.')
        resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
        self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                "Ping responsed percent werenot good enough.")


class AP_GUEST_CLEAR(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_clear_sta_guest(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_PSK2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_MIXEDPSK(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_guest(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_guest(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_guest(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")


class AP_GUEST_CLEAR_WHITELIST(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

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
        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] != '':
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                passPercent = resPingPercent['pass']
            else:
                passPercent = 0

        option = {
            'model': 1,
            'mac': self.staMac,
            'option': 1
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        self.assertTrue(res2gConn, "Association should be successful which sta in whitelist.")
        self.assertGreaterEqual(passPercent, v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")

        # connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)
        # if self.staMac in connType.keys():
        #     self.fail(msg='STA should be kicked off.')

    def assoc_clear_sta_outof_whitelist_guest(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        self.assertFalse(res2gConn, "Association wasnot supposed to be successful which sta outof whitelist.")
        # option = {
        #     'model': 1,
        #     'mac': '11:22:33:44:55:66',
        #     'option': 1
        # }
        # api.setEditDevice(self.dut, self.__class__.__name__, **option)
        #
        # res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
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
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
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

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getAdbPingStatus(self.device[0], v.PING_TARGET, v.PING_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS,
                                        "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

    def assoc_clear_sta_in_blacklist_guest(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        self.assertTrue(res2gConn, "Association should be successful which sta outof blacklist.")

        option = {
            'model': 0,
            'mac': self.staMac,
            'option': 0,
        }
        api.setEditDevice(self.dut, self.__class__.__name__, **option)

        connType = api.getOnlineDeviceType(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

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
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'none',
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_clear_sta_guest(self):

        res2gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_GUEST_MIXEDPSK_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk_sta_guest(self):

        res2gConn = setAdbPskStaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk2_sta_guest(self):

        res2gConn = setAdbTkipPsk2StaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_tkippsk_sta_guest(self):

        res2gConn = setAdbTkipPskStaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_GUEST_PSK2_REPEAT(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        optionGuest = {
            'wifiIndex': 3,
            'ssid': v.GUEST_SSID,
            'encryption': 'psk2',
            'pwd': v.KEY,
        }
        api.setWifi(self.dut, self.__name__, **optionGuest)
        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        option2g = {
            'wifiIndex': 1,
            'on': 0,
        }
        api.setWifi(self.dut, self.__name__, **option2g)
        self.dut.close()

    def assoc_repeat_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")


class AP_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = api.HttpClient()
        ret1 = self.dut.connect(host=v.HOST, password=v.WEB_PWD)
        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

        self.device = getAdbDevices()

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

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)

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

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)

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

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)

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

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)

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

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)

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

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)

        option5g = {
            'wifiIndex': 2,
            'on': 0
        }
        api.setWifi(self.dut, self.__class__.__name__, **option5g)

        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

class AP_CHECK(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        self.dut2 = api.HttpClient()
        ret2 = self.dut2.connect(host=v.HOST, password=v.WEB_PWD)

        if ret1 is False:
            raise Exception("Connection is failed for dut1. please check your remote settings.")

        if ret2 is False:
            raise Exception("Connection is failed for dut2. please check your remote settings.")

        option2g = {
            'wifiIndex': 1,
            'ssid': 'peanuts_check',
            'encryption': 'mixed-psk',
            'pwd': v.KEY,
            'channel': v.CHANNEL,
        }
        option5g = {
            'wifiIndex': 2,
            'ssid': 'peanuts_check',
            'encryption': 'mixed',
            'pwd': v.KEY,
            'channel': v.CHANNEL_5G,
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
                    self.dut = SshClient(v.CONNECTION_TYPE)
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
                txPower2g = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                t.sleep(1)

            if power2g <= (txPower2g-5) or power5g <= (txPower5g-5):
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
                        self.dut = SshClient(v.CONNECTION_TYPE)
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
                txPower2g = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                t.sleep(1)

            if power2g <= (txPower2g-5) or power5g <= (txPower5g-5):
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
                    self.dut = SshClient(v.CONNECTION_TYPE)
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

            #router_init
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
                txPower2g = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                t.sleep(1)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                t.sleep(1)

            loop = 0
            while power2g <= (txPower2g-5) or power5g <= (txPower5g-5):
                t.sleep(10)
                power2g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                txPower2g = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
                power5g = getWlanLastEstPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
                txPower5g = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)

                loop += 1
                if loop >= 360:
                    self.fail(msg='last est power check is failed')
            count += 1
            self.dut2.connect(host=v.HOST, password=v.WEB_PWD)


if __name__ == '__main__':
    v.HOST = "192.168.110.1"
    v.WEB_PWD = "12345678"
    cases = [
        'assoc_psk2_sta_ssidchinese_5g',
    ]

    suite = TestSuite(map(AP_MIXEDPSK_CHAN_SSIDCHINESE, cases))
    curTime = t.strftime('%Y.%m.%d %H.%M.%S', t.localtime())
    f = open(curTime + '_RESULT.log', 'a')
    runner = TextTestRunner(f, verbosity=2)
    runner.run(suite)
    f.close()