import pyaudio as au
import sys
import wave
import pandas as pd
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import sqlite3

from channel import micro
from func import power_off
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

def OpenFunc(func):
    match func:
        case 'screen_shot_full':
            print('1')
        case 'pc_off':
            print('выключаю')
            power_off.powerOff(0)
        
