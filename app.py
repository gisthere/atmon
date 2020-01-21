import logging
import time

import serial
from prometheus_client import start_http_server, Gauge

if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s/%(asctime)s] %(message)s', level=logging.INFO)
    logging.info('App is running.')
    serial_dev = '/dev/serial0'
    ser = serial.Serial(serial_dev, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, timeout=1.0)
    co2_level = Gauge('co2_level_ppm', 'CO2 level (ppm)')
    start_http_server(8080)
    while True:
        ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
        res = ser.read(9)
        if len(res) >= 4 and res[0] == 0xff and res[1] == 0x86:
            co2 = res[2] * 256 + res[3]
            co2_level.set(co2)
            logging.info('Last CO2 level: %s', co2)
        time.sleep(1)
