def calculoOptimos(trabajos):
    optimos = [0] * (len(trabajos)+1)
    optimos[0] = 0
    optimos[1] = trabajos[0]
    optimos[2] = trabajos[0] + trabajos[1]

    #ec de recurrencia:
    #opt del dia i = maximo entre: el optimo anterior, trabajr el dia pero no trabajr el anterior o trabajar los ultimos dos dias
    for i in range(3,len(optimos)):
        optimos[i] = max(optimos[i-1], trabajos[i-1] + optimos[i-2], trabajos[i-1] + trabajos[i-2] + optimos[i-3])

    return optimos

def inversionOptimos(trabajos, optimos, pos, resultados):
    if pos <= 1:
        resultados.append(trabajos[pos-1])
        return resultados
    
    if optimos[pos-1] >=  trabajos[pos-1] + optimos[pos-2] and optimos[pos-1] >= trabajos[pos-1] + trabajos[pos-2] + optimos[pos-3]:
        return inversionOptimos(trabajos,optimos,pos-1,resultados)
    elif trabajos[pos-1] + optimos[pos-2] >= trabajos[pos-1] + trabajos[pos-2] + optimos[pos-3]:
        resultados.append(trabajos[pos-1])
        return inversionOptimos(trabajos, optimos, pos-2, resultados)
    else:
        resultados.append(trabajos[pos-1])
        resultados.append(trabajos[pos-2])
        return inversionOptimos(trabajos, optimos, pos-3, resultados)

def juanElNoVago(trabajos):
    optimos = calculoOptimos(trabajos)

    resultados = []
    inversionOptimos(trabajos, optimos, len(optimos)-1, resultados)

    resultados = list(reversed(resultados))
    return resultados


t = [100,20,90,30,50]
print(juanElNoVago(t))
