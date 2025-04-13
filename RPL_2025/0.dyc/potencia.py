"""Calcular b^n en O(logn)"""

def potencia(b,n):
    if n == 1:
        return b
    if n == 0:
        return 1
    
    if n % 2:
        #exponente par
        particion = potencia(b, n//2)
        return particion * particion
    else:
        #exponente impar
        particion = potencia(b, (n-1)//2)
        return b * particion * particion
    
#T(n) = AT(n/b) + O(n^c) -> A = 1, B = 2, C = 0
# T(n) = T(n/2) + O(1) -> Por TM -> la complejidad del algo es logB(A) = 0 = C -> O(n^clogn) -> O(logn)