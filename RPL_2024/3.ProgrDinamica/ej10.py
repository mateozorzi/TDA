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

def invertirCiudades(mantenimientoLondres, mantenimientoCalifornia,pos,londres,california,mudanza,ciudades):
    if pos == 1:
        return ciudades

    if ciudades[-1] == 'california':
        if mantenimientoCalifornia[pos-1] + california[pos-1] == mantenimientoCalifornia[pos]:
            ciudades.append('california')
        elif mantenimientoLondres[pos-1] + mudanza + california[pos-1] == mantenimientoCalifornia[pos]:
            ciudades.append('londres')
    elif ciudades[-1] == 'londres':
        if mantenimientoLondres[pos-1] + londres[pos-1] == mantenimientoLondres[pos]:
            ciudades.append('londres')
        elif mantenimientoCalifornia[pos-1] + mudanza + londres[pos-1] == mantenimientoLondres[pos]:
            ciudades.append('california')
    
    return invertirCiudades(mantenimientoLondres, mantenimientoCalifornia,pos-1,londres,california,mudanza,ciudades)
    
def calculoMantenimiento(londres, california,costo_M):
    optimosLondres = [0]*(len(londres)+1)
    optimosCalifornia = [0]*(len(california)+1)

    optimosLondres[1] = londres[0]
    optimosCalifornia[1] = california[0]

    for i in range(1,len(california)):
        optimosLondres[i+1] = londres[i] + min(optimosLondres[i], optimosCalifornia[i] + costo_M)
        optimosCalifornia[i+1] = california[i] + min(optimosCalifornia[i], optimosLondres[i] + costo_M)
        
    return optimosLondres, optimosCalifornia


def plan_operativo(arreglo_L, arreglo_C, costo_M):
    ciudades = []
    mantenimientoLondres, mantenimientoCalifornia = calculoMantenimiento(arreglo_L, arreglo_C, costo_M)

    if mantenimientoCalifornia[-1] < mantenimientoLondres[-1]:
        ciudades.append('california')
    else:
        ciudades.append('londres')
        
    invertirCiudades(mantenimientoLondres, mantenimientoCalifornia, len(mantenimientoCalifornia)-1, arreglo_L, arreglo_C, costo_M,ciudades)

    ciudades = list(reversed(ciudades))
#complejidad  #O(n)
#
    return ciudades


# Ejemplo de uso
arreglo_L = [5, 46, 18, 88, 33, 13, 22, 35, 58]
arreglo_C = [20, 10, 65, 24, 55, 2, 28, 14, 94]
costo_M = 25
secuencia_optima = plan_operativo(arreglo_L, arreglo_C, costo_M)
print(secuencia_optima) 
"""Mudanza
75

75

75

25

75

25

25

25

25
"""
"""cali
[50]

[100]

[100, 50]

[50, 100]

[75, 100]

[100, 50]

[75, 25, 45, 5, 25, 35, 25, 55]

[85, 25, 55, 5, 25, 45, 45, 55]

[20, 10, 65, 24, 55, 2, 28, 14, 94]
"""

"""london
[100]

[50]

[75, 100]

[100, 50]

[100, 50]

[50, 100]

[85, 15, 55, 5, 25, 35, 55, 35]

[85, 15, 55, 5, 25, 35, 55, 35]

[5, 46, 18, 88, 33, 13, 22, 35, 58]
"""