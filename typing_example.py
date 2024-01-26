#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
from PIL import Image,ImageDraw,ImageFont
import keyboard
import time
import signal

logging.basicConfig(level=logging.DEBUG)
logging.info("epd4in2 Demo")

logging.info("set font object")
font18 = ImageFont.truetype('Font.ttc', 18)

text = ""

#Startup keyboard ---


def init_display():
    #initialize and clear display
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

'''
def on_key_press(key, draw, epd, current_text):
    try:
        if key == keyboard.Key.enter:
            current_text += '\n'
        elif key == keyboard.Key.backspace:
            current_text = current_text[:-1]
        elif hasattr(key, 'char') and key.char:
            current_text += key.char

        draw.rectangle((0, 0, 300, 30), fill=255)
        draw.text((10, 10), current_text, font=font18, fill=0)
        epd.display_Partial(epd.getbuffer(draw))
    except Exception as e:
        logging.error("Error in on_key_press: " + str(e))

def capture_and_display_input(draw, epd):
    current_text = "Initialization text"
    listener = keyboard.Listener(on_press=lambda key: on_key_press(key, draw, epd, current_text))
    listener.start()
    listener.join()
'''

# Not currently working. This method is displaying some of the CLI for some reason. 
def get_input_text(e):
    logging.info("Enter display_image()")
    global text
    #while True:
    #logging.info("enter display_image while loop")
    #key_event = keyboard.read_event()
    #if key_event.event_type == keyboard.KEY_DOWN:
    #key = key_event.name
    key = e.name
    logging.info("succesfully read a key")
    if key == 'enter':
        logging.info("\nKey Pressed:" + e.name)
        text += '\n'
    elif key == 'backspace':
        logging.info("\nKey Pressed:" + e.name)
        text = text[:-1]
    elif len(key) == 1:  # Check if the key is a character
        logging.info("\nKey Pressed:" + e.name)
        text += e.name
    time.sleep(.05)
    return text

def partial_update_text(draw, draw_image,text, epd):
    logging.info("draw text")
    draw.rectangle((0, 0, 300, 30), fill=255)
    draw.text((10, 10), text, font=font18, fill=0)
    epd.display_Partial(epd.getbuffer(draw_image))

def cleanup(epd):
    # Cleanup and sleep
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()

keyboard.on_press(get_input_text, suppress=True) #handles keyboard input
epd = init_display()
draw, draw_image = init_image(epd)

while True:
    try:
        partial_update_text(draw, draw_image, text, epd)
        time.sleep(1)
        #capture_and_display_input(draw,epd) 

    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2_V2.epdconfig.module_exit(cleanup=True)
        cleanup(epd) 
        exit()