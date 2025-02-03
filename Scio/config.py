#
#
#


# global state
# global y1


import pygame
from pygame.locals import *
import time
import subprocess as sp
import os
import OPi.GPIO as GPIO
from OPi.pin_mappings import sunxi
# import wifimanagement as wifi

# ~~~~~~ MUST have .py file in same folder: ~~~~~~
from smbus2 import SMBus
from bme280 import BME280
import MPR121 as MPR121
import VL53L0X
from mpu6050 import mpu6050
import os
import shutil

import matplotlib.pyplot as plt
import io                           # io.BytesIO

# NanoPi Neo Pin == Linux Pin Number:
# GPIO Buttons:
assert sunxi("PA00") == 0  # UP
assert sunxi("PA01") == 1  # DOWN
assert sunxi("PA02") == 2  # BACK
assert sunxi("PA03") == 3  # ENTER/SELECT/OK
# assert sunxi("PA06") == 6    # SPI-0 OLED RST
# assert sunxi("PA07") == 7    # GPIO-A7 - ONLY on Neo Core
assert sunxi("PA10") == 10     # GPIO-A10 - STATUS LED
# I2C-0:
# assert sunxi("PA11") == 11   # I2C-0 SCLK
# assert sunxi("PA12") == 12   # I2C-0 SDA
# I2C-2: (ONLY on Neo Core)
# assert sunxi("PE12") == 11   # I2C-0 SCLK
# assert sunxi("PE13") == 12   # I2C-0 SDA
# SPI-1: (ONLY on Neo Core)
# assert sunxi("PA13") == 13   # SPI-1 OLED-CS
# assert sunxi("PA14") == 14   # SPI-1 OLED-CLK
# assert sunxi("PA15") == 15   # SPI-1 OLED-MOSI
# assert sunxi("PA16") == 16   # SPI-1 MISO
assert sunxi("PA17") == 17  # SPDIFF OUT
# I2S-0:
# assert sunxi("PA18") == 18  # I2S-0 - LR-CLK
# assert sunxi("PA19") == 19  # I2S-0 - BCLK
# assert sunxi("PA20") == 20  # I2S-0 - SDOUT
# assert sunxi("PA21") == 21  # I2S-0 - SDIN
# SPI-0:
# assert sunxi("PC00") == 64   # SPI-0 OLED MOSI
# assert sunxi("PC01") == 65   # SPI-0 OLED MISO
# assert sunxi("PC02") == 66   # SPI-0 OLED CLK
# assert sunxi("PC03") == 67   # SPI-0 OLED CS
# assert sunxi("PG06") == 198  # GPIO-G6 - UART1 TX
# assert sunxi("PG07") == 199  # GPIO-G7 - UART1 RX
assert sunxi("PG08") == 200  # GPIO-G8
# assert sunxi("PG09") == 201  # GPIO-G9 - OLED-DC
assert sunxi("PG10") == 202  # GPIO-G10 - LED PWR
assert sunxi("PG11") == 203  # GPIO-G11 - Wake/Sleep Pin DRV5053
assert sunxi("PL11") == 363  # GPIO-L11 IR RX

# ~~~~~~~~~~~ Screen Setup: ~~~~~~~~~~~

# turns off blinking curser from console:
os.system('setterm -cursor off')

geom = sp.getoutput("fbset -fb /dev/fb0 | grep geometry").split()
xres, yres, bpp = int(geom[1]), int(geom[2]), int(geom[5])


# ~~~~~~~~~~~ PyGame Setup: ~~~~~~~~~~~
pygame.font.init()
pygame.mixer.pre_init(44100, 16, 1, 1024) # (max frequency in hz, bitdepth, no. channels, mono or stereo, buffer size (power of 2))
pygame.mixer.init(44100, 16, 1, 1024)
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF, 16)
oled = pygame.Surface((xres, yres))  # Set surface to display on
clock = pygame.time.Clock()

