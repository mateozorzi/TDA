"""
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso.
Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen,
pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo
día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la casa,
y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas.
El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k] - p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo.
Indicar y justificar la complejidad del algoritmo implementado.
"""
def buscarOptimos(p):
    optimoCompra = [0] * (len(p)+1)

    #caso base: no puedo comprar el ultimo dia, porque no voy a poder venderla
    optimoCompra[-1] = 0
    #con el subproblema de un solo dia, compro la casa
    optimoCompra[1] = p[0]

    #ec recurrencia de compra -> para el dia j, me conviene comprar la casa ese dia, o habia un dia anterior donde la casa valia menos
    # entonces optimoCompra[j] = min(p[j-1], optimoCompra[j-1])
    for j in range(2, len(optimoCompra)-1):
        optimoCompra[j] = min(p[j-1], optimoCompra[j-1])
    

    optimoVenta = [0] * (len(p)+1)

    #caso base: para el subproblema sin dias, no pude haber comprado nada
    optimoVenta[0] = 0
    # para el subrpoblema de un solo dia, tampoco pude haber comprado, entonces no pude vender
    optimoVenta[1] = 0

    #ec de recurrencia de venta -> para el dia k, tengo dos opciones, vender este dia o hay un dia anterior a k donde me convenia vender
    # entonces optimoVenta[k] = max(p[k-1] - optimoCompra[k-2], optimoVenta[k-1])
    for k in range(2,len(optimoVenta)):
        optimoVenta[k] = max(p[k-1] - optimoCompra[k-1], optimoVenta[k-1])
    
    return optimoCompra, optimoVenta

def reconstruccion(p, optimosCompra, pos, optimosVenta):
    diaCompra = 0
    diaVenta = 0

    #busco primero el dia de venta, luego tendre un set mas acotado para buiscar el dia de compra, ya que tiene que ser menor
    while pos > 1:
        # diaActual y optimosCompraAyer son compatibles por que si al diaActual le damos la notacion de k
        # y a optimosCompraAyer le damos la notacion de j, como estamos agarrando un optimo anterior del dia actual
        # entonces siempre se cumple la relacion de que k > j.
        diaActual = p[pos-1]
        optimosCompraAyer = optimosCompra[pos-1]
        gananciaConActual = diaActual - optimosCompraAyer

        #optimosVentaAyer contiene la ganacia maxima que se pudo opbtener hasta el dia k', comprando un dia j'
        # que tambien cumple la relacion que k' > j'
        optimoVentaAyer = optimosVenta[pos-1]
        gananciaAnterior = optimoVentaAyer

        if gananciaConActual >= gananciaAnterior:
            #vendi el dia (pos-1)
            diaVenta = pos-1
            pos -= 1
            break
        else:
            #no vendia el dia (pos-1), sigo buscando
            pos -= 1
    
    #ya encontre el dia de venta, ahora tengo que buscar el dia de compra desde pos hacia atras
    while pos > 0:
        #guardo cuanto sale comprar el dia actual
        diaActual = p[pos-1]

        #voy a comprar con el optimo de compra hasta ese dia
        optimoCompraAyer = optimosCompra[pos-1]

        if diaActual <= optimoCompraAyer:
            #compre este dia (pos-1)
            diaCompra = pos-1
            break
        else:
            #no compre el dia (pos-1)
            pos -= 1
    
    return diaCompra, diaVenta


def compra_venta(p):
    optimosCompra, optimosVenta = buscarOptimos(p) #O(n^2)

    return reconstruccion(p, optimosCompra, len(optimosCompra)-1, optimosVenta) #O(n)
#comlejidad O(n^2), siendo n la cantidad de dias en el arreglo p


p = [3179, 425, 4986, 5183, 6507, 6924, 4732, 6907, 1915, 188, 9402, 9297, 9514, 8004, 628, 4232, 478, 7576, 5406, 389, 8407, 7737, 1885, 4737, 2804, 2463, 9673, 7695, 3755, 8726, 1206, 1092, 6756, 1031, 748, 7564, 2357, 5044, 7263, 4907, 3410, 5056, 8372, 332, 3536, 5541, 6875, 6476, 8229, 9044, 994, 145, 2022, 579, 252, 428, 1344, 4669, 6032, 2628, 4466, 9685, 9885, 16, 5069, 2198, 1101, 3983, 5527, 2924, 1061, 3884, 4957, 5016, 5429, 9139, 1829, 1728, 5261, 990, 5511, 1484]
print(compra_venta(p))
#optimoCompra =     [0, 20, 20, 1, 0]
#optimoVenta =      [0, 0, 80, 80, 89]