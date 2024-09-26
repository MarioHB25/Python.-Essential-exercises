'''
This program allows you to manage user reservations in an airline company.
The program allows you to add passengers and the reasons why they are traveling and
calculates if the flight reservation is available
'''
#This class uses flight data
class Vuelo:
    def __init__(self, num_vuelo, origen, destino, capacidad):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.lista_pasajeros = []

#This function calculates the available seats
    def asientos_disponibles(self):
        return(self.capacidad - len(self.lista_pasajeros))

#This function adds the passenger if there are seats available
    def agrgar_pasajero(self, nombre_pasajero):
        if self.asientos_disponibles() > 0:
            self.lista_pasajeros.append(nombre_pasajero)
            print(f'El pasajero {nombre_pasajero} ha sido agregado al vuelo {self.num_vuelo}.')
            print(f'Quedan {self.asientos_disponibles()} asientos disponibles en este vuelo.')
        else:
            print('No hay asientos disponibles en este vuelo.')

#Creation of the class that determines the characteristics of the flight
class VueloEspecial(Vuelo):
    def __init__(self, num_vuelo, origen, destino, capacidad):
        super().__init__(num_vuelo, origen, destino, capacidad)

#This function adds the reason for the trip
    def motivo_viaje(self, motivo):
        for pasajero in self.lista_pasajeros:
            print(f'El pasajero {pasajero} viaja por motivos de {motivo}.')

#Example of use
vuelo1 = VueloEspecial(2222, 'TNF', 'AGP', 50)

vuelo1.agrgar_pasajero('Juan')

vuelo1.motivo_viaje('Vacaciones')

vuelo1.agrgar_pasajero('Ana')

vuelo1.motivo_viaje('Trabajo')
