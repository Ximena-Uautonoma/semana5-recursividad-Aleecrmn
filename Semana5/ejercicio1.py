"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""


def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    lista_resultado = []
    for i in range(1, n + 1):
        lista_resultado.append(i)
    
    return lista_resultado




def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    if n == 1:
        return [1]
    
    return contar_recursivo(n - 1) + [n]

num = int(input("ingrese numero: \n"))

resultado_iterativo = contar_ciclo(num)
resultado_recursivo = contar_recursivo(num)
print(f"resultado ciclo: {resultado_iterativo}")
print(f"resultado recursivo:{resultado_recursivo}")