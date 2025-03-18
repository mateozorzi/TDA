"""
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo. Ejemplos:

[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
"""
def es_continuo(izq, der, arr):
    ultimo_izq = izq[-1]
    primero_der = der[0]

    mitad = len(arr)//2

    if arr[mitad-1] == ultimo_izq and arr[mitad] == primero_der:
        return True
    return False

def max_subarray(arr):
    if len(arr) == 1:
        return arr
    
    mitad = (len(arr))//2

    izq = arr[:mitad]
    der = arr[mitad:]

    #veo cuanto sumala parte izq y la parte der

    sum_izq = max_subarray(izq)
    sum_der = max_subarray(der)

    if sum(arr) > sum(sum_izq) + sum(sum_der) and sum(arr) > sum(sum_izq) and sum(arr) > sum(sum_der):
        return arr
    
    partes_juntas = []
    #veo si el subarreglo de la izq es continuo con el de la derecha
    if es_continuo(sum_izq, sum_der, arr):
        #devuevlo la suma de los dos
        partes_juntas = sum_izq + sum_der

    if sum(partes_juntas) > sum(sum_izq) and sum(partes_juntas) > sum(sum_der):
        return partes_juntas
    
    if sum(sum_izq) > sum(sum_der):
        return sum_izq
    else:
        return sum_der
    

arr = [5, -4, 2, 4]
print(max_subarray(arr))