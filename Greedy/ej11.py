"""Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, 
encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. 
Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. [5,4,3,2,1]
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado."""
#[5,1,1,1,1,1,1,1,1,1]
def bolsas(capacidad, productos):
    if(len(productos) == 0):
        return []
    productos = sorted(productos, reverse=True)
    bolsa = []
    bolsasCargadas = []
    

    for i in range(len(productos)):
        if(sum(bolsa) + productos[i] == capacidad):
            bolsa.append(productos[i])
        else:
            bolsa.append(productos[i])
            for j in range(i+1,len(productos)):
                if(sum(bolsa) + productos[j] <= capacidad):
                    bolsa.append(productos[j])
        bolsasCargadas.append(bolsa)
        bolsa = []


    return bolsasCargadas


arr = [4,4,3,2,2,2,2,1,1]
print(bolsas(9,arr))