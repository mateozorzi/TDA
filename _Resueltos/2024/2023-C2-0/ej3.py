"""
DS: Dado un grafo G y un numero K, existe un subconjunto de a lo sumo k vertices dado que para todo v
se cumple una de estas dos condicones:
    1. v esta en el subconjunto
    2. v es adyacente a un elemento del subconjunto

Para probar que DS es NP-C
1. validador polinomial, comprueba que DS esta en NP
2. Reducir un problema NP-C a DS

Reduccion:
VC: Dado un grafo G' y un numero k', existe un subconjunto de vertices de a lo sumo k' vertices,
que cubra todas las aristas?
VC(G', k') <=p DS(G, k)

Dada la reduccion, se realiza una trnasformacion. A partir de G' creo un nuevo grafo G, donde por cada par de vertices
unidos en G', agrego un nuevo vertice unido a estos dos que simbolizara la arista que comparten
A su vez, como los dos problemas de decision buscan minimizar el tamaño del subconjunto,
en este caso k' == k == K

Si hay VC hay DS:
Dada la transformacion, si en G' existia un VC de a lo sumo K, entonces en este nuevo grafo G habra un DS de a lo
sumo tamaño K. Esto debido a que se agregaron vertices que representan las aristas del grafo,unidos a los dos vertices
de la arista. Por lo que si existe un conjunto que cubra todas las aristas del grafo G' (vertex cover), en el 
grafo G todos los vertices estaran dominados, ya sea los vertices originales del grafo (porque si no esta v en el conjunto,
estara w) y los vertices que representan las aristas (ya que v o w estan el conjunto).

Si hay DS hay VC:
Dada la instancia y la tranformacion planteada, si en G existe un conjunto DS, donde las vertices que representan las
aristas estan siendo dominadas, entonces en el grafo G' todos los vertices estaran cubiertos, dado que en G los vertices 
que simbolizan las aristas son ady a algun elemento del conjunto, entonces estos elementos estaran cubiriendo todas
las aristas en el grafo G'.


"""

def esAdy(grafo, vertice, solucion):
    for s in solucion:
        if grafo.estan_unidos(vertice, s):
            return True
    return False

def validador(grafo, vertices, solucion, k):
    if len(solucion) > k:
        return False

    setVertices = set(vertices)
    for v in solucion:
        if v not in setVertices:
            return False
        
    setSolucion = set(solucion)
    for w in vertices:
        if w in setSolucion:
            continue
        if esAdy(grafo, w, solucion):
            continue

    
                
    return True