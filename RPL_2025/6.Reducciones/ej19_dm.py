"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: 
o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. 
El problema de decisión del set dominante implica, dado un grafo G y un número k,
determinar si existe un set dominante D de a lo sumo tamaño k. 
Demostrar que el Dominating Set Problem es un problema NP-Completo. Ayuda: recomendamos recordar Vertex Cover, que puede ser útil para esto

Para comprobar que DM es NP-C:
1. validador polinoimial de una solucion
2. Reduccion de un poroblema NP-C concoido a DM

VC(grafo,k) <= DM(grafo,k)
VC: existe un conjunto solucion de a lo sumo k vertices, tal que por cada par de vertices adyacentes, al menos uno de los dos
este en el conjunto
DM: Existe un conjunto solucion de a lo sumo k vertices, tal que para cada vertice se cumple que: v pertence al conjunto o v es adyacente a un vertice del conjunto

Dada una instancia inicial del problema de VC, con un grafo G y un valor k. Se realiza una transofrmacion,
para crear una instancia del problema de DM, un grafo G' y un k'.
Creo el grafo G' como una copia de G, pero agrego por cada par de vertices unidos, un tercer vertice que mostraria la union entre estos dos vertices,
si v -- w en G, entonces en G' tendria v -- w, v -- (v,w) y w -- (v,w)
y k' = k, ya que ambos problemas buscan a lo sumo k vertice en la solucion

Si hay VC hay DM
Si dado G y k, existe un conjunto VC, el conjunto de vertices en el vc cubre todas las aristas del grafo, entonces exisitria un DM que:
Dado que el grafo G' contiene todos los vertices y aristas de G y ademas se le agregó un vertice que simboliza la union de dos vertices.
Para que todo vertice sea el dominador o este dominado, para cada triangulo formado por u,v,(u,v) al menos uno de ellos debe pertenecer al conjunto DM,
siendo (u,v) el vertice "arista" que simboliza la arista union entre los vertices y lo que VC busca cubrir. Entonces al agregarla al grafo G', DM para teneer un 
set dominante de G' debera incluir al menos uno de los vertices u,v para dominar el triangulo por completo.


Si hay DM hay VC
SI dada la trasnformacion, existe solucion de DM en G', entonces deberia existir un conjunto solucion VC en G.
El vertice "arista" agregado en G' que simboliza la union de dos pares de vertices que comparten arista, hace que DM se vea obligado a incluir 
en el conjunto solucion al menos uno de los vertice, para poder dominar el vertice "arista", de esta forma el conjunto solucion DM indicara que en el 
grafo original los vertices podrian formar un conjunto VC de a lo sumo k vertices. Si dada dos vertices ady u,v en G', que ademas estan unidos al vertice "arista",
si al menos uno de los dos esta en el conjunto DM, entonces este se necesitara en G para armar el conjunto VC minimo. Si en cambio en DM se elige el vertice "arista", significara
que cualquiera de los dos vertices o ambos deben estar en el conjunto VC de G.
"""


def validador(grafo, solucion,k):
    if len(solucion) > k:
        return False #no es de a lo sumo k
    vertices = grafo.obtener_vertices()
    for s in solucion:
        if not s in vertices:
            return False #no existe el vertice
    
    for v in grafo.obtener_vertices():
        #para cada vertice veo:
        # i) si esta en la sol
        # ii) si es ady a un vertice de la sol
        if v in solucion:
            continue
        adyacentes = grafo.adyacentes(v)
        encontrado = False
        for ady in adyacentes:
            if ady in solucion:
                encontrado = True
        
        if not encontrado:
            #no cumple los criterios DM
            return False
        
    return True
#Complejidad O(V + E)
    