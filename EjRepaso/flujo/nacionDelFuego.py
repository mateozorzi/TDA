import grafo

def flujo_maximo(sistema):
    pass

#rios = [(rioX, cantidadAgua,[riegos]), (...), ...]
#riegos = [(riegoX, cantidadAguaUtilizada), (...), ...]
def modelar_sistema(rios, riegos):
    g = grafo.Grafo(True)

    #creo fuente
    g.agregar_vertice("fuente")
    #creo sumidero
    g.agregar_vertice("sumidero")

    #creo los k rios
    for r in rios: #O(k)
        g.agregar_vertice(r[0])
        g.agregar_arista("fuente", r[0], r[1])

    #creo los m puntos de riego
    for m in riegos: #O(m)
        g.agregar_vertice(m[0])
        g.agregar_arista(m[0], "sumidero", m[1])
    
    #conecto con tuberias los rios y riegos
    for r in rios: #O(k*m)
        setRiegos = set(r[2])
        for m in riegos:
            if m[0] in setRiegos:
                g.agregar_arista(r[0], m[0], r[1])
    
    return g




def obtener_corte_minimo(sistema, flujo):
    pass

def cortar_tuberia(rios, riegos):

    sistema = modelar_sistema(rios, riegos)

    #flujo[(a1,a2)] = flujo que pasa por la arista
    flujo = flujo_maximo(sistema)

    #debo buscar la tuberia que pertenzca al corte minimo y que tenga el mayor flujo posible
    #Corte minimo, suma lo mismo que el flujo maximo

    corteMinimo = obtener_corte_minimo(sistema, flujo)

