#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
from PIL import Image,ImageDraw,ImageFont
from pynput import keyboard
#import keyboard

logging.basicConfig(level=logging.DEBUG)
logging.info("epd4in2 Demo")

logging.info("set font object")
font18 = ImageFont.truetype('Font.ttc', 12)

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
def display_image(draw, draw_image, epd):
    logging.info("Keyboard input...")
    text = "Startup Text"
    draw.text((10, 10), text, font=font18, fill=0)
    epd.display_Partial(epd.getbuffer(draw_image))

    while True:
        if keyboard.is_pressed('esc'):
            break  # Exit on pressing Escape key
        if keyboard.read_key():
            key = keyboard.read_key()
            if key == 'space':
                key = ' '  # Replace 'space' with a space character
            elif key == 'a':
                key = 'a'
            text += key
            draw.rectangle((0, 0, 400, 300), fill=255)  # Adjust as needed
            draw.text((10, 10), text, font=font18, fill=0)
            epd.display_Partial(epd.getbuffer(draw_image))
            time.sleep(0.1)  # Adjust as needed for responsiveness
    '''

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
    #display_image(draw, draw_image, epd)
    capture_and_display_input(draw,epd)
    cleanup(epd)  

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2_V2.epdconfig.module_exit(cleanup=True)
    exit()