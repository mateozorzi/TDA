"""
Dado un arreglo de enteros ordenado, un elemento y un valor entero k, implementar una función que, usando división
y conquista, encuentre los k valores del arreglo más cercanos al elemento en cuestión (que bien podría estar en el
arreglo, o no). La complejidad de la función implementada debe ser menor a O(n), suponiendo que k < n. Justificar
adecuadamente la complejidad del algoritmo implementado.
"""

"""
T(n) = AT(n/B) + O(n^c) -> 1T(n/2) + O(1) -> A=1, B=2, C=0 -> log2(1) = 0 = C -> O(n^c logn) -> O(logn)
"""

def buscoElemento(numeros, elemento, inicio, fin):
    if inicio == fin:
        return inicio
    
    mitad = (fin+inicio) //2

    elementos_mitad = numeros[mitad]

    if elementos_mitad == elemento:
        return mitad
    elif elementos_mitad > elemento:
        return buscoElemento(numeros, elemento, inicio, mitad)
    else:
        return buscoElemento(numeros, elemento, mitad, fin)


def k_valores(numeros, elemento, k, solucion):
    indice_elemento = buscoElemento(numeros, elemento, 0, len(numeros)-1) #O(logn)

    solucion = []


    izq = -1
    der = len(numeros)
    if indice_elemento > 0:
        izq = indice_elemento-1
    if indice_elemento < len(numeros)-1:
        der = indice_elemento+1

    while len(solucion) != k: #O(k)
        if izq >= 0 and der < len(numeros):
            elemento_izq = numeros[izq]
            elemento_der = numeros[der]

            if elemento - elemento_izq <= elemento_der - elemento:
                solucion.append(elemento_izq)
                izq -= 1
            else:
                solucion.append(elemento_der)
                der -= 1
            continue
        elif izq < 0 and der < len(numeros):
            elemento_der = numeros[der]
            solucion.append(elemento_der)
            der += 1
            continue
        elif der >= len(numeros) and izq >= 0:
            elemento_izq = numeros[izq]
            solucion.append(elemento_izq)
            izq += 1
            continue
        elif der >= len(numeros) and izq < 0:
            break

    return solucion
            
