"""Tenemos una mochila con una capacidad W. Hay elementos a guardar, 
cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo que, por programación dinámica, 
reciba los valores y pesos de los elementos, 
y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
Indicar y justificar la complejidad del algoritmo implementado."""

def calcularOptimos(elementos,W):
    optimos = [[0] * (W+1) for _ in range(len(elementos)+1)] #O(n.(W+1))
    for i in range(len(optimos)):
        optimos[i][0] = 0   #Cuando la cap es cero
    for j in range(len(optimos[0])):
        optimos[0][j] = 0   #cuando no tengo elementos
       
    for j in range(1,len(optimos[0])):
        for i in range(1,len(optimos)):
            if elementos[i-1][1] > j:   #Si el elemento excede la cap
                optimos[i][j] = optimos[i-1][j]
            else:
                optimos[i][j] = max(optimos[i-1][j], optimos[i-1][j-elementos[i-1][1]] + elementos[i-1][0])            

    return optimos

def reconstruccion(elementos,W,optimos,pos,usados):
    if pos == [0,0]:
        return usados
    
    if elementos[pos[0]-1][1] > pos[1]:
        return reconstruccion(elementos,W,optimos,[pos[0]-1,pos[1]],usados)
    else:
        optimoAnteSinElemento = optimos[pos[0]-1][pos[1]]
        optimoAntConEspacio = optimos[pos[0]-1][pos[1]-elementos[pos[0]-1][1]]
        actual = elementos[pos[0]-1][0]
        if optimoAnteSinElemento < optimoAntConEspacio + actual:
            usados.append(elementos[pos[0]-1])
            return reconstruccion(elementos,W,optimos,[pos[0]-1,pos[1]-elementos[pos[0]-1][1]],usados)
        else:
            return reconstruccion(elementos,W,optimos,[pos[0]-1,pos[1]],usados)

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    if W == 0:
        return []
    optimos = calcularOptimos(elementos,W) #O(n.(W+1))
    mayorGanancia = optimos[-1][-1]
    elementosUsados = []
    reconstruccion(elementos,W,optimos,[len(optimos)-1,len(optimos[0])-1],elementosUsados) #O(n + (W+1))
    elementosUsados = list(reversed(elementosUsados)) #O(n)
    return elementosUsados
#Complejidad #O(n.(W+1))

arr = [(10,6), (1,1), (8,3), (100,100), (6,4), (11,2),(7,8),(2,7),(11,9)]
print(mochila(arr,19))