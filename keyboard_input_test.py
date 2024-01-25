#!/usr/bin/python
import logging
import keyboard
import time

def on_key_event(e):
    print(f"Key: {e.name}")

keyboard.on_press(on_key_event)

print("Listening for keypresses... Press Ctrl+C to stop.")
try:
    keyboard.wait()
except KeyboardInterrupt:
    print("Stopped listening for keypresses.")

