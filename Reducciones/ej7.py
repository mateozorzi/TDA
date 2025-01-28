"""
 Definir los problemas de decisión de Independent Set y K-Clique. 
 Hacer una reducción de Independet Set a K-Clique. 
 Dada esta reducción, ¿podemos afirmar que K-Clique es un problema NP-Completo?
"""

"""
Son los dos NP? si
IS(grafo,k) -> True, existe un subconjunto de al menos k elementos
            -> False
IS -> NP-C
            
k_clique(grafo,k)   -> True, existe un subconjunto de al menos k elementos
                    -> False
(subgrafo de tamaño k, donde todos los vertices se conectan)

Para ver si k-clique es NP-C, tengo que reducir:
IS <=p k-clique

A partir de mi grafo original, creo un grafo_complemento. Donde estaran los mismos vertices 
pero borro las aristas del grafo y agrego las que no existen en el original. Y se lo paso  
a mi caja negra que resuelve k-clique. Si da True, existe un subgrafo de al menos tamaño k,
donde los vertices estan conectados. Esto significa que en el gafo original, estos vertices 
no estan conectados, por lo que forman un IS de al menos tamaño k.
Entonces k-clique es NP-C

si existe un IS, hay un k-clique valido?
Si parto de que en mi grafo existe un IS valido, para cada vertice este sera independiente a al menos k-1 vertices.
Si hacemos el grafo complemento, estos vertices independientes formaran un k-clique de al menos tamaño k.

Si y solo si
Si puedo hacer la reduccion a la inversa.
Si hay un k-clique en el grafo, para las conidciones del problema, existe un IS valido?
Si tengo un IS valido. Para cada vertice en el IS, significa que estos no estan conectados entre si.
Si la cantidad de vertices es al menos k
significa que en el otro grafo estos vertices estaran unidos por aristas, y como son al meno k vertices, formaran el k clique

"""