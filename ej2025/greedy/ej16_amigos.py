import grafo


def modelar_grafo(amigos):
    agregados = set()
    g = grafo.Grafo()
    for a1,a2 in amigos:
        if a1 not in agregados:
            g.agregar_vertice(f"{a1}")
            agregados.add(a1)
        if a2 not in agregados:
            g.agregar_vertice(f"{a2}")
            agregados.add(a2)

        g.agregar_arista(f"{a1}",f"{a2}",1)
    return g

def obtener_invitados(conocidos):
    g = modelar_grafo(conocidos)

    hubo_desinvitado = True

    while hubo_desinvitado: 
        hubo_desinvitado = False 
        borrar = []  
        for v in g.obtener_vertices():
            if len(g.adyacentes(v)) < 4:
                #no puede ser invitados
                borrar.append(v)
                hubo_desinvitado = True
                break
        for w in borrar:
            g.borrar_vertice(w)

    return g.obtener_vertices()

#Regla greedy, dado mi estado actual observo si hay algun vertice que tenga menos de 4 aristas, 
#si encuentro borro esta arista porque no puede ser parte de la solucion.
#Me sigo fijando hasta que le pregunta a todos los invitados cuantos conocen y todos me digan 4 o mas

#Es optimo, ya que al ir bortrando los vertices con menos de 4 ady, y chequear nuevamente si algun ady se actualizo en otro vertice
#enotnces me aseguro que siempre queden lso vertices que tengan 4 ady.

