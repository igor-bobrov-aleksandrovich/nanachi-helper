import os

def powerOff(time = 0):
    os.system('shutdown -s')

import pyautogui

def screen_full():
    pyautogui.screenshot('screens/screenshot.png')
