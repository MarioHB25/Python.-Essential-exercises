'''
This program allows a company to manage a database with
the information of its employees.
The program allows you to add new employees
and the department to which they belong,
update salaries, show the complete list of employees,
and calculate the average salary for each department
'''
#Employee database
empresa = {}

#Add new employees
continuar = True

while continuar:
    opcion = input('1. Introducir un nuevo empleado.\n\
                    2. Actualizar el salario de un empleado Existente.\n\
                    3. Mostrar salario medio de un departamento.\n\
                    4. Mostrar lista de trabjadores.\n\
                    5. Salir del programa.\n----------\n\
                    Introduzca una opción del 1 al 5: ')
    
    if opcion == '1':
        trabajador = input('Introduzca el nombre del nuevo empleado: ')
        departamento = input('Introduzca el departamento al que pertenece el nuevo empleado: ')
        salario = int(input('introduzca el salario del nuevo empleado: '))
        empresa[trabajador] = {'departamento': departamento, 'salario': salario}
        
#Update salary     
    elif opcion == '2':
        nombre = input('Introduzca el nombre del empleado al que quiere actualizar el salario: ')
        if nombre in empresa:
            actualizacion_salario = int(input('Introduzaca el salario actualizado: '))
            empresa[nombre]['salario'] = actualizacion_salario
            print('Salario actualizado con exito')
#Error control
        else:
            print('El trabajador no existe.')

#Show average salary for a department
    elif opcion == '3':
        salario_departamento = 0
        contador = 0
        departamento_sueldo = int(input('Introduzca el departamento: '))
        for trabajador in empresa.values():
            if departamento_sueldo == empresa['departamento']:
                salario_departamento = salario_departamento + departamento_sueldo['salario']
                contador = contador + 1
        if contador > 0:
            salario_departamento = salario_departamento / contador
#Error control
        else:
            print('No hay empleados en el departamento seleccionado')


        print(f'El salario medio del departamento {departamento_sueldo} es {salario_departamento} Euros')

#Show employee list
    elif opcion == '4':
       for trabajador in empresa:
           print(f'{trabajador}\n \tDepartamento: {empresa[trabajador]["departamento"]}\n \tSalario: {empresa[trabajador]["salario"]}')

#Exit the program
    elif opcion == '5':
        print('Saliendo del programa.')
        continuar = False
#Error control
    else:
        print("La opción introducida no es válida. Introduzca 1, 2, 3, 4 ó 5")
