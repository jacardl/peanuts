from unittest import *
from tcdata import *

class AP_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']
    @classmethod
    def tearDownClass(self):

        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)

        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)

        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)

        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)

        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_CLEAR_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_PSK2_CHAN(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_PSK2_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_GUEST_CLEAR_CHAN(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_GUEST, self.__name__)
        v.BSSID = v.BSSID['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def ping_clear_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_GUEST_CLEAR_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_clear_sta_guest(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_GUEST_PSK2_CHAN(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_GUEST, self.__name__)
        v.BSSID = v.BSSID['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def ping_psk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_GUEST_PSK2_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_GUEST_MIXEDPSK_CHAN(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_GUEST, self.__name__)
        v.BSSID = v.BSSID['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def ping_psk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_GUEST_MIXEDPSK_CHAN2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_guest(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_guest(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_guest(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "guest", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_BW80(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw80_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_BW802(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw80_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_BW40(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw40_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_BW402(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw40_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_BW20(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw20_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_BW202(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_bw20_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_5g(self):

        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_5g(self):

        res5gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_SSIDSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_ssidspec_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SPECIAL_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SPECIAL_SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SPECIAL_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SPECIAL_SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SPECIAL_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SPECIAL_SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SPECIAL_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SPECIAL_SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_ssidspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_ssidspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_SSIDSPEC2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_ssidspec_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_ssidspec_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidspec_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidspec_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_2g(self):
        res2gConn = setAdbTkipPskStaConn(self.device[0], "spec", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidspec_5g(self):
        res5gConn = setAdbTkipPskStaConn(self.device[0], "spec", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_KEYSPEC(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_keyspec_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_keyspec_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_keyspec_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_keyspec_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_keyspec_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_KEYSPEC2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_keyspec_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_keyspec_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_keyspec_5g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_keyspec_5g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_2g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "2g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_keyspec_5g(self):

        res2gConn = setAdbTkipPskStaConn(self.device[0], "normal", "5g", self.__class__.__name__, key="spec")
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

class AP_MIXEDPSK_CHAN_SSIDCHINESE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        self.sta = SshClient(v.STA_CONNECTION_TYPE)

        dutRet = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        staRet = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)

        if dutRet is False or staRet is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_ssidchinese_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_psk2_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.CHINESE_SSID.decode('GB2312').encode('utf-8'))
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk2_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.CHINESE_SSID_5G.decode('GB2312').encode('utf-8'))
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_psk_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.CHINESE_SSID.decode('GB2312').encode('utf-8'))
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_psk_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.CHINESE_SSID_5G.decode('GB2312').encode('utf-8'))
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.CHINESE_SSID.decode('GB2312').encode('utf-8'))
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk2_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.CHINESE_SSID_5G.decode('GB2312').encode('utf-8'))
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_tkippsk_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.CHINESE_SSID.decode('GB2312').encode('utf-8'))
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_tkippsk_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.CHINESE_SSID_5G.decode('GB2312').encode('utf-8'))
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_psk2_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk2_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk2_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_psk_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_psk_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk2_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk2_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_ssidchinese_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidchinese_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_tkippsk_sta_ssidchinese_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_tkippsk_sta_ssidchinese_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_MIXEDPSK_CHAN_SSIDCHINESE2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_ssidchinese_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk2_sta_ssidchinese_5g(self):

        res5gConn = setAdbPsk2StaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_2g(self):

        res2gConn = setAdbPskStaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_psk_sta_ssidchinese_5g(self):

        res5gConn = setAdbPskStaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_2g(self):

        res2gConn = setAdbTkipPsk2StaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPsk2StaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        res2gConn = setAdbTkipPskStaConn(self.device[0], "chinese", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        res5gConn = setAdbTkipPskStaConn(self.device[0], "chinese", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_CLEAR_LOW(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_low_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_CLEAR_LOW2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_low_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_CLEAR_HIGH(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_high_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def ping_clear_sta_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gIp = getIntfIpAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        if res2gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res2gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

    def ping_clear_sta_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gIp = getIntfIpAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        if res5gIp['ip'] == '':
            self.fail(msg='no ip address got.')
        else:
            resPingPercent = getPingStatus(self.dut, res5gIp['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
            self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS)

class AP_CLEAR_HIGH2(TestCase):
    @classmethod
    def setUpClass(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_high_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_clear_sta_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)
        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_5g(self):

        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)
        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')
            else:
                resPingPercent = getPingStatus(self.dut, result['ip'], v.PING_PERCENT_COUNT, self.__class__.__name__)
                self.assertGreaterEqual(resPingPercent['pass'], v.PING_PERCENT_PASS, "Ping responsed percent werenot good enough.")
        else:
            self.assertTrue(res5gConn, "Association wasnot successful.")

class AP_CLEAR_LOW_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_low_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

    def autochan_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if power >= 19.55 and power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if power >= 12.8 and power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def autochan_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 16.25
            """
            if power >= 16.0 and power <= 16.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if power >= 12.8 and power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan13_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", v.CHANNEL, self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19.75
            """
            if power >= 19.55 and power <= 19.95:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if power >= 12.8 and power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan36_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "36", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 15.5
            """
            if power >= 15.3 and power <= 15.7:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 13
            """
            if power >= 12.8 and power <= 13.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

class AP_CLEAR_MID_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_mid_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

    def autochan_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if power >= 23.0 and power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if power >= 14.8 and power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def autochan_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 19
            """
            if power >= 18.8 and power <= 19.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if power >= 14.8 and power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan13_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", v.CHANNEL, self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 23.25
            """
            if power >= 23.0 and power <= 23.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if power >= 14.8 and power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan36_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "36", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 18.25
            """
            if power >= 18 and power <= 18.45:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 15
            """
            if power >= 14.8 and power <= 15.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

class AP_CLEAR_HIGH_TXPOWER(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_high_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

    def autochan_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if power >= 26.8 and power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if power >= 15.8 and power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def autochan_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "0", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "2", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 22
            """
            if power >= 21.8 and power <= 22.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if power >= 15.8 and power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan13_txpower_2g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "channel", v.CHANNEL, self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "2g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "2g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 27
            """
            if power >= 26.8 and power <= 27.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if power >= 15.8 and power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

    def chan36_txpower_5g(self):
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "channel", "36", self.__class__.__name__)
        setUCIWirelessDev(self.dut, v.DUT_MODULE, "5g", "set", "autoch", "0", self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        power = getWlanTxPower(self.dut, v.DUT_MODULE, "5g", self.__class__.__name__)
        if v.DUT_MODULE == "R1D" or v.DUT_MODULE == "R2D":
            """
            exactly 21
            """
            if power >= 20.8 and power <= 21.2:
                pass
            else:
                self.fail("R1D/R2D txpower isnot correct.")

        elif v.DUT_MODULE == "R1CM":
            """
            exactly 16
            """
            if power >= 15.8 and power <= 16.2:
                pass
            else:
                self.fail("R1CM txpower isnot correct.")

class AP_CLEAR_CHANSELECTION(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        if ret1 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

    def chanselection_2g(self):
        count = 0
        chan_2g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        while count < 10:
            result = getWlanInfo(self.dut, "2g", self.__class__.__name__)
            try:
                chan_2g.index(int(result["channel"]))
                setWifiRestart(self.dut, self.__class__.__name__)
                count +=1
            except:
                self.fail("Current auto-selected channel isnot between 1 and 11.")

    def chanselection_5g(self):
        count = 0
        chan_5g = [149, 153, 157, 161]
        while count < 10:
            result = getWlanInfo(self.dut, "5g", self.__class__.__name__)
            try:
                chan_5g.index(int(result["channel"]))
                setWifiRestart(self.dut, self.__class__.__name__)
                count +=1
            except:
                self.fail("Current auto-selected channel isnot between 149 and 161.")

class AP_SSIDHIDE(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()
        self.sta.close()

    def ap_clear_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
        count = 0
        while ret1 is False and count < 5:
            ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret1:
            self.fail(msg='specified wifi is no exist.')
        elif result1['ssid'] != '':
            self.fail(msg='2.4g wifi is not hidden.')

        ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
        count = 0
        while ret2 is False and count < 5:
            ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret2:
            self.fail(msg='specified wifi is no exist.')
        elif result2['ssid'] != '':
            self.fail(msg='5g wifi is not hidden')

    def ap_psk2_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
        count = 0
        while ret1 is False and count < 5:
            ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret1:
            self.fail(msg='specified wifi is no exist.')
        elif result1['ssid'] != '':
            self.fail(msg='2.4g wifi is not hidden.')

        ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
        count = 0
        while ret2 is False and count < 5:
            ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret2:
            self.fail(msg='specified wifi is no exist.')
        elif result2['ssid'] != '':
            self.fail(msg='5g wifi is not hidden')

    def ap_mixedpsk_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
        count = 0
        while ret1 is False and count < 5:
            ret1, result1 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret1:
            self.fail(msg='specified wifi is no exist.')
        elif result1['ssid'] != '':
            self.fail(msg='2.4g wifi is not hidden.')

        ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
        count = 0
        while ret2 is False and count < 5:
            ret2, result2 = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1
        if not ret2:
            self.fail(msg='specified wifi is no exist.')
        elif result2['ssid'] != '':
            self.fail(msg='5g wifi is not hidden')

class AP_SSIDHIDE2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def ap_clear_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)
        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)
        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_psk2_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)
        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)
        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

    def ap_mixedpsk_ssidhide(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_ssidhide_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        ret2g = setAdbScanSsidNoExist(self.device[0], "normal", "2g", self.__class__.__name__)
        if ret2g is False:
            self.fail(msg='2.4g wifi is not hidden..')

        ret5g = setAdbScanSsidNoExist(self.device[0], "normal", "5g", self.__class__.__name__)
        if ret5g is False:
            self.fail(msg='5g wifi is not hidden..')

class AP_CLEAR_CHAN_WHITELIST(TestCase):

    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_whitelist_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__class__.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__class__.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']
        v.STA_MAC = getIntfHWAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        v.STA_MAC = v.STA_MAC['mac']
        v.STA_MAC_5G = getIntfHWAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        v.STA_MAC_5G = v.STA_MAC_5G['mac']

    def tearDown(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_in_whitelist_2g(self):

        setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_in_whitelist_5g(self):

        setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC_5G, self.__class__.__name__)
        setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC_5G, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_clear_sta_outof_whitelist_2g(self):
        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)
        self.assertDictEqual(res2gConn, {'ssid': '', 'bssid': ''})

    def assoc_clear_sta_outof_whitelist_5g(self):
        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)
        self.assertDictEqual(res5gConn, {'ssid': '', 'bssid': ''})

class AP_CLEAR_CHAN_WHITELIST2(TestCase):

    @classmethod
    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_whitelist_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
        v.STA_MAC = wlanInfo["mac"]

    @classmethod
    def tearDown(self):
        setWifiMacfilterModel(self.dut, 0, logname=self.__name__)
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)
        self.dut.close()

    def assoc_clear_sta_in_whitelist_2g(self):

        # setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)
        setWifiMacfilterModel(self.dut, 1, 1, v.STA_MAC, self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_in_whitelist_5g(self):

        # setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)
        setWifiMacfilterModel(self.dut, 1, 1, v.STA_MAC, self.__class__.__name__)
        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_clear_sta_outof_whitelist_2g(self):

        setWifiMacfilterModel(self.dut, 1, 1, logname=self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful.")

    def assoc_clear_sta_outof_whitelist_5g(self):

        setWifiMacfilterModel(self.dut, 1, 1, logname=self.__class__.__name__)
        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertFalse(res5gConn, "Association wasnot supposed to be successful.")

class AP_CLEAR_CHAN_BLACKLIST(TestCase):

    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_blacklist_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_2G, self.__class__.__name__)
        v.BSSID = v.BSSID['mac']
        v.BSSID_5G = getIntfHWAddr(self.dut, v.INTF_5G, self.__class__.__name__)
        v.BSSID_5G = v.BSSID_5G['mac']
        v.STA_MAC = getIntfHWAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        v.STA_MAC = v.STA_MAC['mac']
        v.STA_MAC_5G = getIntfHWAddr(self.sta, v.STA_INTF_5G, self.__class__.__name__)
        v.STA_MAC_5G = v.STA_MAC_5G['mac']

    def tearDown(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_outof_blacklist_2g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_outof_blacklist_5g(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res5gConn['ssid'], v.SSID_5G)
        self.assertEqual(res5gConn['bssid'], v.BSSID_5G)

    def assoc_clear_sta_in_blacklist_2g(self):

        setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_2g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)
        self.assertDictEqual(res2gConn, {'ssid': '', 'bssid': ''})

    def assoc_clear_sta_in_blacklist_5g(self):

        setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC_5G, self.__class__.__name__)
        setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC_5G, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_5G, v.BSSID_5G.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_5G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_5g():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res5gConn = getApclii0Conn(self.sta, self.__class__.__name__)
        self.assertDictEqual(res5gConn, {'ssid': '', 'bssid': ''})

class AP_CLEAR_CHAN_BLACKLIST2(TestCase):

    @classmethod
    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_blacklist_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
        v.STA_MAC = wlanInfo["mac"]

    @classmethod
    def tearDown(self):
        setWifiMacfilterModel(self.dut, 0, logname=self.__name__)
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)
        self.dut.close()

    def assoc_clear_sta_outof_blacklist_2g(self):

        setWifiMacfilterModel(self.dut, 1, 0, logname=self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_outof_blacklist_5g(self):

        setWifiMacfilterModel(self.dut, 1, 0, logname=self.__class__.__name__)
        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        if res5gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res5gConn, "Association wasnot successful.")

    def assoc_clear_sta_in_blacklist_2g(self):

        # setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)
        setWifiMacfilterModel(self.dut, 1, 0, v.STA_MAC, self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful.")

    def assoc_clear_sta_in_blacklist_5g(self):

        # setUCIWirelessIntf(self.dut, v.INTF_5G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setUCIWirelessIntf(self.dut, v.INTF_2G, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)
        setWifiMacfilterModel(self.dut, 1, 0, v.STA_MAC, self.__class__.__name__)
        res5gConn = setAdbClearStaConn(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertFalse(res5gConn, "Association wasnot supposed to be successful.")

class AP_GUEST_CLEAR_CHAN_WHITELIST(TestCase):

    def setUp(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_whitelist_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_GUEST, self.__class__.__name__)
        v.BSSID = v.BSSID['mac']
        v.STA_MAC = getIntfHWAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        v.STA_MAC = v.STA_MAC['mac']

    def tearDown(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_in_whitelist_guest(self):

        setUCIWirelessIntf(self.dut, v.INTF_GUEST, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_outof_whitelist_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertDictEqual(res2gConn, {'ssid': '', 'bssid': ''})

class AP_GUEST_CLEAR_CHAN_WHITELIST2(TestCase):

    @classmethod
    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_whitelist_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
        v.STA_MAC = wlanInfo["mac"]

    @classmethod
    def tearDown(self):
        setWifiMacfilterModel(self.dut, 0, logname=self.__name__)
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)
        self.dut.close()

    def assoc_clear_sta_in_whitelist_guest(self):

        # setUCIWirelessIntf(self.dut, v.INTF_GUEST, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)
        setWifiMacfilterModel(self.dut, 1, 1, v.STA_MAC, self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_outof_whitelist_guest(self):

        setWifiMacfilterModel(self.dut, 1, 1, logname=self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful.")

class AP_GUEST_CLEAR_CHAN_BLACKLIST(TestCase):

    def setUp(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)
        # exception deal
        self.sta = SshClient(v.STA_CONNECTION_TYPE)
        ret2 = self.sta.connect(v.STA_IP, v.STA_USR, v.STA_PASSWD)
        # exception deal

        if ret1 is False or ret2 is False:
            raise Exception('Connection is failed. please check your remote settings.')
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_blacklist_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        v.BSSID = getIntfHWAddr(self.dut, v.INTF_GUEST, self.__class__.__name__)
        v.BSSID = v.BSSID['mac']
        v.STA_MAC = getIntfHWAddr(self.sta, v.STA_INTF_2G, self.__class__.__name__)
        v.STA_MAC = v.STA_MAC['mac']

    def tearDown(self):
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.sta_tear_down():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

        self.dut.close()
        self.sta.close()

    def assoc_clear_sta_outof_blacklist_guest(self):

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertEqual(res2gConn['ssid'], v.GUEST_SSID)
        self.assertEqual(res2gConn['bssid'], v.BSSID)

    def assoc_clear_sta_in_blacklist_guest(self):

        setUCIWirelessIntf(self.dut, v.INTF_GUEST, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        setWifiRestart(self.dut, self.__class__.__name__)

        ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)

        count = 0
        while ret is False and count < 5:
            ret, result = chkSiteSurvey(self.sta, v.STA_INTF_2G, v.BSSID.lower(), self.__class__.__name__)
            count += 1

        if count >= 5:
            self.fail(msg='specified wifi is no exist')

        setIwpriv(self.sta, v.INTF_2G, 'Channel', result['channel'], self.__class__.__name__)
        d = TestCommand(v.DUT_MODULE)
        for staCommand in d.assoc_clear_sta_guest():
            setConfig(self.sta, staCommand, self.__class__.__name__)

        res2gConn = getApcli0Conn(self.sta, self.__class__.__name__)

        self.assertDictEqual(res2gConn, {'ssid': '', 'bssid': ''})

class AP_GUEST_CLEAR_CHAN_BLACKLIST2(TestCase):

    @classmethod
    def setUp(self):
        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_blacklist_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

        wlanInfo = getAdbShellWlan(self.device[0], self.__name__)
        v.STA_MAC = wlanInfo["mac"]

    @classmethod
    def tearDown(self):
        setWifiMacfilterModel(self.dut, 0, logname=self.__name__)
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)
        self.dut.close()

    def assoc_clear_sta_outof_blacklist_guest(self):

        setWifiMacfilterModel(self.dut, 1, 0, logname=self.__class__.__name__)
        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        if res2gConn:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            if result['ip'] == '':
                self.fail(msg='no ip address got.')

        self.assertTrue(res2gConn, "Association wasnot successful.")

    def assoc_clear_sta_in_blacklist_guest(self):

        setWifiMacfilterModel(self.dut, 1, 0, v.STA_MAC, self.__class__.__name__)
        # setUCIWirelessIntf(self.dut, v.INTF_GUEST, "add_list", 'maclist', v.STA_MAC, self.__class__.__name__)
        # setWifiRestart(self.dut, self.__class__.__name__)

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertFalse(res2gConn, "Association wasnot supposed to be successful.")

class AP_CLEAR_CHAN_FLOW2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_clear_sta_flow_2g(self):

        res2gConn = setAdbClearStaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

class AP_CLEAR_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()
    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_repeat_clear_sta_2g(self):

        res2gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_clear_sta_5g(self):

        res5gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

class AP_MIXEDPSK_CHAN_FLOW2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

class AP_MIXEDPSK_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()
    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

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

class AP_PSK2_CHAN_FLOW2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()
    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_psk2_sta_flow_2g(self):

        res2gConn = setAdbPsk2StaConn(self.device[0], "normal", "2g", self.__class__.__name__)

        if res2gConn is True:
            result = getAdbShellWlan(self.device[0], self.__class__.__name__)
            iperfOn = SetAdbIperfOn(self.device[0], self.__class__.__name__)
            iperfOn.start()
            t.sleep(3.0)
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
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
            ret = setIperfFlow(result["ip"], v.IPERF_INTERVAL, v.IPERF_TIME, self.__class__.__name__ )
            self.assertTrue(ret, "Excute iperf flow error, connection refused.")

        else:
            self.assertTrue(res2gConn, "Connecting wifi is failed.")

class AP_PSK2_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_repeat_psk2_sta_2g(self):

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "2g", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

    def assoc_repeat_psk2_sta_5g(self):

        res5gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "5g", self.__class__.__name__)

        self.assertTrue(res5gConn, "Not all association were successful.")

class AP_GUEST_CLEAR_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_repeat_clear_sta_guest(self):

        res2gConn = setAdbClearStaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

class AP_GUEST_MIXEDPSK_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_mixedpsk_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

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

class AP_GUEST_PSK2_CHAN_REPEAT2(TestCase):
    @classmethod
    def setUpClass(self):

        self.dut = SshClient(v.CONNECTION_TYPE)
        ret1 = self.dut.connect(v.HOST, v.USR, v.PASSWD)

        ret2 = chkAdbDevicesCount(1)

        if ret1 is False:
            raise Exception("Connection is failed. please check your remote settings.")

        if ret2 is False:
            raise Exception("USB devices arenot ready!")
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_psk2_chan_set_up():
            setConfig(self.dut, dutCommand, self.__name__)

        self.device = getAdbDevices()

    @classmethod
    def tearDownClass(self):
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_guest_tear_down():
            setConfig(self.dut, dutCommand, self.__name__)

        self.dut.close()

    def assoc_repeat_psk2_sta_guest(self):

        res2gConn = setAdbPsk2StaConnRepeat(self.device[0], "normal", "guest", self.__class__.__name__)

        self.assertTrue(res2gConn, "Not all association were successful.")

class AP_TEST(TestCase):

    @classmethod
    def setUpClass(self):
        print "setupclass" + self.__name__

    @classmethod
    def tearDownClass(self):
        print "teardownclass" + self.__name__

    def test1(self):
        print "test1" + self.__class__.__name__
        self.dut = SshClient(v.CONNECTION_TYPE)
        self.dut.connect("192.168.108.1", v.USR, v.PASSWD)
        d = TestCommand(v.DUT_MODULE)
        for dutCommand in d.ap_clear_chan_set_up():
            setConfig(self.dut, dutCommand, self.__class__.__name__)

    def test2(self):
        print "test2"

if __name__ == '__main__':
    cases = [
        'assoc_psk2_sta_5g',
        ##            'ap_clear_ping_clear_sta_2g',
    ]

    suite = TestSuite(map(AP_MIXEDPSK_CHAN_BW402, cases))
    curTime = t.strftime('%Y.%m.%d %H.%M.%S', t.localtime())
    f = open(curTime + '_RESULT.log','a')
    runner = TextTestRunner(f, verbosity = 2)
    runner.run(suite)
    f.close()
