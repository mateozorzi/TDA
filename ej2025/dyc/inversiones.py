def contar_inversiones_dyc(A,B, inversiones):
    if len(B) == 1:
        return B,inversiones
    
    mitad = len(B)//2
    izq = B[:mitad]
    der = B[mitad:]

    #cuento inversiones del subporoblema de la izq
    izq, inversiones = contar_inversiones_dyc(A, izq, inversiones)
    #cuento inversiones del subroplema de la izq
    der, inveriones = contar_inversiones_dyc(A, der, inversiones)

    indice_izq = 0
    indice_der = 0

    ordenado = []
    while indice_izq < len(izq) and indice_der < len(der):
        if izq[indice_izq] > der[indice_der]:
            #una inversion
            ordenado.append(der[indice_der])
            indice_der += 1
            inversiones += len(izq) - indice_izq
        else:
            #no hay inversion
            ordenado.append(izq[indice_izq])
            indice_izq += 1
    
    if indice_izq < len(izq):
        ordenado.extend(izq[indice_izq:])
    else:
        ordenado.extend(der[indice_der:])

    return ordenado, inversiones

def contar_inversiones(A, B):
    inversiones = 0

    B, inversiones = contar_inversiones_dyc(A,B, inversiones)

    return inversiones

#Estudio de la complejidad:
#Por llamado de funcion, hay 2 llamados recursivos
# En cada llamado divido al problema en 2 subproblemas de igual tamaño
#Las operaciones para contar las inversiones son comparar indices de arreglos y agregar elementos de manera ordenada
#Entonces: A = 2
        #  B = 2
        #  C = 1
#Por teorema del maestro -> T(n) = A*T(n/B) + (n^C)
#Estoy en el caso en el que log B (A) = C -> O(n logn)