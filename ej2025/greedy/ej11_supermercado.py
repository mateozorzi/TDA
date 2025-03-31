"""
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, 
encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. 
Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.
"""

def bolsas(capacidad, productos):
    if capacidad == 0:    
        return []
    
    bolsas = []

    productos = sorted(productos, key=lambda x: x, reverse=True) #[1,2,3,4,5]

    for p in productos:
        agregado = False
        for b in bolsas:
            if sum(b) == capacidad or sum(b) + p > capacidad:
                continue
            elif sum(b) + p <= capacidad:
                b.append(p)
                agregado = True
                break
        
        if not agregado:
            #creo una bolsa
            bolsa = [p]
            bolsas.append(bolsa)

    return bolsas

arr = [16,14,10,9,8,5]
cap = 31

print(bolsas(cap,arr))
