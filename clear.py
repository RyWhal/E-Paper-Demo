#!/usr/bin/python
import logging
from waveshare_epd import epd4in2_V2
import time
from PIL import Image,ImageDraw,ImageFont

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

def cleanup(epd):
    # Cleanup and sleep
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()


try:
    epd = init_display()
    cleanup(epd)  

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2_V2.epdconfig.module_exit(cleanup=True)
    exit()