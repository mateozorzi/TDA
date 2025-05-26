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
VC: existe un conjunto solucion de a lo sumo k vertices, tal que por cada par de vertices adyacentes, al menos uno e los dos
este en el conjunto
DM: Existe un conjunto solucion de a lo sumo k vertices, tal que para cada vertice se cumple que: v pertences al conjunto o v es adyacentea aun vertice del conjunto

Dada una iunstancia incial del problema de VC, con un grafo G y un vertice k. Se realiza una transofrmacion,
para crear una instancia del problema de DM, un grafo G' y un k'.
Creo el grafo G' como una copia de G, pero agrego por cada par de vertice unidos, un tercer vertice que mostraria la union entre estos dos vertices,
si v -- w en G, entonces en G' tednria v -- w, v -- v,w y w -- v,w
y k' = k, ya que ambos problemas buscan a lo sumo k vertice en la solucion

Si hay VC hay DM
Si dado G y k, existe un conjunto VC, dado la transformacion tambien deberia exsitir un DM
Dado que G' tiene los mismo vertices que G, mas el vertice que se agrego que muestra la union de los vertices, entonces si un vertice v esta unido a w, y esta dentro de la solucion de VC
Entonces al hacer la transofrmacion y reoslver por la caja negra de DM, v podria estar dentro de la solucion ya que cumple con las eglas de DM y sus adyacentes tambien, al ser adyacentes a v


Si hay DM hay VC
SI dada la trasnformacion, al caja negra de DM devuelve que existe un conjunto solucion DM en G', entonces deberia existir unnconjunto solucion VC en G.
Al agregar un vertice por cada arista, unionedolo a cada par de vertice, simbolizando launion de ellos, para que el vertice que simboliza la arista
este dominada por algun vertice, se debe cumplir que, simepre para una arsita v -- w, al menos 
uno de los dos vertices estara en el conjunto solucion DM, como v y w tambien estan unidos en G, los vertices que se agregan al conjunto solucion DM
formara un conjunto solucon valido de VC.


"""


def validador(grafo, solucion,k):
    if len(solucion) > k:
        return False #no es de alo sumo k
    
    for v in grafo.obtener_vertices():
        if v in solucion:
            continue
        adyacentes = grafo.adyacentes(v)
        encontrado = False
        for ady in adyacentes:
            if ady in solucion:
                encontrado = True
        
        if not encontrado:
            return False
        
    return True
    