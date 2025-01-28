def cajas(capacidad,libros):
    libros = sorted(libros,reverse=True) 

    libreria = []

    while libros:
        indice = 0
        caja = []

        while len(libros) - indice > 0:
            if libros[indice] + sum(caja) <= capacidad:
                caja.append(libros.pop(indice))
            else:
                indice += 1
            
            if sum(caja) == capacidad:
                indice = len(libros)
        libreria.append(caja.copy())        
    return libreria


libros = [1,5,10]
print(cajas(10,libros))


"""[4, 2, 1, 3, 5]
5

[9, 8, 6, 5]
10

7,[3, 3, 2, 2, 2, 2]
7"""