import pyaudio as au
import sys
import wave
import pandas as pd
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import sqlite3

def DB_read():
    connect = sqlite3.connect('db/DBnanachi.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM inputDB")
    resDB = cursor.fetchall()
    connect.close()
    return resDB

#cursor.execute("INSERT INTO <table_name> (id, name, surname, birthdate) VALUES (2, 'Petr', 'Ivanov', '2003-12-13') ")
#connect.commit()
