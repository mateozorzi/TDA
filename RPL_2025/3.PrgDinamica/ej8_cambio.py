"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. 
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, 
y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. Indicar y justificar la complejidad del algoritmo implementado.
"""

def buscarOptimos(monedas, monto):
    optimos = [0] * (monto+1)
    optimos[0] = 0

    #ec de recurrencia: Para cada monto tengo que especificar la cantidad de monedas que tengo que dar de cambio segun mi sist monetario.
    # Entonces para el monto i recorro mis monedas, y voy viendo cual es la cantidad min de ambio que doy si doy la moneda j + opt[i-mon[j]]

    #Ec de recurrencia -> opt[i] = min(opt[i], 1+opt[i-mon[j]]), 0 <= j < len(monedas)
    for i in range(1, len(optimos)):
        optimos[i] = i
        for j in range(len(monedas)):
            if monedas[j] > i:
                #no entra la moneda
                continue
            optimos[i] = min(optimos[i], 1 + optimos[i-monedas[j]])
    
    return optimos

def reconstruccion(monedas, monto, optimos, pos):
    sol = []

    while pos > 0:
        optimos_actual = optimos[pos]
        for j in range(len(monedas)):
            optimo_con_moneda = optimos[pos-monedas[j]]
            if optimos_actual == optimo_con_moneda + 1:
                #use la moneda
                pos -= monedas[j]
                sol.append(monedas[j])
                break
            #no use la moneda
            continue

    return sol

def cambio(monedas, monto):
    optimos = buscarOptimos(monedas, monto)

    return reconstruccion(monedas, monto, optimos, len(optimos)-1)

ej1 = [13,9,7,2,1]
print(cambio(ej1,26))

ej2 = [1000,500,100,50,20,10,5,2,1]
print(cambio(ej2,1546))
