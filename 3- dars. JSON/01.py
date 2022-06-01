import json
import re
file_name = "moshinalar"

def write(obj):
    text = json.dumps(obj, indent=4)
    with open(file_name, "w") as file:
        file.write(text)

def read():
    with open(file_name, "r") as file:
        text = file.read()
    if text:
       obj = json.loads(text)
       return obj
    else:
       return []

def kiritish():
    model = input("Modelini kiriting: ")
    rangi = input("Rangini kiriting: ")
    yili  = input("Yilini kiriting: ")
    moshina = {
        "modeli": model,
        "rangi": rangi,
        "yili": yili
    }
    moshinalar = read()
    moshinalar.append(moshina)
    write(moshinalar)

def view():
     moshinalar = read()
     i = 0
     for m in moshinalar:
         i+=1
         print(f"{i}"
               f"{m['modeli'].center(10)}"
               f"{m['rangi'].center(10)}"
               f"{m['yili']}"
               )

def delete():
    moshinalar = read()
    view()
    print('  ')
    choice = int(input("Qaysi moshinani ochirmoqchisiz?: ")) - 1
    if 0 <= choice < len(moshinalar):
       moshinalar.pop(choice)
    write(moshinalar)


def change():
    moshinalar = read()
    view()
    choice = int(input("Qaysi moshinani ozgartirmoqchisiz?: "))-1
    if 0<=choice< len(moshinalar) :

        print(moshinalar)
        vibor =int(input("Nimasini ozgartirmoqchisiz? (1 - modelini, 2 - rangini, 3 - yilini): "))
        if vibor == 1:
           moshinalar[choice]["modeli"] = input("Modelini kiriting")
        if vibor == 2:
           moshinalar[choice]["rangi"] = input("Rangini kiriting:")

        if vibor == 3:
           moshinalar[choice]["yilini"] = input("Yilini kiriting")
        write(moshinalar)

def search():
    moshinalar = read()
    txt = "malibu"
    r = re.findall(txt,moshinalar)
    print(r)



def menu():
    first = True
    while True:
        if first:
            tanlov = input(""" Menu:
            1. Kiritish
            2. Korish
            3. Ozgartirish
            4. Ochirish
            5. Qidirish
            6. Chiqish\n""")
            first = False
        else:
            tanlov = input("Error boshqattan kiriting: ")
        if tanlov.isdigit() and int(tanlov) in range(1,7):
            return int(tanlov)



if __name__ == "__main__":
    while True:
        tanlov = menu()
        if tanlov == 1:
            kiritish()
        elif tanlov == 2:
            view()
        elif tanlov == 3:
            change()
        elif tanlov == 4:
            delete()
        elif tanlov == 5:
            search()
        elif tanlov == 6:
            break