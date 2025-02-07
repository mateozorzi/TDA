def buscarOptimos(precios):
    optimoCompra = [0] * (len(precios)) #No puedo comprar el ultimo dia, porque no tendria ganancias vendiendo
    optimoCompra[0] = precios[0] #Caso base: compro el dia 1
    optimoCompra[-1] = 0 #No puedo comprar el ultimo dia, porque no tendria ganancias vendiendo

    for i in range(1, len(optimoCompra)-1):
        optimoCompra[i] = min(optimoCompra[i-1], precios[i])
    
    optimoVenta = [0] * len(precios) 
    optimoVenta[0] = 0 #Caso base: No puedo vender el priemr dia, porque no compre ningun dia anterior

    for j in range(1,len(precios)):
        optimoVenta[j] = max(optimoVenta[j-1], precios[j] - optimoCompra[j-1])

    return optimoCompra,optimoVenta

def reconstruccion(precios, optimoVenta, optimoCompra, ganancia, dia):
    if dia < 0:
        return ganancia
    
    if optimoCompra[dia] == precios[dia] and dia < ganancia[1]: #compre ese dia
        ganancia[0] = dia
        return reconstruccion(precios, optimoVenta, optimoCompra, ganancia, dia-1)
    if precios[dia] - optimoCompra[dia] == optimoVenta[dia] and ganancia[1] == 0: #vendi ese dia
        ganancia[1] = dia
        return reconstruccion(precios, optimoVenta, optimoCompra, ganancia, dia-1)
    else: #no vendi ese dia
        return reconstruccion(precios, optimoVenta, optimoCompra, ganancia, dia-1)
    

#n dias
def inmueble(precios):
    optimoCompra,optimoVenta = buscarOptimos(precios) #O(n)
    ganancia = optimoVenta[-1]

    #ganancia = [diaCompra, diaVenta]
    ganancia = [0,0]
    ganancia = reconstruccion(precios, optimoVenta,optimoCompra, ganancia,len(precios)-1)
    #Complejidad O(n), se llama n veces (dia veces) y se realizan op O(1) en cada llamado

    return ganancia

#Complejidad O(n)

p = [100, 180, 260, 310, 40, 50, 60]
dias = inmueble(p)

print("El inmueble se compro el dia", dias[0], " y se vendio el dia ", dias[1]) # 4, 3