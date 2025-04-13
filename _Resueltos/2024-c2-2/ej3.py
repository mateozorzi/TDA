"""
k-ciclo: Dado un grafo G y un numero entero K, existe un ciclo dentro del grafo de al menos K vertices?

Para probar si k-c es un problema NP-C
1. Compruebo que es NP con un vlaidador polinomial
2. Reducir un problema NP-C al problema de k-c

CicloH: Dado un grafo G', se puede crear un ciclo que pase todos los vertices del grafo una vez y regrese al v incial?
Reduccion:
CicloH(G') <=p k-c(G,K)

Para la reduccion creamos un grafo G, a partir del G' y K = # vertices de G'

Si hay cicloH hay k-c:
Si hay un ciclo hamiltoniano en G', dada la reduccion el problema de k-c enocntrara
un cilo de al menos k vertices, siendo que al haber un ciclo hamiltoniano en G' y K == # cant vertices G'
entonces el ciclo que se encuntra es de tamaño igual a la cantidad de vertices de G'

Si hay k-c hay cicloH:
Dada la reduccion y que K == # vertices G', entonces si existe en el problema de k-c
un cilo de al menos k vertices, en G' habra un ciclo que pasa una vez por todos los vertices,
dado que k == # vertices de G'.

"""

def validador(grafo, solucion, k):
    if len(solucion) < k:
        return False
    
    vistos = set()
    for v in solucion:
        if v not in grafo or v in vistos:
            return False
        vistos.add(v)

    if solucion[0] != solucion[1]:
        #no es un ciclo
        return False
    
    for i in range(1,len(solucion)):
        if not grafo.estan_unidos(solucion[i-1], solucion[i]):
            #no son adyacentes
            return False

    return True