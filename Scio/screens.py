#
# 
#
# ~~~~~~~~~~~~~~~~~~~~ Screens: ~~~~~~~~~~~~~~~~~~~

from datetime import datetime, date
import psutil
from colours import *
from functions import *
import config


def Welcome():
    oled.fill(black)
    # draw_text2("Scicorder", 25, (white), 0, 34)
    draw_text("Pro", 18, blue, 95, 60)

    draw_text("Linux Powered", 13, grey, 23, 95)
    draw_text("Open-Source Scanner", 13, grey, 0, 110)

    draw_text2("Scicorder", 25, def_col_breathe, 0, 34)
    col_change_breathe(def_col_breathe, col_dir_breathe)
    # draw_text("Pro", 18, def_col_breathe3, 95, 60)
    # col_change_breathe(def_col_breathe3, col_dir_breathe)

    refresh()  # must be called to refresh the screen


def copy_to_usb():
    # fetch all files
    y1 = 30
    oled.fill(black)
    draw_text("Copying logs to USB..", 12, white, 0, 0)
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            draw_text(file_name, 12, white, 0, y1)
            y1 += 15
            refresh()
    #refresh()
    pygame.time.wait(3000)
    oled.fill(black)
    draw_text("Backup Complete", 15, green, 0, 64)
    refresh()
    os.system("pumount sda1")
    pygame.time.wait(2000)
    config.mode ='Y'
    Saved()

def Saved():
    oled.fill(black)
    draw_text("USB Unmounted", 13, white, 12, 44)
    draw_text("Please remove USB", 15, green, 0, 64)
    refresh()
    pygame.time.wait(3000)
    config.mode = 'B'

#wifi_status = wifi.status()

def cpu_temperature():
    temp = os.popen("cat /sys/class/hwmon/hwmon0/temp1_input").readline()
    return temp.replace("temp=", " ").replace("'C", "")

def Stats():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    cpu_temp = cpu_temperature()
    res = [int(i) for i in cpu_temp.split() if i.isdigit()]
    ext_temp = round(bme280.get_temperature(), 2)
    mpu_temp = round(mpu.get_temp(), 2)
    
    oled.fill(black)
    draw_text("CPU:", 13, white, 0, 8)                # font size 13 seems to fit well with 20 pixels between lines
    draw_text2(f"{cpu}%", 13, green, 73, 8)
    draw_text("RAM USED:", 13, white, 0, 28)
    draw_text2(f"{memory}%", 13, green, 73, 28)
    draw_text("CPU Temp:", 13, white, 0, 68)
    draw_text2(str(str(res)), 13, green, 73, 68)
    draw_text("Int. Temp:", 13, white, 0, 88)
    draw_text2(f"{mpu_temp}*C", 13, green, 73, 88)
    draw_text("Ext. Temp:", 13, white, 0, 108)
    draw_text2(f"{ext_temp}*C", 13, green, 73, 108)

    #ip = wifi.ip()
    #draw_text("IP: ", 12, white, 0, 98)
    #draw_text2(f"{ip}", 12, green, 48, 98)
    #pygame.time.wait(100)
    refresh()
    #pygame.time.wait(200)


#page = 1
def Info():
    page = 1
    oled.fill(black)    # 16 characters wide at fontsize 14, font3 (NovaMono) in 6 lines (128x128)

    text1 = ["NanoPi-Neo Core",
            "Armbian23 6.1.63",
            "SSD1351 SPI OLED",
            "1200mAh LiPo",
            "Class-D Amp",
            "       V      ",
            ]

    text2 = ["   Hardware:",
             "BME280, MPU6050",
             "TCS34725, SI1145",
             "VL53L0X, HMC588L",
             "LTR390UV, MPR121",
             "TP4056X, 1200mAh",
             ]


    # Up Button
    if GPIO.input(button_1) == GPIO.LOW:
        page -= 1
        if page <=0:
            page = 2
        time.sleep(0.1)

    # Down Button
    if GPIO.input(button_2) == GPIO.LOW:
        page +=1
        if page >=3:
            page = 1
        time.sleep(0.1)

    if page == 1:
        oled.fill(black)
        y1 = 0
        for i in range(len(text1)):
            draw_text3(text1[i], 13, white, 0, y1)     # 16 characters at fontsize 14, font3 (NovaMono)
            y1 += 16  # change to reflect spacing between font prints - check pixel:font chart
        refresh()

    if page == 2:
        oled.fill(black)
        y1 = 0
        for i in range(len(text2)):
            draw_text3(text2[i], 13, white, 0, y1)  # 16 characters at fontsize 14, font3 (NovaMono)
            y1 += 16  # change to reflect spacing between font prints - check pixel:font chart
        refresh()
    refresh()


