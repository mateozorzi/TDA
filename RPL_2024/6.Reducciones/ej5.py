"""
Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad.

a. Dado un número por parámetro, si es la solución al problema de Búsqueda del máximo en un arreglo 
b. Dado un arreglo, si es la solución a tener el arreglo ordenado 
c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos N-reinas en un tablero NxN
"""
#a. verifico que el arreglo exista, que el numero este en el arreglo y que el numero sea el maximo
def verificadorNumeroMax(arreglo, numero):
    if not arreglo:
        return False
    
    if numero not in arreglo:
        return False
    
    maximo = arreglo[0]
    for num in arreglo:
        if num >= maximo:
            maximo == num
    if maximo != numero:
        return False
    
    return True
#Complejidad O(n)

#b. verificar que existan los arreglos, verifico si esta ordenado, verifico que coincidan en largo
def verificadorOrdenado(arreglo, ordenado):
    if not arreglo or not ordenado:
        return False
    
    if len(arreglo) != len(ordenado):
        return False
    
    solucion = sorted(arreglo)
    for i in range(len(solucion)):
        if solucion[i] != ordenado[i]:
            return False
    
    return True
#Complejidad O(nlog(n))

#c. verifico que sea una pos validas, verifico la solucion
def verificadNreinas(tablero, solucion, N):
    if not tablero or not solucion:
        return False
    
    if len(solucion) != N:
        return False
    #compruebo pos dentro del tablero
    reinasPuestas = []
    for reina in solucion:
        if reina[0] >= N or reina[0] < 0:
            return False
        if reina[1] >= N or reina[1] < 0:
            return False
        for r in reinasPuestas:
            if reina[0] == r[0] or reina[1] == r[1] or abs(reina[0] - r[0]) == abs(reina[1] - r[1]):
                return False
        reinasPuestas.append(reina)
    
    return True
#Complejidad O(len(solucion)^2)