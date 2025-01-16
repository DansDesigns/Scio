#
#
#
# ~~~~~~~~~~~~~~~~~~~~ Blank Menu: ~~~~~~~~~~~~~~~~~~~
import time

from screens import *
import config


state = 1

def Menu_device():

    global state

    oled.fill(black)
    options = ["Device Status", "Info", "Gyro", "Backup Data"]

    y1 = 0

    for i in range(len(options)):
        draw_text2(options[i], 15, white, 15, y1)
        y1 += 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21

    # UP:
    if GPIO.input(button_1) == GPIO.LOW:
        GPIO.output(LED_STAT, True)
        cursor_rect.y -= 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21
        state -=1
        if cursor_rect.y < 0:
            cursor_rect.y = 96
        if state < 1:
            state = 4
        time.sleep(0.1)
        GPIO.output(LED_STAT, False)

    # DOWN:
    if GPIO.input(button_2) == GPIO.LOW:
        GPIO.output(LED_STAT, True)
        cursor_rect.y += 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21
        state +=1
        if cursor_rect.y > 98:
            cursor_rect.y = 0
        if state > 4:
            state = 1
        time.sleep(0.1)
        GPIO.output(LED_STAT, False)

    # ENTER/SELECT/OK:
    if GPIO.input(button_3) == GPIO.LOW:
        global mode
        GPIO.output(LED_STAT, True)
        time.sleep(0.1)
        GPIO.output(LED_STAT, False)
        if state == 1:
            state, cursor_rect.y = 1, 0
            config.mode = 'S'
            Stats()
        if state == 2:
            state, cursor_rect.y = 1, 0
            config.mode = 'I'
            Info()
        if state == 3:
            state, cursor_rect.y = 1, 0
            config.mode = 'G'
            Gyro()
        if state == 4:
            state, cursor_rect.y = 1, 0
            config.mode = 'I'
            #Info()
            copy_to_usb()

    # BACK/EXIT:
    if GPIO.input(button_4) == GPIO.LOW:
        GPIO.output(LED_STAT, True)
        time.sleep(0.1)
        GPIO.output(LED_STAT, False)
        config.mode = 'Z'
        state, cursor_rect.y = 1, 0
        Welcome()


    draw_text4(">", 20, def_col_breathe2, cursor_rect.x, cursor_rect.y)
    col_change_breathe(def_col_breathe2, col_dir_breathe2)
    GPIO.output(LED_STAT, False)
    refresh()


# def menu():
#     oled.fill(black)
#     options = ["item1", "item2", "item3", "item4"]
#     y1 = 0
#     global mode
#     global state
#
#     for i in range(len(options)):
#         draw_text3(options[i], 20, white, 20, y1)
#         y1 += 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21
#
#     # UP:
#     if GPIO.input(button_1) == GPIO.LOW:
#         GPIO.output(LED_STAT, True)
#         cursor_rect.y -= 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21
#         state -=1
#         if cursor_rect.y < 0:
#             cursor_rect.y = 96
#         if state < 1:
#             state = 4
#         time.sleep(0.1)
#         GPIO.output(LED_STAT, False)
#
#     # DOWN:
#     if GPIO.input(button_2) == GPIO.LOW:
#         GPIO.output(LED_STAT, True)
#         cursor_rect.y += 32  # 128 / number of menu items = space to move cursor, /4 items = 32, /5 items = 25, /6 items = 21
#         state +=1
#         if cursor_rect.y > 98:
#             cursor_rect.y = 0
#         if state > 4:
#             state = 1
#         time.sleep(0.1)
#         GPIO.output(LED_STAT, False)
#
#     # ENTER/SELECT/OK:
#     if GPIO.input(button_3) == GPIO.LOW:
#         GPIO.output(LED_STAT, True)
#         time.sleep(0.1)
#         GPIO.output(LED_STAT, False)
#         if state == 1:
#             state, cursor_rect.y = 0, 0
#             mode = 'A'
#             #function to enable..
#         if state == 2:
#             state, cursor_rect.y = 0, 0
#             mode = 'A'
#             #function to enable..
#         if state == 3:
#             state, cursor_rect.y = 0, 0
#             mode = 'A'
#             #function to enable..
#         if state == 4:
#             state, cursor_rect.y = 0, 0
#             mode = 'A'
#             #function to enable..
#
#     # BACK/EXIT:
#     if GPIO.input(button_4) == GPIO.LOW:
#         GPIO.output(LED_STAT, True)
#         mode = 'Z'
#         state, cursor_rect.y = 0, 0
#         time.sleep(0.1)
#         GPIO.output(LED_STAT, False)
#         welcome()
#
#
#     draw_text4(">", 20, def_col_breathe2, cursor_rect.x, cursor_rect.y)
#     col_change_breathe(def_col_breathe2, col_dir_breathe2)
#     GPIO.output(LED_STAT, False)
#     refresh()


