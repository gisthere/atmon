from prometheus_client import start_http_server, Gauge
import random
import time

import mh_z19

if __name__ == '__main__':
    co2_level = Gauge('co2_level_ppm', 'CO2 level (ppm)')
    start_http_server(8080)
    while True:
        if sensor_data := mh_z19.mh_z19():
            co2_level.set(sensor_data['co2'])
        time.sleep(1)
