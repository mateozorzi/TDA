"""
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es la de maximizar la ganancia dada por p[k] -p[j]
POR DYC
"""

#T(n) = 2T(n/2) + O(n) -> A = 2, B = 2, C = 1 -> log2(1) = 1 = 1 = C -> O(nlogn)

def busquedaMaximo(valores, inicio, fin):
    if inicio == fin:
        return inicio,valores[inicio], inicio,valores[inicio] #tenes 1 dia, compras y vendes, 0 ganancia
    
    if fin - inicio == 1: #caso base con 2 dias, si el inicio tiene valor menor compro y vendo en fin
        if valores[inicio] < valores[fin]:
            return inicio,valores[inicio], fin, valores[fin] # >0 ganancia
        else: #fin tiene valor menor
            return fin, valores[fin], inicio,valores[inicio]
        
        
    mitad = (fin + inicio) // 2

    minDia_izq,min_izq, maxDia_izq, max_izq = busquedaMaximo(valores, inicio, mitad)
    minDia_der,min_der, maxDia_der, max_der = busquedaMaximo(valores, mitad+1, fin)

    #if minDia_izq < maxDia_izq puedo comprar minDia_izq
    #sino, no puedo comprar minDia_izq, trato de comprar a partir de maxDia_izq
    g1 = 0
    if minDia_izq < maxDia_izq:
        #puedo comprar en min dia y vender en max
        g1 = valores[maxDia_izq] - valores[minDia_izq]
    else:
        #el max esta antes del min, entonces no puedo comprar de esta manera
        minDia_izq = maxDia_izq


    #if minDia_der < maxDia_der puedo comprar en minDia_der
    #no compro en minDia_der, pero puedo seguir vendiendo en maxDia_der
    g2 = 0
    if minDia_der < maxDia_der:
        #puedo comprar en min y vender en max
        g2 = valores[maxDia_der] - valores[minDia_der]
    else:
        #si el max esta antes del min, no puedo vender de esta manera
        maxDia_der = minDia_der

    diaMinCentro = minDia_izq if minDia_izq < maxDia_izq else maxDia_der
    diaMaxCentro = maxDia_der

    for i in range(diaMinCentro, diaMaxCentro+1):
        if valores[i] < valores[diaMinCentro]:
            diaMinCentro = i
    for i in range(diaMinCentro, diaMaxCentro):
        if valores[i] > valores[diaMaxCentro] and i > diaMinCentro:
            diaMaxCentro = i
    
    g3 = 0
    if diaMinCentro < diaMaxCentro:
        g3 = valores[diaMaxCentro] - valores[diaMinCentro]

    
    if g1 >= g2 and g1 >= g3:
        return minDia_izq, valores[minDia_izq], maxDia_izq, valores[maxDia_izq]
    elif g2 >= g3:
        return minDia_der, valores[minDia_der], maxDia_der, valores[maxDia_der]
    else:
        return diaMinCentro, valores[diaMinCentro], diaMaxCentro, valores[diaMaxCentro]



def compra_venta(valores):
    compra,valor1, venta, valor2 = busquedaMaximo(valores, 0 , len(valores)-1)

    return compra, venta
    

p = [999,1000,1,2,30,150]
#p = [3179, 425, 4986, 5183, 6507, 6924, 4732, 6907, 1915, 188, 9402, 9297, 9514, 8004, 628, 4232, 478, 7576, 5406, 389, 8407, 7737, 1885, 4737, 2804, 2463, 9673, 7695, 3755, 8726, 1206, 1092, 6756, 1031, 748, 7564, 2357, 5044, 7263, 4907, 3410, 5056, 8372, 332, 3536, 5541, 6875, 6476, 8229, 9044, 994, 145, 2022, 579, 252, 428, 1344, 4669, 6032, 2628, 4466, 9685, 9885, 16, 5069, 2198, 1101, 3983, 5527, 2924, 1061, 3884, 4957, 5016, 5429, 9139, 1829, 1728, 5261, 990, 5511, 1484]
#p= [8409, 4579, 1685, 6035, 5210, 5648, 2131, 8240, 5540, 9668, 9012, 5014, 5990, 1950, 3884, 1948, 8547, 9751, 7938, 4083, 8097, 621, 4955, 4686, 6409, 9011, 4855, 3128, 1063, 897]
#p = [100, 102, 105, 107, 110, 113]
#p = [100, 102, 99, 104, 103, 108, 107]

compra, venta = compra_venta(p)

print(compra,",",p[compra])
print(venta,",",p[venta])