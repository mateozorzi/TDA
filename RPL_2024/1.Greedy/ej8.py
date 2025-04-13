"""Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    if(len(elementos) == 0):
        return []
    elementosxValor = sorted(elementos, key=lambda x :(x[0]/x[1]), reverse=True)
    elementosGuardados = []
    pesoGuardado = 0

    indice = 0
    while(pesoGuardado <= W and indice < len(elementos)):
        if(elementosxValor[indice][1] + pesoGuardado <= W):
            elementosGuardados.append(elementosxValor[indice])
            pesoGuardado += elementosxValor[indice][1]
        indice += 1
    return elementosGuardados
        
arr = [(20,2), (3,10), (10,10), (10,1)]
print(mochila(arr,20))
