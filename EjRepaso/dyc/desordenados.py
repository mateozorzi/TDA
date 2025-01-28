def elemento_desordenado(arr): #[1,90,3,5]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return None
    if len(arr) < 2:
        return None
    mitad = len(arr) // 2

    #caso del medio
    if(arr[mitad-1] > arr[mitad]):
        return arr[mitad-1]
    
    #veo el arr d ela izquiera
    izq = arr[:mitad]

    elemento = elemento_desordenado(izq)
    if elemento:
        return elemento
    
    #sino el arr de la derecha
    der = arr[mitad:]
    return elemento_desordenado(der)
        
#Teorema maestro
#A = 1
#B = 2
#C = 1
#log2 (1) = 0 < C = 1
#Por TM la complejidad es O(n)
arr = [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]
print(elemento_desordenado(arr))

"""
[1, 2, 3, 4, 5, 6, 7, 8, 90, 10]

[1, 2, 3, 4, 5, 6, 7, 13, 9, 10]

[15, 20, 35, 30, 40, 50]

[1, 2, 15, 20, 40, 30]

[1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""