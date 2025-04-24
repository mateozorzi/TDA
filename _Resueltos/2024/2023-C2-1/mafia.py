
#kilometros = (inicio, fin)
def mafias(kilometros):
    #Como quiero acomodar la mayor cantidad de mafias posibles,mas prioridad a los que menos ocupen
    kilometros = sorted(kilometros, key=lambda x: x[1])

    #Ordeno las mafias por cantidad de kilometros que ocupan
    #Ahora itero sobre estas dandole pripridad a las que menos ocupen
    permisos = []
    permisos.append(kilometros[0])
    for i in range(1,len(kilometros)):
        finUltimaMafia = permisos[-1][1]
        if finUltimaMafia >= kilometros[i][0]: #el final de una mafia esta mas alla del incio de la otra
            #no le doy el permiso
            continue
        permisos.append(kilometros[i])

    return permisos
#complejidad O(n), n -> cantidad de mafias

#Regla Greedy: Agregar a la lista de permisos, por orden de terminacion del rango del pedido. Maximizando la cantidad de
#espacio disponible y de permisos entregados.
#Es optimo ya que al siempre agregar la mafia cuyo rango termine antes, dejarmeos el amyor espacio libre posible
#para poder ubicar otra mafia fuera de este rango


resul = mafias([(5, 10), (12, 15)])
print(resul)
