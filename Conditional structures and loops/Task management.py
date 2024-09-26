'''
This program allows you to create a database with the tasks 
that each member of a team has to take care of.
The program allows you to add a task, the description of the task
and the person who is in charge of the task.
'''

#Database creation
tareas = {}

#Add a number of tasks X, the description and the person in charge
num_tareas = int(input('¿Qué número de tareas nuevas quiere introducir? '))

for i in range (num_tareas):
    tareas['tareaNueva'+str(i+1)] = {'nombre':input('Introduzca el nombre de la nueva tarea: '),
                            'descripcion':input('Introduzca la descripción de la tarea: '),
                            'responsable':input('Introduzca a la persona encargada de la tarea: ')}
    print('------------------------')

#Show complete list of tasks and the people responsible for each task
i = 0
for tarea in tareas.values():
    nombre_tarea = tarea['nombre']
    descripcion_tarea = tarea['descripcion']
    responsable_tarea = tarea['responsable']
    i = i + 1
    print(f'La tarea {i} es: {nombre_tarea}.\n Su descripción es: {descripcion_tarea}.\n El responsable de la tarea es: {responsable_tarea}')
    print('----------------------------------')
