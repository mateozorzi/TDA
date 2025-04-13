def sumatorias_n_bt(lista, n, sumatorias,parcial, indice):
    if sum(parcial) == n:
        sumatorias.append(parcial.copy())
        return sumatorias
    
    if indice >= len(lista):
        return sumatorias

    parcial.append(lista[indice])
    sumatorias = sumatorias_n_bt(lista,n,sumatorias,parcial,indice+1)
    parcial.pop()
    sumatorias = sumatorias_n_bt(lista,n,sumatorias,parcial,indice+1)

    return sumatorias

def sumatorias_n(lista, n):
    sumatorias = []
    parcial = []
    indice = 0
    sumatorias = sumatorias_n_bt(lista,n,sumatorias, parcial, indice)
    return sumatorias

lista = [1, 2, 3, 4, 5, 6, 8, 9]
n = 12
print(sumatorias_n(lista, n))
"""
[1, 2, 3, 4, 5, 6, 8, 9]

---------

12

????????

[7]

---------

14

????????

[6]

---------

7

????????

[6]

---------

6

????????

[5, 6]

---------

12

????????

[7, 11]

---------

17

????????

[1, 3]

---------

4

????????

[7, 5, 2, 6, 1, 3]

---------

14

????????

[1, 3, 6, 2, 7, 2, 11, 15, 14, 22, 8, 4, 12, 9, 17, 25, 21, 22, 18, 17]

---------

25

????????

[1, 2, 4, 11, 3, 5, 8, 7]

---------

15
"""