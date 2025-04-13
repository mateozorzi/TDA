"""
Implementar una función (que utilice división y conquista) de complejidad O(n logn) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. Ejemplos:

[1, 2, 1, 2, 3] -> false
[1, 1, 2, 3] -> false
[1, 2, 3, 1, 1, 1] -> true
[1] -> true
"""

def mas_de_la_mitad_dyc(arr):
    if len(arr) == 1:
        return arr[0], 0
        
    mitad = len(arr) // 2

    izq = arr[:mitad]
    der = arr[mitad:]

    candidatoIzq, contadorIzq = mas_de_la_mitad_dyc(izq)
    contadorIzq = 0
    candidatoDer, contadorDer = mas_de_la_mitad_dyc(der)
    contadorDer = 0

    for num in arr:
        if num == candidatoIzq:
            contadorIzq += 1
        elif num == candidatoDer:
            contadorDer += 1
    
    if contadorIzq > contadorDer:
        return candidatoIzq, contadorIzq
    else:
        return candidatoDer, contadorDer


def mas_de_la_mitad(arr):
    if len(arr) == 1:
        return True
    candidato, contador = mas_de_la_mitad_dyc(arr)
    if contador > len(arr)//2:
        return True
    return False

#Complejidad O(n logn) -> T(n) = AT(n/B) + O(n^C) -> T(n) = 2T(n/2) + O(n) -> A = 2, B = 2, C = 1

arr = [1, 2, 3, 1, 1, 1]
print(mas_de_la_mitad(arr))