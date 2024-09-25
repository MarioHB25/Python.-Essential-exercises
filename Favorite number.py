'''
This program shows the user's favorite number if it is stored, if not it first asks for it and then saves it.
'''

import json

#Search favorite number function
def comprobar_num_fav():
    try:
        with open('Número favorito.json', 'r') as file:
            num_fav = json.load(file)
            return num_fav
    except FileNotFoundError:
        return None

#Save favorite number function
def guardar_num_fav(numero_favorito):
    with open('Número favorito.json', 'w') as file:
        json.dump(numero_favorito, file)

#Ask favorite number function
def preguntar_num_fav():
    num_fav = int(input('Introduce tu número favorito: '))
    guardar_num_fav(num_fav)
    return(num_fav)

#Write favorite number function
def imprimir_num_fav(numero_favorito):
    print(f'Se cuál es tu núemro favorito... Es: {numero_favorito}')

numero_favorito = comprobar_num_fav()

if numero_favorito:
    imprimir_num_fav(numero_favorito)
else:
    numero_favorito = preguntar_num_fav()
    imprimir_num_fav(numero_favorito)
