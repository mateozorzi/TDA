"""
Separacion R-Cliques: Dado un grado y un valor entero R, se pueden se parar
todos los vertices en a lo sumo R vertices (cant cliques = k <= R)?
Coloreo: Dado un grafo y un valor entero k, se puede colorear los vertices 
del grafo de manera que se utilicen a los sumo k colores?

1. Verifico que rC este en NP, con un validador polionmial

2. Reduzo cun problema que se que es NP-C a rC, para comprobar
que rC tambien es NP-C

coloreo(grafo, k) <=p rC(grafo', R)
Para esta reduccion, tenemos una caja negra que resuelve un problem de rC, el cual
esta instancia es una solucion correcta para el problema de coloreo.
Para esto debemos crar un grafo copia del original -> grafo', en el cual se invierten todas las adyacencias
de los vertices. En este nuevo grafo, los vertices que no eran adyacnetes ahora lo son.
Al valor de R le damos el mismo que k, ya que buscamos a lo sumo k colores, lo mismo que decir
que buscamos a lo sumo R cliques. Entonces k == R.
Si al utilizar la caja negra con los parametros correspondientes
Y obtenemos True del problema de decision de rC,es decir, existen a lo sumo R cliques
donde la union de estos a como resultado todos los vertices. Entonces existen k colores 
con los que pintar a los vertices del grafo original.

Si hay coloreo hay rC:
Si podemos colorear el grafo en a los sumo k colores, podremos organizar los vertices de grafo' en 
a lo sumo R cliques. Esto ya que los vertices que se colorean del mismo color, no son adyacentes en grafo, pero si en grafo'. Por lo que,
pueden pertenecer a un mismo clique.
Entonces en los conjuntos de cliques, no habran vertices que sean adyacnetes del grafo original.

Si hay rC, hay coloreo:
A su vez, si podemos separar los vertices en a los sumo R cliques en grafo', esto quiere decir
que en el grafo original tambien podremos colorear los vertices en a lo sumo k colores, siendo los vertices
del mismo color no adycnetes entre si en el grafo original, pero en grafo' al estar invertidas las ady
perteneceran al mismo clique.

En conclusion, con esta reduccion podemos afrimar que el problema e rC es NP-C
"""

def esClique(clique, grafo):
    for i in range(len(clique)):
        for j in range(len(clique)):
            if i == j:
                continue
            if not grafo.estan_unidos(clique[i], clique[j]):
                return False
    
    return True

def validador(grafo, R, cliques):
    if len(cliques) < R:
        return False
    
    for clique in cliques: #O(c*v^2)
        if not esClique(clique, grafo):
            return False
        
    #comprobar que un vertice no se repita
    # c = cantidad de cliques
    for i in range(len(cliques)): #O(c^2*v)
        for j in range(len(cliques)):
            if i == j:
                continue
            verticesJ = set(cliques[j])

            for v in cliques[i]:
                if v in verticesJ:
                    return False #hay un vertice que se repite en dos cliques
        
        return False     
        
    return True

#complejidad O( c*(v^2) + v*(c^2) )
    
