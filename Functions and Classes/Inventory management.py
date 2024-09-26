'''
This program allows you to register elements of a business in a database.
With this program you will be able to add products to the database,
store the identification, price and quantity of available stock of a product,
show the inventory, remove sold products from the inventory and
notify if there is'nt enough stock of a product.
'''

#Creation of the class that contains the product ID, price and stock
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#Creating the class that contains the business database
class Tienda:
    def __init__(self):
        self.lista = []
      
#Function to add products
    def agregar_productos(self, producto):
        self.lista.append(producto)

#Function to display the inventory
    def mostrar_inventario(self):
        for producto in self.lista:
            print(f'Nombre: {producto.nombre} - Precio: {producto.precio}Eu. - Stock: {producto.stock}')
          
#Function to remove sold products from inventory and notify if stock is insufficient
    def comprar_producto(self, nombre, cantidad):
        for producto in self.lista:
            if producto.nombre == nombre:
                if cantidad <= producto.stock:
                    producto.stock -= cantidad
                    print(f'Se compraron {cantidad} {producto.nombre}, por valor de {producto.precio * cantidad} Euros.')
                else:
                    print('No Hay suficiente stock en la tienda.')
                return
        print('El producto introducido no existe.')    

#Example of use
tienda = Tienda()

#Product Creation
producto1 = Producto('Camiseta', 20, 50)
producto2 = Producto('Pantalón', 30, 40)
producto3 = Producto('Zapatos', 50, 10)

#Adding products to inventory
tienda.agregar_productos(producto1)
tienda.agregar_productos(producto2)
tienda.agregar_productos(producto3)

#Showing inventory
tienda.mostrar_inventario()

#Removal of sold products from inventory
tienda.comprar_producto('Camiseta', 4)
tienda.comprar_producto('Pantalón', 5)
tienda.comprar_producto('Zapatos', 10)

#Showing updated inventory
tienda.mostrar_inventario()
