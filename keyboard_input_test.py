#!/usr/bin/python
import logging
import keyboard
import time

logging.basicConfig(level=logging.DEBUG)
text = ""

def get_input_text(e):
    global text
    #while True:
    #logging.info("enter display_image while loop")
    #key_event = keyboard.read_event()
    #if key_event.event_type == keyboard.KEY_DOWN:
    #key = key_event.name
    key = e.name
    print(e.name)
    if key == 'enter':
        text += '\n'
    elif key == 'backspace':
        text = text[:-1]
    elif len(key) == 1:  # Check if the key is a character
        logging.info("key pressed" + key)
        text += e.name
    time.sleep(.05)
    return text

print("start the keyboard listener")
keyboard.on_press(get_input_text, suppress=True) #handles keyboard input

while True:
    print("top of the loop")
    print(text)
    time.sleep(5)

