#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
import time
from PIL import Image,ImageDraw,ImageFont
import keyboard 

logging.basicConfig(level=logging.DEBUG)
logging.info("set font object")
font18 = ImageFont.truetype('Font.ttc', 18)

def init_display():
    logging.info("epd4in2 Demo")
    
    epd = epd4in2_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    return epd

def init_image(epd):
    logging.info("Draw Image")
    draw_image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    
    logging.info("set image object")
    draw = ImageDraw.Draw(draw_image)
    return draw,draw_image

def display_image(draw, draw_image, epd):
    logging.info("Keyboard input...")
    text = ""
    while True:
        if keyboard.is_pressed('esc'):
            break  # Exit on pressing Escape key
        if keyboard.read_key():
            key = keyboard.read_key()
            if key == 'space':
                key = ' '  # Replace 'space' with a space character
            text += key
            draw.rectangle((0, 0, 300, 30), fill=255)  # Adjust as needed
            draw.text((10, 10), text, font=font18, fill=0)
            epd.display_Partial(epd.getbuffer(draw_image))
            time.sleep(0.1)  # Adjust as needed for responsiveness

def cleanup(epd):
    # Cleanup and sleep
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()


try:
    epd = init_display()
    draw, draw_image = init_image(epd)
    display_image(draw, draw_image, epd)
    cleanup(epd)  

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2_V2.epdconfig.module_exit(cleanup=True)
    exit()