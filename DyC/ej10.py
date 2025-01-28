def mas_de_la_mitad(arr):
    if(len(arr) == 0):
        return None
    if len(arr) == 1:
        return arr[0]
    
    mitad = []

    for i in range(1,len(arr),2):
        if arr[i] == arr[i-1]:
            mitad.append(arr[i])
    candidato = mas_de_la_mitad(mitad)
    if candidato is not None and arr.count(candidato) > len(arr)//2:
        return candidato
    elif len(arr)%2 == 1 and arr.count(arr[-1]) > len(arr)//2:
        return arr[-1]
    else:
        return None

arr1 = [1,2,3,4,5,6,7,8,9,7,6,4,32,5,45,6,57,34,23,4,5,456,5,7,4,52,34,2342]
arr = [1,1,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,44]
arr3 = [1,1,1,1,2,2]
arr4 = [2,1,2,1,2]
#print(mas_de_la_mitad(arr1))
#print(mas_de_la_mitad(arr))
print(mas_de_la_mitad(arr4))
#print(mas_de_la_mitad(arr4))