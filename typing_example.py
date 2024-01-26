#!/usr/bin/python
import os
import logging
from waveshare_epd import epd4in2_V2
from PIL import Image,ImageDraw,ImageFont
import keyboard
import time

class text_partial_update:
    def __init__(self):
        #initialize some vars
        logging.basicConfig(level=logging.DEBUG)
        self.font18 = ImageFont.truetype('Font.ttc', 11)
        self.text = ""

    def init_display(self):
        #initialize and clear display
        self.epd = epd4in2_V2.EPD()
        logging.info("init and Clear")
        self.epd.init()
        self.epd.Clear()
        #return epd 

    def init_image(self):
        logging.info("Draw Image")
        self.draw_image = Image.new('1', (self.epd.width, self.epd.height), 255)  # 255: clear the frame
        #logging.info("set image object")
        self.draw = ImageDraw.Draw(self.draw_image)
        #return draw,draw_image

    # Not currently working. This method is displaying some of the CLI for some reason. 
    def get_input_text(self,e):
        self.text = "init text"
        logging.info("succesfully read a key")
        if e.name == 'enter':
            logging.info("\nKey Pressed:" + e.name)
            e.name += '\n'
        elif key == 'backspace':
            logging.info("\nKey Pressed:" + e.name)
            self.text = self.text[:-1]
        elif len(e.name) == 1:  # Check if the key is a character
            logging.info("\nKey Pressed:" + e.name)
            self.text += e.name
        time.sleep(.1)

    def partial_update_text(self, text):
        logging.info("draw text")
        self.draw.rectangle((140, 80, 240, 105), fill = 255)
        self.draw.text((140, 80), text, font = self.font18, fill=0)
        self.epd.display_Partial(self.epd.getbuffer(self.draw_image))

    def cleanup(self):
        # Cleanup and sleep
        self.epd.init()
        self.epd.Clear()
        self.epd.sleep()

class run(text_partial_update):
    def main(self):
        logging.info("starting main")
        # start keyboard listener and callback to get_input_text method
        keyboard.on_press(self.get_input_text, suppress=True) #handles keyboard input
        epd = self.init_display() #initialize the display one time. 
        self.draw, self.draw_image = self.init_image(epd)

        while True:
            logging.info("entering main while loop")
            try:
                self.partial_update_text()
                time.sleep(6)
                #capture_and_display_input(draw,epd) 

            except IOError as e:
                logging.info(e)
                
            except KeyboardInterrupt:    
                logging.info("ctrl + c:")
                epd4in2_V2.epdconfig.module_exit(cleanup=True)
                self.cleanup(self.epd) 
                exit()

