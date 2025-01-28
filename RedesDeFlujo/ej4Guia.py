"""
Dada una red residual, dar un algoritmo que encuentre un camino de aumento 
que minimice el número de aristas utilizadas.

Uso recorrido BFS, que primero encuentra el camino mas corto
"""
import queue
def caminoAumentoMinimo(redResidual, s , t):
    visitados = set()
    caminoMinimo = ()
    padres = {}
    orden = {}
    q = queue.Queue()
    visitados.agregar(s)
    padres [s] = None
    orden[s] = 0
    q.put(s)
    while not q.empty():
        v = q.get()
        for w in redResidual.adyacentes(v):
            if( w not in visitados):
                visitados.add (w)
                padres [w] = v
                orden [w] = orden [v] + 1
                q.put (w)
            
        if v == t:
            caminoAux = []
            nodo_aux = t
            while nodo_aux is not None:
                caminoAux.insert(0, nodo_aux)
                nodo_aux = padres[nodo_aux]
            
            return caminoMinimo
    
    return None
