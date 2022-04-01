import os
from pynput.keyboard import key, Controller
import time

os.system('notepad.exe')
time.sleep(3)
keyboard = Controller()
keyboard.type('Hello world')