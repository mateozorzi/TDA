def mas_de_la_mitad(arr):
    contador = 0
    candidato = numero_repetido(arr)
    for numero in arr:
        if numero == candidato:
            contador += 1
    if contador > len(arr)//2:
        return True
    return False

def numero_repetido(arr): #111122 - #111 y #122 - #11 y #12
    if(len(arr) <= 1):
        return arr[0]

    mitad = (len(arr)) // 2

    canIzq = numero_repetido(arr[:mitad]) #111 - #11 #12 - #1 y #1
    izq = 0
    canDer = numero_repetido(arr[mitad:]) #122 - #1 #2 - #1 y #2
    der = 0

    for num in arr:
        if num == canIzq:
            izq += 1
        if num == canDer:
            der += 1

    if izq > der:
        return canIzq
    else:
        return canDer



arr1 = [1,2,3,4,5,6,7,8,9,7,6,4,32,5,45,6,57,34,23,4,5,456,5,7,4,52,34,2342]
arr = [1,1,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,44]
arr3 = [1,1,1,1,2,2]
arr4 = [1,1,2,2,2]
#print(mas_de_la_mitad(arr1))
#print(mas_de_la_mitad(arr))
print(mas_de_la_mitad(arr3))
#print(mas_de_la_mitad(arr4))

    

