"""


Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.
"""

def parte_entera_raiz_dyc(n, raiz):
    if n == 0:
        return 0
    if n == 1:
        return 1

    #mitad = raiz//2

    if (raiz*raiz < n and (raiz+1)*(raiz+1) > n) or (raiz*raiz == n):
        #la parte entera de la raiz es mitad
        return raiz
    
    # mitad*mitad > n

    if (raiz+1)*(raiz+1) > (raiz)*(raiz) and (raiz+1)*(raiz+1) <= n:
        return parte_entera_raiz_dyc(n,raiz+1)
    else:
        return parte_entera_raiz_dyc(n,raiz//2)
    

#T(n) = A * T(n/B) + O(n ^ C)
#O(logn) -> T(n) = T(n/2) + O(1)
#A = 1, B = 2, C = 0
    

def parte_entera_raiz(n):
    return parte_entera_raiz_dyc(n,n//2)

n = 25
print(parte_entera_raiz(n)) # 3