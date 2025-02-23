def buscarOptimos(argnazon, fuddle):
    optimos = [0] * len(argnazon)+1
    indice_semana = 1

    #caso base: semana 0 no hay computo
    optimos[0] = 0
    #caso base: semana 1

    while indice_semana < len(optimos):


# computo i = tiempo de copmputoen la nube en la semana i
def computo_nube(computo, argnazon, fuddle):
    gastos_argnazon = []
    for c in computo:
        gastos_argnazon.append(argnazon*c)

    optimos = buscarOptimos(gastos_argnazon, fuddle)