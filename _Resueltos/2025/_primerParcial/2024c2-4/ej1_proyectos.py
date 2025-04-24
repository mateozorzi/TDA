"""
Tenemos un listado de proyectos a realizar, que tienen tiempo de inicio y tiempo de finalización. Contamos además con K equipos que
pueden realizar los proyectos. Cada proyecto puede estar asignado a un único equipo (o ninguno, si no se realiza). No hay distinción
entre los equipos (todos pueden realizar todos los proyectos). Un mismo equipo no puede estar trabajando en dos proyectos a la
vez, aunque varios equipos pueden estar trabajando en proyectos diferentes en simultáneo sin problemas. Implementar un algoritmo
greedy que determine la asignación de proyectos a los diferentes equipos, de tal manera que se maximice la cantidad de proyectos a
realizar. Indicar y justificar la complejidad del algoritmo implementado. Indicar por qué se trata, en efecto, de un algoritmo greedy.
El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo (es muy probable que el algoritmo NO sea óptimo,
así que pensar bien por un contraejemplo antes de decir que lo es)
"""


#proy[i] = (inicio, fin)
def proyectos(proy, K):
    proy = sorted(proyectos, key=lambda x: x[1])

    asignacion = {i:[] for i in range(K)}


    for p in proy:
        for i in range(K):
            proyectos_equipo = asignacion[i]
            if len(proyectos_equipo) == 0:
                #este equipo no tiene asignado ningun proyecto
                #no se puede superponer con otro proyecto
                proyectos_equipo.append(p)
                break
            #si ya tiene proyectos asignados, veo cuando tiene finalizacion el ultimo poryecto asignado
            #(que tiene tiempo de finalizacion mayor)
            ultimo_proyecto = proyectos_equipo[-1]
            tiempo_finalizacion = ultimo_proyecto[1]

            tiempo_inicio_proyecto_actual = p[0]
            if tiempo_finalizacion >= tiempo_inicio_proyecto_actual:
                #se superponen, no puedo asignar este proyercto a este equipo
                continue

            #si pasa todas las verifcaciones, este proyecto puede ser realizado por este equipo
            proyectos_equipo.append(p)
            break

#Regla greedy: En mi situacion local, busco asignar un proyecto de menor tiempo de finalizacion (termina antes) al primer equipo que tenga ese horario libre
#Es optimo? 