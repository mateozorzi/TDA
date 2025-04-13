"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""

def cambio(monedas, monto):
    if monto == 0:
        return []
    
    monedas = sorted(monedas, key=lambda x : x, reverse=True)

    cambio = []

    for i in range(len(monedas)):
        if monedas[i] > monto:
            continue
        
        cant = monto // monedas[i] #el resulktado sera la cantidad de mon[i]
        monto -= cant*monedas[i]   #Resto el monto

        for _ in range(cant):
            cambio.append(monedas[i])
        
        if monto == 0:
            break

    return cambio

#Regla greedy: En mi situacion actual, trato de saciar el monto a dar con la moneda de mayor denominacion que sea < al monto
#No es optimo, ya que puede haber una conbinacion de monedas de menor denominacion que de un optimo. Por ej: [10,7,3,1], monto = 14 -> Greedy -> [10,3,1]
                                                                                                                                    #-> optimo -> [7,7] Minimiza la cant de monedas
#complejidad O(n) en el pero de los casos recorro las n monedas
                
