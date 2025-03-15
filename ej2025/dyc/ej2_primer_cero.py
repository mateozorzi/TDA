"""
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.
"""
def indice_primer_cero_dyc(arr, inicio, fin):
    if inicio == fin:
        if arr[inicio] == 0:
            return inicio
        else:
            return -1

    mitad = (inicio + fin) // 2

    if arr[mitad] == 0:
        if arr[mitad-1] == 1:
            #es el primer cero
            return mitad
        return indice_primer_cero_dyc(arr,inicio, mitad)
    else:
        return indice_primer_cero_dyc(arr, mitad+1, fin)

def indice_primer_cero(arr):
    return indice_primer_cero_dyc(arr, 0, len(arr)-1)

#Complejidad del algortimo
# T(n) = AT(n/B) + O(n^C)
#A = 1
#B = 2
#C = 0

arr = [1,1,1,1,1,1,1,0,0]
print(indice_primer_cero(arr)) # 4