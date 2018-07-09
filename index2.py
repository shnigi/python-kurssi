# -*- coding: utf-8 -*-
import sys
import json
invalid_input = True
tietokanta = "tietokanta.json"

def apua():
    print('0. Apu')
    print('1. Lisää baarikierros')
    print('2. Listaa baarikierrokset')
    print('3. Poista baarikierros')
    print('4. Lopeta')

def exit():
    print('Kiitos ja näkemiin!')
    invalid_input = True;
    sys.exit()

def addBaarikierros():
    print('Lisätäänpä baarikierros')

def listBaarikierrokset():
    print('Baarikierrokset')
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for kierros in data['Baarikierrokset']:
            print('Nimi: ' + kierros['name'])

def removeBaarikierros():
    print('Mikä kierros poistetaan?')

def start():
    toDo = input('Kuis laitetaa? 0 = help\n')
    if toDo == '0':
        apua()

    elif toDo == '1':
        invalid_input = False
        addBaarikierros()

    elif toDo == '2':
        invalid_input = False
        listBaarikierrokset()

    elif toDo == '3':
        invalid_input = False
        removeBaarikierros()

    elif toDo == '4':
        exit()

    else:
        invalid_input = False
        print('Vain numeroita 1-3 pls')

while invalid_input:
    start()
