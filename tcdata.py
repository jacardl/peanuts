from var import *
from common import *


class TestCommand:
    def __init__(self, dut):
        if dut == "R1CM":
            self.DEV_2G = "mt7620"
            self.DEV_5G = "mt7612"
            self.WIFI_IF_2G = "@wifi-iface[1]"
            self.WIFI_IF_5G = "@wifi-iface[0]"
        elif dut == "R1D" or dut == "R2D":
            self.DEV_2G = "wl1"
            self.DEV_5G = "wl0"
            self.WIFI_IF_2G = "@wifi-iface[1]"
            self.WIFI_IF_5G = "@wifi-iface[0]"
        elif dut == "R1CL":
            self.DEV_2G = "mt7628"
            self.DEV_5G = ""
            self.WIFI_IF_2G = "@wifi-iface[0]"
            self.WIFI_IF_5G = ""

        self.SPECIAL_SSID_BASH = convertStrToBashStr(SPECIAL_SSID)
        self.SPECIAL_SSID_5G_BASH = convertStrToBashStr(SPECIAL_SSID_5G)
        self.SPECIAL_KEY_BASH = convertStrToBashStr(SPECIAL_KEY)

    # ------------common------------------
    def sta_tear_down(self):
        sta_tear_down = ['iwpriv apcli0 set ApCliAutoConnect=0',
                         'iwpriv apcli0 set ApCliEnable=0',
                         'ifconfig apcli0 down',
                         'iwpriv apclii0 set ApCliAutoConnect=0',
                         'iwpriv apclii0 set ApCliEnable=0',
                         'ifconfig apclii0 down',
                         ]
        return sta_tear_down

    def ap_tear_down(self):
        ap_tear_down = ['uci set wireless.' + self.DEV_2G + '.channel=0',
                        'uci set wireless.' + self.DEV_2G + '.autoch=2',
                        'uci set wireless.' + self.DEV_2G + '.disabled=1',
                        'uci set wireless.' + self.DEV_2G + '.bw=0',
                        'uci set wireless.' + self.DEV_2G + '.txpwr=mid',
                        'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                        'uci set wireless.' + self.WIFI_IF_2G + '.macfilter=disabled',
                        'uci del wireless.' + self.WIFI_IF_2G + '.maclist=',
                        'uci set wireless.' + self.DEV_5G + '.channel=0',
                        'uci set wireless.' + self.DEV_5G + '.autoch=2',
                        'uci set wireless.' + self.DEV_5G + '.disabled=1',
                        'uci set wireless.' + self.DEV_5G + '.bw=0',
                        'uci set wireless.' + self.DEV_5G + '.txpwr=mid',
                        'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                        'uci set wireless.' + self.WIFI_IF_5G + '.macfilter=disabled',
                        'uci del wireless.' + self.WIFI_IF_5G + '.maclist=',
                        'uci commit wireless',
                        "wifi; sleep 10"
                        ]
        return ap_tear_down

    def ap_guest_tear_down(self):
        ap_guest_tear_down = [
                              # 'uci set wireless.guest_2G.open=0',
                              'uci set wireless.guest_2G.disabled=1',
                              'uci set wireless.' + self.DEV_2G + '.channel=0',
                              'uci set wireless.' + self.DEV_2G + '.autoch=2',
                              'uci set wireless.' + self.DEV_2G + '.disabled=1',
                              'uci set wireless.guest_2G.macfilter=disabled',
                              'uci del wireless.guest_2G.maclist=',
                              'uci commit wireless',
                              "wifi; sleep 10",
                              ]
        return ap_guest_tear_down

    # ---------------setup--------------------
    def ap_clear_set_up(self):
        ap_clear_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                           'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                           'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                           'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                           'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                           'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                           'uci set wireless.' + self.DEV_2G + '.channel=0',
                           'uci set wireless.' + self.DEV_2G + '.autoch=2',
                           'uci set wireless.' + self.DEV_2G + '.disabled=0',
                           'uci set wireless.' + self.DEV_5G + '.channel=0',
                           'uci set wireless.' + self.DEV_5G + '.autoch=2',
                           'uci set wireless.' + self.DEV_5G + '.disabled=0',
                           'uci commit wireless',
                           'wifi; sleep 10'
                           ]
        return ap_clear_set_up

    def ap_clear_chan_set_up(self):
        ap_clear_chan_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                'uci commit wireless',
                                'wifi; sleep 10'
                                ]
        return ap_clear_chan_set_up

    def ap_clear_chan2_set_up(self):
        ap_clear_chan2_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL2,
                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL2_5G,
                                'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                'uci commit wireless',
                                'wifi; sleep 10'
                                ]
        return ap_clear_chan2_set_up

    def ap_clear_chan3_set_up(self):
        ap_clear_chan3_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL3,
                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL3_5G,
                                'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                'uci commit wireless',
                                'wifi; sleep 10'
                                ]
        return ap_clear_chan3_set_up

    def ap_clear_chan4_set_up(self):
        ap_clear_chan4_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL4,
                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL4_5G,
                                'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                'uci commit wireless',
                                'wifi; sleep 10'
                                ]
        return ap_clear_chan4_set_up

    def ap_clear_low_set_up(self):
        ap_clear_low_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.txpwr=min',
                               'uci set wireless.' + self.DEV_5G + '.txpwr=min',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10'
                               ]
        return ap_clear_low_set_up

    def ap_clear_mid_set_up(self):
        ap_clear_mid_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.txpwr=mid',
                               'uci set wireless.' + self.DEV_5G + '.txpwr=mid',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10']

        return ap_clear_mid_set_up

    def ap_clear_high_set_up(self):
        ap_clear_high_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                'uci set wireless.' + self.DEV_2G + '.txpwr=max',
                                'uci set wireless.' + self.DEV_5G + '.txpwr=max',
                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                'uci commit wireless',
                                'wifi; sleep 10'
                                ]
        return ap_clear_high_set_up

    def ap_clear_ssidhide_set_up(self):
        ap_clear_ssidhide_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                    'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                    'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                    'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                    'uci set wireless.' + self.WIFI_IF_5G + '.hidden=1',
                                    'uci set wireless.' + self.WIFI_IF_2G + '.hidden=1',
                                    'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                    'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                    'uci commit wireless',
                                    'wifi; sleep 10'
                                    ]
        return ap_clear_ssidhide_set_up

    def ap_clear_chan_whitelist_set_up(self):
        ap_clear_chan_whitelist_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                          'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                          'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                          'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                          'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                          'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                          'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                          'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                          'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                          'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                          'uci set wireless.' + self.WIFI_IF_5G + '.macfilter=allow',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.macfilter=allow',
                                          'uci commit wireless',
                                          'wifi; sleep 10'
                                          ]
        return ap_clear_chan_whitelist_set_up

    def ap_clear_chan_blacklist_set_up(self):
        ap_clear_chan_blacklist_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=none',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.encryption=none',
                                          'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                          'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                          'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                          'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                          'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                          'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                          'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                          'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                          'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                          'uci set wireless.' + self.WIFI_IF_5G + '.macfilter=deny',
                                          'uci set wireless.' + self.WIFI_IF_2G + '.macfilter=deny',
                                          'uci commit wireless',
                                          'wifi; sleep 10']
        return ap_clear_chan_blacklist_set_up

    def ap_psk2_chan_set_up(self):
        ap_psk2_chan_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                               'uci set wireless.' + self.DEV_2G + '.autoch=0',
                               'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                               'uci set wireless.' + self.DEV_5G + '.autoch=0',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10'
                               ]
        return ap_psk2_chan_set_up

    def ap_psk2_chan2_set_up(self):
        ap_psk2_chan2_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL2,
                               'uci set wireless.' + self.DEV_2G + '.autoch=0',
                               'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL2_5G,
                               'uci set wireless.' + self.DEV_5G + '.autoch=0',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10'
                               ]
        return ap_psk2_chan2_set_up

    def ap_psk2_chan3_set_up(self):
        ap_psk2_chan3_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL3,
                               'uci set wireless.' + self.DEV_2G + '.autoch=0',
                               'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL3_5G,
                               'uci set wireless.' + self.DEV_5G + '.autoch=0',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10'
                               ]
        return ap_psk2_chan3_set_up

    def ap_psk2_chan4_set_up(self):
        ap_psk2_chan4_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=psk2',
                               'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                               'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL4,
                               'uci set wireless.' + self.DEV_2G + '.autoch=0',
                               'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL4_5G,
                               'uci set wireless.' + self.DEV_5G + '.autoch=0',
                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                               'uci commit wireless',
                               'wifi; sleep 10'
                               ]
        return ap_psk2_chan4_set_up

    def ap_psk2_ssidhide_set_up(self):
        ap_psk2_ssidhide_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=psk2',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=psk2',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=1',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=1',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10'
                                   ]
        return ap_psk2_ssidhide_set_up

    def ap_mixedpsk_set_up(self):
        ap_mixedpsk_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.DEV_2G + '.channel=0',
                                   'uci set wireless.' + self.DEV_2G + '.autoch=2',
                                   'uci set wireless.' + self.DEV_5G + '.channel=0',
                                   'uci set wireless.' + self.DEV_5G + '.autoch=2',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10',
                                   ]
        return ap_mixedpsk_set_up

    def ap_mixedpsk_chan_set_up(self):
        ap_mixedpsk_chan_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                   'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                   'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10'
                                   ]
        return ap_mixedpsk_chan_set_up

    def ap_mixedpsk_chan2_set_up(self):
        ap_mixedpsk_chan2_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL2,
                                   'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL2_5G,
                                   'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10'
                                   ]
        return ap_mixedpsk_chan2_set_up

    def ap_mixedpsk_chan3_set_up(self):
        ap_mixedpsk_chan3_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL3,
                                   'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL3_5G,
                                   'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10'
                                   ]
        return ap_mixedpsk_chan3_set_up

    def ap_mixedpsk_chan4_set_up(self):
        ap_mixedpsk_chan4_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                   'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                   'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                   'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                   'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                   'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL4,
                                   'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL4_5G,
                                   'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                   'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                   'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                   'uci commit wireless',
                                   'wifi; sleep 10'
                                   ]
        return ap_mixedpsk_chan4_set_up

    def ap_mixedpsk_ssidhide_set_up(self):
        ap_mixedpsk_ssidhide_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                       'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                       'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                       'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                       'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                       'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                       'uci set wireless.' + self.WIFI_IF_5G + '.hidden=1',
                                       'uci set wireless.' + self.WIFI_IF_2G + '.hidden=1',
                                       'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                       'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                       'uci commit wireless',
                                       'wifi; sleep 10'
                                       ]
        return ap_mixedpsk_ssidhide_set_up

    def ap_guest_clear_chan_set_up(self):
        ap_guest_clear_chan_set_up = ['uci set wireless.guest_2G.encryption=none',
                                      'uci set wireless.guest_2G.ssid=' + GUEST_SSID,
                                      # 'uci set wireless.guest_2G.open=1',
                                      'uci set wireless.guest_2G.disabled=0',
                                      'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                      'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                      'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                      'uci commit wireless',
                                      'wifi; sleep 10'
                                      ]
        return ap_guest_clear_chan_set_up

    def ap_guest_clear_chan_whitelist_set_up(self):
        ap_guest_clear_chan_whitelist_set_up = ['uci set wireless.guest_2G.encryption=none',
                                                'uci set wireless.guest_2G.ssid=' + GUEST_SSID,
                                                # 'uci set wireless.guest_2G.open=1',
                                                'uci set wireless.guest_2G.disabled=0',
                                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                                'uci set wireless.guest_2G.macfilter=allow',
                                                'uci commit wireless',
                                                'wifi; sleep 10'
                                                ]
        return ap_guest_clear_chan_whitelist_set_up

    def ap_guest_clear_chan_blacklist_set_up(self):
        ap_guest_clear_chan_blacklist_set_up = ['uci set wireless.guest_2G.encryption=none',
                                                'uci set wireless.guest_2G.ssid=' + GUEST_SSID,
                                                # 'uci set wireless.guest_2G.open=1',
                                                'uci set wireless.guest_2G.disabled=0',
                                                'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                                'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                                'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                                'uci set wireless.guest_2G.macfilter=deny',
                                                'uci commit wireless',
                                                'wifi; sleep 10']
        return ap_guest_clear_chan_blacklist_set_up

    def ap_guest_psk2_chan_set_up(self):
        ap_guest_psk2_chan_set_up = ['uci set wireless.guest_2G.encryption=psk2',
                                     'uci set wireless.guest_2G.key=' + KEY,
                                     'uci set wireless.guest_2G.ssid=' + GUEST_SSID,
                                     # 'uci set wireless.guest_2G.open=1',
                                     'uci set wireless.guest_2G.disabled=0',
                                     'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                     'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                     'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                     'uci commit wireless',
                                     'wifi; sleep 10']
        return ap_guest_psk2_chan_set_up

    def ap_guest_mixedpsk_chan_set_up(self):
        ap_guest_mixedpsk_chan_set_up = ['uci set wireless.guest_2G.encryption=mixed-psk',
                                         'uci set wireless.guest_2G.key=' + KEY,
                                         'uci set wireless.guest_2G.ssid=' + GUEST_SSID,
                                         # 'uci set wireless.guest_2G.open=1',
                                         'uci set wireless.guest_2G.disabled=0',
                                         'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                         'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                         'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                         'uci commit wireless',
                                         'wifi; sleep 10']
        return ap_guest_mixedpsk_chan_set_up

    def ap_mixedpsk_chan_bw80_set_up(self):
        ap_mixedpsk_chan_bw80_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                        'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                        'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                        'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                        'uci set wireless.' + self.DEV_5G + '.bw=80',
                                        'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                        'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                        'uci commit wireless',
                                        'wifi; sleep 10'
                                        ]
        return ap_mixedpsk_chan_bw80_set_up

    def ap_mixedpsk_chan_bw40_set_up(self):
        ap_mixedpsk_chan_bw40_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                        'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                        'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                        'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                        'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                        'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                        'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                        'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                        'uci set wireless.' + self.DEV_2G + '.bw=40',
                                        'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                        'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                        'uci set wireless.' + self.DEV_5G + '.bw=40',
                                        'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                        'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                        'uci commit wireless',
                                        'wifi; sleep 10'
                                        ]
        return ap_mixedpsk_chan_bw40_set_up

    def ap_mixedpsk_chan_bw20_set_up(self):
        ap_mixedpsk_chan_bw20_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                        'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                        'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                        'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                        'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                        'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                        'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                        'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                        'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                        'uci set wireless.' + self.DEV_2G + '.bw=20',
                                        'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                        'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                        'uci set wireless.' + self.DEV_5G + '.bw=20',
                                        'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                        'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                        'uci commit wireless',
                                        'wifi; sleep 10'
                                        ]
        return ap_mixedpsk_chan_bw20_set_up

    def ap_mixedpsk_chan_ssidspec_set_up(self):
        ap_mixedpsk_chan_ssidspec_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                            'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                            'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                            'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                            'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + self.SPECIAL_SSID_5G_BASH,
                                            'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + self.SPECIAL_SSID_BASH,
                                            'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                            'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                            'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                            'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                            'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                            'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                            'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                            'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                            'uci commit wireless',
                                            'wifi; sleep 10'
                                            ]
        return ap_mixedpsk_chan_ssidspec_set_up

    def ap_mixedpsk_chan_ssidchinese_set_up(self):
        ap_mixedpsk_chan_ssidchinese_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                               'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                               'uci set wireless.' + self.WIFI_IF_5G + '.key=' + KEY,
                                               'uci set wireless.' + self.WIFI_IF_2G + '.key=' + KEY,
                                               'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + CHINESE_SSID_5G,
                                               'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + CHINESE_SSID,
                                               'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                               'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                               'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                               'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                               'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                               'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                               'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                               'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                               'uci commit wireless',
                                               'wifi; sleep 10'
                                               ]
        return ap_mixedpsk_chan_ssidchinese_set_up

    def ap_mixedpsk_chan_keyspec_set_up(self):
        ap_mixedpsk_chan_keyspec_set_up = ['uci set wireless.' + self.WIFI_IF_5G + '.encryption=mixed-psk',
                                           'uci set wireless.' + self.WIFI_IF_2G + '.encryption=mixed-psk',
                                           'uci set wireless.' + self.WIFI_IF_5G + '.key=' + self.SPECIAL_KEY_BASH,
                                           'uci set wireless.' + self.WIFI_IF_2G + '.key=' + self.SPECIAL_KEY_BASH,
                                           'uci set wireless.' + self.WIFI_IF_5G + '.ssid=' + SSID_5G,
                                           'uci set wireless.' + self.WIFI_IF_2G + '.ssid=' + SSID,
                                           'uci set wireless.' + self.WIFI_IF_5G + '.hidden=0',
                                           'uci set wireless.' + self.WIFI_IF_2G + '.hidden=0',
                                           'uci set wireless.' + self.DEV_2G + '.channel=' + CHANNEL,
                                           'uci set wireless.' + self.DEV_2G + '.autoch=0',
                                           'uci set wireless.' + self.DEV_5G + '.channel=' + CHANNEL_5G,
                                           'uci set wireless.' + self.DEV_5G + '.autoch=0',
                                           'uci set wireless.' + self.DEV_2G + '.disabled=0',
                                           'uci set wireless.' + self.DEV_5G + '.disabled=0',
                                           'uci commit wireless',
                                           'wifi; sleep 10'
                                           ]
        return ap_mixedpsk_chan_keyspec_set_up

        # -----------clear-------------

    def assoc_clear_sta_2g(self):
        assoc_clear_sta_2g = ['ifconfig apcli0 down',
                              'ifconfig apcli0 up',
                              'iwpriv apcli0 set ApCliAuthMode=OPEN',
                              'iwpriv apcli0 set ApCliEncrypType=NONE',
                              'iwpriv apcli0 set ApCliSsid=' + SSID,
                              'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                              'udhcpc -q -i apcli0 -t 10'
                              ]
        return assoc_clear_sta_2g

    def assoc_clear_sta_guest(self):
        assoc_clear_sta_guest = ['ifconfig apcli0 down',
                                 'ifconfig apcli0 up',
                                 'iwpriv apcli0 set ApCliAuthMode=OPEN',
                                 'iwpriv apcli0 set ApCliEncrypType=NONE',
                                 'iwpriv apcli0 set ApCliSsid=' + GUEST_SSID,
                                 'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                 'udhcpc -q -i apcli0 -t 10'
                                 ]
        return assoc_clear_sta_guest

    def assoc_clear_sta_5g(self):
        assoc_clear_sta_5g = ['ifconfig apclii0 up',
                              'iwpriv apclii0 set ApCliAuthMode=OPEN',
                              'iwpriv apclii0 set ApCliEncrypType=NONE',
                              'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                              'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                              'udhcpc -q -i apclii0 -t 10'
                              ]
        return assoc_clear_sta_5g

        # --------------psk2-------------

    def assoc_psk2_sta_2g(self):
        assoc_psk2_sta_2g = ['ifconfig apcli0 down',
                             'ifconfig apcli0 up',
                             'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                             'iwpriv apcli0 set ApCliEncrypType=AES',
                             'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                             'iwpriv apcli0 set ApCliSsid=' + SSID,
                             'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                             'udhcpc -q -i apcli0 -t 10'
                             ]
        return assoc_psk2_sta_2g

    def assoc_psk2_sta_ssidspec_2g(self):
        assoc_psk2_sta_ssidspec_2g = ['ifconfig apcli0 down',
                                      'ifconfig apcli0 up',
                                      'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                      'iwpriv apcli0 set ApCliEncrypType=AES',
                                      'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                      'iwpriv apcli0 set ApCliSsid=' + self.SPECIAL_SSID_BASH,
                                      'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                      'udhcpc -q -i apcli0 -t 10'
                                      ]
        return assoc_psk2_sta_ssidspec_2g

    def assoc_psk2_sta_ssidchinese_2g(self):
        assoc_psk2_sta_ssidchinese_2g = ['ifconfig apcli0 down',
                                         'ifconfig apcli0 up',
                                         'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                         'iwpriv apcli0 set ApCliEncrypType=AES',
                                         'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                         'iwpriv apcli0 set ApCliSsid=' + CHINESE_SSID,
                                         'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apcli0 -t 10'
                                         ]
        return assoc_psk2_sta_ssidchinese_2g

    def assoc_psk2_sta_keyspec_2g(self):
        assoc_psk2_sta_keyspec_2g = ['ifconfig apcli0 down',
                                     'ifconfig apcli0 up',
                                     'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                     'iwpriv apcli0 set ApCliEncrypType=AES',
                                     'iwpriv apcli0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                     'iwpriv apcli0 set ApCliSsid=' + SSID,
                                     'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                     'udhcpc -q -i apcli0 -t 10'
                                     ]
        return assoc_psk2_sta_keyspec_2g

    def assoc_psk2_sta_guest(self):
        assoc_psk2_sta_guest = ['ifconfig apcli0 down',
                                'ifconfig apcli0 up',
                                'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                'iwpriv apcli0 set ApCliEncrypType=AES',
                                'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                'iwpriv apcli0 set ApCliSsid=' + GUEST_SSID,
                                'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                'udhcpc -q -i apcli0 -t 10'
                                ]
        return assoc_psk2_sta_guest

    def assoc_psk2_sta_5g(self):
        assoc_psk2_sta_5g = ['ifconfig apclii0 down',
                             'ifconfig apclii0 up',
                             'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                             'iwpriv apclii0 set ApCliEncrypType=AES',
                             'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                             'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                             'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                             'udhcpc -q -i apclii0 -t 10'
                             ]
        return assoc_psk2_sta_5g

    def assoc_psk2_sta_ssidspec_5g(self):
        assoc_psk2_sta_ssidspec_5g = ['ifconfig apclii0 down',
                                      'ifconfig apclii0 up',
                                      'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                      'iwpriv apclii0 set ApCliEncrypType=AES',
                                      'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                      'iwpriv apclii0 set ApCliSsid=' + self.SPECIAL_SSID_5G_BASH,
                                      'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                      'udhcpc -q -i apclii0 -t 10'
                                      ]
        return assoc_psk2_sta_ssidspec_5g

    def assoc_psk2_sta_ssidchinese_5g(self):
        assoc_psk2_sta_ssidchinese_5g = ['ifconfig apclii0 down',
                                         'ifconfig apclii0 up',
                                         'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                         'iwpriv apclii0 set ApCliEncrypType=AES',
                                         'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                         'iwpriv apclii0 set ApCliSsid=' + CHINESE_SSID_5G,
                                         'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apclii0 -t 10'
                                         ]
        return assoc_psk2_sta_ssidchinese_5g

    def assoc_psk2_sta_keyspec_5g(self):
        assoc_psk2_sta_keyspec_5g = ['ifconfig apclii0 down',
                                     'ifconfig apclii0 up',
                                     'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                     'iwpriv apclii0 set ApCliEncrypType=AES',
                                     'iwpriv apclii0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                     'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                     'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                     'udhcpc -q -i apclii0 -t 10'
                                     ]
        return assoc_psk2_sta_keyspec_5g
        # --------------psk-------------

    def assoc_psk_sta_2g(self):
        assoc_psk_sta_2g = ['ifconfig apcli0 down',
                            'ifconfig apcli0 up',
                            'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                            'iwpriv apcli0 set ApCliEncrypType=AES',
                            'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                            'iwpriv apcli0 set ApCliSsid=' + SSID,
                            'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                            'udhcpc -q -i apcli0 -t 10'
                            ]
        return assoc_psk_sta_2g

    def assoc_psk_sta_ssidspec_2g(self):
        assoc_psk_sta_ssidspec_2g = ['ifconfig apcli0 down',
                                     'ifconfig apcli0 up',
                                     'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                     'iwpriv apcli0 set ApCliEncrypType=AES',
                                     'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                     'iwpriv apcli0 set ApCliSsid=' + self.SPECIAL_SSID_BASH,
                                     'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                     'udhcpc -q -i apcli0 -t 10'
                                     ]
        return assoc_psk_sta_ssidspec_2g

    def assoc_psk_sta_ssidchinese_2g(self):
        assoc_psk_sta_ssidchinese_2g = ['ifconfig apcli0 down',
                                        'ifconfig apcli0 up',
                                        'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                        'iwpriv apcli0 set ApCliEncrypType=AES',
                                        'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                        'iwpriv apcli0 set ApCliSsid=' + CHINESE_SSID,
                                        'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                        'udhcpc -q -i apcli0 -t 10'
                                        ]
        return assoc_psk_sta_ssidchinese_2g

    def assoc_psk_sta_keyspec_2g(self):
        assoc_psk_sta_keyspec_2g = ['ifconfig apcli0 down',
                                    'ifconfig apcli0 up',
                                    'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                    'iwpriv apcli0 set ApCliEncrypType=AES',
                                    'iwpriv apcli0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                    'iwpriv apcli0 set ApCliSsid=' + SSID,
                                    'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                    'udhcpc -q -i apcli0 -t 10'
                                    ]
        return assoc_psk_sta_keyspec_2g

    def assoc_psk_sta_guest(self):
        assoc_psk_sta_guest = ['ifconfig apcli0 down',
                               'ifconfig apcli0 up',
                               'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                               'iwpriv apcli0 set ApCliEncrypType=AES',
                               'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                               'iwpriv apcli0 set ApCliSsid=' + GUEST_SSID,
                               'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                               'udhcpc -q -i apcli0 -t 10'
                               ]
        return assoc_psk_sta_guest

    def assoc_psk_sta_5g(self):
        assoc_psk_sta_5g = ['ifconfig apclii0 down',
                            'ifconfig apclii0 up',
                            'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                            'iwpriv apclii0 set ApCliEncrypType=AES',
                            'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                            'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                            'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                            'udhcpc -q -i apclii0 -t 10'
                            ]
        return assoc_psk_sta_5g

    def assoc_psk_sta_ssidspec_5g(self):
        assoc_psk_sta_ssidspec_5g = ['ifconfig apclii0 down',
                                     'ifconfig apclii0 up',
                                     'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                     'iwpriv apclii0 set ApCliEncrypType=AES',
                                     'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                     'iwpriv apclii0 set ApCliSsid=' + self.SPECIAL_SSID_5G_BASH,
                                     'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                     'udhcpc -q -i apclii0 -t 10'
                                     ]
        return assoc_psk_sta_ssidspec_5g

    def assoc_psk_sta_ssidchinese_5g(self):
        assoc_psk_sta_ssidchinese_5g = ['ifconfig apclii0 down',
                                        'ifconfig apclii0 up',
                                        'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                        'iwpriv apclii0 set ApCliEncrypType=AES',
                                        'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                        'iwpriv apclii0 set ApCliSsid=' + CHINESE_SSID_5G,
                                        'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                        'udhcpc -q -i apclii0 -t 10'
                                        ]
        return assoc_psk_sta_ssidchinese_5g

    def assoc_psk_sta_keyspec_5g(self):
        assoc_psk_sta_keyspec_5g = ['ifconfig apclii0 down',
                                    'ifconfig apclii0 up',
                                    'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                    'iwpriv apclii0 set ApCliEncrypType=AES',
                                    'iwpriv apclii0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                    'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                    'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                    'udhcpc -q -i apclii0 -t 10'
                                    ]
        return assoc_psk_sta_keyspec_5g

        # --------------tkip-psk2-------------

    def assoc_tkippsk2_sta_2g(self):
        assoc_tkippsk2_sta_2g = ['ifconfig apcli0 down',
                                 'ifconfig apcli0 up',
                                 'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                 'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                 'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                 'iwpriv apcli0 set ApCliSsid=' + SSID,
                                 'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                 'udhcpc -q -i apcli0 -t 10'
                                 ]
        return assoc_tkippsk2_sta_2g

    def assoc_tkippsk2_sta_ssidspec_2g(self):
        assoc_tkippsk2_sta_ssidspec_2g = ['ifconfig apcli0 down',
                                          'ifconfig apcli0 up',
                                          'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                          'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                          'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                          'iwpriv apcli0 set ApCliSsid=' + self.SPECIAL_SSID_BASH,
                                          'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                          'udhcpc -q -i apcli0 -t 10'
                                          ]
        return assoc_tkippsk2_sta_ssidspec_2g

    def assoc_tkippsk2_sta_ssidchinese_2g(self):
        assoc_tkippsk2_sta_ssidchinese_2g = ['ifconfig apcli0 down',
                                             'ifconfig apcli0 up',
                                             'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                             'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                             'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                             'iwpriv apcli0 set ApCliSsid=' + CHINESE_SSID,
                                             'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                             'udhcpc -q -i apcli0 -t 10'
                                             ]
        return assoc_tkippsk2_sta_ssidchinese_2g

    def assoc_tkippsk2_sta_keyspec_2g(self):
        assoc_tkippsk2_sta_keyspec_2g = ['ifconfig apcli0 down',
                                         'ifconfig apcli0 up',
                                         'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                         'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                         'iwpriv apcli0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                         'iwpriv apcli0 set ApCliSsid=' + SSID,
                                         'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apcli0 -t 10'
                                         ]
        return assoc_tkippsk2_sta_keyspec_2g

    def assoc_tkippsk2_sta_guest(self):
        assoc_tkippsk2_sta_guest = ['ifconfig apcli0 down',
                                    'ifconfig apcli0 up',
                                    'iwpriv apcli0 set ApCliAuthMode=WPA2PSK',
                                    'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                    'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                    'iwpriv apcli0 set ApCliSsid=' + GUEST_SSID,
                                    'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                    'udhcpc -q -i apcli0 -t 10'
                                    ]
        return assoc_tkippsk2_sta_guest

    def assoc_tkippsk2_sta_5g(self):
        assoc_tkippsk2_sta_5g = ['ifconfig apclii0 down',
                                 'ifconfig apclii0 up',
                                 'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                 'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                 'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                 'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                 'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                 'udhcpc -q -i apclii0 -t 10'
                                 ]
        return assoc_tkippsk2_sta_5g

    def assoc_tkippsk2_sta_ssidspec_5g(self):
        assoc_tkippsk2_sta_ssidspec_5g = ['ifconfig apclii0 down',
                                          'ifconfig apclii0 up',
                                          'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                          'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                          'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                          'iwpriv apclii0 set ApCliSsid=' + self.SPECIAL_SSID_5G_BASH,
                                          'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                          'udhcpc -q -i apclii0 -t 10'
                                          ]
        return assoc_tkippsk2_sta_ssidspec_5g

    def assoc_tkippsk2_sta_ssidchinese_5g(self):
        assoc_tkippsk2_sta_ssidchinese_5g = ['ifconfig apclii0 down',
                                             'ifconfig apclii0 up',
                                             'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                             'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                             'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                             'iwpriv apclii0 set ApCliSsid=' + CHINESE_SSID_5G,
                                             'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                             'udhcpc -q -i apclii0 -t 10'
                                             ]
        return assoc_tkippsk2_sta_ssidchinese_5g

    def assoc_tkippsk2_sta_keyspec_5g(self):
        assoc_tkippsk2_sta_keyspec_5g = ['ifconfig apclii0 down',
                                         'ifconfig apclii0 up',
                                         'iwpriv apclii0 set ApCliAuthMode=WPA2PSK',
                                         'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                         'iwpriv apclii0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                         'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                         'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apclii0 -t 10'
                                         ]
        return assoc_tkippsk2_sta_keyspec_5g

        # --------------tkip-psk-------------

    def assoc_tkippsk_sta_2g(self):
        assoc_tkippsk_sta_2g = ['ifconfig apcli0 down',
                                'ifconfig apcli0 up',
                                'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                'iwpriv apcli0 set ApCliSsid=' + SSID,
                                'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                'udhcpc -q -i apcli0 -t 10'
                                ]
        return assoc_tkippsk_sta_2g

    def assoc_tkippsk_sta_ssidspec_2g(self):
        assoc_tkippsk_sta_ssidspec_2g = ['ifconfig apcli0 down',
                                         'ifconfig apcli0 up',
                                         'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                         'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                         'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                         'iwpriv apcli0 set ApCliSsid=' + self.SPECIAL_SSID_BASH,
                                         'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apcli0 -t 10'
                                         ]
        return assoc_tkippsk_sta_ssidspec_2g

    def assoc_tkippsk_sta_ssidchinese_2g(self):
        assoc_tkippsk_sta_ssidchinese_2g = ['ifconfig apcli0 down',
                                            'ifconfig apcli0 up',
                                            'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                            'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                            'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                            'iwpriv apcli0 set ApCliSsid=' + CHINESE_SSID,
                                            'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                            'udhcpc -q -i apcli0 -t 10'
                                            ]
        return assoc_tkippsk_sta_ssidchinese_2g

    def assoc_tkippsk_sta_keyspec_2g(self):
        assoc_tkippsk_sta_keyspec_2g = ['ifconfig apcli0 down',
                                        'ifconfig apcli0 up',
                                        'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                        'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                        'iwpriv apcli0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                        'iwpriv apcli0 set ApCliSsid=' + SSID,
                                        'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                        'udhcpc -q -i apcli0 -t 10'
                                        ]
        return assoc_tkippsk_sta_keyspec_2g

    def assoc_tkippsk_sta_guest(self):
        assoc_tkippsk_sta_guest = ['ifconfig apcli0 down',
                                   'ifconfig apcli0 up',
                                   'iwpriv apcli0 set ApCliAuthMode=WPAPSK',
                                   'iwpriv apcli0 set ApCliEncrypType=TKIP',
                                   'iwpriv apcli0 set ApCliWPAPSK=' + KEY,
                                   'iwpriv apcli0 set ApCliSsid=' + GUEST_SSID,
                                   'iwpriv apcli0 set ApCliAutoConnect=1;sleep 5',
                                   'udhcpc -q -i apcli0 -t 10'
                                   ]
        return assoc_tkippsk_sta_guest

    def assoc_tkippsk_sta_5g(self):
        assoc_tkippsk_sta_5g = ['ifconfig apclii0 down',
                                'ifconfig apclii0 up',
                                'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                'udhcpc -q -i apclii0 -t 10'
                                ]
        return assoc_tkippsk_sta_5g

    def assoc_tkippsk_sta_ssidspec_5g(self):
        assoc_tkippsk_sta_ssidspec_5g = ['ifconfig apclii0 down',
                                         'ifconfig apclii0 up',
                                         'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                         'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                         'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                         'iwpriv apclii0 set ApCliSsid=' + self.SPECIAL_SSID_5G_BASH,
                                         'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                         'udhcpc -q -i apclii0 -t 10'
                                         ]
        return assoc_tkippsk_sta_ssidspec_5g

    def assoc_tkippsk_sta_ssidchinese_5g(self):
        assoc_tkippsk_sta_ssidchinese_5g = ['ifconfig apclii0 down',
                                            'ifconfig apclii0 up',
                                            'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                            'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                            'iwpriv apclii0 set ApCliWPAPSK=' + KEY,
                                            'iwpriv apclii0 set ApCliSsid=' + CHINESE_SSID_5G,
                                            'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                            'udhcpc -q -i apclii0 -t 10'
                                            ]
        return assoc_tkippsk_sta_ssidchinese_5g

    def assoc_tkippsk_sta_keyspec_5g(self):
        assoc_tkippsk_sta_keyspec_5g = ['ifconfig apclii0 down',
                                        'ifconfig apclii0 up',
                                        'iwpriv apclii0 set ApCliAuthMode=WPAPSK',
                                        'iwpriv apclii0 set ApCliEncrypType=TKIP',
                                        'iwpriv apclii0 set ApCliWPAPSK=' + self.SPECIAL_KEY_BASH,
                                        'iwpriv apclii0 set ApCliSsid=' + SSID_5G,
                                        'iwpriv apclii0 set ApCliAutoConnect=1;sleep 5',
                                        'udhcpc -q -i apclii0 -t 10'
                                        ]
        return assoc_tkippsk_sta_keyspec_5g


if __name__ == '__main__':
    pass