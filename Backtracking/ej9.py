"""Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, 
cada materia está representada con una lista de cursos/horarios posibles a cursar 
(solo debe elegirse un horario por cada curso). 
Cada materia puede tener varios cursos. 
Implementar un algoritmo de backtracking que 
devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia 
sin que se solapen los horarios. 
Considerar que existe una función son_compatibles(curso_1, curso_2) 
que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo."""

def obtener_combinaciones(materias):
    # codigo de muestra
    combinaciones = []
    resul = []
    # por cada materia
    indice = 0
    horarioMateria = 0
    materias = sorted(materias,key=lambda x:len(x))
    print(materias)
    print('\n')
    return obtener_combinaciones_bt(materias, indice, horarioMateria, resul, combinaciones)

def obtener_combinaciones_bt(materias, indice, horario, resul,combinaciones):
    if(indice == len(materias)):
        if(resul not in combinaciones):
            combinaciones.append(resul.copy())
            return 
    

    if(horario < len(materias[indice])):
        resul.append(materias[indice][horario])
        if horariosCompatibles(materias[indice][horario], resul):
            obtener_combinaciones_bt(materias,indice+1,0,resul,combinaciones)
        resul.remove(materias[indice][horario])
        obtener_combinaciones_bt(materias,indice,horario+1,resul,combinaciones)
    
    return combinaciones

def horariosCompatibles(horarioMateria, resul):
    for materia in resul:
        if materia != horarioMateria:
            if not son_compatibles(materia, horarioMateria):
                return False
    return True

def convertir_a_minutos(hora):
    # Convertir una cadena de hora en formato HH:MM a minutos desde la medianoche
    partes = hora.split(' ')
    dia = partes[0]
    hora_inicio = partes[1].split(':')[0]
    minutos_inicio = partes[1].split(':')[1]
    hora_fin = partes[3].split(':')[0]
    minutos_fin = partes[3].split(':')[1]

    minutos_desde_medianoche_inicio = int(hora_inicio) * 60 + int(minutos_inicio)
    minutos_desde_medianoche_fin = int(hora_fin) * 60 + int(minutos_fin)

    return dia, minutos_desde_medianoche_inicio, minutos_desde_medianoche_fin

def son_compatibles(curso_1, curso_2):
    # Convertir los horarios de cursos a minutos desde la medianoche
    dia_1, inicio_1, fin_1 = convertir_a_minutos(curso_1)
    dia_2, inicio_2, fin_2 = convertir_a_minutos(curso_2)

    # Verificar si los cursos son en días diferentes
    if dia_1 != dia_2:
        return True  # Los cursos son en el mismo día, por lo que no son compatibles

    # Verificar si los horarios se solapan
    if inicio_1 >= fin_2 or fin_1 <= inicio_2:
        return True  # Los horarios no se solapan
    else:
        return False  # Los horarios se solapan



materias = [
    # Materia 1 con 2 cursos posibles
    ['Lunes 8:00 - 10:00', 'Miércoles 14:00 - 16:00'],
    # Materia 2 con 3 cursos posibles
    ['Lunes 9:00 - 11:00', 'Miércoles 8:00 - 10:00', 'Jueves 12:00 - 14:00'],
    # Materia 3 con 2 cursos posibles
    ['Lunes 15:00 - 17:00', 'Viernes 10:00 - 12:00', 'Jueves 12:00 - 15:00'],
]

print(obtener_combinaciones(materias))