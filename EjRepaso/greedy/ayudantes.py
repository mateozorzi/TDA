#ayudante = (nombre, dia, horario)
def comite(ayudantes):
    comite_ayudantes = []

    ayudantes = sorted(ayudantes, key=lambda x: (x[2][1] - x[2][0], x[2][0]), reverse=True,)

    for a in ayudantes:
        diaAyudante = a[1]
        inicio = a[2][0]
        fin = a[2][1]
        superpuesto = False
        for c in comite_ayudantes:
            diaComite = c[1]
            inicioComite = c[2][0]
            finComite = c[2][1]
            if diaAyudante == diaComite:
                if inicioComite <= fin or finComite >= inicio:
                    #hay un miembro del comite en el horario del ayudante
                    superpuesto = True
                    break

        if superpuesto:
            continue
        else:
            comite_ayudantes.append(a)

    return comite_ayudantes

#Regla greedy: En cada interacion agrego un ayudante fuera del comite que
# mas horas tenga en su turno y que ninguno del comite se superpone en horarios
# Con esto me aseguro que en cda iteracion, de ser posible agrego al comite
# al ayudante que mas horas cubra.

#No es optimo, ya que aunque cubra la mayor cantidad de horas, al poder estar
# al menos una sola parte del horario de otro ayudante, podrian haber configuraciones
# mas optimas para el comite, como por ej el aydante que en su turno este 
# superpuesto con la mayor cantidad de turno de otros ayudantes.
# ej: N = 3, ayudante 1 = Lunes 10-20, ayudnate 2 = Lunes 19-22, ayudante 3 = Lunes 21-23
# El algorimto greedy daria como comite al ayudante 1 y 3, pero
# la solucion ioptima seria el ayudante 2, ya que cubre se superpone con los horarios
# de los otros dos ayuidantes.

ayudantes = [

    ("Ayudante 1", "Lunes", (16, 20)),
    ("Ayudante 2", "Lunes", (18, 22)),
    ("Ayudante 3", "Lunes", (21, 23)),
]
print(comite(ayudantes))  

