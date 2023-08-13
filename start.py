import pyaudio as au
import sys
import wave
import pandas as pd
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import sqlite3
from Visual import *
from FF import *
from db import DB

DBph = DB.DB_read()

phrase = micro.record_volume()
print(DBph)
funcName = FindPhrase(phrase, DBph)
print('результат', funcName)
OpenFunc(funcName)


#a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
#print(fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир'))
#city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
#a = process.extractOne("Краногрск", city)
#os.listdir('C:\\Users\\hartp\\Desktop\\')

#https://waksoft.susu.ru/2021/05/20/kak-vosproizvodit-i-zapisyvat-audio-na-python/
