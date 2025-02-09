def buscarOptimos(k):
    optimos = [0] * (k+1)
    #casos base
    optimos[0] = 0
    optimos[1] = 1
    optimos[2] = 2

    #ec de recurrencia:
    #opt[i] -> k//2 == 0 -> min(opt[i//2], opt[i-1]) + 1 #Multiplico por 2 o sumo 1
           #-> k//2 != 0 -> opt[i-1] + 1 #Sumo 1

    for i in range(3, len(optimos)):
        if i % 2 == 0:
            optimos[i] = min(optimos[i//2], optimos[i-1]) + 1
        else:
            optimos[i] = optimos[i-1] + 1

    return optimos 

def reconstruccion(k, optimos, pos, operaciones):
    if pos <= 0:
        return operaciones
    
    if pos % 2 == 0:
        if optimos[pos//2] < optimos[pos-1]:
            operaciones.append("x2")
            return reconstruccion(k, optimos, pos//2, operaciones)
    
    operaciones.append("+1")
    return reconstruccion(k ,optimos, pos-1, operaciones)

def minOp(k):
    optimos = buscarOptimos(k) #O(k)

    operaciones = []
    operaciones = reconstruccion(k, optimos, len(optimos)-1, operaciones) #O(k)
    operaciones = list(reversed(operaciones))

    return optimos[-1], operaciones

#complejidad O(k)

k = 20
cant, op = minOp(k)
print(f"Cant: {cant}")
print(f"op: {op}")