'''
This program creates a database for a business with information on the items, the number of them that have been sold and their price.
'''
ventas = []

#Function to add a sale
def agregar_venta(producto, precio):
    venta = {'Producto': producto,
             'Precio': precio}
    ventas.append(venta)

#Function to display sales list
def mostrar_ventas():
    for venta in ventas:
        print('Producto:',venta['Producto'])
        print('Precio', venta['Precio'])
        print('----------')

#This loop asks the user to enter the number 1, 2 or 3 to select an option
continuar = True
while continuar:
    opcion = input('Introduzca 1, 2 ó 3.\n----------\n1-Agragar venta.\n2-Mostrar lista de ventas.\n3-Salir.\n----------\n')
    print('----------')

#By entering 1 you will be able to add all the purchased products, specifying the number of products first
    if opcion == '1':
        num_ventas = int(input('Introduzca el número de ventas que desea agragar: '))
        print('----------')
        for i in range (num_ventas):
            agregar_venta(input('Introduzca el artículo: '), float(input('Introduzca el precio del artículo: ')))
            print('----------')

#By entering the 2 you will be able to check the list of sold items
    elif opcion == '2':
        mostrar_ventas()

#By entering 3 you will be able to exit the program
    elif opcion == '3':
        print('Saliendo del programa.')
        continuar = False

#If the option entered does not correspond to 1, 2 or 3, the program throws an error and requests an option again
    else:
        print('La opción introducida no es válida. Introduzca 1, 2 ó 3.')
        print('----------')
