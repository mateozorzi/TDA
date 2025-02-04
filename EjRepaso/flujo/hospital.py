import grafo

def hospital(pacientes, medicos):
    g = grafo.Grafo()

    g.agregar_vertice("Fuente")
    g.agregar_vertice("Sumidero")

    for p in pacientes:
        g.agregar_vertice(p[0])
        g.agregar_arista("Fuente", p[0], 1)
    
    especialidades = set()
    horarios = set()
    for m in medicos:
        if m[1] not in especialidades:
            g.agregar_vertice(m[1])
            especialidades.add(m[1])
        
        for h in m[2]:
            if h not in horarios:
                g.agregar_vertice(m[2])
                g.agregar_arista(m[1], h,1)
                g.agregar_arista(m[2], "Sumidero", "inf")
                horarios.add(m[2])
    
    for p in pacientes:
        for e in especialidades:
            g.agregar_arista(p[0], e, 1)

    return g
#Flujo -> cantidad de turnos que se asignan a los medicos del hospital
#Complejidad: O(p + m + p*e) siendo p la cantidad de pacientes y m la cantidad de medicos