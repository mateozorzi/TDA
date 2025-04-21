
def buscarOptimos(diccionario, mensaje):
    return 


# voy a guardar mis optmos en una matriz, donde el indice de la fila simboliza el inicio de una serie de letras (i)
# y donde el indice de la columna el final de la serie de letras del mensaje (j)
# es decir que se debe cumplir que j > i, sino el optimo sera 0
# pregunto si el mensaje desde i hasta j (mensaje[i:j+1]) es una palabra del diccionario
#   -> Si es: entonces el optimo[i][j] = (j+1)-i
#   -> No es: veo cual es el optimo calculado anteriormente con una letra menos, moviendo el inicio de la secuencia en 1 (i+1)
#           optimoAnterior = optimos[i+1][j] = k
#           ahora no tengo en cuenta esas k letras desde j hacia atras, y compruebo si
#           -> si mensaje[i:j-k+1] es una palabra entonces: optimo[i][j] = (j+1-k) - i + optimos[i+1][j]
#           -> si no es palabra, entonces: tendre que seguir dividinedo en otras iteraciones, me quedo con el optimo de esas letras restantes
#                                           que esta calculado en opt[i][j - optimos[i+1][j]]
#                                           y luego sumo los resultados opt[i][j] = opt[i][j - optimos[i+1][j]] + opt[i+1][j]
# el calculo de los optimos comenzara con i = n-2 (no empieza en la ultima letra) y j = n-1
# con esto me quedaria el optimo en la posicion optimos[i][j] con i = 0 y j = n-1,
# para que exista un mensaje donde se encutran palabras del diccionario el largo de optimos[i][j] tiene que se igual a len(mensaje)
#por ejemplo si tengo el mensaje "heestado", i = 0, j = 8
# veo si "heestado" es una plaabra del diccionario
# -> no lo es: el optimos anterior opt[i+1][j] = 6 ("estado")
#entonces me queda comprobar si "he" es una palabra del diccionario o tengo que volver a dividirla

def palabras(diccionario, mensaje):
    optimos = buscarOptimos(diccionario, mensaje)