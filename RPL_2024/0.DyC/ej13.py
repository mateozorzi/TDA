def max_subarray(arr):
    if(len(arr) <= 1):
        return arr
    
    mitad = (len(arr)) // 2
    izq = arr[:mitad] 
    der = arr[mitad:] 

    izq = max_subarray(izq) #T(n/2)
    der = max_subarray(der) #T(n/2)

    sumaCentro = 0
    sumaCentroMax = -9999999999
    centro = []
    indiceInicio = 0; indiceFinal = 0
    indiceInicioMax = 0; indiceFinalMax = 0

    for i in range(len(arr)):
        aux = arr[i]
        if(arr[i] >= sumaCentro + arr[i]):
            indiceInicio = i
            indiceFinal = i
            sumaCentro = arr[i]
        else:
            indiceFinal += 1
            sumaCentro += arr[i]
        
        if(sumaCentro >= sumaCentroMax):
            sumaCentroMax = sumaCentro
            indiceInicioMax = indiceInicio
            indiceFinalMax = indiceFinal
    
    centro = arr[indiceInicioMax:indiceFinalMax+1]

    sumaIzq = 0
    for n in izq:
        sumaIzq += n
    
    sumaDer = 0
    for n in der:
        sumaDer += n
    
    sumaCentro = 0
    for n in centro:
        sumaCentro += n

    if(sumaCentro >= sumaIzq and sumaCentro >= sumaDer):
        return centro
    elif(sumaIzq > sumaCentro and sumaIzq >= sumaDer):
        return izq
    else:
        return der


# Ejemplos de uso
arr1 = [5, 3, 2, 4, -1]
arr2 = [5, 3, -5, 4, -1]
arr3 = [5, -4, 2, 4, -1]
arr4 = [5, -4, 2, 4]
arr5 = [-3, 4, -1, 2]
arr6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr_aleatorio = [-3, 4, -1, 2, 1, 2, -5, 1, 2, 1] 

print(max_subarray(arr1)) 
print(max_subarray(arr2))  
print(max_subarray(arr3))  
print(max_subarray(arr5))  
print(max_subarray(arr6))  
print(max_subarray(arr_aleatorio)) 