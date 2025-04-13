import grafo
#alumnos -> dict con clave nombre del alumno y un set de libros que quiere
#libros -> set de libros presentes en la biblioteca
def modelado(alumnos, libros):
    g = grafo.Grafo()

    g.agregar_vertice("biblioteca") #fuente
    g.agregar_vertice("Prestados") #sumidero

    for l in libros:
        g.agregar_vertice(l)
        g.agregar_arista("biblioteca", l, 3) #la maxima cantidad de copias pretadas de uin libro es 3
        
    for a in alumnos:
        g.agregar_vertice(a)
        g.agregar_arista(a, "Prestados", 10) #10 es la cantidad maxima que un alumno puede pedir prestado
    

    #ahora uno los vertices de los alumnos con los de los libros que quieren

    for a in alumnos:
        for libro in alumnos[a]:
            g.agregar_arista(libro, a, 1) #el alumno se lleva una sola copia de cada libro
    
    return g

def biblioteca(alumnos, libros):
    g = modelado(alumnos, libros)

    #el flujo del problema seran la cantidad de libros prestados, calculo el flujo con FF
    flujo = ford_fulkerson(g, "biblioteca", "Prestados")

    cantidad_max_prestados = 0

    for (v1,v2) in flujo:
        if v2 == "Prestados":
            cantidad_max_prestados += flujo[(v1,v2)] #sumo la cantidad de prestados de cada alumno
    
    return cantidad_max_prestados
#complejiodad del problema:
#El modelado es O(a+l) donde a es la cantidad de alumnos y l la cantidad de libros
#El calculo del flujo es O(V * (E^2) ) donde V es la cantidad de vertices y E la cantidad de aristas
#la comlejidad total es O(a + l + V * (E^2) ) = O(V * (E^2))