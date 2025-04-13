import grafo
#Habitantes[0] = nombre
#Habitantes[1] = partido
#Habitantes[2] = set de clubes
def comision(habitantes):

    g = grafo.Grafo()

    partidos = set()
    clubes = set()

    for h in habitantes:
        if h[1] not in partidos:
            partidos.add(h[1])
            g.agregar_vertice(h[1])
        
        for c in h[2]:
            if c not in clubes:
                clubes.add(c)
                g.agregar_vertice(c)
        
        g.agregar_vertice(h[0])
    
    #fuente y sumidero
    g.agregar_vertice("fuente")
    g.agregar_vertice("sumidero")

    for h in habitantes:
        for p in partidos:
            if h[1] == p:
                g.agregar_arista(p,h[0],1)
                break
    
    for c in clubes:
        for h in habitantes:
            if c in h[2]:
                g.agregar_arista(h[0],c,1)
    
    for p in partidos:
        g.agregar_arista("fuente",p,len(habitantes)//2)
    
    for c in clubes:
        g.agregar_arista(c,"sumidero",1)

    return g