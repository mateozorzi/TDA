import pulp

#elementos -> [0] peso, [1] valor
def mochila(elementos, W):
    #Una variable por cada elemento, de tipo binario, 1 si esta en la mochila, 0 si no
    variables = {}
    for e in elementos:
        variables[e] = pulp.lpVariable(f"{e}", cat="Binary")
    
    problema = pulp.lpProblem("Mochila", pulp.lpMaximize)

    #restriccion 1: si dos elementos juntos no caben el mochila, no pueden ir juntos
    M = len(elementos) + 1
    
    for e in elementos:
        no_entran = []
        for f in elementos:
            if e == f:
                continue
            if e[0] + f[0] > W:
                no_entran.append(f)
        #una restriccion por elemento, si variable[e] = 1, entonces la sumatoria debe valer cero
        #si variables[e] = 0, entonces algunos de estos elementos pueden entrar en la mochila
        problema += variables[e] + pulp.lpSum([variables[f] for f in no_entran]) <= 1 + M(1 - variables[e])
    
    


    problema += pulp.lpSum([variables[i] * elementos[i][1] for i in range(len(elementos))])
    problema.solve()