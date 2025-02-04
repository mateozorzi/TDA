import grafo

def hospital(pacientes, medicos):
    g = grafo.Grafo()

    g.agregar_vertice("Fuente")
    g.agregar_vertice("Sumidero")

    for p in pacientes:
        g.agregar_vertice(p[0])
        g.agregar_arista("Fuente", p[0], 1)
    
    especialidades = {}
    for m in medicos:
        g.agregar_vertice(m[0])
        g.agregar_arista(m[0], "Sumidero", len(m[2]))
        especialidad = m[1]
        horarios = m[2]

        if especialidad not in especialidades:
            especialidades[especialidad] = set()
        
        for h in horarios:
            if h not in especialidades[especialidad]:
                especialidades[especialidad].add(h)
                g.agregar_vertice(especialidad + "-" + h)
                g.agregar_arista(especialidad + "-" + h, m[0], 1)

        
    for p in pacientes:
        especialidad = p[1]
        horarios = p[2]
        for e in especialidades:
            if e == especialidad:
                for h in horarios:
                    if h in especialidades[e]:
                        g.agregar_arista(p[0], e + "-" + h, 1)
                break

    return g
#Flujo -> cantidad de turnos que se asignan a los medicos del hospital
#Complejidad: O(p + m + p*e) siendo p la cantidad de pacientes y m la cantidad de medicos