"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, 
tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. 
El problema de decisión del set dominante implica, dado un grafo G y un número
k, determinar si existe un set dominante D de a lo sumo tamaño k. 
Demostrar que el Dominating Set Problem es un problema NP-Completo. 
Ayuda: recomendamos recordar Vertex Cover, que puede ser útil para esto.
"""

"""
Problema de decision:
DM: Existe un subconjunto de vertices, de tamaño a lo sumo k. Tal que para cualquier vertice
o pertenece a D, o el ady a D.

Es NP? SI, puedo crear un validador polinomial que verifique una solucion

Reduzco:
VC <=p DM

creo un nuevo grafo, con los vertices y aristas originales
pero por cada arista del grafo original, agrego un vertice que este unido a los dos vertices que se unen en la arista
utilizo la caja negra de DM para ver si encuentra un set dominante.


Si hay un DM, habra un VC valido?
Si hay un DM, habra un VC de a lo sumo k elementos, ya que al elegir uno de los tres vertices del triangulo que forme para cada arista
se representara en el VC como una arista cubierta, y que uno de los dos vertices que la unen deberia estar en el subconjunto VC. CUbriendo 
todas las aristas del grafo

si y solo si

Si hay VC, habra un DM valido?
Si hay un vertex cover de al menos k elemenotos en el grafo original, con la reduccion se encontrara un 
set dominante vlido en el grafo de al menos k elementos. Ya que ese nuevo vertice que agregamos por cada arista, 
se podria entender para el problema original de VC, como que la arista esta siendo cubierta.

"""