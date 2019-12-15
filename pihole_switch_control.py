#! /usr/bin/env python
# coding=utf-8

import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SW1 = 17
SW2 = 22
SW3 = 23
SW4 = 27
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.RISING)
GPIO.add_event_detect(SW2, GPIO.RISING)
GPIO.add_event_detect(SW3, GPIO.RISING)
GPIO.add_event_detect(SW4, GPIO.RISING)
with open("/sys/class/backlight/soc:backlight/brightness") as fd:
    brightness = fd.readline()
    backlight_status = True if brightness[0] == '1' else False

try:
    while True:
        if GPIO.event_detected(SW1):
            if backlight_status:
                os.system("sudo sh -c \'echo \"0\" > /sys/class/backlight/soc\:backlight/brightness\'")
                backlight_status = False
            else:
                os.system("sudo sh -c \'echo \"1\" > /sys/class/backlight/soc\:backlight/brightness\'")
                backlight_status = True
                
        if GPIO.event_detected(SW2):
            pass
        if GPIO.event_detected(SW3):
            pass
        if GPIO.event_detected(SW4):
            pass
        time.sleep(0.1)
except:
    GPIO.cleanup()