def Atmos():
    # global mode
    # mode = 'A'
    temperature = round(bme280.get_temperature(), 2)  # round(xxx, 2) limits output to 2sf
    pressure = round(bme280.get_pressure(), 2)
    humidity = round(bme280.get_humidity(), 2)
    mpu_temp = round(mpu.get_temp(), 2)

    oled.fill(black)

    temperature_col = white
    if 2 <= temperature <= 16:
        temperature_col = def_col_breathe3
        # add low temperature arrow warning: ?
    elif 16 <= temperature <= 26:
        temperature_col = green
    elif 26 <= temperature <= 35:
        temperature_col = orange
    elif 35 <= temperature <= 100:
        temperature_col = def_col_breathe4
        # add high temperature arrow warning: ?

    humid_col = white
    if 0 <= humidity <= 41:
        humid_col = def_col_breathe4
        # add low humidity arrow warning: ?
    elif 41 <= humidity <= 59:
        humid_col = green
    elif 59 <= humidity <= 100:
        humid_col = def_col_breathe3
        # add high humidity arrow warning: ?

    press_col = white
    if 800 <= pressure <= 981:
        press_col = def_col_breathe3
        # add low pressure arrow warning: ?
    elif 981 <= pressure <= 1011:
        press_col = green
    elif 1011 <= pressure <= 1100:
        press_col = def_col_breathe4
        # add high pressure arrow warning: ?

    draw_text2("Temp.", 18, white, 0, 8)
    draw_text2(f"{temperature} ", 22, temperature_col, 55, 22)
    draw_text2("Humi.", 18, white, 0, 48)
    draw_text2(f"{humidity} ", 22, humid_col, 55, 62)
    draw_text2("Press.", 18, white, 0, 85)
    draw_text2(f"{pressure} ", 22, press_col, 25, 105)
    col_change_breathe_warn(def_col_breathe3, col_dir_breathe3)
    col_change_breathe_warn(def_col_breathe4, col_dir_breathe4)

    # ~~~~~~~~~~~~~~~~~~~~~~~~ SAVE SENSOR DATA ~~~~~~~~~~~~~~~~~~~~~~~~
    # Find how to put as function to be simply called by button press within each sensor page or in main file as specific button..
    # ENTER/SELECT/OK:
    if GPIO.input(button_3) == GPIO.LOW:
        today = datetime.today()
        now = datetime.now()

        # Open ~/sensorlogs/ & make/append log with today's date as name & date&time as first entry
        #savefile = open("/home/pi/savefile.txt", 'a')    # 'w' for write, 'a' for append, 'r' for read-only
        savefile = open("/home/pi/sensorlogs/log-" + (today.strftime("%d-%m-%y")) + ".txt", 'a')    # 'w' for write, 'a' for append, 'r' for read-only
        savefile.write(today.strftime("%d-%m-%y") + " @ " + now.strftime("%H:%M:%S") + ": ")

        # Change below to match sensor group
        savefile.write("Temp: " + f"{temperature}" + "*C | ")
        savefile.write("Humidity: " + f"{humidity}" + "%RH | ")
        savefile.write("Pressure: " + f"{pressure}" + "hPa | ")

        # Seperate entries with lots of lines
        savefile.write("\n")
        savefile.write("------------------------------------------------------------------------------------")
        savefile.write("\n")
        savefile.close()
        pygame.draw.rect(oled, grey_blue, pygame.Rect(0, 60, 128, 25))
        draw_text2("Data Saved!", 16, black, 15, 64)
        refresh()
        pygame.time.wait(800)
    # Exit/Back/Other:
    if GPIO.input(button_4) == GPIO.LOW:
        a=("Temp: " + f"{temperature}" + "*C | ")
        b=("Humidity: " + f"{humidity}" + "%RH | ")
        c=("Pressure: " + f"{pressure}" + "hPa | ")
        d=("InnerTemp: " + f"{mpu_temp}" + "*C | ")
        save_to_log(a,b,c,d)

    refresh()


def Distance():
    oled.fill(black)
    distance = tof.get_distance()               # mm
    distance_cm = (tof.get_distance()/10)       # cm

    draw_text2("Distance:", 18, white, 0, 8)
    draw_text2(f"{distance} mm", 22, green, 45, 32)
    draw_text2(f"{distance_cm} cm", 22, blue, 45, 62)

    refresh()


def Gyro():
    oled.fill(black)
    accel_data = mpu.get_accel_data()

    accel_x = str(accel_data['x'])

    draw_text2("Acc X : " + accel_x,13, white, 0,0)
    draw_text2("Acc Y : " + str(accel_data['y']),13, white, 0, 15)
    draw_text2("Acc Z : " + str(accel_data['z']),13, white, 0, 30)

    gyro_data = mpu.get_gyro_data()

    draw_text2("Gyro X : " + str(gyro_data['x']),13, white, 0, 65)
    draw_text2("Gyro Y : " + str(gyro_data['y']),13,white,0,80)
    draw_text2("Gyro Z : " + str(gyro_data['z']),13,white,0,95)

    refresh()


def ip():
    ip_i = os.popen("ip r | grep -i src").read()
    ip_i = ip_i.split("src ")[1]
    ip_i = ip_i.split(" metric")[0]
    return ip_i


def Wifi_feed():
    oled.fill(black)

    ip_i = os.popen("ip r | grep -i src").read()
    ip_i = ip_i.split("src ")[1]
    ip_i = ip_i.split(" metric")[0]

    draw_text2("WiFi Sensor Feed:", 18, white, 0, 8)
    draw_text2("Active", 22, green, 10, 32)
    draw_text2(f"{ip_i}", 22, blue, 10, 62)

    # add wifi webserver here

    refresh()

    # EOF
