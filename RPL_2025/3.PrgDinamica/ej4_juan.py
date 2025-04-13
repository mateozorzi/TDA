"""
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplo:
Para: [100, 5, 50, 1, 1, 200]
Devolver: [0, 2, 5]
"""

def buscarOptimos(trabajos):
    #Ec de recurrecnia. Como no puedo trabajr dos dias seguidos, tengo entre elegir entre trabajar el dia k, pero no podria haber trbajado el dia k-1
    #o trabajr el dia k-1, pero no puedo trabajar el dia k

    optimos = [0] * (len(trabajos)+1)
    optimos[0] = 0
    optimos[1] = trabajos[0] #trabajo el dia 0

    #Es de recurrencia: optimos[i] = max(       optimo[i-1]         ,           optimos[i-2] + trabajo[i-1])
                                        #  trabaje el dia anterior         traabajo el dia i-1, pero no el dia i-2
    for i in range(1, len(optimos)):
        optimos[i] = max(optimos[i-1], optimos[i-2] + trabajos[i-1])

    return optimos

def reconstruccion(trabajos, optimos, pos):
    sol = []

    pos = len(optimos)-1

    while pos > 0:
        hoy = pos-1
        optimoAyer = optimos[pos-1]
        optimosAnteAyer = optimos[pos-2]
        trabajoHoy = trabajos[pos-1]

        if optimosAnteAyer + trabajoHoy >= optimoAyer:
            #trabaje hoy, no ayer
            sol.append(hoy)
            pos -= 2
        else:
            #no trabaje hoy, quiza ayer
            pos -= 1

    sol = list(reversed(sol))
    return sol


def juan_el_vago(trabajos):
    if len(trabajos) == 0:
        return []
    optimos = buscarOptimos(trabajos)

    sol = []
    sol = reconstruccion(trabajos, optimos, 1)
    
    # devolver un arreglo de los índices de días a trabajar
    return sol


arr = [100,20,30,70,50]
print(juan_el_vago(arr))