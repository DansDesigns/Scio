# from https://community.sparkfun.com/t/lipo-fuel-gauge-max1704x-with-python/47625/3

import smbus2

FG_ADDRESS = 0x36
REGISTER_VCELL = 0x02
REGISTER_SOC = 0x04

bus = smbus2.SMBus(1)

data = bus.read_i2c_block_data(FG_ADDRESS, REGISTER_VCELL, 2)
value = (data[0] << 8) | data[1]
volts=str("%.2f" % round(((value>>4)*0.00125),2) )
print("volts: ",volts)

data = bus.read_i2c_block_data(FG_ADDRESS, REGISTER_SOC, 2)
value = (data[0] << 8) | data[1]
soc=str("%.2f" % round((value/256),2) )
print("soc: ",soc)

bus.close()
