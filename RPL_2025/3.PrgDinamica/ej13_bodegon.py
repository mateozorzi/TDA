"""Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, 
y la cantidad de integrantes que conforma a cada uno. 
Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, 
siendo en total n grupos. Como se trata de un restaurante familiar, 
las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, mediante programación dinámica, 
obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa 
(o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo."""

def buscarOptimos(P,W):
    optimos = [[0] * (W+1) for _ in range(len(P)+1)]

    #ec de recurrencia -> optimos[i][j] -> si el len(grupo i) entra entonces = max(optimos[i-1][j],optimos[i-1][j-len(grupo i)] + len(grupo i))
                                    #   -> si no entran el grupo entonces = optimos[i-1][j], lo salteo
    
    #casos base -> W = 0 -> optimos [i][0] = 0

    for i in range(1,len(optimos)):
        for j in range(1, len(optimos[0])):
            cantidad = P[i-1]

            if cantidad > j:
                optimos[i][j] = optimos[i-1][j]
            
            else:
                #entra el grupo
                optimos[i][j] = max(optimos[i-1][j],optimos[i-1][j-cantidad] + cantidad)
    
    return optimos

def reconstruccion(P, W, optimos, i, j):
    sol = []

    while i > 0 and j > 0:
        cant = P[i-1]
        if cant > j:
            #no entra el grupo
            i -= 1
            continue
    
        #el grupó puede entrar

        anteriorSin = optimos[i-1][j]
        anteriorCon = optimos[i-1][j-cant]

        if anteriorCon + cant >= anteriorSin:
            sol.append(cant)
            #se seinte el grupo
            i -= 1
            j -= cant
        else:
            #mejor que no se siente
            i -= 1
    
    return sol


def bodegon_dinamico(P, W):
    optimos = buscarOptimos(P,W)

    return reconstruccion(P,W, optimos, len(optimos)-1, len(optimos[0])-1)
#O(P.W)

P = [10, 7, 5, 14]

W = 16

print(bodegon_dinamico(P,W))