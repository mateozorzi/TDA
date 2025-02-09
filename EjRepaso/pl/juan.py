import pulp

def juan_el_vago(trabajos):
    variables = []
    #una varibale por dia de trabajo

    for i in range(len(trabajos)):
        variables.append(pulp.lpVariable(f"d{i}", cat="Binary"))
    
    problema = pulp.lpProblem("Juan el Vago", pulp.lpMaximize)

    #restricciones

    #no puede trabajar dos dias seguidos
    for i in range(2, len(trabajos)):
        problema += variables[i-2] + variables[i-1] + variables[i] <= 2
    

    problema += pulp.lpSum(variables[i] * trabajos[i] for i in range(len(trabajos)))
    problema.solve()