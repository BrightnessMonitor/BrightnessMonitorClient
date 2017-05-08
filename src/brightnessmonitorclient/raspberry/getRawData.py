#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO, time, os

timing = 0
GPIOPIN = 11
GPIO.setmode(GPIO.BCM)


def RCtime():
    reading = 0
    GPIO.setup(GPIOPIN, GPIO.OUT)
    GPIO.output(GPIOPIN, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(GPIOPIN, GPIO.IN)
    while (GPIO.input(GPIOPIN) == GPIO.LOW):
        reading += 1
    return reading