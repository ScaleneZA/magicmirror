import RPi.GPIO as GPIO
import time

import config

def turnOn(name):
    pin = config.GPIO[name]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)

def turnOff(name):
    pin = config.GPIO[name]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()