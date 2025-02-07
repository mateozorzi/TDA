import pulp

def osvaldo(precios):
    variablesCompra =[]
    for i in range(len(precios)):
        variablesCompra.append(pulp.LpVariable("compra"+str(i), 0, 1, cat="Binary"))
    
    variablesVenta = []
    for i in range(len(precios)):
        variablesVenta.append(pulp.LpVariable("venta"+str(i), 0, 1, cat="Binary"))
    
    problema = pulp.LpProblem("Inmueble", pulp.LpMaximize)

    #restriccion, no puedo vender el dia cero
    problema += variablesVenta[0] == 0

    #restriccion, no cpuedo comprar el ultimo dia
    problema += variablesCompra[-1] == 0

    #no puedo vender si antes no compre, o si compre el mismo dia
    for diaVenta in range(1, len(precios)):
        for diaCompra in range(diaVenta, len(precios)):
            if diaVenta <= diaCompra:
                problema += variablesVenta[diaVenta] + variablesCompra[diaCompra] == 0
    

    #ec objetivo
    problema += pulp.lpSum(precios[i]*variablesVenta[i] for i in range(len(variablesVenta))) - pulp.lpSum(precios[i]*variablesCompra[i] for i in range(len(variablesCompra)))
    problema.solve()

    compraYventa = []

    for diaCompra in range(len(variablesCompra)):
        if variablesCompra[diaCompra].varValue == 1:
            compraYventa.append(diaCompra)
    
    for diaVenta in range(len(variablesVenta)):
        if variablesVenta[diaVenta].varValue == 1:
            compraYventa.append(diaVenta)

    return compraYventa

p = [100, 180, 260, 310, 40, 50, 60]
dias = osvaldo(p)

print("Se compro el dia: ", dias[0], "y se vendio el dia:", dias[1])

