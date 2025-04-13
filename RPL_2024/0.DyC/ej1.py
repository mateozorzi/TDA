"""

"""

def elemento_desordenado_rec(arr, inicio, fin, mitad):
    if inicio == fin:
        return arr[inicio]
    
    mitad = (inicio + fin) // 2

    izq = elemento_desordenado_rec(arr, inicio, mitad)
    der = elemento_desordenado_rec(arr, mitad, fin)

    if der < izq:
        return izq

    if arr[inicio] > arr[fin]:
        return arr[inicio]
    else:
        return elemento_desordenado(arr, inicio,)

def elemento_desordenado(arr):
    if len(arr) == 1:
        return arr[0]

    mitad = len(arr) // 2

    izqMax = elemento_desordenado(arr[:mitad])
    derMax = elemento_desordenado(arr[mitad:])

    if izqMax > derMax:
        return izqMax
    return None

"""arr = [1,4,3,5,6]    
print(elemento_desordenado(arr))"""

