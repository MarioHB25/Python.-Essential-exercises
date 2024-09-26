'''
A common problem when requesting data from a user occurs when the
people enter different parameters than those requested.

This program captures the error and allows the user 
to re-enter the requested data without stopping the program execution.
'''
#The loop prevents program execution from stopping even if an input error occurs
continuar = True
while continuar:
  
#Two numbers are requested from the user to be processed
    try:
        num1s = (input('Introduzca un número: '))
        num2s = (input('Introduzca otro número: '))
        print('--------------------')
        num1 = int(num1s)
        num2 = int(num2s)
        resultado = num1 + num2
        print(f'El resultado de la suma del número {num1} y el número {num2} es: {resultado}')
        print('----------Saliendo del programa----------')
        continuar = False

  #If the data is'nt correct, the program notifies the user and requests the data again
    except ValueError:
        print('¡¡CUIDADO!! Uno de los datos introducidos no es un número.')
        print('--------------------')
        print('----------Introduzca de nuevo los números.----------')
        print('--------------------')
