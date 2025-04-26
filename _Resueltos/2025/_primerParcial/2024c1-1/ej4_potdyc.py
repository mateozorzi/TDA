"""

Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b^n en tiempo O(log n). Justificar
adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia.
Por ejemplo, que a^h ·a^k = a^(h+k)
"""

#T(n) = 1T(n/2) + O(1) -> A= 1, B = 2, C = 0 -> O(logn)

def potencia_dyc(b,n):
    if n == 0:
        return 1
    if n == 1:
        return b
    
    #si n es par
    if n % 2 == 0:
        pot = potencia_dyc(b,n//2)
        return pot*pot
    else:
        #es imapar
        pot = potencia_dyc(b,n-1)
        return pot*b

def potencia(b, n):
    return potencia_dyc(b,n)

print(potencia(2,10))