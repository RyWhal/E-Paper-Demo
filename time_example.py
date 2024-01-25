#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)




try:
    logging.info("epd4in2 Demo")
    
    epd = epd4in2_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    logging.info("set font object")
    font18 = ImageFont.truetype('Font.ttc', 18)

    logging.info("Draw Image")
    draw_image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    
    logging.info("set image object")
    draw = ImageDraw.Draw(draw_image)

    logging.info("show time...")
    num = 0
    while (True):
        draw.rectangle((140, 80, 240, 105), fill = 255)
        draw.text((140, 80), time.strftime('%H:%M:%S'), font = font18, fill = 0)
        epd.display_Partial(epd.getbuffer(draw_image))
        num = num + 1
        time.sleep(0.5)
        if(num == 20):
            break

    # Cleanup and sleep
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2_V2.epdconfig.module_exit(cleanup=True)
    exit()