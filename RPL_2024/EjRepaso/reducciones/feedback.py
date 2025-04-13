from bfs import bfs
"""
feedback: Dao un grafo G, se puede construir un subconjunto X de vertices
de a lo sumo k verttices, tal que si se eliminan del grafo los vertices de
X, este no tiene ciclos.

1. Validador polinomial, comprueba que feedback esta en NP

2. Reduccion polinomial de un problema NP-C a feedback.

Reduccion:
VC(G, k) <=p feedback(G',k)

VC: dado un grafo G y un entero k, existe un subconunto de vertices
tal que por cada par de vertices al menos uno de los dos este en el conjunto
y el tamaño de la solucion sea a los sumo k.

Para la reduccion se realiza un atransformacion:
A parti de G, se cre un nuevo grafo G' en el que se crean nuevos vertices,
por cada arista (u,v) se cre un vertice w y se los aune a u y v respectivbamnte.
De esta forma hay ciclos en G'.
Luego el valor de K se mantiene.

Si hay VC hay  feedback:
Si en el grafo G hay un vertex cover de tamaño a lo sumo k, entonces en G'
existira un suibconjunto X de vertices de tamaño a lo sumo k tal que si se
eliminan del grafo, este dejara de tener ciclos. Esto es ya que al agregar un
tercer vertice por cada par de vertices ady, se crean ciclos. Los vertices
que forman el vertex cover en G seran los vertices a eliminar del grafo G'
para que deje de tener ciclos. Ya que se debe elimanr por cada triangulo formado
uno de los vertices, en vertex cover esto seria agrwegar uno de los vertices al 
conjunto solucion y asi cubrir el vertice
por ej:
Si en G tenemos la arista (u,v), en G' tendremos (u,v), (w,u), (w,v)
Para que no haya un ciclo en G' debemos de eliminar uno de los vertices,
ya sea u o v. Mientras en G para crear un vertex cover, uno de los dos vertices
debe estar en el conjunto solucion.

Si hay feedback hay VC:
Si en G' se encuentra un feedback set dado que en el grafo resultante no hay mas ciclos,
entonces dada la insatncia creada por la trnasformacion, en G habra un vertex cover
de tamaño a lo sumo k. Esto dado que lso vertices que se eliminan en G' para que no haya ciclos,
seran los mismo que cubran las aristas del grafo G. Ya que en G' se creo un triangulo de aristas por
cada par de vertice, entonces para destruir el ciclo uno de los vertices del triangulo  se debe eliminar, para
la aruista (u,v) se creo un tirnagulo con el nuevo vertice w, para elimanr el ciclo u o v
se debe elimainar.
Esto en G representaria que la  arista (u,v) esta siendo cubierta ya sea por u o v
"""

def validador(grafo, vertices, X, grafoResultante,k):
    if len(X) > k:
        return False
    
    setVertices = set(vertices)
    setVerticesResultantes = set(grafoResultante.obtener_vertices())
    for v in X: #O(k)
        if v not in setVertices:
            return False
        if v in setVerticesResultantes:
            return False
    

    for v in grafoResultante.obtener_vertices():
        camino = bfs(grafoResultante,v,v) #O(V + A)
        if camino != None:
            return False

    return True
