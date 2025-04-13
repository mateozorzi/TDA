def indice_primer_cero(lista):
    buscado = 0
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        
        if (medio == 0 and lista[medio] == buscado):
            return medio
        else:      
            if lista[medio] == buscado and lista[medio-1] == buscado:
                final = medio - 1
            elif lista[medio] > buscado:
                inicio = medio + 1
            elif lista[medio] == buscado and lista[medio-1] > buscado:
                return medio
            else:
                return medio
    return -1

#numeros = [1,1,1,1,0,0]
#numeros = [1,0,0,0,0,0]
numeros = [1,1]
print(indice_primer_cero(numeros))