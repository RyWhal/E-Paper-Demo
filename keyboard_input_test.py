#!/usr/bin/python
import logging
import keyboard
import time

logging.basicConfig(level=logging.DEBUG)
text = ""

def get_input_text(e):
    global text
    text += e.name
    time.sleep(.05)
    return text

print("start the keyboard listener")
keyboard.on_press(get_input_text, suppress=True) #handles keyboard input

while True:
    print("Text is:"+text)
    time.sleep(5)

