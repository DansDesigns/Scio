
 #Scio
 Linux Powered Multi-Sensor Scientific Data Recorder
 Inspired by Star Trek TNG/DS9/Voyager Tricorder


Discover,
Record,
Learn.


```
STILL IN ACTIVE DEVELOPMENT
```



## Hardware:
```
NanoPi Neo Air - Quad-core 1.2Ghz Allwinner-H3 with WiFi & BT, 512Mb Ram, 8Gb EMMC
Support micro SD Card upto 128Gb (default location for Sensor Logs is Internal Storage)
SSD1351 1.5" RGB OLED
x4 Physical Tactile Push Buttons
x3 Neopixel Status LEDs powered by onboard ESP32-C3F4H
MPR121 Capacitive Touch Controller
MAX17048 LiPo Battery Monitor
3.7v 2000mAh LiPo
5v 1.2A Power Converter
MAX98357A I2S Audio Amplifier
8 Ohm 2 Watt Speaker
PCF8574RGTR I2C Extender
```

## Sensors:
```
MPU6050 6-axis Gyroscope & IMU
BME280 Temperature, Pressure & Humidity Sensor
AGM8833 IR Thermal Camera
x1 NeoPixel for Colour Spectroscopy
VEML6040 Colour Sensor
VL53L0X IR Long Range 940nm Distance Sensor (35cm-2m)
SI1145 UV, Visible, IR Spectrum Sensor & Close Range IR Distance Sensor (<1cm-50cm)
HMC5883L Magnetic Field Sensor
IR Transmitter/Receiver
AGS10 Volatile Gas Sensor
SCD40 CO2 Sensor
MiCS-5524 Multi-Gas Sensor

```

## Functions:
```
WIP = In Progress | TBS = To Be Started  | DONE = Finished dev | R&D = Refinement Needed
-------------------------------------------------------------------------------------------------------
Atmospheric Scan - Temperature, Pressure, Humidity, Gas Level				DONE		R&D
Audio Spectrum - 									WIP
Distance Scan - Close Range & Long Range 						DONE		R&D
Database - 										WIP
EMF - Electromagnetic and Magnetic Field						DONE		R&D
Gyroscope & Accelerometer - 								DONE		R&D
IR - Transmit, Receive & Thermal Vision							WIP
Visible Light - Intensity, Spectrum & Spectroscopy					WIP/DONE	R&D
UV - Index Level									DONE		R&D
Radio - Including:									
-WiFi Hotspot & Config AP - Connect to Hotspot to configure WiFi Connections		WIP
-WiFi Scanner (2.4Ghz) - Scan & Ranging of SSID						TBS
-Remote Bluetooth Sensor - Wireless Addon Sensors					WIP
-Bluetooth Scanner (2.4Ghz) - Scan & Ranging of local Bluetooth devices			TBS
-Live Web-Sensor - Displays Sensor info on a webpage on local IP			WIP

OTA Updating - Using this repo to Update on the go					WIP
Audio Playback (Alerts, Beeps & Charge Events)						DONE		R&D
Backup Sensor Logs to hot-swappable USB							DONE		
Serial control of Neopixel Status LEDs via internal ESP32C3				WIP		


```
