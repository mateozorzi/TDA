"""
Definir los problemas de decisión de Camino Hamiltoniano y Ciclo Hamiltoniano. 
Sabiendo que Ciclo Hamiltoniano es NP-Completo, demostrar que Camino Hamiltoniano es NP-Completo.
"""

""" 
son los dos NP? SI
caminoH (grafo,inicio, final) ->True
                ->False

cicloH (grafo) ->True
                ->False
NP-C

Para demostrar si caminoH es NP-C, reduzco:
cicloH <=p caminoH

Elijo vertice al azar y creo un nuevo grafo,m donde a este vertice lo parto en 2,
v' solo tendra las salidas de v
v'' solo tendra las entradas de v
Paso este grafo a mi caja negra que resuelve caminoH, si da True es decir ecxiste un camino
de empieza en v' y termina en v'' y pasa por todos los vertices. Esto quiere decir que en mi grafo
original existe un cicli que empieza en v y termina en v.
Si pruebo con un vertice y da false, debo considerar otro hasa probar con todos
caminoH es NP-C
"""