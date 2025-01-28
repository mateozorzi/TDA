"""
Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). 
Dado un grafo dirigido y dos vértices 
s y t, encontrar el máximo número de caminos disjuntos s-t en G. 
Dar una metodología, explicando en detalle cómo se modela el problema, 
cómo se lo resuelve 
y cómo se consigue el máximo número de caminos disjuntos. 
¿Cuál es el orden temporal de la solución implementada?

Si ponemos todos los pesos de las aristas en 1, el algo FF obtendria los maximos caminos dijuntos
el flujo maximo sumaria la cantidad de caminos disjuntos
Complejidad O(V*A), como las aritas son de peso unitario se reduce la complejidad
"""