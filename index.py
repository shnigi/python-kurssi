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
    print('4. Lopeta\n')
    start()

def exit():
    print('Kiitos ja näkemiin! \n')
    invalid_input = True;
    sys.exit()

def addBaarikierros():
    print('Lisätäänpä baarikierros \n')
    name = input('Kierroksen nimi:\n')
    location = input('Kierroksen lokaatio: \n')
    time = input('Aika tunteina:\n')
    drinkAmount = input('juomien määrä tölkeissä:\n')
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        data['Baarikierrokset'].append({
            'name': name,
            'location': location,
            'time': time,
            'drinkAmount': drinkAmount
        })
    with open(tietokanta, 'w') as f:
        json.dump(data, f)
    print('Kierros lisätty onnistuneesti\n')
    start()

def listOnly():
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for index, kierros in enumerate(data['Baarikierrokset']):
            print(index, kierros['name'])
    print('\n')

def listBaarikierrokset():
    listOnly()
    start()

def removeBaarikierros():
    print('Kierrokset:\n')
    listOnly()
    index = int(input('Mikä kierros poistetaan? Anna numero.\n'))
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        del data['Baarikierrokset'][index]
    with open(tietokanta, 'w') as f:
        json.dump(data, f)
    print('Poistettu onnistuneesti.\n')
    start()

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
