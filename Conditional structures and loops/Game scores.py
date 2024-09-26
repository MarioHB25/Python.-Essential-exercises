'''
This program allows you to track scores in a game,
as well as store player names and scores in a database.
It also shows the high score, the average score and
the names and scores of each participating player.
'''

#Creating the database
juego = {}
continuar = True

#Entering player names and scores. Storing the data
while continuar:
    nombre = input("Introduzca un jugador (ó si no hay más jugadores introduzca 'salir'): ")
    if nombre.lower() == 'salir':
        continuar = False
    else:
        puntos = int(input("Introduzca la puntuación: "))
        juego[nombre] = puntos
    print('----------')    
    print(f'Participantes:\n {juego}')
    print('----------')

#Showing the highest score
    max_puntos = max(juego, key= juego.get)
    print(f'El/La jugador/a con mayor puntuación es: {max_puntos}')
    print('----------')

#Showing the measured score
    media_puntos = sum(juego.values()) / len(juego)
    print(f'La puntuación media es: {media_puntos}')
    print('----------')

#Showing the players and their scores
    print(f'La cantidad de jugadores es: {len(juego)}')
    print('----------')
