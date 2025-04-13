def contarInversiones(arr):
    aux, inversiones = mergesort(arr)
    return inversiones

def mergesort (arr) :
    if len (arr) <= 1:
        return arr,0
    medio = len (arr) // 2
    izq, invIzq = mergesort (arr[:medio])
    der, invDer = mergesort (arr[medio:])
    return intercalar_ordenado (izq, der, invIzq + invDer) #O(n)

def intercalar_ordenado(izq, der, inversiones):
    contador = 0
    indiceIzq = 0
    indiceDer = 0
    intercalado = []
    while (indiceIzq < len(izq) and indiceDer < len(der)):
        if(izq[indiceIzq] <= der[indiceDer]):
            intercalado.append(izq[indiceIzq])
            indiceIzq += 1
        else:
            intercalado.append(der[indiceDer])
            indiceDer += 1
            contador += 1
    if(len(izq) == indiceIzq):
        intercalado += der[indiceDer:]
    elif(len(der) == indiceDer):
        intercalado += izq[indiceIzq:]
    return intercalado, inversiones + contador

#Ecuacion de recurrencia T(n) = 2T(n/2) + O(n), resolucion queda O(nlogn)
#El 2T es por los llamados recursivos

arr = [1,3,5,2,4]
print(mergesort(arr))