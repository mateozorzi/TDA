"""
Sea G un grafo dirigido "camino" (las aristas son de la forma (vi, vi-1)). Cada vertice tiene un valor (positivo).
Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima
dentro de un grafo de dichas características. Dar la ecuación de recurrencia correspondiente al problema. Indicar
y justificar la complejidad del algoritmo implementado. Indicar y justificar la complejidad espacial del algoritmo
implementado, y si hay una optimización que permita consumir menos espacio.
"""
import grafo

def buscarOptimos(vertices):
    optimos = [0] * (len(vertices)+1)
    #casos base
    optimos[0] = 0
    optimos[1] = int(vertices[0])
    optimos[2] = min(int(vertices[0]), int(vertices[1]))

    #Ec de recurrencia: busco un dm de suma minima. sera un dm minimo de suma minima, cuantos menos vertices agregue menos voy a sumar
    #Entonces para el subproblema con i vertices, puedo elegir entre no agregar el vertice, entonces tengo que agregar el vertice anterior y quedarme con al sol de tres pasos atras
    #sino, puedo agregar el vertice y sumarle el optio de dos pasos atras
    #Ec de recu -> optimos[i] = min(vertices[i-1] + optimos[i-2],   vertices[i-2] + optimos[i-2] ,vertices[i-2] + optimos[i-3])
    #                               agrego el vertice actual        agrego el anterior            , agrego el anterior
    #                               me salteo el ant sol              con una sol ant                   me salteo dos sol ant
    #[1000, 1, 1, 1000]
    for i in range(3, len(optimos)):
        agrego_actual = int(vertices[i-1]) + optimos[i-2]
        anterior_1 = int(vertices[i-2]) + optimos[i-2]
        anterior_2 = int(vertices[i-2]) + optimos[i-3]

        optimos[i] = min(agrego_actual, anterior_1, anterior_2)

    return optimos

def reconstruccion(vertices, optimos, pos):
    sol = []

    while pos > 0:
        agregar_actual_sin_anterior = int(vertices[pos-1]) + optimos[pos-2]
        agregar_anterior_con_el_siguiente = int(vertices[pos-2]) + optimos[pos-2]
        agregar_anterior_sin_siguiente = int(vertices[pos-2]) + optimos[pos-3]

        if agregar_actual_sin_anterior == optimos[pos]:
            sol.append(vertices[pos-1])
            pos -= 2
        elif agregar_anterior_con_el_siguiente == optimos[pos]:
            sol.append(vertices[pos-2])
            pos -= 2
        else:
            sol.append(vertices[pos-2])
            pos -= 3


    return list(reversed(sol))
            

def camino(grafo):
    optimos = buscarOptimos(grafo.obtener_vertices())

    return reconstruccion(grafo.obtener_vertices(), optimos, len(optimos)-1)


"""g = grafo.Grafo()
g.agregar_arista("1000", "1", 1)
g.agregar_arista("1", "2", 1)
g.agregar_arista("2", "1001", 1)

print(camino(g))"""
A = grafo.Grafo()
vertices1 = [4, 1, 3, 7, 8, 2]
A.agregar_arista(4, 1,1)
A.agregar_arista(1, 3,1)
A.agregar_arista(3, 7,1)
A.agregar_arista(7, 8,1)
A.agregar_arista(8, 2,1)


print(camino(A))