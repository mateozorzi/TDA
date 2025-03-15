"""
lo mimso que el ej9 pero en O(n)
"""

def mas_de_la_mitad_dyc(arr):
    if len(arr) == 1:
        return arr[0]
    
    mitad = len(arr) // 2

    izq = arr[:mitad]
    der = arr[mitad:]

    candidatos = mas_de_la_mitad_dyc(izq)

    


def mas_de_la_mitad(arr):
    return False

#Complejidad -> T(n) = AT(n/B) + O(n^c) -> T(n) = T(n/2) + O(n) -> A = 1, B = 2, C = 1, por TM logB(A) < C -> O(n)

arr = [1,2,2,1,1,1]