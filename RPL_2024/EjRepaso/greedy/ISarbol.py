def buscarHojas(grafo):
    hojas = []
    padres = []
    for v in grafo.obtener_vertices():
        if len(grafo.adyacentes(v)) == 1:
            hojas.append(v)
            padres.append(grafo.adyacentes(w) for w in grafo.adyacentes(v))
    
    return hojas, padres


#regla greedy: agrego al is las hojas del arbol y borro a sus padres, y nuevamete agrego las hojas hata quedarme sin vertices
def ISarbol(grafo):
    is_max = []
    
    while (len(grafo.obtener_vertices()) > 0):
        hojas, padres = buscarHojas(grafo)
        is_max.extend(hojas)
        for v in hojas:
            grafo.borrar_vertice(v)
        for v in padres:
            grafo.borrar_vertice(v)
    
    return is_max

#Es greddy ya que en cada iteracion agrega al conjunto los vertices hoja del grafo, borrando a los padres de estas hojas
# ya qu eno pueden estar en el conjunto, hasta quedarse sin vertices
# es optimo ya que al ir agregando las hojas y eliminando los padres, se asegura que la proxima iteracion alla la 
# maxima cantidad de nuevas hojas que eran los padres de los padres borrados y que peuden agregarse al conjunto.
