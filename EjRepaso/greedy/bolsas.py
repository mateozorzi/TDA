def bolsas(capacidad, productos):
    
    productos = sorted(productos, reverse=True)

    bolsasCargadas = []
    
    for p in productos:
        colocado = False
        for bolsa in bolsasCargadas:
            #veo si entra en una bolsa
            if sum(bolsa) + p <= capacidad:
                colocado = True
                bolsa.append(p)
                break
        
        if colocado:
            continue

        #si no entra en ninguna bolsa
        bolsasCargadas.append([p])
    
    return bolsasCargadas


productos = [ 4, 2, 1, 3, 5 ]
capacidad = 5
