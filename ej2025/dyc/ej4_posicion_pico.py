"""
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

Implementar un algoritmo de división y conquista de complejidad O(log n) que encuentre la posición p del pico: func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.

Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

def posicion_pico(v, ini, fin):
    if ini == fin:
        return ini
    if fin-ini == 1:
        if v[ini] > v[fin]:
            return ini
        else:
            return fin
    
    mitad = (ini + fin) // 2

    if v[mitad] > v[mitad-1] and v[mitad] > v[mitad+1]:
        return mitad

    if v[mitad] < v[mitad-1]:
        #el pico esta mas a la der
        return posicion_pico(v, ini, mitad-1)
    else:
        return posicion_pico(v, mitad, fin)

#Complejidad TM
# T(n) = T(n/2) + O(1)
#A = 1, B = 2, C = 0