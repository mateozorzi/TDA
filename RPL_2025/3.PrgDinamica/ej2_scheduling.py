"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""
def buscarConexiones(charlas):
    #busco la primera charla anterior compatible con la actual, entonces todas las anteriores tambien seran compatibles porque estan ordenadas porordend e finalizacion
    conexiones = [-1] * len(charlas)

    for i in range(len(charlas)-1,-1,-1):
        actual = charlas[i]
        if actual[0] == 0:
            #comienza primero, no puede haber una charla antes 
            continue
        for j in range(i-1,-1,-1):
            anterior = charlas[j]

            if actual == anterior:
                continue

            if anterior[1] <= actual[0]:
                conexiones[i] = j
                break
    
    return conexiones


def buscarOptimos(charlas, conexiones):
    #Ec de recurrencia:
    #opt[i] = max(  opt[i-1]  ,   charlas[i-1][1] + opt[conexiones[i-1]]    ) if conexiones[i] != -1, else opt[i] = max(opt[i-1], charlas[i-1][1])

    optimos = [0] * (len(charlas)+1)
    optimos[0] = 0 #ninguna charla
    optimos[1] = charlas[0][2] #la primera charla

    for i in range(2,len(optimos)):
        if conexiones[i-1] != -1:
            optimos[i] = max(optimos[i-1], charlas[i-1][2] + optimos[conexiones[i-1]+1])
        else:
            optimos[i] = max(optimos[i-1], charlas[i-1][2])

    return optimos


def reconstruccion(charlas, conexiones, optimos, pos, solucion):
    if pos <= 0:
        return solucion
    
    if conexiones[pos-1] != -1:
        if optimos[pos-1] > charlas[pos-1][2] + optimos[conexiones[pos-1]+1]:
            return reconstruccion(charlas, conexiones, optimos, pos-1, solucion)
        else:
            solucion.append(charlas[pos-1])
            return reconstruccion(charlas, conexiones, optimos, conexiones[pos-1]+1, solucion)
    else:
        if optimos[pos-1] > charlas[pos-1][2]:
            return reconstruccion(charlas, conexiones, optimos, pos-1, solucion)
        else:
            solucion.append(charlas[pos-1])
            return reconstruccion(charlas, conexiones, optimos, -1, solucion)    

#charla = [inicio, fin, ganancia]
def scheduling(charlas):
    charlas = sorted(charlas, key=lambda x: x[1])
    conexiones = buscarConexiones(charlas) #O(n^2)
    optimos = buscarOptimos(charlas, conexiones) #O(n)

    solucion = []
    solucion = reconstruccion(charlas, conexiones, optimos, len(optimos)-1, solucion) #O(n)
    solucion = list(reversed(solucion))
    
    return solucion

charlas = [
    (4, 8, 5), 
    (14, 16, 2), 
    (16, 17, 4),
    (2, 8, 4),
    (9, 11, 4),
    (11, 12, 1)
]
print(scheduling(charlas))