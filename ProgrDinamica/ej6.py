"""Dado el teclado numérico de un celular, y un número inicial k, 
encontrar la cantidad de posibles números de longitud N empezando por botón del número inicial k. 
Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 
Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
Para N=2, depende de cuál dígito se comienza.
Empezando por 0, son válidos 00, 08 (cantidad: 2)
Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)
Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)
Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)
Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)
Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)
Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)
Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)"""

import grafo

def construirTeclado():
    teclado = grafo.Grafo()
    teclado.agregar_arista("1","1",1)
    teclado.agregar_arista("1","2",1)
    teclado.agregar_arista("1","4",1)
    teclado.agregar_arista("2","2",1)
    teclado.agregar_arista("2","3",1)
    teclado.agregar_arista("2","5",1)
    teclado.agregar_arista("3","3",1)
    teclado.agregar_arista("3","6",1)
    teclado.agregar_arista("4","4",1)
    teclado.agregar_arista("4","5",1)
    teclado.agregar_arista("4","7",1)
    teclado.agregar_arista("5","5",1)
    teclado.agregar_arista("5","6",1)
    teclado.agregar_arista("5","8",1)
    teclado.agregar_arista("6","6",1)
    teclado.agregar_arista("6","9",1)
    teclado.agregar_arista("7","7",1)
    teclado.agregar_arista("7","8",1)
    teclado.agregar_arista("8","8",1)
    teclado.agregar_arista("8","0",1)
    teclado.agregar_arista("8","9",1)
    teclado.agregar_arista("9","9",1)
    teclado.agregar_arista("0","0",1)
    return teclado

def combinaciones(teclado,matriz):
    for i in range(len(matriz)):
        matriz[i][0] = 1
    
    for j in range(1,len(matriz[0])):
        for i in range(len(matriz)):
            for ady in teclado.adyacentes(f"{i}"):
                aux = int(ady)
                matriz[i][j] += matriz[int(ady)][j-1] 

def numeros_posibles(k, n):
    teclado = construirTeclado()

    matriz = [[0] * (n) for _ in range(10)] #O(n)

    combinaciones(teclado,matriz) #O(n.10.a) -> simplificado #O(n)
    
    return matriz[k][n-1]


print(numeros_posibles(3,2))