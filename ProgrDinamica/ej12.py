"""Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. 
Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. 
La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña,
que denominaremos Gi. Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos.
Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? 
Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa."""


def calculoConexiones(c_publicitaria,P):
    optimos = [[0] *(P+1) for i in range(len(c_publicitaria)+1) ]

    for j in range(1,len(optimos[0])):
        for i in range(1,len(optimos)):
            if c_publicitaria[i-1][1] > j:
                optimos[i][j] = optimos[i-1][j]
            else:
                optimos[i][j] = max(optimos[i-1][j],
                              optimos[i-1][j-c_publicitaria[i-1][1]] + c_publicitaria[i-1][0])

    return optimos

def publicidadesUsadas(c_publicitaria,optimos,pos,publicidades):
    if pos == [0,0]:
        return publicidades
    
    if c_publicitaria[pos[0]-1][1] > pos[1]:
        return publicidadesUsadas(c_publicitaria,optimos,[pos[0]-1,pos[1]],publicidades)
    else:
        if optimos[pos[0]-1][pos[1]-c_publicitaria[pos[0]-1][1]] + c_publicitaria[pos[0]-1][0] > optimos[pos[0]-1][pos[1]]:
            publicidades.append(c_publicitaria[pos[0]-1])
            return publicidadesUsadas(c_publicitaria,optimos,[pos[0]-1,pos[1]-c_publicitaria[pos[0]-1][1]],publicidades)
        else:
            return publicidadesUsadas(c_publicitaria,optimos,[pos[0]-1,pos[1]],publicidades)



# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    optimos = calculoConexiones(c_publicitaria,P)
    publicidades = []
    publicidadesUsadas(c_publicitaria,optimos,[len(optimos)-1, len(optimos[0])-1],publicidades)
    publicidades = list(reversed(publicidades))
    return publicidades
#O(P.n)

campañas = [(5,3), (100,100), (10,5), (9,5), (7,4), (2,1)]
presupuesto = 12
print(carlitos(campañas,presupuesto))