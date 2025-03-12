def elemento_desordenado(arr):
    if len(arr) == 1:
        return None
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return None
    
    mitad = len(arr)//2

    elemento_mitad = arr[mitad]
    if arr[mitad-1] > elemento_mitad:
        return arr[mitad-1]

    izq = arr[:mitad]
    der = arr[mitad:]

    elemento_izq = elemento_desordenado(izq)
    elemento_der = elemento_desordenado(der)

    if elemento_izq != None:
        return elemento_izq
    elif elemento_der != None:
        return elemento_der
    return None
#Teorema del maestro -> A = 2, B = 2, C = 1 -> O(nlogn)
    

arr = [1, 2, 3, 4, 5, 6, 7, 13, 9, 10]
print(elemento_desordenado(arr))