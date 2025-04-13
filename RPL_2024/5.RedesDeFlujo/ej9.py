"""
Dado un grafo no dirigido, un match es un subconjunto de las aristas 
en el cual para todo vértice v a lo sumo una arista del match incide en 
v (en el match, tienen grado a lo sumo 1). Decimos que el vértice v está matcheado 
si hay alguna arista que incida en él (sino, está unmatcheado). 
El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible). 
Dar una metodología para encontrar el matching máximo de un grafo, 
explicando en detalle cómo se modela el problema, 
cómo se lo resuelve y cómo se consigue el matching máximo. 
¿Cuál es el orden temporal de la solución implementada?

Creamos una superfuente y un super sumidero. Unimos y mandamos flujo a los nodos, 
estas artistas solole ponemos peso 1, 
por lo que solo se podran usar una sola vez por cada arista
por lo que maximizaremos la cantidad de aristas utilizadas
Uso el algortimo FF, y modifico el peso de todas las aristas a 1.
Complejidad O(V*A)
"""