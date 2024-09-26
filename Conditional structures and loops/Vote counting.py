'''
This program stores information about elections in a database.
It allows you to store the candidates, the votes,
the number of votes received by each one,
show the list of candidates and votes, show the winning candidate and
show the percentage of votes that each candidate received.
'''

#Creating database
votaciones = {}
continuar = True
i = 0

#Adding candidates
while continuar:
    opcion = input('1. Introducir candidatos.\n2. Modificar votos de algún candidato.\n3. Mostrar candidatos.\n4. Mostrar ganador.\n5. Mostrar porcentaje de votos.\n6. Salir.\n----------\nIntroduzca un número del 1 al 6: ')
    if opcion == '1':
        votaciones['candidato' + str(i+1)] = {'nombre': input('Introduzca el nombre del candidato: '), 'votos': int(input('Introduzca la cantidad de votos: '))}
        i +=1
        print('-----------')
        print('Candidato añadido con éxito.')
        print('-----------')

  #Modifying votes
    elif opcion == '2':
        nombre = input('Selecciones el candidato al que desea modificar sus votos: ')
        votos = int(input('Introduzca la nueva cantidad de votos: '))
        for candidato, info_candidato in votaciones.items():
            if nombre == info_candidato['nombre']:
                info_candidato['votos'] = votos
        print('-----------')
        print('Votos actualizados con éxito.')
        print('-----------')

#Showing candidates
      elif opcion == '3':
        for datos in votaciones:
            print('-----------')
            print(f"{datos}\n\tNombre: {votaciones[datos]['nombre']}\n\tVotos: {votaciones[datos]['votos']}" )
            print('-----------')

#Showing winner
        elif opcion == '4':
        ganador = 0
        candidato_ganador = ''
        for datos in votaciones.values():
            if datos['votos'] > ganador:
                ganador = datos['votos']
                candidato_ganador = datos['nombre']
        print('-----------')        
        print(f'El candidato más votado es: {candidato_ganador}')
        print('-----------')
            

#Showing percentage of votes
    elif opcion == '5':
        total_votos = 0
        porcentaje = 0
        for datos in votaciones.values():
            total_votos += datos['votos']
       
        for datos in votaciones.values():
            porcentaje = 100 / (total_votos / datos['votos'])
            print('-----------')
            print(f"El candidato {datos['nombre']} obtuvo un {porcentaje:.2f} % de los votos")
            print('-----------')

#Exiting the program
    elif opcion == '6':
        continuar = False
        print('-----------')
        print('Saliendo del programa.')
#controlling errors
    else:
        print('La opción seleccionada no es válida. Introduzca 1, 2, 3, 4, 5 ó 6.')
        print('-----------')