# ~~~~~~~~~~~ Hardware Setup: ~~~~~~~~~~~
# I2C Addresses:
# BME280 = 0x76, MPU6050 = 0x68, MPR121 = 0x5A, VL53L0X = 0x29, SI1145 = 0x60, GY271(HMC5883L) = 0x0D,
# MAX17048 = 0x36, AGS10 = 0x1A, AGM8833 = 0x69, PCF8574RGTR = 0x20, VEML6040 = 0x10, INA226 = 0x40, 
# SCD40 = 0x62,  

bus = SMBus(0)
bme280 = BME280(i2c_dev=bus)
cap = MPR121.MPR121()
cap.begin(busnum=0)
tof = VL53L0X.VL53L0X()
mpu = mpu6050(0x68)

# VL53L0X tof Sensor mode:
# VL53L0X_GOOD_ACCURACY_MODE = 0  # Good Accuracy mode
# VL53L0X_BETTER_ACCURACY_MODE = 1  # Better Accuracy mode
# VL53L0X_BEST_ACCURACY_MODE = 2  # Best Accuracy mode
# VL53L0X_LONG_RANGE_MODE = 3  # Longe Range mode
# VL53L0X_HIGH_SPEED_MODE = 4  # High Speed mode
# tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
tof.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000

LED_STAT = "PA10"
LED_PWR = "PL10"
button_1 = "PA00"
button_2 = "PA01"
button_3 = "PA02"
button_4 = "PA03"
button_wake = "PG11"


# ~~~~~~~~~~~~~~~~~~~ Pin Settings: ~~~~~~~~~~~~~~~~#
GPIO.setmode(GPIO.SUNXI)
GPIO.setwarnings(False)  # disable when production ready..

# LEDs & Sleep Pin Setup:
GPIO.setup(LED_STAT, GPIO.OUT)
GPIO.setup(LED_PWR, GPIO.OUT)
GPIO.output(LED_PWR, True)
GPIO.output(LED_STAT, True)

# Button Setup:
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)
GPIO.setup(button_3, GPIO.IN)
GPIO.setup(button_4, GPIO.IN)
GPIO.setup(button_wake, GPIO.IN)


# ~~~~~~~~~~~ Breathing Colours: def_col_breathe[R,G,B]~~~~~~~~~~~
# white
col_dir_breathe = [1, 1, 1]
def_col_breathe = [100, 100, 100]
# green
col_dir_breathe2 = [0, 1, 0]
def_col_breathe2 = [0, 255, 0]
# blue - alert
col_dir_breathe3 = [1, 0, 0]
def_col_breathe3 = [0, 0, 255]
# red - alert
col_dir_breathe4 = [1, 0, 0]
def_col_breathe4 = [255, 0, 0]
# orange
col_dir_breathe5 = [1, 1, 1]
def_col_breathe5 = [255, 153, 0]
# yellow
col_dir_breathe6 = [1, 1, 1]
def_col_breathe6 = [255, 255, 204]

col_spd = 33
col_spd_warn = 66
minimum = 100
maximum = 255

# ~~~~~~~~~~ Menu Constants: ~~~~~~~~~~~
page = 1
mode = 'Z'
cursor_rect = pygame.Rect(0, 0, 20, 20)  # may have to have as a global..

# ~~~~~~~~~~ Wifi Sensor Server State: ~~~~~~~~~~
server_state = "Inactive"

# ~~~~~~~~~~ Sensor Log Locations: ~~~~~~~~~~
source_folder = r"/home/pi/sensorlogs/"
destination_folder = r"/media/usb0/"

# ~~~~~~~~~~ Sound file Locations: ~~~~~~~~~~
scan_alert_sound = pygame.mixer.Sound("sounds/scan_alert.mp3")
deep_alert_sound = pygame.mixer.Sound("sounds/deep_error_beep.mp3")
sonar_beep = pygame.mixer.Sound("sounds/sonar_beep.mp3")

# to play use: <name_of_sound>.play()


# EOF
