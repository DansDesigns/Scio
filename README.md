
 # Scio
 
 Linux Powered Multi-Sensor Scientific Data Recorder
 Inspired by Star Trek TNG/DS9/Voyager Tricorder


Discover, Record, Learn.



* STILL IN ACTIVE DEVELOPMENT
* Updated Hardware 03/02/2025





## Hardware:
```
LuckFox Core1106 RV1106G3 Linux SBC
	Quad-Core 1.2Ghz CPU with 256Mb DDR3L, 8Gb EMMC, Wifi6 & BLE/BT5.2
	with dedicated RKNPU offering 1TOPS for Internal RNN's & supporting ONNX

ESP32-C3-F4H microController (Programmable over Internal USB Bus)
SSD1351 1.5" RGB OLED
x4 Physical Tactile Push Buttons
x3 Neopixel Status LEDs powered by onboard ESP32-C3
MPR121 Capacitive Touch Controller
MAX17048 LiPo Battery Monitor
3.7v 1600mAh LiPo
TP4056x LiPo Charger
5v 1A Power Converter
MAX98357A I2S Audio Amplifier
8 Ohm 2 Watt Speaker
PCF8574RGTR I2C Extender

```

## Sensors:
```
MPU6050 6-axis Gyroscope & IMU
BME280 Temperature, Pressure & Humidity Sensor
AGM8833 IR Thermal Camera
x1 Dedicated NeoPixel for Colour Spectroscopy
VEML6040 Colour Sensor
SI1145 UV, Visible, IR Spectrum & Intensity Sensor & Close Range IR Distance Sensor (<1cm-50cm)
VL53L0X IR Long Range 940nm Distance Sensor (35cm-2m)
HMC5883L Magnetic Field Sensor
Separate IR Transmitter & Receiver (allowing full-duplex data transfer)
AGS10 VOC Sensor (Volatile Organic Compounds)
SCD40 CO2 Sensor
MiCS-5524 Multi-Gas Sensor (CO, CH4, C2H5OH, C3H8, C4H10, H2, H2S, NH3)

```

## Functions:
```
TBS = To Be Started | WIP = In Progress | DONE = Finished Dev | R&D = Refinement Needed
-------------------------------------------------------------------------------------------------------
* Atmospheric Scan - Temperature, Pressure, Humidity, Gas Level				DONE	R&D
- Audio Spectrum - 									WIP
* Distance Scan - Close Range & Long Range 						DONE	R&D
- Database - 										WIP
* EMF - Electromagnetic and Magnetic Field						DONE	R&D
* Gyroscope & Accelerometer - 								DONE	R&D
- IR - Transmit, Receive & Thermal Vision						WIP
- Visible Light - Intensity, Spectrum & Spectroscopy					WIP	R&D
- UV - Index Level									DONE	R&D
Radio - Including:									
- WiFi Hotspot & Config AP - Connect to Hotspot to configure WiFi Connections		WIP
- WiFi Scanner (2.4Ghz) - Scan & Ranging of SSID						TBS
- Remote Bluetooth Sensor - Wireless Addon Sensors					WIP
- Bluetooth Scanner (2.4Ghz) - Scan & Ranging of local Bluetooth devices			TBS
- Live Web-Sensor - Displays Sensor info on a webpage on local IP			WIP

- OTA Updating - Using this repo to Update on the go					WIP
* Audio Playback (Alerts, Beeps & Charge Events)					DONE	R&D
* Backup Sensor Logs to hot-swappable USB						DONE		
* Serial control of Neopixel Status LEDs via internal ESP32C3				DONE	R&D		
* USB Device - Scan for Hazardous & Infected Files					DONE	R&D
- NFC Scanning & Emulating 									TBS

Addon USB Extensions:
- Multimeter (Voltage, Amperage, Resistance & Capacitance)				WIP
- Medical Sensors (Heart-rate, Blood Oxygen, HRV, ECG, Human Presence Detection, etc)	WIP
- Future Upgrades										TBS

```

## Future Upgrade Plans:
```
26Ghz/60Ghz mmWave Scanning
Custom Integrated Neural Network for increased Sensor Resolution and Data Analysis
Image Recognition RNN designed for Plant/Insect/Rock Identification

```
