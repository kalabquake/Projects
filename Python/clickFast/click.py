import keyboard
import mouse
import time
import sys


time.sleep(5)

while True:
    mouse.click('left')
    if(keyboard.is_pressed('ctrl')):
        sys.exit()
    #time.sleep(0.0000001)
