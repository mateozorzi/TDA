import grafo

#medicos -> (nombre, dias feriados)
#feriados -> (feriado, fechas de los feriados)

#tengo n medicos, que avisan que que feriados pueden trabajr, solo pueden trabajr 1 dia por epoca de feriados. Y no pueden trabajr mas de F feriados

def modelado(medicos, feriados, F):
    g = grafo.Grafo()

    g.agregar_vertice("fuente")
    g.agregar_vertice("sumidero")

    for n in medicos: #O(n)
        g.agregar_vertice(n[0])
        g.agregar_arista("fuente", n[0], F)
    #O(n)
    
    for f in feriados: #O(f)
        g.agregar_vertice(f[0])
        for dia in f[1]: #O(d)
            g.agregar_vertice(dia)
            g.agregar_arista(f[0], dia, 1)
            g.agregar_arista(dia, "sumidero", 1)
    #O(f*d)
    
    for n in medicos:
        setDias = set(n[1])
        for f in feriados:
            for dia in f[1]:
                if dia in setDias:
                    g.agregar_vertice(n[0], f, 1)
    #O(n*f*d)
    
    return g



def cornograma(medicos, feriados, F):
    grafo = modelado(medicos, feriados, F)