import grafo

def caminos_hijos(cuadrasAdy, casa, escuela):
    g = grafo.Grafo()

    set_cuadras = set()
    for esquina in cuadrasAdy:
        for cuadra in esquina: #O(e * c)
            if cuadra not in set_cuadras:
                set_cuadras.add(cuadra)
                g.agregar_vertice(cuadra)

    for esquina in cuadrasAdy: #O(e)
        g.agregar_arista(esquina[0], esquina[1], 1)
    
    g.agregar_vertice(escuela, "super_sumidero",5)
    g.agregar_vertice("super_fuente", casa, 5)

    return g

#resuelvo por FF calculando el flujo maximo. Si este es igual a 5, esntonces los 5 hijso pueden llegar a la escual sin cruzarse por la misma cuadra



