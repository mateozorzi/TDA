#productos = (valor, ml)
def robo_farmacia(productos, W):
    #ordeno por valor/cantidad -> QUe prductos me conviene llevarme segun los ml que hay
    productos = sorted(productos, key=lambda x: x[0]/x[1], reverse=True)
    indice = 0

    mochila = []

    capacidad = 0
    while capacidad < W and indice < len(productos):
        if productos[indice][1] + capacidad <= W:
            #entra todo el producto
            capacidad += productos[indice][1]
            mochila.append(productos[indice])
        else:
            #no entra, sino solo una parte, fracciono el producto
            prod = []
            fraccion = W - capacidad
            capacidad += fraccion
            prod = [fraccion, fraccion*productos[indice][0]]
            mochila.append(prod)
        indice += 1

#Regla greedy: ordeno los productos segun valor/capacidad, para elegir en cada iteracion
#el prodcuto con el mejor valor segun la capacidad restante del producto. Es greedy ya que usa
#esta regla sencilla para cargar en la mochila siempr el producto que mas valor aporta, ya sea si entra en toda la mochila
#o tambien de manera fraccionada.