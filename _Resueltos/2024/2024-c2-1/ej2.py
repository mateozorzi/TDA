#perdidas: set de perdidas de compuesto x unidad de tiempo
def congeladores(congeladores):
    #ordeno los congeladores por su perdida
    congeladores = sorted(congeladores, key=lambda x: sum(x))
    
    perdidas = 0
    for i in range(1,len(congeladores)):
        #hago el movimiento para los dos conegladores que 
        #menos perdida sumen
        congOrigen = congeladores[i-1]
        congDestino = congeladores[i]

        #sumo las perdidas x unidad de tiempo de los compuestos
        #de ambos conegeladores
        perdidas += sum(congOrigen) + sum(congDestino)

        #agrego los compuestos al congelador Destino
        for compuesto in congOrigen:
            congDestino.append(compuesto)
        congOrigen.clear()


    return perdidas
#Regla greedy: Ordeno os congeladores de menor a mayor perdida
#Voy moviendo en cada iteracion los dos congeladores con menos perdida
#de compuesto x unidad de tiempo. Al ordenar al principio del algortimo
#e ir moviendo los congeladores de menor a mayor, evitamos mover muchas veces
#loc ompuestos de gran perdida, que son los que mas perdidas generan.
#por lo que nuestro algritmo obtendra siempre el minimo optimo de perdidas
#moviendo los congeladores.

#Muevo [3] al [5] -> 8
#Muevo [5,3] al [7,4,1] -> 20
#pierdo en total 28
#congeladoresLab = [[5],[3],[7,4,1]]

#Muevo [2] al [100] -> 102
#Muevo [100,2] al [101] -> 303
#pierdo en total 405
congeladoresLab = [[2],[100],[101]]
print("Perdidas totales: ",congeladores(congeladoresLab))