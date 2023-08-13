import pyaudio as au
import sys
import wave
import pandas as pd
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import sqlite3

from channel import micro
from func import power_off
from func import file_editor
from db import DB

def FindPhrase(Phrase, DB):
    commandID = -1
    fzMaxPer = 70
    for i in range(len(DB)):
        fz = fuzz.partial_ratio(Phrase, DB[i][1]) 
        if fz > fzMaxPer > DB[i][2]:
            fzPer = fz
            fzMaxPer = fz
            commandID = i
        print(fz)
    return DB[commandID][0]

def OpenFunc(func, name = 'defoult'):
    match func:
        case 'screen_shot_full':
            power_off.screen_full()
        case 'pc_off':
            print('выключаю')
            power_off.powerOff(0)
        case 'add_txt_file_desk':
            file_editor.add_file(name, 'txt')  
