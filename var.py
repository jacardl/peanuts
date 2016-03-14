# -*- coding: utf8 -*-
from common import *

TOOL_LIST = ["General", "Memory Tracking", "Log Collection", "Test Suite"]

# ----------------General-----------------

SAVE_BTN_FLAG = False  # represent save button pressed or not

HOST = "192.168.31.1"
USR = "root"
PASSWD = "admin"

STA_IP = '192.168.32.1'
STA_USR = 'root'
STA_PASSWD = 'admin'
STA_COUNT = "1"

SERIAL_PORT = ""
BAUDRATE = 115200


"""
connection_type = 1 represent ssh
                  2 represent telnet
                  3 serial
"""
CONNECTION_TYPE = 1
STA_CONNECTION_TYPE = 1

VER = '3.0.1'

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

# ----------------Log Collection-----------------

GET_MODEL = 'uci get /usr/share/xiaoqiang/xiaoqiang_version.version.HARDWARE'

# ----------------Test Suite-----------------

DUT_MODULE = 'R1D'
STA_MODULE = 'Android'

INTF_2G = 'wl1'
INTF_5G = 'wl0'
INTF_GUEST = 'guest'

STA_INTF_2G = 'apcli0'
STA_INTF_5G = 'apclii0'

TEST_SUITE_LOG_PATH = os.getcwd() + os.sep + 'LOG_TEST_SUITE' + os.sep
IPERF_PATH = os.getcwd() + os.sep + "iperf" + os.sep
DEFAULT_PATH = os.getcwd() + os.sep
SSH_LOG_PATH = TEST_SUITE_LOG_PATH + "ssh_connection.log"

WORD_RANGE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
SPEC_RANGE = '`~!@#$%^&*() =+\\|]}[{\'\";:/?.>,<'
CHINESE_RANGE = "花生自动化小米路由器棒棒哒"

SSID = generateRandomString(WORD_RANGE, 31)
SSID_5G = generateRandomString(WORD_RANGE, 31)
GUEST_SSID = generateRandomString(WORD_RANGE, 31)

SPECIAL_SSID = generateRandomString(SPEC_RANGE, 31)
SPECIAL_SSID_5G = generateRandomString(SPEC_RANGE, 31)

CHINESE_SSID = generateRandomString(CHINESE_RANGE, 10)
CHINESE_SSID_5G = generateRandomString(CHINESE_RANGE, 10)

KEY = generateRandomString(WORD_RANGE, 63)
SPECIAL_KEY = generateRandomString(SPEC_RANGE, 63)

PING_PERCENT_PASS = 100
PING_COUNT = 5
PING_TARGET = 'www.baidu.com'

BSSID = ''
BSSID_5G = ''
STA_MAC = ''
STA_MAC_5G = ''

FAIL_RETRY = 3

CHANNEL = '11'
CHANNEL_5G = '149'

CHANNEL2 = '1'
CHANNEL2_5G = '36'

CHANNEL3 = '6'
CHANNEL3_5G = '52'

CHANNEL4 = '13'
CHANNEL4_5G = '165'

IPERF_INTERVAL = ""
IPERF_TIME = "60"
# IPERF_INTERVAL = "1"
# IPERF_TIME = "5"

SEND_MAIL = 1
MAILTO_LIST = ["liujia5@xiaomi.com", "fengjiang@xiaomi.com", "hexiaoliang@xiaomi.com", "linli1@xiaomi.com",
               "wangchunxuan@xiaomi.com", "wangyue3@xiaomi.com", "youguidong@xiaomi.com", "zhangjunjie@xiaomi.com",
               "zhaoziqiang@xiaomi.com", ]
# MAILTO_LIST = ["liujia5@xiaomi.com"]
MAIL_HOST = "mail.srv"  #设置服务器
MAIL_USER = "robot"    #用户名
MAIL_PASS = ""   #口令
MAIL_POSTFIX="xiaomi.com"  #发件箱的后缀
MAILFROM_LIST = "robot@xiaomi.com"

MAIL_PIC1 = "total_memory_used.png"
MAIL_PIC2 = "throughput.png"
MAIL_PIC3 = "throughput_in_%s.png"
MAIL_XLSX = "memory_tracking.xlsx"

MEM_MONITOR_INTERVAL = 60

# -------------api test------------------#
WEB_USERNAME = 'admin'
WEB_PWD = '12345678'
WEB_KEY = 'a2ffa5c9be07488bbb04a3a47d3c5f6a'
IV = '64175472480004614961023454661220'
# uci export account
ACCOUNT_DEFAULT_PWD = 'b3a4190199d9ee7fe73ef9a4942a69fece39a771'
