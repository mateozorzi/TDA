def busqueda_binaria_minimo(alumnos, inicio, fin):
    mitad = (fin + inicio) // 2

    if validar_mas_bajo(alumnos, mitad):
        return mitad
    
    if alumnos[mitad] < alumnos[mitad-1]:
        #esta decreciendo
        return busqueda_binaria_minimo(alumnos, mitad, fin)
    else:
        #me pase del mas bajo porque esta creciendo
        return busqueda_binaria_minimo(alumnos, inicio, mitad)


def indice_mas_bajo(alumnos):
    return busqueda_binaria_minimo(alumnos, 0, len(alumnos)-1)


def validar_mas_bajo(alumnos, indice):
    alumno_mas_bajo = alumnos[indice]
    alumno_izquierda = alumnos[indice-1]
    alumno_derecha = alumnos[indice+1]

    if alumno_mas_bajo <= alumno_izquierda and alumno_mas_bajo < alumno_derecha:
        return True
    
    return False


alumnos = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 0.78, 1.23]
print(indice_mas_bajo(alumnos)) # 5