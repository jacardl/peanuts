# -*- coding: utf8 -*-
from common2 import *
import os

VER = '3.8.2'

TOOL_LIST = ["General", "Memory Tracking", "Test Suite"]

# ----------------General-----------------

SAVE_BTN_FLAG = False  # represent save button pressed or not

DUT_MODULE_LIST = ['R1D', 'R1CM', 'R2D', "R1CL", "R3", "R3L", "R3P"]
DUT_MODULE = DUT_MODULE_LIST[0]
HOST = "192.168.31.1"
HOST_ORIGINAL = ""
USR = "root"
PASSWD = "admin"

"""
connection_type = 1 represent ssh
                  2 represent telnet
                  3 serial
"""
CONNECTION_TYPE = 1

SERIAL_PORT = ""
BAUDRATE = 115200

ANDROID_SERIAL_NUM = ''
ANDROID_MODEL = ''
STA_COUNT = "1"

# ----------------Memory Tracking-----------------

WIDTH = 2000
WIDTH2 = 4000
INTERVAL = 1
COUNT = 10

"""
1.periodically launched by cpulimit_daemon.sh
/bin/mpstat 4 1 -P 0 | awk 'NR>6 {print $11}' | awk -F. '{print $1}'
2.periodically launched by Peanuts
ps w
"""
EXCEPTIONS = ['ps', 'awk', 'sleep', 'mpstat', 'cpulimit_daemon']
KERNEL_EXCEPTIONS = []

# ----------------Test Suite-----------------

INTF_2G = 'wl1'
INTF_5G = 'wl0'
INTF_GUEST = 'guest'

WORD_RANGE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
SPEC_RANGE = '`~!@#$%^&*() =+\\|]}[{\'\";:/?.>,<'
CHINESE_RANGE = "宣室求贤访逐臣贾生才调更无伦可怜夜半虚前席不问苍生问鬼神"

SSID = generateRandomString(WORD_RANGE, 31)
SSID_5G = generateRandomString(WORD_RANGE, 31)
GUEST_SSID = generateRandomString(WORD_RANGE, 31)

SPECIAL_SSID = generateRandomString(SPEC_RANGE, 31)
SPECIAL_SSID_5G = generateRandomString(SPEC_RANGE, 31)

CHINESE_SSID = generateRandomString(CHINESE_RANGE, 10)
CHINESE_SSID_5G = generateRandomString(CHINESE_RANGE, 10)

WIRELESS_RELAY_SSID = generateRandomString(WORD_RANGE, 28)
WIRELESS_RELAY_SSID_5G = WIRELESS_RELAY_SSID + "_5G"
WIRELESS_RELAY_SPECIAL_SSID = generateRandomString(SPEC_RANGE, 28)
WIRELESS_RELAY_SPECIAL_SSID_5G = WIRELESS_RELAY_SPECIAL_SSID + "_5G"
WIRELESS_RELAY_CHINESE_SSID = generateRandomString(CHINESE_RANGE, 9)
WIRELESS_RELAY_CHINESE_SSID_5G = WIRELESS_RELAY_CHINESE_SSID + "_5G"

KEY = generateRandomString(WORD_RANGE, 63)
SPECIAL_KEY = generateRandomString(SPEC_RANGE, 63)

REPORT_NAME = ""
REPORT_FILE_NAME = ""
TEST_SUITE_LOG_PATH = os.getcwd() + os.sep + "TEST_SUITE_LOG" + os.sep
OOKLA_SHOT_PATH = TEST_SUITE_LOG_PATH + "OOKLA" + os.sep
IPERF_PATH = os.getcwd() + os.sep + "iperf" + os.sep
DEFAULT_PATH = os.getcwd() + os.sep
SSH_LOG_PATH = DEFAULT_PATH + "ssh_connection.log"
DEVICE_STATUS_LOG = "device_status_log"

PING_PERCENT_PASS = 100
PING_COUNT = 5
PING_TARGET = 'www.baidu.com'
CHECK_ACCESS_URL = "http://miwifi.com/cgi-bin/luci/web"
CHECK_ACCESS_URL2 = "http://m.baidu.com"
CHECK_ACCESS_URL3 = "http://www.sohu.com"
CHECK_ACCESS_URL4 = "http://m.taobao.com"
CHECK_ACCESS_URL5 = "http://m.jd.com"
CHECK_ACCESS_URL5 = "http://m.sina.cn"

BSSID = ''
BSSID_5G = ''
STA_MAC = ''
STA_MAC_5G = ''

CHANNEL1 = '1'
CHANNEL6 = '6'
CHANNEL11 = '11'
CHANNEL13 = '13'

CHANNEL36 = '36'
CHANNEL44 = '44'
CHANNEL52 = '52'
CHANNEL60 = '60'

CHANNEL149 = '149'
CHANNEL157 = '157'
CHANNEL165 = '165'

IPERF_INTERVAL = ""
IPERF_TIME = "60"
# IPERF_INTERVAL = "1"
# IPERF_TIME = "5"

QOS_MAXUP = 500
QOS_MAXDOWN = 500

ROOT_AP_SSID = "peanuts_automatic_test_root_ap_"
ROOT_AP_PWD = "12345678"
ROOT_AP_CHANNEL = 11

UPLOAD_LOG = 1
FAIL_RETRY = 3
MEM_MONITOR_INTERVAL = 300

# -------------api------------------#
WEB_USERNAME = 'admin'
WEB_PWD = '12345678'
WEB_KEY = 'a2ffa5c9be07488bbb04a3a47d3c5f6a'
IV = '64175472480004614961023454661220'
# uci export account
ACCOUNT_DEFAULT_PWD = 'b3a4190199d9ee7fe73ef9a4942a69fece39a771'

# -------------process report------------------#
WIFI_MAX_THROUGHPUT = 300


# -------------mail------------------#
SEND_MAIL = 1
MAILTO_LIST = ['miwifi-test-wifi@xiaomi.com']
MAIL_HOST = "mail.srv"  #设置服务器
MAIL_USER = "robot"    #用户名
MAIL_PASS = ""   #口令
MAIL_POSTFIX="xiaomi.com"  #发件箱的后缀
MAILFROM_LIST = "robot@xiaomi.com"
MAIL_TITLE = ""

MAIL_PIC1 = TEST_SUITE_LOG_PATH + "total_memory_used.png"
MAIL_PIC2 = TEST_SUITE_LOG_PATH + "dut_to_2g.png"
MAIL_PIC3 = TEST_SUITE_LOG_PATH + "dut_to_5g.png"
MAIL_PIC4 = TEST_SUITE_LOG_PATH + "current_cpu_load.png"
MAIL_PIC5 = TEST_SUITE_LOG_PATH + "lan_to_2g.png"
MAIL_PIC6 = TEST_SUITE_LOG_PATH + "lan_to_5g.png"
MAIL_PIC7 = TEST_SUITE_LOG_PATH + "wan_to_2g.png"
MAIL_PIC8 = TEST_SUITE_LOG_PATH + "wan_to_5g.png"
MAIL_XLSX = TEST_SUITE_LOG_PATH + "memory_tracking.xlsx"
MAIL_THROUGHPUT_XLSX_ORIGINAL = "throughput.xlsx"
MAIL_THROUGHPUT_XLSX = TEST_SUITE_LOG_PATH + MAIL_THROUGHPUT_XLSX_ORIGINAL