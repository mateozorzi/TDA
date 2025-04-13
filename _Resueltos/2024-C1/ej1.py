"""
HS: Dado un conjunto A de n elementos y m subconjuntos B de A y un numero k. Existe un subconjunto C de A
tal que tenga a los umo k elementos tal que tenga al menos un elmtno de cada subconjunto Bi.

DM: Dado un grafo y un numero k', existe un conjunto D de vertices de a los sumo k' vertice
tal que para cada vertice se cumple que: v pertenece D o v es adyacente a un vertice de D.

Quiero probar que HS es NP-C

1. Validador poninomial, para comprobar que HS esta en NP

2. Para comprobar que HS es NP-C, voy a reducir un problema NP-C a HS

Reduccion:
DM(grafo, k') <=p HS(A, B, k)

Para la reduccion, realizamos una transformacion.
El conjunto A sera el conjunto de los vertices del grafo.
Los subconjuntos Bi, estaran conformados por cada vertice y sus adyacentes, esto representaria
a que vertices domina cada vertice o porque vertices se verian domiandos.
k = k' porque buscamos elegir un elemento de cada Bi seria equivalente a elegir un vertice dominador, que puede
repetirse en mas de un conjunto (dominar o ser dominado por varios vertices). Y como los dos problemas buscan minimazar 
los conjunto solucion -> k = k'

Si hay DM hay HS:
Si dado el grafo existe un conjunto D de vertice que cumple con las condiciones de DM, dada la reduccion
en el problema de HS, se podra formar un conjunto C de elementos, dado que haya al menos uno de cada subconjunto Bi.
Esto ya que, cada subconjunto representa los vertices dominados por un vertice o los vertices que dominan tal vertice
Entonces si existen a lo sumo k vertices que dominen a todos los vertices, el conjunto C estaria formado por estos vertices
que se formarian parte de los subconjuntos Bi de los vertices que dominan. Si un elemento domina muchos vertices,
este tambien se repteria en varios subconjuntos Bi, asi siempre habria al menos un elemento de cada subconjunto Bi.

Si hay HS hay DM:
Si dada la reduccion existe un HS, tambien habra un DM. Esto porque los elementos que representan al conjunto C solucion,
serian los vertices dominadores del grafo. Ya que cada subconjunto Bi estaba conformados por los vertices dominados por v o
los vertices que dominan a v, como hay al menos un elemento de cada subconjunto Bi en la solucion, ningun vertice
quedara sin ser dominado. 


"""

def validador(A, B, k, C):
    if len(C) > k:
        return False
    
    setC = set(C)
    setA = set(A)

    for c in C:
        if c not in setA:
            return False

    for sub in B:
        encontro = False
        for v in sub:
            if v in setC:
                encontro = True
                break
        
        if not encontro:
            return False

    return True
    
