"""Definir el problema de decisión de las N-Reinas. 
Usar que N-Reinas es un problema NP-Completo para demostrar que Demostrar que Independent Set es un problema NP-Completo.

Para demostrar que IS es NP-C

1. Validador polinomial que compruebe una solucion del problema
2. Reducciona un problema NP-C conocido
N-reinas(tabnlero,k') <= IS(grafo)

n-reinas: existe una disposcion en el tablero en el que puedo colocar al menos k' sin que se puedan comer entre ellas
IS: existe un cojunto de vertices del grafo de tamaño al menos k, tal que no sean adyacentes entre si

Conozco el propbnlema de n-reinas es NP-C, entonces para comprobar si IS es tambien NP-C, 
tengo que poder reducir n-reinas a IS, entonces este sera NP-C

Dada la instancia del problema de N-Reinas, donde recibo un tablero y tengo un valor k'.
Modelo el grafo G, un vertice para cada casillero del tablero y creo als adyacencias segun las casillas que podria ir la reina 
si estuveira en esta.
Busco colocar al menos k' reinas en el tablero, con la trnasformacion buscare al menos k=k' vertices no adyacentes entre si

Si hay n-reinas hay IS
Dado que en la instanci aincial de las n-reinas, se puedeencontrar una disposcion talque se coloquen al menos k' reinas en el tablero,
dado que el grafo G esta modelado siguiendo las casillas y las adyacencias segun las casillas a las que pordria ir la reina, las casillas
donde serian colocoadas las reinas en el tablero, conformarian en la transformacion los k vertices no adyacentes entre si del problema de IS

Si hay IS hay n-reinas
Por cada vertice del conjunto solucion de IS, existe una transofrmacion que indica en el tablero a que casilla correpsonde,
por lo que si existe un conjunto de al menos k vertices no adyacentes entre si, las k casillas a las que corresponden estos vertices
seran las casillas donde se podran colocar las reinas sin que puedan comerse entre si

NO JUSTIFICA QUE N-REINAS ES NP-COMPLETO

"""


def validador(grafo, solucion, k):
    if len(solucion) < k:
        return False #no es de al emnos k vertices
    
    for v in solucion:
        for w in solucion:
            if v == w:
                continue
            if grafo.estan_unidos(v,w):
                return False #son ady
    

    return False
#Complejidad O(n*2), siendo n la cantidad de vertices del conjunto