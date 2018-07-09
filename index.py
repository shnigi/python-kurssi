# -*- coding: utf-8 -*-
import sys
import json

def apua():
    print('0. Apu')
    print('1. Lisää baarikierros')
    print('2. Listaa baarikierrokset')
    print('3. Poista baarikierros')
    print('4. Muokkaa kierrosta')
    print('5. Lopeta\n')

def exit():
    print('Kiitos ja näkemiin!')
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

def listBaarikierrokset():
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for index, kierros in enumerate(data['Baarikierrokset']):
            print(index, kierros['name'])
            print('  ', 'Lokaatio:', kierros['location'])
            print('  ', 'Aika:', kierros['time'])
            print('  ', 'Juomien määrä:', kierros['drinkAmount'])
    print('\n')

def removeBaarikierros():
    print('Poista kierros:\n')
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for index, kierros in enumerate(data['Baarikierrokset']):
            print(index, kierros['name'])
    print('\n')
    index = int(input('Mikä kierros poistetaan? Anna numero.\n'))
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        del data['Baarikierrokset'][index]
    with open(tietokanta, 'w') as f:
        json.dump(data, f)
    print('Poistettu onnistuneesti.\n')

def editKierros():
    print('Muokkaa kierrosta:\n')
    with open(tietokanta) as json_file:
        data = json.load(json_file)
        for index, kierros in enumerate(data['Baarikierrokset']):
            print(index, kierros['name'])
    print('\n')
    index = int(input('Mitä kierrosta muokataan? Anna numero.\n'))
    print(data['Baarikierrokset'][index]['name'])
    name = input('uusi nimi kierrokselle:') or data['Baarikierrokset'][index]['name']
    print(data['Baarikierrokset'][index]['location'])
    location = input('uusi lokaatio kierrokselle:') or data['Baarikierrokset'][index]['location']
    print(data['Baarikierrokset'][index]['time'])
    time = input('uusi aika kierrokselle:') or data['Baarikierrokset'][index]['time']
    print(data['Baarikierrokset'][index]['drinkAmount'])
    drinkAmount = input('Juomien määrä kierrokselle:') or data['Baarikierrokset'][index]['drinkAmount']
    data['Baarikierrokset'][index]['name'] = name
    data['Baarikierrokset'][index]['location'] = location
    data['Baarikierrokset'][index]['time'] = time
    data['Baarikierrokset'][index]['drinkAmount'] = drinkAmount
    with open(tietokanta, 'w') as f:
        json.dump(data, f)
    print('Muokattu onnistuneesti.\n')

def FileCheck(fn):
    global tietokanta
    dbName = fn + ".json"
    try:
      open(dbName, "r")
      tietokanta = dbName
      return
    except IOError:
      print("Tietokantaa ei ole vielä luotu. Luodaan uusi.")
      dbName = fn + ".json"
      f = open(dbName, "w+")
      with open(dbName, "a") as database:
          database.write('{"Baarikierrokset": []}')
      tietokanta = dbName
      print("Tietokanta luotu onnistuneesti.")
      return

def start():
    while True:
        toDo = input('Kuis laitetaa? Syötä numero:\n')
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
            editKierros()
        elif toDo == '5':
            exit()
        else:
            print('Vain numeroita 1-3 pls')

dbName = input('Syötä tietokannan nimi (jos ei löydy luodaan uusi):\n')
FileCheck(dbName)
print('Baarikierros softa versio 1.0 \n 0. Apu \n 1. Lisää baarikierros \n 2. Listaa baarikierrokset \n 3. Poista baarikierros \n 4. Muokkaa kierrosta \n 5. Lopeta \n')
start()
