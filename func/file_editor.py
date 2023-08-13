import os

def add_file(name, type_file):
    path = directory()
    text_file = open(f"{path}\\{name}.{type_file}", "w")

def directory():
    print("Текущая деректория:", os.getcwd())
    return os.getcwd()

def get_user():
    pass

#if not os.path.isdir("folder"):
#     os.mkdir("folder")
#text_file.write("Это текстовый файл")
