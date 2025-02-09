def clasificacion_dyc(ranking, rivalesSuperados):
    if len(ranking) == 1:
        return ranking, rivalesSuperados
    
    mitad = len(ranking) // 2
    izq, rivalesSuperados = clasificacion_dyc(ranking[:mitad], rivalesSuperados)
    der, rivalesSuperados = clasificacion_dyc(ranking[mitad:], rivalesSuperados)

    indiceIzq = 0
    indiceDer = 0

    while indiceIzq < len(izq):
        if izq[indiceIzq][1] > der[indiceDer][1]:
            #el jugador lo paso en relacion al ranking anterior
            rivalesSuperados[izq[indiceIzq][0]] += 1
        indiceDer += 1
        if indiceDer >= len(der):
            indiceDer = 0
            indiceIzq += 1
    
    return ranking, rivalesSuperados

    

def clasificacion(ranking):
    rivalesSuperados = {}
    for jugador in ranking:
        rivalesSuperados[jugador[0]] = 0
    
    ranking, rivalesSuperados = clasificacion_dyc(ranking, rivalesSuperados)
    return rivalesSuperados

ranking = [("A", 3), ("B", 4), ("C", 2), ("D", 8), ("E", 6), ("F", 5)]
print(clasificacion(ranking))