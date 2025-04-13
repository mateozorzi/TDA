"""
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. Indicar y justificar la complejidad del algoritmo implementado.

Definición:

n = 0 --> Debe devolver 1
n = 1 --> Debe devolver 1
n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    dosAnterior = 1
    anterior = 1

    for i in range(1,n):
        nuevo = dosAnterior + anterior
        dosAnterior = anterior
        anterior = nuevo

    return nuevo