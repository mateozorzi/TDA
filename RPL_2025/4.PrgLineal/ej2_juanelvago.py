"""
Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD)
"""

import pulp
def juan_pl(trabajos):

    #creo una varibale binaria para cada dia, 1 si trabajo, 0 si no
    #restricciones, no puedo trabajr dos dias seguidos, asi que si en i trbaajo, en i-1 y i+1 no puedo trabajar
    #mi funcion objetico buscara maximizar la ganaica de los dias que trabajoi

    variables = []
    for i in range(len(trabajos)):
        variables.append(pulp.LpVariable(f"dia{i}", cat="Binary"))

    problema = pulp.LpProblem("juan el vago", pulp.LpMaximize)

    #restricciones
    for j in range(1, len(trabajos)):
        problema += variables[i-1] + variables[i] <= 1


    problema += sum(variables[i]*trabajos[i] for i in range(len(trabajos)))

    return list(map(lambda yi: pulp.value(yi), variables))

