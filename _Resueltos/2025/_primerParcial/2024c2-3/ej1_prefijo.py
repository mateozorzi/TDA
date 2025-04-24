"""
Dada una expresión representada por una cadena con aperturas y cierres de paréntesis, es sencillo implementar un
algoritmo que, utilizando una pila, determine si la expresión se encuentra balanceada, o no (esto es un algoritmo sencillo
de la materia anterior). Por ejemplo, la secuencia ()(), se encuentra balanceada, así como (()) también lo está, pero
((), no lo está, ni )()(. Implementar un algoritmo greedy que reciba una cadena y determine el largo del prefijo
balanceado más largo (es decir, el largo de la subsecuencia balanceada más larga que sí o sí comienza en el inicio de
la cadena). Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo greedy.
El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.
Ejemplo: para ()())(())()((), la respuesta es 4
"""
#()()((
def prefijo(cadena):
    largo = 0

    cantIzq = 0 # (
    abrir = "("
    cantDer = 0 # )
    cerrar = ")"

    while cantIzq >= cantDer and largo < (len(cadena)):
        if cadena[largo] == abrir:
            cantIzq += 1
            largo += 1
        elif cadena[largo] == cerrar:
            cantDer += 1
            largo += 1

    
    if cantIzq != cantDer:
        return largo-1
    
    return largo

c = "(()"
print(prefijo(c))