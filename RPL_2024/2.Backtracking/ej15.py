"""Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, 
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, 
se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos.
Como se trata de un restaurante familiar, 
las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, por backtracking, 
obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, 
que dejan la menor cantidad de espacios vacíos)."""

def max_grupos_bodegon(P, W):
    maximo = []
    parcial = []
    indice = 0

    return max_grupos_bodegon_bt(P,indice,W,maximo,parcial)
    
def max_grupos_bodegon_bt(P,indice,W,maximo,parcial):
    if sum(parcial) > sum(maximo) and sum(parcial) <= W:
        maximo[:] = parcial[:]

    if indice >= len(P):
        return
    
    if sum(parcial) + P[indice] <= W:
        parcial.append(P[indice])
        max_grupos_bodegon_bt(P,indice+1,W,maximo,parcial)
        parcial.pop()
    max_grupos_bodegon_bt(P,indice+1,W,maximo,parcial)

    return maximo

P = [4, 3, 2, 5, 1]
W = 10

print(max_grupos_bodegon(P,W))