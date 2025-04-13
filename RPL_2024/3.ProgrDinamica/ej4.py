"""Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, 
pero no quiere trabajar dos días seguidos. 
Dado un arreglo con el monto esperado a ganar cada día, determinar, 
por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. 
Hacer una reconstrucción para verificar qué días debe trabajar. 
Indicar y justificar la complejidad del algoritmo implementado."""

def calculoOptimos(trabajos):
    optimos = [0] * (len(trabajos)+1)
    optimos[0] = 0
    optimos[1] = trabajos[0]

    for i in range(1,len(trabajos)):
        optimos[i+1] = max(trabajos[i]+optimos[i-1], optimos[i])

    return optimos

def inversionOptimos(trabajos,optimos,pos,dias):
    if pos < 0:
        return dias

    if optimos[pos] == optimos[pos+1]:
        return inversionOptimos(trabajos,optimos,pos-1,dias)
    else:
        dias.append(pos)
        return inversionOptimos(trabajos,optimos,pos-2,dias)

def juan_el_vago(trabajos):
    #Ec recurrencia -> Ganacias = max(opt[i-1], trabajos[i]+opt[i-2])

    optimos = calculoOptimos(trabajos)  #O(n)
    dias = []
    inversionOptimos(trabajos,optimos,len(trabajos)-1,dias) #O(n)
    dias = sorted(dias) #O(nlogn)
    return dias
#Complejidad algo -> O(nlogn)

trab = [100,20,30,90,50]
print(juan_el_vago(trab))