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
        return cls(titulo, autor, isbn)

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito.")
        else:
            print("El libro ya se encuentra prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto con éxito.")
        else:
            print("El libro ya se encuentra disponible.")

    @staticmethod
    def mostrar(biblioteca):
        if not biblioteca:
            print("No hay libros en la biblioteca.")
        else:
            for libro in biblioteca:
                disp = "Sí" if libro.disponible else "No"
                print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disp}")

    @staticmethod
    def buscar(biblioteca, isbn):
        for libro in biblioteca:
            if libro.isbn == isbn:
                disp = "Sí" if libro.disponible else "No"
                print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disp}")
                return libro
        print("Libro no encontrado.")
        return None

def main():
    biblioteca = []
    
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    
    # Bucle principal del programa
    while True:
        print("\n1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            libro = Libro.agregar()
            biblioteca.append(libro)
            print("Libro agregado con éxito.")
            
        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.prestar()
                
        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.devolver()
                
        elif opcion == "4":
            Libro.mostrar(biblioteca)
            
        elif opcion == "5":
            isbn = input("Ingresa el ISBN a buscar: ")
            Libro.buscar(biblioteca, isbn)
            
        elif opcion == "6":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == '__main__':
    main()