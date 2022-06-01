import os
import pyinputplus as plus
import  shutil

def korish():
    print(os.listdir())

def copy():
    shutil.copy("test.txt", "copyed file")

def delete():
    os.remove(input("Ochirmoqchi bolgan faylningizni nomini yozing: "))

def new_papka():
    os.mkdir(input("Papkani nomini yozing:"))

def new_file():
    with open(input("Faylga nom bering: "), "x"): pass

while True:
    menu = plus.inputInt("""    1. Ko'rish
    2. Ko'chirish
    3. O'chirish
    4. Yangi papkani ochish
    5. Yangi fayl ochish
    6. Chiqish\n""")
    if menu == 1:
        korish()
    elif menu == 2:
        copy()
    elif menu == 3:
        delete()
    elif menu == 4:
        new_papka()
    elif menu == 5:
        new_file()
    elif menu == 6:
        break