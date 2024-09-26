"""
This program allows the complete management of a library. 
You can have a database with books and their data, 
another database with library users and their personal information, 
and methods that allow the library to add new books, check out books, return books, and display inventory.
"""

# Definition of the Book class
class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

# Definition of the User class
class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

# Definition of the Library class
class Biblioteca:
    def __init__(self):
        self.libros = []

#Add a book to the library inventory. libro: The Book object to add.
    def agregar_libro(self, libro):
        self.libros.append(libro)

# Lend a book to a user if available. usuario: The User object that requests the loan. titulo: The title of the book to be loaned.
    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares_disponibles > 0:
                usuario.libros_prestados.append(libro)
                libro.ejemplares_disponibles -= 1
                print(f"El libro {titulo} ha sido prestado a {usuario.nombre}")
                return
        print("El ejemplar no está disponible")

# Returns a book borrowed by a user. usuario: The User object that returns the book. titulo: The title of the book to be returned.
    def devolver_libro(self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares_disponibles += 1
                print(f"El libro {titulo} ha sido devuelto por {usuario.nombre}")

# Shows the inventory of books available in the library.
    def mostrar_inventario(self):
        for libro in self.libros:
            print(f"{libro.titulo} de {libro.autor} - Disponibles: {libro.ejemplares_disponibles}")


# Example of Use
biblioteca = Biblioteca()  # Create a Library instance
libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 3)  # Create a book
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 5)  # Create another book

biblioteca.agregar_libro(libro1)  # Add book1 to library inventory
biblioteca.agregar_libro(libro2)  # Add book2 to library inventory

biblioteca.mostrar_inventario()  # Show library inventory

usuario1 = Usuario("Lara", "12345")  # Create a user1
usuario2 = Usuario("Ana", "54321")  # Create a user2

biblioteca.prestar_libro(usuario1, "El Gran Gatsby")  # Lend book1 to user1
biblioteca.prestar_libro(usuario2, "Cien Años de Soledad")  # Lend book2 to user2

biblioteca.mostrar_inventario()  # Show library inventory after checking out books

biblioteca.devolver_libro(usuario1, "El Gran Gatsby")  # Return book1 borrowed by user1

biblioteca.mostrar_inventario()  # Show library inventory after returning a book
