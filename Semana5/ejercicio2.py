"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """

    suma = 0
    for i in range (1, n+1):
        suma+= i
    return suma
    


def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
   """
    if n == 0:
        return 0

    return n + suma_recursiva(n-1)

n = int(input("\ningrese un numero entero positivo: "))

print(f"suma con iterativo:  {suma_ciclo(n)}")
print(f"suma con recursivo: {suma_recursiva(n)}")
