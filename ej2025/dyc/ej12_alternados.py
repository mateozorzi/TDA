"""
Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). ¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.
"""

def alternar_dyc(arr):
    if len(arr) == 2:
        return arr
    if len(arr) == 4:
        aux = arr[1]
        arr[1] = arr[2]
        arr[2] = aux
        return arr
    
    mitad = (len(arr)-1)//2

    arr = alternar_dyc(arr[:mitad//2+1]+arr[mitad+1:mitad+(mitad//2)+2]) + alternar_dyc(arr[mitad//2+1:mitad+1] + arr[mitad+(mitad//2)+2:mitad+(mitad//2)+2+(mitad//2)+1])

    return arr

#T(n) = 2T(n/2) + O(1), A = 2, B = 2, C = 0 -> Por TM -> log B(A) = 1 > C = O(n^(logb(a))) = O(n)

def alternar(arr):
    return alternar_dyc(arr)


arr = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13", "d14", "d15", "d16"]
#print(alternar(arr))

arr = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]
#print(alternar(arr))

arr =  [0,2,4,6,1,3,5,7]
print(alternar(arr))


    