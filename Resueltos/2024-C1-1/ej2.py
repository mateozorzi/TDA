import grafo
def viajante_greedy(g,v):
    origen = v
    visitados = [v]

    while len(visitados) < len(g.obtener_vertices())+1: #O(V)
        peso_minimo = 0
        arista_minima = None
        for ady in g.adyacentes(v): #O(V)
            if (g.peso_arista(v,ady) < peso_minimo or peso_minimo == 0) and ady not in visitados:
                peso_minimo = g.peso_arista(v,ady)
                arista_minima = ady
        
            if len(visitados) == len(g.obtener_vertices()) and ady == origen:
                peso_minimo = g.peso_arista(v,ady)
                arista_minima = origen
                break
        
        v = arista_minima
        visitados.append(arista_minima)

    peso = 0
    for i in range(1,len(visitados)): #O(V)
        peso += g.peso_arista(visitados[i-1], visitados[i])

    return peso
#comkplejidad O(V^2)

#Es un algortimos greedy, ya que itera sobre un vertice actual buscando el sig del camino, con el peso de su arista minimo
#y que no este en el set de visitados. Asegurando que seimpre se agregue al set el camino de peso minimo del vertice actual.
#No simepre da la solucion optima, ya que no tiene en cuenta los pesos del vertice siguiente, ya que al elegir otro de quiza mayor peso en el paso i,
#puede uqe en el paso i+1 pero en otro vertice hayaun peso menor
#ej
"""
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 10)
g.agregar_arista('A', 'D', 10)
g.agregar_arista('B', 'C', 10000000000)
g.agregar_arista('B', 'D', 10000000000)
g.agregar_arista('C', 'B', 10)
g.agregar_arista('C', 'D', 1)
g.agregar_arista('D', 'B', 1)
"""

# Crear el grafo
g = grafo.Grafo()
"""g.agregar_arista('A', 'B', 10)
g.agregar_arista('A', 'C', 15)
g.agregar_arista('A', 'D', 20)
g.agregar_arista('B', 'C', 35)
g.agregar_arista('B', 'D', 25)
g.agregar_arista('C', 'D', 30)"""
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 10)
g.agregar_arista('A', 'D', 10)
g.agregar_arista('B', 'C', 10000000000)
g.agregar_arista('B', 'D', 10000000000)
g.agregar_arista('C', 'D', 1)

# Ejecutar el algoritmo greedy para el TSP
costo_total = viajante_greedy(g, 'A')

print(f"Costo Total: {costo_total}")



                
