# Conceptos básicos y sintaxis de Python: ejercicios

## Funcion
# def suma(a, b):
#     return a + b

# x = suma(2, 3)
# print(x)

# y = suma(2.7, 4.0)
# print(y)

# z = suma('Me gusta ', 'Python')
# print(z)


# ## Funciones anidadas
# def f1(a):
#     print(a)
#     b = 100
#     def f2(x):
#         print(x)
#     f2(b)

# f1('Python')

# ## Recursividad
# def factorial(x):
#     if x > 1:
#         return x*factorial(x - 1)
#     else:
#         return 1

# fact = factorial (5)
# print(fact)

# ## Devolución múltiple de valores
# def maxmin(lista):
#     return max(lista), min(lista)

# listado = [1, 3, 5, 6, 0]
# maximo, minimo = maxmin(listado)

# print(minimo, maximo, sep = ' ,')

# ## Experimenta
# def prime_factors(n):
#     factors = []
#     divisor = 2
#     while n > 1:
#         while n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         divisor += 1
#     return factors

# prime_l = prime_factors(100)
# print(prime_l)

# # Scope de las variables: regla LEGB (Local, Enclosing, Global, Built-in)
# G = 'Esta variable es Global'
# def f1():
#     E = 'Esta variable es local a f1 y Enclosing a f2'
#     def f2():
#         L = 'Esta variable es local a f2'
#         print(L, E, G, sep = '\n')
#     f2()
# f1()

# G = 'Esta variable es Global'
# def f1():
#     E = 'Esta variable es local a f1 y Enclosing a f2'
#     def f2():
#         L = 'L es local a f2'
#         E = 'E es local a f2'
#         G = 'G el local a f2'
#         print(L, E, G, sep = '\n')
#     f2()
# f1()

# G = 'Esta variable es Global'
# def f1():
#     E = 'Esta variable es local a f1 y Enclosing a f2'
#     def f2():
#         L = 'L es local a f2'
#         E = 'E es local a f2'
#         G = 'G el local a f2'
#         print(L, E, G, sep = '\n')
#     def f3():
#         print(L)        # Devuelve error
#     f2()
#     f3()
# f1()

# G = 'Esta variable G es Global'
# def f1():
#     E = 'Esta variable E es local a f1 y Enclosing a f2'
#     def f2():
#         L = 'L es local a f2'
#         E = 'E es local a f2'
#         G = 'G el local a f2'
#         print(L, E, G, sep = '\n')
#     def f3():
#         print(E, G, sep = '\n')
#     f2()
#     f3()
# f1()

# Parámetros y objetos inmutables
# def suma(a, b):     # Modificamos a y b en el scope de la suma
#     a = 3
#     b = 4
#     return a + b

# a, b = 5, 10
# print(suma(a,b))
# print(a, b)         # a y b no cambian fuera de la función

# Parametros y objetos mutables
# def modificar_lista(lista):
#     lista[0] = 1000  # Modificamos el primer elemento de la lista
#     return min(lista)  # Devolvemos el valor mínimo de la lista modificada

# mi_lista = [1, 2, 3]

# minimo_original = min(mi_lista)
# print("Antes de la función:", mi_lista)
# print("Mínimo valor en la lista original:", minimo_original)

# minimo_nuevo = modificar_lista(mi_lista)  # Llamamos a la función
# print("Después de la función:", mi_lista)  # La lista original se ha modificado
# print("Mínimo valor en la lista modificada:", minimo_nuevo)

# Es recomendable que no se modifique la lista original:
# def modificar_lista(lista):
#     lista[0] = 1000
#     return min(lista)

# mi_lista = [1, 2, 3]
# nueva_lista = mi_lista[:]  # Se crea una copia de la lista

# minimo_original = min(mi_lista)
# print("Antes de la función:", mi_lista)
# print("Mínimo valor en la lista original:", minimo_original)
# print()
# minimo_copia = min(nueva_lista)
# print("Copia de la lista:", nueva_lista)
# print("Mínimo valor nueva copia lista:", minimo_copia)
# print()
# minimo_nuevo = modificar_lista(nueva_lista)
# print("Después de la función, lista original:", mi_lista)
# print("Después de la función, copia de la lista:", nueva_lista)
# print("Mínimo valor en la copia de lista modificada:", minimo_nuevo)
# print()

# # Misma funcionalidad pero sintaxis más avanzada
# def modificar_lista(lista):
#     lista[0] = 1000
#     return min(lista)

# mi_lista = [1, 2, 3]
# nueva_lista = mi_lista[:]  # Se crea una copia de la lista original

# print("Antes de la función:")
# print(f"Lista original: {mi_lista} → Mínimo: {min(mi_lista)}")
# print(f"Copia de la lista: {nueva_lista} → Mínimo: {min(nueva_lista)}")

# minimo_nuevo = modificar_lista(nueva_lista)

# print("\nDespués de la función:")
# print(f"Lista original (sin cambios): {mi_lista}")
# print(f"Copia de la lista modificada: {nueva_lista} → Mínimo: {minimo_nuevo}")

# def f(**kargs):  # Acepta un número variable de argumentos con nombre
#     print(kargs)  # Imprime el diccionario de argumentos

# # Llamadas a la función con diferentes números de argumentos con nombre
# f()              
# f(a=1)          
# f(a=1, b=2)    
# f(a=1, c=3, b=2)

def f(a, b, c, d):  # La función acepta exactamente 4 argumentos
    print(a, b, c, d)  # Imprime los valores en el orden recibido

# Llamadas a la función con diferentes valores desempaquetados
f(*[1, 2, 3, 4])  # Se desempaqueta la lista en argumentos posicionales
f(*[100, 1, 2, 3])
f(*[100, 200, 1, 2])