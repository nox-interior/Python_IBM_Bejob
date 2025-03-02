# Sistema de Gestión de Biblioteca
# Este programa permite registrar libros y gestionar préstamos a usuarios.
# Se deben respetar los siguientes requisitos:
# 1. Clase Libro con atributos: titulo (str), autor (str), isbn (str) y disponible (bool, inicialmente True).
# 2. Métodos de la clase Libro:
#    - agregar(): Permite introducir un nuevo libro leyendo sus características.
#    - prestar(): Cambia el estado de 'disponible' a False si el libro está disponible; 
#                 si ya está prestado, muestra un mensaje.
#    - devolver(): Cambia el estado de 'disponible' a True si estaba prestado; 
#                  si ya estaba disponible, muestra un mensaje.
#    - mostrar(): Muestra en pantalla todos los libros registrados con todos sus datos y el estado (disponible o no).
#    - buscar(): Busca un libro por su ISBN y muestra en pantalla sus datos junto con su disponibilidad.
#
# 3. Gestión del inventario:
#    - Se utiliza una lista para almacenar objetos de la clase Libro.
#    - Se implementa un bucle que permite al usuario interactuar mediante un menú con las siguientes opciones:
#         1. Agregar libro
#         2. Prestar libro
#         3. Devolver libro
#         4. Mostrar libros
#         5. Buscar
#         6. Salir
#
# Se valida que el ISBN ingresado exista antes de prestar o devolver un libro.
# Si se ingresa una opción inválida, se muestra un mensaje de error y se pide nuevamente una opción.

class Libro:
    inventario = []

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    @classmethod
    def agregar(cls):
        print("Ingrese los datos del libro:")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        nuevo_libro = cls(titulo, autor, isbn)
        cls.inventario.append(nuevo_libro)
        print("Libro agregado con éxito.")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito.")
        else:
            print("El libro no se encuentra disponible para préstamo.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto con éxito.")
        else:
            print("El libro no se puede devolver: disponible para préstamo.")

    @classmethod
    def mostrar(cls):
        if not cls.inventario:
            print("No existen registros en el catálogo de la biblioteca.")
        else:
            for libro in cls.inventario:
                estado = "Sí" if libro.disponible else "No"
                print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {estado}")

    @classmethod
    def buscar(cls):
        isbn = input("ISBN del libro a buscar: ")
        for libro in cls.inventario:
            if libro.isbn == isbn:
                estado = "Sí" if libro.disponible else "No"
                print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {estado}")
                return
        print("ISBN no disponible en el catálogo de la biblioteca.")

    @classmethod
    def prestar_libro(cls):
        isbn = input("ISBN del libro a prestar: ")
        for libro in cls.inventario:
            if libro.isbn == isbn:
                libro.prestar()
                return
        print("Error: No se encontró un libro con ese ISBN.")

    @classmethod
    def devolver_libro(cls):
        isbn = input("ISBN del libro a devolver: ")
        for libro in cls.inventario:
            if libro.isbn == isbn:
                libro.devolver()
                return
        print("Error: No se encontró un libro con ese ISBN.")

# Opciones biblioteca
if __name__ == "__main__":
    while True:
        print("\n1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("\nElige una opción: ").strip()

        if opcion == '1':
            Libro.agregar()
        elif opcion == '2':
            Libro.prestar_libro()
        elif opcion == '3':
            Libro.devolver_libro()
        elif opcion == '4':
            Libro.mostrar()
        elif opcion == '5':
            Libro.buscar()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 6.")