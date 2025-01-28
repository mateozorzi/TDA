def elemento_desordenado(arr):
    indice = 0
    inicio = 0
    final = len(arr) - 1

    
    
    return arr[indice]
#[1,3,5,2,6,7] mitad = 5
#[3,5,2,6,7] mitad = 2
# Ejemplo de uso
alturas = [1,3,5,6,7,9,10,11,22,30,100,31,45,67,80,99]
#alturas = [1,3,5,2,6,7]
#alturas = [1,3,5,4,6,7]
#alturas = [1,99,4,6,7]
elemento = elemento_desordenado(alturas)
print("El elemento fuera de lugar es:", elemento)