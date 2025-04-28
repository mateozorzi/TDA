"""
Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser
también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Importante: antes
de escribir código, escribir (y describir) la ecuación de recurrencia
"""

#Ec de recurrencia: Para cada paso i, debo encontrar la cantidad posible de diferentes cambios que puedo dar para dar cambio i.
#Para el paso i, recorrere mis sistema monetario en busca de las monedas que puedan entrar en mi cambios, si una moneda entra,
#entonces le sumo a mi paso i la cantidad de combinaciones que hay para dar i-moneda[j]
# optimos[i] = optimos[i-moneda[j]] para todo j, tal que i >= moneda[j]


def buscarOptimos(monedas, cambio):
    optimos = [0] * (cambio+1)

    #caso base
    optimos[0] = 1 # para dar cambio de cero tengo una opcion
    optimos[1] = 1 # para dar cambio de 1 tengo una opcion, se asume que siempre hay una moneda de 1 en el sistema monetario

    for i in range(2, len(optimos)):
        for j in range(len(monedas)):
            if monedas[j] > i:
                #no puedo usar esta moneda
                continue
            optimos[i] += optimos[i-monedas[j]]

    return optimos


def cambio_distintos(monedas, cambio):
    optimos = buscarOptimos(monedas, cambio)

    return cambio, optimos[-1]


monedas = [13,7,5,2,1]
cambio = 5
print(cambio_distintos(monedas, cambio))
