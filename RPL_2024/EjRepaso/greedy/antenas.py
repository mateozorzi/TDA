#casas -> km en el que esta ubicada cada casa
def cobertura(casas, R, K):
    casas = sorted(casas) #ordeno la ubicaciones de las casas #O(nlogn)

    antenas = []
    cubierto = 0 #hasta que km esta cubriendo las antenas
    for c in casas:
        if c > cubierto:
            if c + R < K:
                antenas.append(c + (R)) #pngo la antena en el borde
                cubierto = c + (2*R)
            else:
                antenas.append(K)
                cubierto = K

    return antenas

#Regla greedy: En cada iteracion, si veo que una casa no esta cubierta, entonces agrego una nueva antena en el rango maximo de cobertura
# para poder cubrir el mayor km posible.
#Es optimo? SI porque cada local cubre la mayor cantidad de km, entonces las antenas cubriran el mayor rango posible, por lo que en cada
#itreacion llegamos a un optimo local, para construir mi optimio global

# Ejemplo de uso
casas = [10, 14]  # Ejemplo de ubicaciones de las casas en kilómetros
R = 3  # Rango de cobertura de las antenas en kilómetros
K = 1000  # Longitud total de la ruta en kilómetros

print(cobertura(casas, R, K))