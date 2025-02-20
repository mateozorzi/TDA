"""Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, 
reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, 
e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. 
Indicar y justificar la complejidad del algoritmo implementado."""

def scheduling_aux(charlas):
    p = [-1] * len(charlas)
    #busco las charlas mas proximas habilitadas con la charla actual
    for i in range(len(charlas)):
        for j in range(i-1, -1, -1):
            if charlas[i][0] >= charlas[j][1]:
                p[i] = j
                break
    return p

def buscarOptimos(charlas,p):
    optimos = [0] * len(charlas)
    optimos[0] = charlas[0][2]

    for i in range(1,len(charlas)):
        if p[i] == -1:
            optimos[i] = max(charlas[i][2], optimos[i-1])
        else:
            optimos[i] =max ( max(   ( optimos[j] for j in range(  p[i]+1  ) )   ) + charlas[i][2] , optimos[i-1] )
    
    return optimos

def reconstruccion(charlas, p ,optimos, pos, sol):
    if pos == -1:
        return sol
    if pos == 0:
        sol.append(charlas[pos])
        return sol
    if optimos[pos] == charlas[pos][2] + optimos[p[pos]]:
        sol.append(charlas[pos])
        return reconstruccion(charlas, p, optimos, p[pos], sol)
    elif optimos[pos] == optimos[pos-1]:
        return reconstruccion(charlas, p , optimos, pos-1, sol)


#charlas = (incio, fin, ganancia)
def scheduling(charlas):
    charlas = sorted(charlas, key=lambda x: x[1])

    p = scheduling_aux(charlas)

    optimos = buscarOptimos(charlas,p)
    
    sol = []
    sol = reconstruccion(charlas, p, optimos, len(optimos)-1, sol)
    return sol

charlas = [
    (4, 8, 5), 
    (14, 16, 2), 
    (16, 17, 4),
    (2, 8, 4),
    (9, 11, 4),
    (11, 12, 1)
]
print(scheduling(charlas))