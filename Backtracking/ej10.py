"""Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. 
La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, 
debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. 
¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?"""

def sumatoria_dados(n, s):
    combinaciones = []
    parcial = []
    caraDado = 1

    sumatoria_dados_bt(n,s,parcial,combinaciones,caraDado,caraDado)

    return combinaciones

def sumatoria_dados_bt(n,s,parcial,combinaciones,caraDado,caraActual):
    if(sum(parcial) == s and len(parcial) == n):
        combinaciones.append(parcial.copy())
        return
    if(len(parcial) >= n):
        return
    if(caraDado > 6 or caraActual > 6):
        return 
    
    if len(parcial) == 0:
       parcial.append(caraActual)
    else:
        parcial.append(caraDado)
    sumatoria_dados_bt(n,s,parcial,combinaciones,caraDado,caraActual)
    parcial.pop()
    if len(parcial) == 0:    
        sumatoria_dados_bt(n,s,parcial,combinaciones,1,caraActual+1)
    else:
        sumatoria_dados_bt(n,s,parcial,combinaciones,caraDado+1,caraActual)

    return combinaciones
    



n = 10
s = 55
print(sumatoria_dados(n,s))