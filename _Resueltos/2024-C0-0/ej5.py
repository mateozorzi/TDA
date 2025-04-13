#productos(cant, valor x cant)
def roboFarmacia(productos, L):
    productos = sorted(productos, key=lambda x: productos[x][1], reverse=True)

    mochila = []
    indice = 0
    capacidadRestante = L

    while capacidadRestante <= 0 or indice >= len(productos):
        if productos[indice][0] <= capacidadRestante:
            mochila.append(productos[indice])
            capacidadRestante -= productos[indice][0]
        else:
            valorFraccionado = (productos[indice][1]*capacidadRestante) / productos[indice][0]
            mochila.append([capacidadRestante, valorFraccionado])
        indice += 1
    
    return mochila

#es un algorimto greesy, porque utiliza una regla sencilla en la iteracion de la mochila, ya que al ordenar
#a los productos por su valor y poder agregar cantidades fraccionarias, siempre en cada optimo local esamos agregando 
#la mayor cantidad del producto mas valioso en ese momento. Por lo que, ademas, el algortimo da un resultado optimo

