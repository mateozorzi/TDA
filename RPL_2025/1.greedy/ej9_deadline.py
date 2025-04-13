"""
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0).
Nuestra latencia máxima será aquella i que maximice el valor L_i.
Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. Indicar y justificar la complejidad del algoritmo implementado.

Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""
#T_tareas[i] = cuanto dura la tarea i
#L_deadline[i] = tiempo de deadline
def minimizar_latencia(L_deadline, T_tareas):
    if len(T_tareas) == 0:
        return []
    
    tiempo = 0

    tarea_deadline = []
    for i in range(len(T_tareas)):
        tarea = []
        tarea.append(T_tareas[i])
        tarea.append(L_deadline[i])
        tarea_deadline.append(tarea)
    
    tarea_deadline = sorted(tarea_deadline, key=lambda x:x[1]) #ordeno por las tareas que tengan un deadline mas corto
    orden = []


    for i in range(len(tarea_deadline)):
        latencia = 0
        tiempo += tarea_deadline[i][0]
        if tiempo > tarea_deadline[i][1]:
            latencia += (tiempo-tarea_deadline[i][1])
        orden.append((tarea_deadline[i][0], latencia))
    
    return orden

#Regla greedy: En mi situacion aactual busco realizar la tares que tenga el deadline mas proximo a finalizar, asi buscando minimzar la latencia de las tareas total
#Es optimo, ya que al realizar primero las tareas que menor deadline tiene, minimzo las latencias en los primeros trabajos