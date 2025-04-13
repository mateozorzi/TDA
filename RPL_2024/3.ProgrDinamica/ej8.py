"""Se tiene un sistema monetario (ejemplo, el nuestro). 
Se quiere dar "cambio" de una determinada cantidad de plata. 
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. 
Implementar un algoritmo que, por programación dinámica, 
reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, 
y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
Indicar y justificar la complejidad del algoritmo implementado."""

def calculoOptimos(monedas,monto):
    optimos = [[0]*(monto+1) for i in range(len(monedas)+1)]
    for i in range(1,len(optimos[0])):
        optimos[0][i] = 99

    for j in range(1,len(optimos[0])):
        for i in range(1,len(optimos)):
            if monedas[i-1] > j:
                optimos[i][j] = optimos[i-1][j]
            else:
                optimos[i][j] = min(optimos[i-1][j], optimos[i][j-monedas[i-1]]+1)
    
    return optimos

def vuelto(monedas,monto,optimos,pos,usados):
    if pos == [0,0] or pos[1] == 0 or pos[0] == 0:
        return usados
    
    if monedas[pos[0]-1] > pos[1]:
        return vuelto(monedas,monto,optimos,[pos[0]-1,pos[1]],usados)
    else:
        if optimos[pos[0]][pos[1]-monedas[pos[0]-1]] < optimos[pos[0]-1][pos[1]]:
            usados.append(monedas[pos[0]-1])
            return vuelto(monedas,monto,optimos,[pos[0],pos[1]-monedas[pos[0]-1]],usados)
        else:
            return vuelto(monedas,monto,optimos,[pos[0]-1,pos[1]],usados)

def cambio(monedas, monto):
    monedas = sorted(monedas) #ordeno de menor a mayor  #O(nlogn)
    optimos = calculoOptimos(monedas,monto)  #O(monto . n)
    usados = []
    vuelto(monedas,monto,optimos,[len(optimos)-1,len(optimos[0])-1],usados)  #O(n + monto)
    usados = list(reversed(usados))  #O(n)
    return usados
#complejidad  #O(monto . n)


ej1 = [13,9,7,2,1]
print(cambio(ej1,16))

ej2 = [1000,500,100,50,20,10,5,2,1]
print(cambio(ej2,1546))