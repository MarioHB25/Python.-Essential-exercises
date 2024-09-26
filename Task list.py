'''
This program allows you to create a list of pending tasks,
as well as add new tasks, display the list and mark them as completed
'''

#Creating the class that contains the task list
class ListaTareas:
    def __init__(self):
        self.tareas = []

#Function to create tasks
    def agregar_tarea(self, tareas):
        self.tareas.append({'nombre':tareas, 'completada':False})

#Function to mark tasks as completed
    def marcar_tarea(self, indice):
        if 0 <= indice <(len(self.tareas)):
            self.tareas[indice]['completada'] = True

#Function to display task list
    def mostrar_tareas(self):
        for indice, tarea in enumerate(self.tareas):
            estado = 'Completada' if tarea['completada'] else 'Pendiente'
            print(f'{indice + 1}. {tarea["nombre"]}-{estado}')
        print('----------------')
    

#Example of use
lista_tareas = ListaTareas()

#Adding tasks
lista_tareas.agregar_tarea('Barrer')
lista_tareas.agregar_tarea('Fregar')
lista_tareas.agregar_tarea('Regar')

#Showing task list
lista_tareas.mostrar_tareas()

#Marking some tasks as finished
lista_tareas.marcar_tarea(0)
lista_tareas.marcar_tarea(1)

#Showing the updated list of tasks
lista_tareas.mostrar_tareas()
