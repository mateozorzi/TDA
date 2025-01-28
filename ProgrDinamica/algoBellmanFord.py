def camino_minimo_bf(grafo, origen):
	distancia = {}
	padre = {}
	for v in grafo:
		distancia[v] = infinito
	distancia[origen] = 0
	padre[origen] = None
	aristas = obtener_aristas(grafo)
	for i in range(len(grafo)):
		for v, w, peso in aristas:
			if distancia[v] + peso < distancia[w]:
				padre[w] = v
				distancia[w] = distancia[v] + peso
	
	for v, w, peso in aristas:
		if distancia[v] + peso < distancia[w]:
			return None # Hay un ciclo negativo (lanzar excep)
	return padre, distancia
