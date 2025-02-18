def complemento(variables, terminos, termino):
    c = ""
    if termino[0] == "!":
        c = termino[1:]
    else:
        c = "!" + termino
    
    if c not in terminos:
        return False
    
    return variables[c]


def esCompatible(clausulas, variables, terminos):
    for c in clausulas:
        verdadero = False
        for termino in c:
            if variables[termino] == complemento(variables, terminos, termino):
                return False
            if variables[termino]:
                verdadero =True
                break
        
        if not verdadero:
            return False
            
    return True

def tres_sat_bt(clausulas, variables,terminos, indice, solucion):
    if esCompatible(clausulas, variables, terminos):
        solucion = variables.copy()
        return solucion

    if indice == len(variables):
        return solucion

    variables[terminos[indice]] = True
    solucion = tres_sat_bt(clausulas, variables,terminos, indice+1, solucion)
    variables[terminos[indice]] = False
    solucion = tres_sat_bt(clausulas, variables,terminos, indice+1, solucion)

    return solucion

def tres_sat(clausulas):
    solucion = []
    variables = {}
    terminos = []

    for c in clausulas:
        for termino in c:
            variables[termino] = False
            terminos.append(termino)

    return tres_sat_bt(clausulas, variables,terminos, 0, solucion)



clausulas = [
    ["X1", "!X2", "X3"],
    ["!X1", "X5", "X8"],
    ["X4", "X6", "!X7"],
    ["X9", "!X1", "!X5"]
]

sol = tres_sat(clausulas) # {'X1': True, 'X2': False, 'X3': True, 'X4': True, 'X5': False, 'X6': True, 'X7': False, 'X8': True, 'X9': True}

for t in sol:
    if sol[t]:
        print(t)

#print(tres_sat(clausulas)) # {'X1': True, 'X2': False, 'X3': True, 'X4': True, 'X5': False, 'X6': True, 'X7': False, 'X8': True, 'X9': True}