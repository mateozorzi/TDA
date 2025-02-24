#participante = (numero, tiempo a pie, tiempo bicicleta, tiempo natacion)
def carrera(participantes):
    participantes = sorted(participantes, ke=lambda x: x[1] + x[2] + x[3])

    inicio = 0
    final = len(participantes) - 1

    largada = []

    while inicio <= final:
        if inicio == final:
            largada.append(participantes[inicio][0])
            inicio += 1
            final -= 1
            continue
        
        largada.append(participantes[inicio][0])
        largada.append(participantes[final][0])
        inicio += 1
        final -= 1 



