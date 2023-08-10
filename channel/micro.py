import pyaudio as au
import sys
import wave
import pandas as pd
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import sqlite3

def record_volume():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        print('слушаю...')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
    except:
        quety = ""
        print('вы молчали')
    print(f'Вы сказали: {query.lower()}')
    return query
