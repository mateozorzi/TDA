import sys
from collections import deque
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

def es_bipartito(grafo):
    grupos = {} #0 pertence al grupo S, 1 pertence al grupo T
    cola = deque()
    if not grafo:
        return True
    
    else:    
        nodoInicial = list(grafo.keys())[0]
        grupos[nodoInicial] = 0
        cola.append(nodoInicial)
        
        
        # Comenzar el recorrido BFS
        for nodo_actual in grafo:
            if nodo_actual not in grupos:
                grupos[nodo_actual] = 0
            #nodo_actual = cola.popleft()

            for a in grafo[nodo_actual]:
                if a not in grupos:
                    grupos[a] = 1 - grupos[nodo_actual]
                    #cola.append(a)
                elif grupos[nodo_actual] == grupos[a]:
                    return False #Conflicto de adyacencia
            
        return True

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3, 5],
    5: [3,4]
}

print(es_bipartito(graph))