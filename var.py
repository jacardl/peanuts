# -*- coding: utf8 -*-
from common import *

VER = '3.5.1'

TOOL_LIST = ["General", "Memory Tracking", "Test Suite"]

# ----------------General-----------------

SAVE_BTN_FLAG = False  # represent save button pressed or not

DUT_MODULE = 'R1D'
HOST = "192.168.31.1"
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

TEST_SUITE_LOG_PATH = os.getcwd() + os.sep + 'LOG_TEST_SUITE' + os.sep
IPERF_PATH = os.getcwd() + os.sep + "iperf" + os.sep
DEFAULT_PATH = os.getcwd() + os.sep
SSH_LOG_PATH = DEFAULT_PATH + "ssh_connection.log"
DEVICE_STATUS_LOG = "device_status_log"

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

PING_PERCENT_PASS = 100
PING_COUNT = 5
PING_TARGET = 'www.baidu.com'
CHECK_ACCESS_URL = "http://miwifi.com/cgi-bin/luci/web"

BSSID = ''
BSSID_5G = ''
STA_MAC = ''
STA_MAC_5G = ''

FAIL_RETRY = 3

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

UPLOAD_LOG = 1
SEND_MAIL = 1
MAILTO_LIST = ['miwifi-test-wifi@xiaomi.com']
MAIL_HOST = "mail.srv"  #设置服务器
MAIL_USER = "robot"    #用户名
MAIL_PASS = ""   #口令
MAIL_POSTFIX="xiaomi.com"  #发件箱的后缀
MAILFROM_LIST = "robot@xiaomi.com"

MAIL_PIC1 = "total_memory_used.png"
MAIL_PIC2 = "throughput.png"
MAIL_PIC3 = "throughput_in_%s.png"
MAIL_PIC4 = "current_cpu_load.png"
MAIL_XLSX = "memory_tracking.xlsx"
MAIL_THROUGHPUT_XLSX = "Throughput.xlsx"


MEM_MONITOR_INTERVAL = 300

QOS_MAXUP = 800
QOS_MAXDOWN = 500

ROOT_AP_SSID = "peanuts_automatic_test_root_ap_"
ROOT_AP_PWD = "12345678"
ROOT_AP_CHANNEL = 11

# -------------api test------------------#
WEB_USERNAME = 'admin'
WEB_PWD = '12345678'
WEB_KEY = 'a2ffa5c9be07488bbb04a3a47d3c5f6a'
IV = '64175472480004614961023454661220'
# uci export account
ACCOUNT_DEFAULT_PWD = 'b3a4190199d9ee7fe73ef9a4942a69fece39a771'

