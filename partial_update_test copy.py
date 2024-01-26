#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
from PIL import Image,ImageDraw,ImageFont
import keyboard
import time
import signal

#initialize some vars
logging.basicConfig(level=logging.DEBUG)
font18 = ImageFont.truetype('Font.ttc', 11)
text = ""
chars_per_line = 45
lines_on_screen = 25
current_line = 0

def init_display():
    #initialize and clear display
    epd = epd4in2_V2.EPD()
    #logging.info("init and Clear")
    epd.init()
    epd.Clear()
    return epd 

def init_image(epd):
    #logging.info("Draw Image")
    draw_image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    #logging.info("set image object")
    draw = ImageDraw.Draw(draw_image)
    return draw,draw_image

# Not currently working. This method is displaying some of the CLI for some reason. 
def get_input_text(e):
    global text
    text = "init text"
    logging.info("succesfully read a key")
    if e.name == 'enter':
        logging.info("\nKey Pressed:" + e.name)
        e.name += '\n'
    elif key == 'backspace':
        logging.info("\nKey Pressed:" + e.name)
        text = text[:-1]
    elif len(e.name) == 1:  # Check if the key is a character
        logging.info("\nKey Pressed:" + e.name)
        text += e.name
    partial_update_text(text)
    time.sleep(.1)
    return text

def partial_update_text(draw, draw_image,text, epd):
    logging.info("draw text")
    draw.rectangle((0, 0, 400, 300), fill = 255)
    draw.text((0, 0), text, font = font18, fill=0)
    epd.display_Partial(epd.getbuffer(draw_image))

def cleanup(epd):
    # Cleanup and sleep
    epd.init()
    epd.Clear()
    epd.sleep()

# start keyboard listener and callback to get_input_text method
keyboard.on_press(get_input_text, suppress=True) #handles keyboard input
epd = init_display() #initialize the display one time. 
draw, draw_image = init_image(epd)

'''
while True:
    try:
        

    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2_V2.epdconfig.module_exit(cleanup=True)
        cleanup(epd) 
        exit()
'''