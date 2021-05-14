#Ejercicio 1.

import json
import requests
import random

def get_carter_by_id(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic


def get_random_character():
    randomCharacterId = random.randrange(1, 82, 2)
    character = get_carter_by_id(randomCharacterId)
    return character

def main():
    char1 = get_random_character()
    char2 = get_random_character()
    tallestCharacter = char1 if char1['height'] > char2['height'] else char2
    heaviestCharacter = char1 if char1['mass'] > char2['mass'] else char2
    beenInMoreMovies = char1 if len(char1['films']) > len(char2['films']) else char2

    print(str(char1['name']) + ' vs ' + str(char2['name']))
    print('El mas alto es: ' + str(tallestCharacter.get('name')))
    print('El mas pesado es: ' + str(heaviestCharacter.get('name')))
    print('El que estuvo en mas peliculas es: ' + str(beenInMoreMovies.get('name')))
    
    if char1['name'].find('Yoda') > -1 or char2['name'].find('Yoda') > -1:
      print('Yoda esta entre los personajes')

    if char1['name'].find('Grievous') > -1 or char2['name'].find('Grievous') > -1:
      print('Yoda esta entre los personajes')

main()


# #Ejercicio 3

from random import randint
lista = []

for i in range (0,79):
    digito1 = randint(1,794)
    lista.append(digito1)

lista.sort()

print ("El menor es ",lista[0])
print ("El mayor es ",lista[78])

print(lista)
for lista in range (0,78):
    if (lista % 2==0):
        print(lista)