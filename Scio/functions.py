#
#
#

from datetime import datetime, date
from colours import *
from config import *

# ~~~~~~~~~~~ Function Definitions: ~~~~~~~~~~~

def refresh():  # refresh or update oled display frame buffer
    # GPIO.output(LED_STAT, True)
    fd = open("/dev/fb0", "wb")  # open, write binary
    fd.write(oled.convert(bpp, 0).get_buffer())  # convert & write to screen
    fd.close()  # close file
   # print(" ")  # refresh screen by printing a space on console.. without this cpu usage is >60%! & oled doesnt update
    clock.tick(60)
    #pygame.display.flip()
    # GPIO.output(LED_STAT,False)


def save_to_log(a,b,c,d):
    today = datetime.today()
    now = datetime.now()

    # Open ~/sensorlogs/ & make/append log with today's date as name & date&time as first entry
    # savefile = open("/home/pi/savefile.txt", 'a')    # 'w' for write, 'a' for append, 'r' for read-only
    savefile = open("/home/pi/sensorlogs/log-" + (today.strftime("%d-%m-%y")) + ".txt", 'a')  # 'w' for write, 'a' for append, 'r' for read-only
    savefile.write(today.strftime("%d-%m-%y") + " @ " + now.strftime("%H:%M:%S") + " | ")

    # Change below to match sensor group
    savefile.write(a)
    savefile.write(b)
    savefile.write(c)
    savefile.write(d)

    # Seperate entries with lots of lines
    savefile.write("\n")
    savefile.write("------------------------------------------------------------------------------------")
    savefile.write("\n")
    savefile.close()
    pygame.draw.rect(oled, grey_blue, pygame.Rect(0, 60, 128, 25))
    draw_text2("Data Saved!", 16, black, 15, 64)
    refresh()
    pygame.time.wait(900)

def draw_text(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    font_type = "/home/pi/fonts/Ubuntu-L.ttf"
    font_object = pygame.font.Font(font_type, size)
    text_surface = font_object.render(text, True, col)  # text, Antialiasing, colour
    oled.blit(text_surface, (x, y))


def draw_text2(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    font_type2 = "/home/pi/fonts/Comfortaa.ttf"
    font_object2 = pygame.font.Font(font_type2, size)
    text_surface2 = font_object2.render(text, True, col)  # text, Antialiasing, colour
    oled.blit(text_surface2, (x, y))

# Mono Font
def draw_text3(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    font_type3 = "/home/pi/fonts/NovaMono.ttf"
    font_object3 = pygame.font.Font(font_type3, size)
    text_surface3 = font_object3.render(text, True, col)  # text, Antialiasing, colour
    oled.blit(text_surface3, (x, y))


def draw_text4(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    #font_type4 = "/home/pi/fonts/WhipsmartBold-genp.ttf"
    font_type4 = "/home/pi/fonts/Whipsmart-XMvZ.ttf"
    font_object4 = pygame.font.Font(font_type4, size)
    text_surface4 = font_object4.render(text, True, col)  # text, Antialiasing, colour
    oled.blit(text_surface4, (x, y))


def col_change_breathe(color: list, direction: list) -> None:
    """
    This function changes an RGB list in a way that we achieve nice breathing effect.
    :param color: List of RGB values.
    :param direction: List of color change direction values (-1, 0, or 1).
    :return: None
    """
    for i in range(3):
        color[i] += col_spd * direction[i]
        if color[i] >= maximum or color[i] <= minimum:
            direction[i] *= -1
        if color[i] >= maximum:
            color[i] = maximum
        elif color[i] <= minimum:
            color[i] = minimum


def col_change_breathe_warn(color: list, direction: list) -> None:
    """
    This function changes an RGB list in a way that we achieve nice breathing effect.
    :param color: List of RGB values.
    :param direction: List of color change direction values (-1, 0, or 1).
    :return: None
    """
    for i in range(3):
        color[i] += col_spd_warn * direction[i]
        if color[i] >= maximum or color[i] <= minimum:
            direction[i] *= -1
        if color[i] >= maximum:
            color[i] = maximum
        elif color[i] <= minimum:
            color[i] = minimum


# def draw_arc():
# pygame.draw.arc(oled, colour, [x, y, width, height], start angle in radians, end angle in radians, line width)
# pygame.draw.arc(oled, colour, [x, y, width, height], pi/2, pi, 2)
