# Conceptos básicos y sintaxis de Python: ejercicios

## Funcion
def suma(a, b):
    return a + b

x = suma(2, 3)
print(x)

y = suma(2.7, 4.0)
print(y)

z = suma('Me gusta ', 'Python')
print(z)


## Funciones anidadas
def f1(a):
    print(a)
    b = 100
    def f2(x):
        print(x)
    f2(b)

f1('Python')

## Recursividad
def factorial(x):
    if x > 1:
        return x*factorial(x - 1)
    else:
        return 1

fact = factorial (5)
print(fact)

## Devolución múltiple de valores
def maxmin(lista):
    return max(lista), min(lista)

listado = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(listado)

print(minimo, maximo, sep = ' ,')

## Experimenta
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

prime_l = prime_factors(100)
print(prime_l)