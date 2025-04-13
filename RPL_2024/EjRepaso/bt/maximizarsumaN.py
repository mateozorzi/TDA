def sumatorias_n_bt(lista, n, sumatorias,parcial, indice):
    if sum(parcial) == n or (sum(parcial) > sum(sumatorias) and sum(parcial) <= n):
        sumatorias = parcial.copy()
    
    if indice >= len(lista):
        return sumatorias

    parcial.append(lista[indice])
    sumatorias = sumatorias_n_bt(lista,n,sumatorias,parcial,indice+1)
    parcial.pop()
    sumatorias = sumatorias_n_bt(lista,n,sumatorias,parcial,indice+1)

    return sumatorias

def max_sumatoria_n(lista, n):
    sumatorias = [0]
    parcial = []
    indice = 0
    sumatorias = sumatorias_n_bt(lista,n,sumatorias, parcial, indice)
    return sumatorias


lista = [1, 3, 6, 2, 7, 2, 11, 15, 14, 22, 8, 4, 12, 9, 17, 25, 21, 22, 18, 17]
n = 25
print(sumatorias_n(lista, n))