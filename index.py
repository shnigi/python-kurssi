# -*- coding: utf-8 -*-
import sys
import json
invalid_input = True
tietokanta = "tietokanta.json"

def begin():
    print('Baarikierros softa versio 1.0 \n Syötä numero: \n 0. Apu \n 1. Lisää baarikierros \n 2. Listaa baarikierrokset \n 3. Poista baarikierros \n 4. Lopeta \n')
    start()

def apua():
    print('0. Apu')
    print('1. Lisää baarikierros')
    print('2. Listaa baarikierrokset')
    print('3. Poista baarikierros')
    print('4. Lopeta')
    start()

def exit():
    print('Kiitos ja näkemiin! \n')
    invalid_input = True;
    sys.exit()

def addBaarikierros():
    print('Lisätäänpä baarikierros \n')
    name = input('nimi\n')
    location = input('lokaatio\n')
    time = input('aika\n')
    drinkAmount = input('juomien määrä\n')
    with open(tietokanta, 'w') as json_file:
        data = json.load(json_file)
        data['Baarikierrokset'].append({
            'name': name,
            'location': location,
            'time': time,
            'drinkAmount': drinkAmount
        })
    json.dump(data, json_file)
    print('Kierros lisätty onnistuneesti\n')
    start()

def listBaarikierrokset():
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for kierros in data['Baarikierrokset']:
            print(kierros['name'])
    print('\n')
    start()

def removeBaarikierros():
    print('Mikä kierros poistetaan?')

def start():
    toDo = input('Kuis laitetaa?\n')
    if toDo == '0':
        print('\n')
        apua()
    elif toDo == '1':
        print('\n')
        addBaarikierros()
    elif toDo == '2':
        print('\n')
        listBaarikierrokset()
    elif toDo == '3':
        print('\n')
        removeBaarikierros()
    elif toDo == '4':
        exit()
    else:
        print('Vain numeroita 1-3 pls')

begin()
