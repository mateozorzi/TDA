def alternar(arr): #[C1, C2, C3, C4, D1, D2, D3, D4] - [C1,C2,D1,D2]
    if(len(arr) <= 2):
        return arr
    
    mitad = len(arr) // 2
    
    izq = arr[:mitad] #[C1, C2, C3, C4] - [C1,C2] 
    der = arr[mitad:] #[D1, D2, D3, D4] - [D1,D2]

    izq1 = izq[:len(izq)//2] + der[:len(der)//2] #[C1,C2,D1,D2] - [C1,D1]
    der1 = izq[len(izq)//2:] + der[len(der)//2:] #[C3,C4,D3,D4] - [C2,D2]

    izq2 = alternar(izq1)
    der2 = alternar(der1)

    return (izq2+der2)

arr = [1,1,2,2]
print(alternar(arr))

arr = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]
print(alternar(arr))

arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
print(alternar(arr))

arr1 = [1,1,1,1,2,2,2,2]
print(alternar(arr1))
# Versión alternada a la mitad
# Arreglo original: [1, 2, 3, 4, 5, 6, 7, 8]
# Arreglo alternado: [1, 5, 2, 6, 3, 7, 4, 8]

    