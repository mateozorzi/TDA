"""
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo. Ejemplos:

[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
"""
def es_continuo(izq, der, arr):
    ultimo_izq = izq[-1]
    primero_der = der[0]

    mitad = len(arr)//2

    if arr[mitad-1] == ultimo_izq and arr[mitad] == primero_der:
        return True
    return False

def max_subarray(arr):
    if len(arr) == 1:
        return arr
    
    mitad = (len(arr))//2

    izq = arr[:mitad]
    der = arr[mitad:]

    #veo cuanto sumala parte izq y la parte der

    sum_izq = max_subarray(izq)
    sum_der = max_subarray(der)
    """
    busco formar un nuevo subarreglo cruzado, usadno el lado izq y der
    Itero desde el lado izq el indice de mayor valor y voy para atras y veo si me conviene o on oagregar el elemento
    Para el lado derehco lo mismo, pero empiezo desde el menor idice hasta que termine
    luego comparo con los candidatos de izq y der antes calculados
    """
    #cruzado = max_subarray_cruzado(izq,der)

    #[i1,i2,....,ik][d1,d2,....,dm]
    #           <--  -->
    #veo desde ik para atras hasta donde me conviene incluir y desde d1 hasta dm hasta donde me conviene incluir

    if sum(arr) > sum(sum_izq) + sum(sum_der) and sum(arr) > sum(sum_izq) and sum(arr) > sum(sum_der):
        return arr
    
    partes_juntas = []
    #veo si el subarreglo de la izq es continuo con el de la derecha
    if es_continuo(sum_izq, sum_der, arr):
        #devuevlo la suma de los dos
        partes_juntas = sum_izq + sum_der

    if sum(partes_juntas) > sum(sum_izq) and sum(partes_juntas) > sum(sum_der):
        return partes_juntas
    
    if sum(sum_izq) > sum(sum_der):
        return sum_izq
    else:
        return sum_der
    

arr = [5, -4, 2, 4]
print(max_subarray(arr))