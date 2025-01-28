"""Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, 
y la cantidad de integrantes que conforma a cada uno. 
Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, 
siendo en total n grupos. Como se trata de un restaurante familiar, 
las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, mediante programación dinámica, 
obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa 
(o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo."""

def calculoOptimos(P,W):
    optimos = [[0] *(W+1) for i in range(len(P)+1) ]

    for i in range(1,len(optimos)):
        for j in range(1,W+1):
            if P[i-1] > j:
                optimos[i][j] = optimos[i-1][j]
            else:
                optimos[i][j] = max(optimos[i-1][j],
                                  optimos[i-1][j-P[i-1]] + P[i-1])
    
    return optimos

def sentados(P,W,optimos,pos,grupos): #A=1, B=1, C=1
    if pos == [0,0] or pos[1] == 0 or pos[0] == 0:
        return grupos
    
    if P[pos[0]-1] > pos[1]:
        return sentados(P,W,optimos,[pos[0]-1,pos[1]],grupos)
    else:
        if optimos[pos[0]-1][pos[1]-P[pos[0]-1]] + P[pos[0]-1] > optimos[pos[0]-1][pos[1]]:
            grupos.append(P[pos[0]-1])
            return sentados(P,W,optimos,[pos[0]-1,pos[1]-P[pos[0]-1]],grupos)
        else:
            return sentados(P,W,optimos,[pos[0]-1,pos[1]],grupos)

def bodegon_dinamico(P, W):
    optimos = calculoOptimos(P,W)
    grupos = []
    sentados(P,W,optimos,[len(optimos)-1, len(optimos[0])-1], grupos)
    grupos = list(reversed(grupos))
    return grupos
#O(P.W)



P = [10, 7, 5, 14]

W = 16

print(bodegon_dinamico(P,W))