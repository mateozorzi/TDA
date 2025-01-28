def buscarOptimos(trabajos):
    optimos = [0] * (len(trabajos)+1)
    optimos[0] = 0
    optimos[1] = trabajos[0]

    for i in range(1, len(trabajos)):
        optimos[i+1] = max(optimos[i], optimos[i-1] + trabajos[i])

    return optimos

def reconstruirSolucion(trabajos, optimos, n, trabajos_realizados):
    if n <= 0:
        return trabajos_realizados
    
    if optimos[n-1] > optimos[n-2]: #trabaje el dia n
        trabajos_realizados.append(n-2)
        return reconstruirSolucion(trabajos, optimos, n-2, trabajos_realizados)
    else:
        #trabaje el dia n-1
        return reconstruirSolucion(trabajos, optimos, n-1, trabajos_realizados)

def juan_el_vago(trabajos):
    if not trabajos:
        return []
    optimos = buscarOptimos(trabajos) #O(n)

    trabajos_realizados = []
    trabajos_realizados = reconstruirSolucion(trabajos, optimos, len(optimos), trabajos_realizados) #O(n)
    trabajos_realizados = trabajos_realizados[::-1] #O(nlogn)
    
    # devolver un arreglo de los índices de días a trabajar
    return trabajos_realizados

#Complejidad O(nlogn)


#ec de recurrencia:
#si trabajo el dia i, no puedo trabajr el dia i+1
# T(i) = max (optimo[i-1] , optimo[i-2] + trabajar[i])
#optimo[i-1] -> tarbaajar ayer, no trabajar hoy
#optimo[i-2] + trabajo[i] -> no trabajar ayer, trabajar hoy

trabajos = [100, 5, 50, 1, 1, 200]
#Devolver: [0, 2, 5]
print(juan_el_vago(trabajos))