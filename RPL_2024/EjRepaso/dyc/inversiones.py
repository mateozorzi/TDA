#A esta ordenado, B desordenado
def contar_inversiones_dyc(A,B):
    if len(B) == 1:
        return 0, B   
    inversiones = 0

    mitad = len(B) // 2
    
    izq = B[:mitad]
    indiceIzq = 0
    der = B[mitad:]
    indiceDer = 0

    inversionesIzq, izq = contar_inversiones_dyc(A, izq)
    inversionesDer, der = contar_inversiones_dyc(A, der)

    inversiones += inversionesIzq + inversionesDer

    ordenado = []
    while indiceIzq < len(izq) and indiceDer < len(der):
        if izq[indiceIzq] > der[indiceDer]:
            ordenado.append(der[indiceDer])
            inversiones += len(izq)-indiceIzq
            indiceDer += 1
        else:
            ordenado.append(izq[indiceIzq])
            indiceIzq += 1
    
    if indiceIzq < len(izq):
        ordenado += izq[indiceIzq:]
    elif indiceDer < len(der):
        ordenado += der[indiceDer:]
    
    return inversiones, ordenado

def contar_inversiones(A,B):
    inversiones, arreglo = contar_inversiones_dyc(A,B)
    return inversiones