"""
El Hitting-Set Problem se define de la siguiente forma: Dado un conjunto de elemento A de n elementos, 
m subconjuntos B1,B2,...,𝐵𝑚 de A (Bi esta incluido en A para todo i) y un numero k 
¿Existe un subconunto C incluido en A, con len(C) <= k,
tal que C tenga al menos un elemento de cada Bi (es decir, C interseccion Bi distinto a vacio)?

Demostrar que el Hitting-Set Problem es un problema NP-Completo.
"""

"""
Es H-S NP? SI, con un validador polinomia puedo verificar una solucion en tiempo polinomial
Problemas de decision:
H-S: Existe un subconjuto C de tamaño <= k, tal que tenga al menosmun elemento de cada subgrupo?
VC: Existe un subgutpo de vertices de tamaño al menos k, que cubre todas las aristas de un grafo?

Yo se que VC es NP-C, entonces puedo reducir el prblema para probar que hitting-set en NP-C
Reduzco:
VC <=p H-S

Creo el conjunto A de elementos con los vertices del grafo, los subgrupos B, estaran formados por aca arista (u,v) y el numero k es el mismo.
Llamos a la caja negra que resuelve H-S. Si devuelve True, existe un conjunto C que tiene al menos un elemento de cada subconjunto, cumple con 
la condicion de VC, ya que por cada arista (u,v) una estara incluida en el subconjunto y se cubriran todas las aristas del grafo.


Si existe un H-S, existe un VC valido:
Como las aristas del grafo estan representadas por lo subgrupos (formados por los vertices que une la arista),
si encuentra a los sumo k subgrupos, sera que se podra formar un conjunto VC de a los sumo k elementos,
por lo que se estaria cubriendo todas las aristas.

si y solo si
Si existe un VC, habra un H-S valido?
Si existen a lo sumo k elemetnos que forman un VC, en el problema de H-S, habran a lo sumo
k subgrupos, formados por los vertices unidos por una arista, tal que habra al menos uno de estos elementos
en el subconjunto C, formando un H-S

"""


