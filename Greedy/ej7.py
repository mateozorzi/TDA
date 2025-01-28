"""a)
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar"""
def precios_inflacion(R):
    preciosOrdenados = sorted(R,reverse=True)
    productosComprados = []
    dia = 0
    for productos in preciosOrdenados:
        productosComprados.append((productos)**(dia+1))
        dia += 1

    return sum(productosComprados)


"""b)Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar"""
def precios_deflacion(R):
    if(len(R) == 0):
        return 0
    preciosOrdenados = sorted(R)
    productosComprados = []
    productosComprados.append(preciosOrdenados[0])
    dia = 0
    for i in range(1,len(preciosOrdenados)):
        productosComprados.append((preciosOrdenados[i])/2)
        for j in range(len(preciosOrdenados)):
            preciosOrdenados[j] = preciosOrdenados[j] / 2
        dia += 1

    return sum(productosComprados)