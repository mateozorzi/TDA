"""Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, 
reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, 
e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. 
Indicar y justificar la complejidad del algoritmo implementado."""

def conexiones_charlas(charlas):
    conectados = [0] * (len(charlas))
    for i in range(len(charlas)-1,-1,-1):
        dif = 9999999
        indice = -1
        for j in range(len(charlas)):
            if charlas[i][0] - charlas[j][1] >= 0:
                if charlas[i][0] - charlas[j][1] <= dif:
                    dif = charlas[i][0] - charlas[j][1]
                    indice = j
        conectados[i] = indice
    
    return conectados
        

def scheduling(charlas):
    charlasOptimas = []
    charlas = sorted(charlas, key=lambda x: x[1])               #O(nlogn)
    
    conexionesOptimas = conexiones_charlas(charlas)             #O(n^2)

    #funcion de recurrencia max(peso[actual]+opt[j], opt[j-1])

    optimo = scheduiling_dinamico(charlas,conexionesOptimas)    #O(n)

    charlasOptimas = scheduling_solucion(charlas,conexionesOptimas,optimo,[],len(charlas)-1) #O(n)

    charlasOptimas = sorted(charlasOptimas,key=lambda x: x[1]) #O(nlogn)

    return charlasOptimas
#Complejidad algrotimo -> O(n^2)

def scheduling_solucion(charlas,conexionesOptimas,optimo,solucion,pos): #A = 1
                                                                        #B = 1
                                                                        #C = 
    if pos == -1:
        return solucion
    
    if conexionesOptimas[pos] == -1: #Si no tiene conectado con otra charla, solo puedo dar esta
        nuevoOptimo = charlas[pos][2]
    else: 
        nuevoOptimo = charlas[pos][2]+optimo[conexionesOptimas[pos]+1]
        
    anteriorOptimo = optimo[pos]

    if nuevoOptimo >= anteriorOptimo:
        solucion.append(charlas[pos])
        return scheduling_solucion(charlas,conexionesOptimas,optimo,solucion,conexionesOptimas[pos])
    else:
        return scheduling_solucion(charlas,conexionesOptimas,optimo,solucion,pos-1)


def scheduiling_dinamico(charlas, conexionesOptimas):
    optimo = [0] * (len(charlas)+1)
    optimo[0] = 0

    for i in range(len(charlas)):
        if conexionesOptimas[i] == -1: #Si no tiene conectado con otra charla, solo puedo dar esta
            nuevoOptimo = charlas[i][2]
        else: 
            nuevoOptimo = charlas[i][2]+optimo[conexionesOptimas[i]+1]
        
        anteriorOptimo = optimo[i]
        optimo[i+1] = max(nuevoOptimo, anteriorOptimo)
    
    return optimo

charlas = [
    (4, 8, 5), 
    (14, 16, 2), 
    (16, 17, 4),
    (2, 8, 4),
    (9, 11, 4),
    (11, 12, 1)
]
print(scheduling(charlas))
