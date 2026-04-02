"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):

    resultado = 1

    for i in range (1, n +1):
        resultado *= i
    return resultado



def factorial_recursivo(n):

    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)

n = int(input("\ningrese un numero entero positivo: "))
print(f"el factorial de {n} en iterativo es: {factorial_ciclo(n)}")
print(f"el factorial de {n} en recursivo es: {factorial_recursivo(n)}")
