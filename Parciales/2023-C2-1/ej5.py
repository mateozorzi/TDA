
def kmMafias(mafias):
    mafias = sorted(mafias, key=lambda x: x[2])
    
    otorgados = []
    otorgados.append(mafias[0])
    for grupo in mafias:
        if grupo[1] >= otorgados[-1][2]:
                otorgados.append(grupo)

    return otorgados


#Es greedy porque ordeno el arreglo, segun el km final que se quiere ocupar 
#Y me fijo de en cada iteracion agregar el prox grupo que antes termina (el km final mas bajo)
#y que no se superponga con el grupo anterior 
#Siempre da la solucion optima, ya que al ordenar por km final, achico el espacio que dejo entre las amfias
#por lo que siempre sera minimo



# Creando una lista de listas con los datos solicitados
mafias = [
    ["Los A", 1, 4],
    ["Los D", 5, 7],
    ["Los E", 7, 13],
    ["Los F", 5, 9],
    ["Los G", 6, 10],
    ["Los H", 8, 11],
    ["Los I", 8, 12],
    ["Los J", 2, 13]
]

print(kmMafias(mafias))
