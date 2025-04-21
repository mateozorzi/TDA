"""
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.
"""

def sumatorias_n_bt(lista, n, indice, parcial, conjuntos):
    if sum(parcial) == n:
        conjuntos.append(parcial[:])
        return conjuntos #devuelvo porque si sigo sumando me paso de n
    
    if sum(parcial) > n or indice > len(lista):
        return conjuntos
    
    if sum(parcial) + sum(lista[indice:]) < n:
        #no llego con la suma con los valores que quedan, podo
        return conjuntos


    parcial.append(lista[indice])
    conjuntos = sumatorias_n_bt(lista, n, indice+1, parcial, conjuntos)
    parcial.pop()
    conjuntos = sumatorias_n_bt(lista, n, indice+1, parcial, conjuntos)

    return conjuntos


def sumatorias_n(lista, n):
    parcial = []
    conjuntos = []
    indice = 0

    conjuntos = sumatorias_n_bt(lista,n, indice,parcial, conjuntos)

    return conjuntos