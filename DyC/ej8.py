def contar_inversiones(A,B):
    if(len(B) <= 1):
        return B,0
    mitad = (len(B)) // 2
    invTotal = 0
    izq = B[:mitad]
    der = B[mitad:]
    izq, invIzq = contar_inversiones_rec(A,izq)
    der, invDer = contar_inversiones_rec(A,der)
    merge, invTotal = inversion(izq,der,invTotal)
    invTotal += invIzq + invDer
    return invTotal

def contar_inversiones_rec(A,B):
    if(len(B) <= 1):
        return B,0
    mitad = (len(B)) // 2
    invTotal = 0
    izq = B[:mitad]
    der = B[mitad:]
    izq, invIzq = contar_inversiones_rec(A,izq)
    der, invDer = contar_inversiones_rec(A,der)
    merge, invTotal = inversion(izq,der,invTotal)
    invTotal += invIzq + invDer
    return merge, invTotal

def inversion(izq,der,inversiones):
    merge = []
    indiceIzq = 0
    indiceDer = 0
    while (len(izq) > indiceIzq and len(der) > indiceDer):
        if(izq[indiceIzq] > der[indiceDer]):
            merge.append(der[indiceDer])
            inversiones += len(izq) - indiceIzq
            indiceDer += 1
        else:
            merge.append(izq[indiceIzq])
            indiceIzq += 1
        
    if(len(izq) == indiceIzq):
        merge += der[indiceDer:]
    elif (len(der) == indiceDer):
        merge += izq[indiceIzq:]
    
    return merge, inversiones


arr = [6,8,7,2,1,5,3,4]
print(contar_inversiones(arr, arr))