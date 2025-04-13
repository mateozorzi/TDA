import grafo
from ff import FF

def modelado(amigos, partidos, y):
    g = grafo.Grafo()

    g.agregar_vertice("fuente")
    g.agregar_vertice("Sumidero")

    for a in amigos:
        g.agregar_vertice(a[0])
        g.agregar_arista("fuente", a[0], 4)

    for p in partidos:
        g.agregar_vertice(p[0])
        g.agregar_arista(p[0], "Sumidero", y)

    for a in amigos:
        fechasNoDisponibles = set(a[1])
        for p in partidos:
            if p[1] in fechasNoDisponibles:
                continue
            g.agregar_arista(a[0],p[0], 1)

    return g

def voley(amigos, partidos, y):
    g = modelado(amigos, partidos, y)
    flujo = FF(g, "fuente", "Sumidero")

    #inscripcion por partido
    jugadoresInscriptos = {p[0]: [] for p in partidos}
    
    for p in partidos:
        for (v1, v2) in flujo:
            if v2 == p[0] and flujo[(v1, v2)] == 1:
                #v1 es un amigo que juega el partido
                jugadoresInscriptos[p[0]].append(v1)
    
    return jugadoresInscriptos

