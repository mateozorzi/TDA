"""
Implementar una función (que utilice división y conquista) de orden O(n) que dado un arreglo de n números enteros 
devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. 
Justificar el orden de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver puramente por división y conquista.
"""

def mas_de_dos_tercios(arr):
    if mas_de_dos_tercios_dyc(arr) is not None:
        return True
    else:
        return False

def mas_de_dos_tercios_dyc(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    
    mitad = []

    for i in range(1,len(arr),2):
        if arr[i] == arr[i-1]:
            mitad.append(arr[i])
    candidato = mas_de_dos_tercios_dyc(mitad)
    if candidato is not None and arr.count(candidato) > len(arr)* (2/3):
        return candidato
    elif len(arr)%2 == 1 and arr.count(arr[-1]) > len(arr)*(2/3):
        return arr[-1]
    else:
        return None
    
arr3 = [1,1,2,1,1,2,1]
print(mas_de_dos_tercios(arr3))