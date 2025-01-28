def orden_topologico(grafo):
    grados = {}
    for v in grafo:
        grados [v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
        grados [w] += 1 #aumento en 1 el grado de entrada si encuentro arista
    q = Cola()
    for v in grafo:
        if grados [v] == 0:
        q. encolar (v)
    resul = []
    while not q. esta_vacia():
        v = q. desencolar()
        resul. append (v)
        for w in grafo.adyacentes(v):
            grados [w] -= 1 #voy desencolando los de grado 0 y restando en 1 a la orden de los adyacentes
            if grados[v] == 0:
                q.encolar(w) #si llega a cero su grado lo encolo
    if len (resul) == len (grafo):
        return resul
    else:
        return None # El grafo tiene algun ciclo