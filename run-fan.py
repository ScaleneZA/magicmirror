# This is intended to be run at startup with a process manager
import time
from gpiozero import CPUTemperature

import config
import control

while True:
    cpu = CPUTemperature().temperature
    if cpu > config.TEMP_MAX:
        control.turnOn("FAN")
    elif cpu < config.TEMP_MIN:
        control.turnOff("FAN")

    time.sleep (10)