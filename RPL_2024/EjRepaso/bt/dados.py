# n=2, s=7
# 1
def dados_bt(numeroDados, sumatoriaDados,tiradas, tirada, numeroCara, dadoSuma):
    if sum(tirada) == sumatoriaDados and len(tirada) == numeroDados:
        tiradas.append(tirada.copy())
        return tiradas

    if sum(tirada) > sumatoriaDados or len(tirada) > numeroDados or numeroCara > 6 or dadoSuma > 6:
        return tiradas
    
    if sum(tirada) + (numeroDados - len(tirada))*6 < sumatoriaDados: #si para los dados que faltan no llego a la sumatoria de los dados, podo el caso
        return tiradas

    if len(tirada) < numeroDados:
        if len(tirada) == 0: #no hay dados cargados, agrego el numero de cara
            tirada.append(numeroCara)
        else: #si ya hay dados carahdos, agrego el numero de la cara a sumar
            tirada.append(dadoSuma)
        tiradas = dados_bt(numeroDados, sumatoriaDados, tiradas, tirada, numeroCara, 1)
        tirada.pop()
        if len(tirada) == 0: #no hay ninguna dado cargado, significa que cambio la cara del primer dado
            tiradas = dados_bt(numeroDados, sumatoriaDados, tiradas, tirada, numeroCara+1, 0)
        else: #todavia hay un dado en la tirada, entonces aumento el vlaor de dado a sumar
            tiradas = dados_bt(numeroDados, sumatoriaDados, tiradas, tirada, numeroCara, dadoSuma+1)

    return tiradas

#n cantidad de dados
#s sumatoria de los dados
def sumatoria_dados(n, s):
    tiradas = []
    tirada = []

    numeroCara = 1
    dadoSuma = 0

    tiradas = dados_bt(n, s, tiradas, tirada, numeroCara, dadoSuma)


    return tiradas

n=10
s=55
print(sumatoria_dados(n,s))