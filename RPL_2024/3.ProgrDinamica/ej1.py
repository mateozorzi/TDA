"""Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. 
Indicar y justificar la complejidad del algoritmo implementado.

Definición:

n = 0 --> Debe devolver 1
n = 1 --> Debe devolver 1
n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ant = 1
    ant_ant = 0

    for i in range(1,n):
        nuevo = ant + ant_ant
        ant_ant = ant
        ant = nuevo
    return ant

print(fibonacci(10))
        