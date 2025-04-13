"""Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, 
devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, 
que devuelva el subconjunto de suma máxima sin superar el valor de n."""

def max_sumatoria_n(lista, n):
    #lista = sorted(lista)

    indice = 0
    subconjunto = []
    sumaMaxima = []
    


    maximo = sumatorias_n_bt(lista,n,indice,sumaMaxima,subconjunto)

    return maximo
    
def sumatorias_n_bt(lista,n,indice,maximo,subconjunto):
    if(sum(subconjunto) == n):
        return subconjunto.copy()
    
    if (sum(subconjunto) > sum(maximo) and sum(subconjunto) < n):
        maximo = subconjunto.copy()
    
    if(sum(subconjunto) > n or indice >= len(lista)):
        return maximo

    
    subconjunto.append(lista[indice])
    maximoCon = sumatorias_n_bt(lista, n, indice + 1, maximo, subconjunto)
    subconjunto.pop()
    maximoSin = sumatorias_n_bt(lista, n, indice + 1, maximo, subconjunto)
    
    if(sum(maximoCon) >= sum(maximoSin)):
        return maximoCon
    else:
        return maximoSin
    

arr =  [1,7,3,4]
n = 5

print(max_sumatoria_n(arr,n))