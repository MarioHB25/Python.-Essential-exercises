'''
This program registers a new user by checking the following requirements:

1. That the name has a minimum length of 3 characters

2. That the telephone number is made up of digits and has a length of 9 characters

3. That the email contains an “@“ and a “.”
'''

#This function checks whether the data entered meets the registration requirements
def validar_formulario(nombre, correo, tlf):
    if (len(nombre) >= 3) and ('@'in correo) and ('.' in correo) and (len(tlf) == 9) and (tlf.isdigit()):
        print('Los datos introducidos cumplen con los requisitos')
        print('------------')
        print(f'Nombre: {nombre}\nCorreo electrónico: {correo}\nTeléfono: {tlf}')
        print('------------')
    else:
        print('Uno o varios de los datos introducidos no cumplen con los requisitos.')
        print('------------')

nombre = input('Introduzca su nombre:\n(Debe contener al menos 3 caracteres)\n')
print('------------')
correo = input('Introduzca su correo electrónico:\n(Debe contener al menos los caracteres "@" y ".")\n')
print('------------')
tlf = input('Introduzca su número de teléfono:\n(Debe contener 9 dígitos)\n')

print('------------')

validar_formulario(nombre, correo, tlf)
