#!/home/pi/testvenv/bin/python3
# !$TERM = bash
# Program to test spi0 using python on display ssd1351
# modified for NanoPi Neo fb0
#
# text function:
# draw_text(<TEXT>, <FONT>, <FONT_COLOUR>, X-COORD, Y-COORD)
#
# text from sensor (.2 significant figures):
# draw_text(f"{temperature}{:.2f}", text_font, (WHITE), 0, 64)
#
#
#    leds:
#    power = GPIO L10
#    status = GPIO A10
#
#   GPIO has no built-in pull-down resistors so need
#   to add 10K
#
# ~~~~~~~~~~~ Imports: ~~~~~~~~~~~
import os
os.environ['PYGAME_DETECT_AVX2'] = '1'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.color import *
from pygame.locals import *
import psutil
import subprocess as sp
from datetime import date
import time
import OPi.GPIO as GPIO
from OPi.pin_mappings import sunxi
from smbus2 import SMBus
from bme280 import BME280
import math
import MPR121 as MPR121  # have .py file in same folder..
# following elements must be called in specific order:
from menus import *
from screens import *
from colours import *
from functions import *
import config

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
GPIO.output(LED_STAT, False)
print(" ")
GPIO.output(LED_STAT, True)
print(" ")
print(" ")
GPIO.output(LED_STAT, False)
print(" ")
print(" ")
print(" ")
GPIO.output(LED_STAT, True)
print(" ")
print(" ")
GPIO.output(LED_STAT, False)
print(" ")
print(" ")
print("Loading GUI...")
print(" ")
print(" ")
GPIO.output(LED_STAT, True)
print(" ")
print(" ")
GPIO.output(LED_STAT, False)
print(" ")
print(" ")
print(" ")
GPIO.output(LED_STAT, True)
print(" ")
print(" ")
GPIO.output(LED_STAT, False)
print(" ")
print(" ")
# pygame.time.wait(777)

# ~~~~~~~~~~~ Main Loop Setup: ~~~~~~~~~~~

GPIO.add_event_detect(button_1, GPIO.FALLING, callback=None, bouncetime=200)
GPIO.add_event_detect(button_2, GPIO.FALLING, callback=None, bouncetime=200)
GPIO.add_event_detect(button_3, GPIO.RISING, callback=None, bouncetime=200)
GPIO.add_event_detect(button_4, GPIO.RISING, callback=None, bouncetime=200)
GPIO.add_event_detect(button_wake, GPIO.RISING, callback=None, bouncetime=200)

today = date.today()
last_touched = cap.touched()  # last thing called before main loop begins..

config.mode = 'Z'
# ~~~~~~~~~~~ Main Loop : ~~~~~~~~~~~

while True:
    current_touched = cap.touched()  # first thing to call in main loop..

    temperature = round(bme280.get_temperature(), 2)  # round(xxx, 2) limits output to 2sf
    pressure = round(bme280.get_pressure(), 2)
    humidity = round(bme280.get_humidity(), 2)



# ~~~~~~~~~~~~~~~~~~~~~~~~~ Device Sleep Check: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PG11 as Sleep/Wake Pin
# pull it LOW (magnet away) to wake (needs pull-down resistor?)
# pull HIGH (magnet near) to sleep (needs pull-up resistor?)

    if GPIO.input(button_wake) == GPIO.HIGH:
       # config.mode='~'
        oled.fill(black)
        os.system("echo +5 > /sys/class/rtc/rtc0/wakealarm")
        os.system("echo mem > /sys/power/state")
        refresh()

    elif GPIO.input(button_wake) == GPIO.LOW:
        #config.mode='@'
        pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Touch Input: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if cap.is_touched(0):
        sonar_beep.play()
        # GPIO.output(LED_STAT, False)
        #GPIO.output(LED_STAT, True)
        #time.sleep(0.3)
        #GPIO.output(LED_STAT, False)
        # oled.fill(black)
        config.mode = 'A'

    if cap.is_touched(1):
        sonar_beep.play()
        # GPIO.output(LED_STAT, False)
        # GPIO.output(LED_STAT, True)
        # time.sleep(0.3)
        # GPIO.output(LED_STAT, False)
        # oled.fill(black)
        config.mode = 'B'

    if cap.is_touched(2):
        sonar_beep.play()
        # GPIO.output(LED_STAT, False)
        # GPIO.output(LED_STAT, True)
        # time.sleep(0.3)
        # GPIO.output(LED_STAT, False)
        # oled.fill(black)
        config.mode = 'D'

    if cap.is_touched(3):
        sonar_beep.play()
        # GPIO.output(LED_STAT, False)
        # GPIO.output(LED_STAT, True)
        # time.sleep(0.3)
        # GPIO.output(LED_STAT, False)
        # oled.fill(black)
        config.mode = 'G'

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Modes: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if config.mode == 'A':
        Atmos()
        refresh()  # must be called to refresh the screen


    if config.mode == 'B':
        Menu_device() # change to BIO Sensors
        refresh()  # must be called to refresh the screen


    if config.mode == 'C':
        copy_to_usb()
        refresh()  # must be called to refresh the screen


    if config.mode == 'D':
        Distance()
        refresh()

    if config.mode == 'G':
        Gyro()
        refresh()  # must be called to refresh the screen


    if config.mode == 'I':
        Info()
        refresh()  # must be called to refresh the screen


    if config.mode == 'M':
        Menu_device()
        refresh()  # must be called to refresh the screen


    if config.mode == 'S':
        Stats()
        refresh()  # must be called to refresh the screen


    if config.mode == 'X':
        # turns on blinking curser on console:
        os.system('setterm -cursor on')
        pygame.QUIT()


    if config.mode == 'Y':
        Saved()
        refresh()  # must be called to refresh the screen


    if config.mode == 'Z':
        Welcome()
        refresh()  # must be called to refresh the screen

    if config.mode =='@':
        oled.fill(black)
        draw_text("button low", 13, grey, 5, 30)
        refresh()

    if config.mode =='~':
        oled.fill(black)
        draw_text("button high", 13, green, 5, 30)
        refresh()


    last_touched = current_touched
    refresh()  # must be called to refresh the screen

# EOF
