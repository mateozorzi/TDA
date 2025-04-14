"""Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. 
Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. 
La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña,
que denominaremos Gi. Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos.
Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? 
Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa."""

def buscarOptimos(publicidades, P):
    optimos = [[0] * (P+1) for _ in range(len(publicidades))]

    #ec de recurrencia -> como en la mochioa buscamos maximizar las ganancias con las publicidades, sin pasarse del presupuesto
    #                   -> opt[i][j] = max(     optimos[i-1][j],        optimos[i-1][j - publicidades[0]] + publicidades[1])
    #                                       no uso la publi i-1                 uso la publiciadad i-1
    #                                       veo el optimo con el mismo P

    #casos base -> sin publicidades el optimos[0][j] = 0
    #           -> sin preuspuesto el optimos[i][0] = 0
    for i in range(len(optimos)):
        for j in range(1,len(optimos[0])):
            publicidad = publicidades[i-1]
            gasto = publicidad[0]
            ganancia = publicidad[1]

            if gasto > j:
                optimos[i][j] = optimos[i-1][j] # no puedo usar esta publicidad, se pasa de preuspuesto
            else:
                optimos[i][j] = max( optimos[i-1][j], optimos[i-1][j-gasto] + ganancia)

    return optimos

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    optimos = buscarOptimos(c_publicitaria, P)

    #recosntruyo ihual que el de la mochila
