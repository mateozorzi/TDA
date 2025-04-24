"""
Tenemos un listado de proyectos a realizar, que tienen tiempo de inicio y tiempo de finalización. Contamos además con K equipos que
pueden realizar los proyectos. Cada proyecto puede estar asignado a un único equipo (o ninguno, si no se realiza). No hay distinción
entre los equipos (todos pueden realizar todos los proyectos). Un mismo equipo no puede estar trabajando en dos proyectos a la
vez, aunque varios equipos pueden estar trabajando en proyectos diferentes en simultáneo sin problemas. Implementar un algoritmo
greedy que determine la asignación de proyectos a los diferentes equipos, de tal manera que se maximice la cantidad de proyectos a
realizar. Indicar y justificar la complejidad del algoritmo implementado. Indicar por qué se trata, en efecto, de un algoritmo greedy.
El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo (es muy probable que el algoritmo NO sea óptimo,
así que pensar bien por un contraejemplo antes de decir que lo es)

HACER CON BACKTRACKING
"""

def es_compatible(asignaciones_equipo):
    ultima_asignaciones = asignaciones_equipo[-1]
    inicio = ultima_asignaciones[0]

    for i in range(len(asignaciones_equipo)-1):
        actual = asignaciones_equipo[i]
        fin_actual = actual[1]

        if fin_actual >= inicio:
            #se solapa con otra asignacion anterior
            return False
        
    return True


def proyectos_bt(proyectos, indice, K, asignaciones):
    if indice >= len(proyectos):
        return asignaciones

    for i in range(K):
        asignaciones[i].append(proyectos[indice])
        if es_compatible(asignaciones[i]):
            asignaciones = proyectos_bt(proyectos, indice+1, K, asignaciones)
            return asignaciones
        asignaciones[i].pop()
    asignaciones = proyectos_bt(proyectos, indice+1, K, asignaciones) #si sale del for, es que no se pudo asignar este proyecto, lo salteo

    return asignaciones #si llego aca no se puedo asignar todos los proyectos

def proyectos(proy, K):
    asignaciones = {i:[] for i in range(K)}

    indice = 0

    asignaciones = proyectos_bt(proy, indice, K, asignaciones)