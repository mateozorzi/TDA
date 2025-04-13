def buscarOptimos(cadena):
    optimos = [[0 for _ in range(len(cadena))] for i in range(len(cadena))]
    #i inicio de la cadena
    #j fin de la cadena

    #casos base
    # i = j -> cadena de largo 1 tiene como optimo 0
    for i in range(len(cadena)):
        optimos[i][i] = 0
    
    # j debe ser siempre mayor a i, sino no tiene sentido y el optimo es 0
    
    for i in range(len(cadena),-1,-1):
        for j in range(i+1, len(cadena)):
            if i > j:
                optimos[i][j] = 0
            else:
                if j - i == 1:
                    if cadena[i] == '(' and cadena[j] == ')':
                        optimos[i][j] = 2
                else:
                    #ec de recurrencia
                    if cadena[j] == '(':
                        optimos[i][j] = optimos[i][j-1]
                    elif cadena[i] == ')':
                        optimos[i][j] = optimos[i+1][j]
                    else:
                        optimos[i][j] = optimos[i+1][j-1] + 2

    return optimos

def balanceado(cadena):
    optimo = buscarOptimos(cadena)
    largo = optimo[0][len(cadena)-1]

    print(largo)

cadena = "()())(())()(()"
balanceado(cadena)  # 6