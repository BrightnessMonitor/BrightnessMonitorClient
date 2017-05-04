#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

timing = 0
GPIOPIN = 11
GPIO.setmode(GPIO.BCM)


def RCtime(GPIOPIN):
    reading = 0
    GPIO.setup(GPIOPIN, GPIO.OUT)
    GPIO.output(GPIOPIN, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(GPIOPIN, GPIO.IN)
    while (GPIO.input(GPIOPIN) == GPIO.LOW):
        reading += 1
    return reading



#  timing = RCtime(GPIOPIN)
#if timing < 500:
#    print "sehr hell"
#elif timing < 1000:
#    print "hell"
#elif timing < 2000:
#    print "schattig"
#elif timing < 10000:
#    print "sehr schattig"
#elif timing < 150000:
#    print "fast dunkel"
#else:
#    print "dunkel"