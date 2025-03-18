"""

Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""
#(valor, peso)
def mochila(elementos, W):
    if W == 0:
        return []
    
    cargados = []

    elementos = sorted(elementos, key=lambda x: x[1]/x[0]) #ordeno por la relacion entre peso y valor del opbjeto

    for e in elementos:
        if e[1] > W:
            continue
        cargados.append(e)
        W -= e[1]

        if W == 0:
            break

    return cargados

#Regla greedy: En mi situacion actual busco cargar en la mochila el elemento con mayor relacion peso/valor, buscando agregar el elem de menor peso pero que mayor valor tenga
#Es optimo ya que agrego el elemnto qeuse gun peso/valor, sea el que menos opcupa en la mopchila y que mas valor agrega
#complejidad:O(n) n =cant elementos