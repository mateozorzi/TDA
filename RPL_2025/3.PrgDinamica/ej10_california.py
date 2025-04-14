"""Manejamos un negocio que atiende clientes en Londres y en California. 
Nos interesa cada mes decidir si operar en una u otra ciudad. 
Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: 
L y C, con valores para todos los meses hasta n. 
Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, 
habrá un costo fijo M por la mudanza. 
Dados los arreglos de costos de operación en Londres (L) y California (C), 
indicar la secuencia de las n localizaciones en las que operar durante los n meses, 
sabiendo que queremos minimizar el total de los costos de operación. 
Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado."""

def mudar_ciudad(c1, c2):
    aux = c1
    c1 = c2
    c2 = aux
    return c1,c2

def buscarOptimos(londres, california, mudanza):
    optimosXlondres = [0] * (len(londres))
    optimosXcalifornia = [0] * (len(california))

    #caso base: empiezo en londres o cali
    optimosXlondres[0] = londres[0]
    optimosXcalifornia[0] = california[0]

    #ec de recurrencia -> opt[i] = min(qudarme donde estoy, ir al otro lado + mudanza)

    #para cuando empiezo en londres
    actual = londres
    otra_ciudad = california
    for i in range(len(optimosXlondres)):
        costo_actual = actual[i]
        costo_otra = otra_ciudad[i]

        if costo_actual <= costo_otra + mudanza:
            #me quedo donde estaba
            optimosXlondres[i] = optimosXlondres[i-1] + costo_actual
        else:
            #me conviene mudarme
            optimosXlondres[i] = optimosXlondres[i-1] + costo_otra + mudanza
            actual, otra_ciudad = mudar_ciudad(actual, otra_ciudad)
    
    #para cuando empiezo en california
    actual = california
    otra_ciudad = londres
    for i in range(len(optimosXcalifornia)):
        costo_actual = actual[i]
        costo_otra = otra_ciudad[i]

        if costo_actual <= costo_otra + mudanza:
            #me quedo donde estaba
            optimosXcalifornia[i] = optimosXcalifornia[i-1] + costo_actual
        else:
            #me conviene mudarme
            optimosXcalifornia[i] = optimosXcalifornia[i-1] + costo_otra + mudanza
            actual, otra_ciudad = mudar_ciudad(actual, otra_ciudad)

    
    if optimosXlondres[-1] <= optimosXcalifornia[-1]:
        #me conviene empezar en londres
        return optimosXlondres, londres, california
    else:
        #me conviene empenzar en california
        return optimosXcalifornia, california, londres

def reconstruccion(londres, california, mudanza, optimos, pos, actual, otra_ciudad):
    sol = []

    while pos >= 0:
        sol.append(actual[pos])

        #tengo que averiguar si vengo de una mundanza o no
        costo_mes_anterior = optimos[pos-1]

        costo_misma_ciudad = actual[pos]
        costo_mudanza = otra_ciudad[pos] + mudanza

        if costo_misma_ciudad + costo_mes_anterior <= costo_mudanza + costo_mes_anterior:
            #el mes anterior estuve en la misma ciudad
            pos -= 1
        else:
            #el mes anterior estaba en la otra ciudad
            pos -= 1
            actual, otra_ciudad = mudar_ciudad(actual, otra_ciudad)

    return sol


def plan_operativo(arreglo_L, arreglo_C, costo_M):
    optimos, actual, otra_ciudad = buscarOptimos(arreglo_L, arreglo_C, costo_M)
    
    sol = reconstruccion(arreglo_L, arreglo_C, costo_M, optimos, len(optimos)-1, actual, otra_ciudad)

    return sol


# Ejemplo de uso
arreglo_L = [5, 46, 18, 88, 33, 13, 22, 35, 58]
arreglo_C = [20, 10, 65, 24, 55, 2, 28, 14, 94]
costo_M = 25
secuencia_optima = plan_operativo(arreglo_L, arreglo_C, costo_M)
print(secuencia_optima) 