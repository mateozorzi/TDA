def calculoOptimos(n):
    optimos = [0]* (n+1)

    for i in range(1,len(optimos)):
        j = 1
        optimos[i] = optimos[i-1] + 1
        while j**2 <= i:
            if optimos[i-((j)**2)] + 1 < optimos[i]:
                optimos[i] = optimos[i-((j)**2)] + 1
            j += 1
        

    return optimos

def inversionOptimos(n, optimos,pos,resultados):
    if pos <= 0:
        return resultados
    
    j = 1
    while j**2 <= pos:
        if optimos[pos-((j)**2)] < optimos[pos-1]:
            resultados.append(j)
            return inversionOptimos(n, optimos, pos-(j)**2, resultados)
        j += 1

    resultados.append(1)
    return inversionOptimos(n, optimos, pos-1, resultados)


        

def sumaCuadrados(n):
    optimos = calculoOptimos(n)

    resultado = []
    inversionOptimos(n, optimos, len(optimos)-1, resultado)
    resultado = list(reversed(resultado))


    return resultado

print(sumaCuadrados(12))