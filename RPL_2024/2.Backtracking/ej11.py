"""Escribir un algoritmo que, utilizando backtracking, 
dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n."""

def sumatorias_n(lista, n):
    #lista = sorted(lista)

    indice = 0
    inicio = 0
    resultado = []
    subconjunto = []
    


    return sumatorias_n_bt(lista,n,indice, inicio,resultado,subconjunto)

def sumatorias_n_bt(lista,n,indice,inicio,resultado,subconjunto):
    if(sum(subconjunto) == n):
        resultado.append(subconjunto.copy())
        subconjunto = []
        return
    
    if(sum(subconjunto) > n or indice >= len(lista)):
        return 
    
    subconjunto.append(lista[indice])
    sumatorias_n_bt(lista,n,indice+1,inicio,resultado,subconjunto)
    subconjunto.pop()
    sumatorias_n_bt(lista,n,indice+1,inicio,resultado,subconjunto)

    return resultado
    
arr =  [1,2,3,4,6]
n = 5

print(sumatorias_n(arr,n))
