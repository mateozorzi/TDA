"""
Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).
"""

import pulp

#lemento = (peso, valor)
def mochila_pl(elementos, W):

    variables = [] #Una variable para cada objeto de la mochila, sera binario, por lo que 1 sera que lo uso, 0 si no
    #restricciones: El peso de los objetos usados no puede superar W
    #funcion objetivo: el valor de los objetos usados debe ser el maximo posible

    for i in range(len(elementos)):
        variables.append(pulp.LpVariable(f"{i}", cat="Binary"))

    problema = pulp.LpProblem("Mochila max", pulp.LpMaximize)

    problema += pulp.LpAffineExpression({variables[i],elementos[i][0]} for i in range(len(variables))) <= W

    problema += pulp.LpAffineExpression({variables[i],elementos[i][1]} for i in range(len(variables)))

    problema.solve()

    return list(map(lambda yi: pulp.value(yi), variables))


W = 19
elementos = [(10,6),
(1,1),
(8,3),
(100,100),
(6,4),
(11,2),
(7,8),
(2,7),
(11,9)]
print(mochila_pl(elementos, W))