def alternar(arr): # [0,2,1,3]
    if len(arr) <= 2:
        return arr
    
    #separo el arreglo a la mitad
    mitad = len(arr) // 2
    primera_mitad = arr[:mitad] #[0,2]
    segunda_mitad = arr[mitad:] #[1,3]

    alternado_izq = primera_mitad[:len(primera_mitad)//2] + segunda_mitad[:len(segunda_mitad)//2]
    alternado_der = primera_mitad[len(primera_mitad)//2:] + segunda_mitad[len(segunda_mitad)//2:]

    # alternado_izq = [0,1]
    alternado_izq = alternar(alternado_izq)
    #alternado_der = [2,3]
    alternado_der = alternar(alternado_der)

    return alternado_izq + alternado_der

#teorema del maestro
# A = cantidad de llamados recursivos = 2
# B = en cuantas partes dividimos el problema = 2
# C = complejidad de las operaciones internas = 1
# T = 2log(n/2) + 1
#log2(2) = 1 = C = 1
#complejidad segun el teroema maestro es O(nlog(n))
arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]
print(alternar(arr))