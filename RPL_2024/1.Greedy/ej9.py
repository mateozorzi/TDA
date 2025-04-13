def minimizar_latencia(L_deadline, T_tareas):
    if(len(T_tareas) == 0):
        return []
    tareasYdeadline = []
    for i in range(len(T_tareas)): #O(n)
        aux = []
        aux.append(T_tareas[i])
        aux.append(L_deadline(i))
        tareasYdeadline.append(aux)

    tareasYdeadline = sorted(tareasYdeadline, key=lambda x: x[1])
    tiempo = 0

    tareas = []
    for tarea in tareasYdeadline: #O(n)
        final = tiempo + tarea[0]
        if(final - tarea[1] > 0):
            latencia = final - tarea[1]
        else:
            latencia = 0
        tiempo = final
        aux = (tarea[0],latencia)
        tareas.append(aux)


    return tareas

t = [10,1]
d = [12,2]

minimizar_latencia(d,t)