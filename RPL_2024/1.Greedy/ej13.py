"""Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. 
En dichas casas vive gente que usa mucho sus celulares. 
El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. 
Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).
Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, 
en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, 
y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, 
y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?"""

def cobertura(casas, R, K):
    if len(casas) <= 1: 
        return casas
    
    casas = sorted(casas)
    antenas = []
    
    
    for casa in casas:
        ubicacionAntena = casa + R

        if(len(antenas) == 0):
            antenas.append(ubicacionAntena)
        if(casa-antenas[-1] <= R):
            pass #casa cubierta
        else:
            antenas.append(ubicacionAntena)
        
    return antenas

# Ejemplo de uso
casas = [1.5, 3, 6, 8, 10.5, 12]  # Ejemplo de ubicaciones de las casas en kilómetros
R = 2  # Rango de cobertura de las antenas en kilómetros
K = 15  # Longitud total de la ruta en kilómetros

print(cobertura(casas, R, K))