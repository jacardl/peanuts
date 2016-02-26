# -*- coding: utf8 -*-
import serial
import serial.tools.list_ports_windows

if __name__ == '__main__':

    for port in sorted(serial.tools.list_ports_windows.comports()):
        print port[0]

