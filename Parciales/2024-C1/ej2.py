import grafo as g
#ej2
def DMdeArbol(A):
    copiaArbol = A.copiar()
    vertices = A.obtener_vertices()
    hojas = []
    for v in vertices: #Busco las hojas del arbol al iniciar
        if len(A.adyacentes(v)) == 1:
            hojas.append(v)
    
    dm = []
    while hojas:
        for h in hojas:
            padre = copiaArbol.adyacentes(h)[0]
            if padre not in dm and any(padre not in A.adyacentes(b) for b in hojas):
                dm.append(padre)
            copiaArbol.borrar_vertice(h)
        vertices = copiaArbol.obtener_vertices()
        hojas = []
        for v in vertices: #Busco las hojas del arbol al iniciar
            if len(copiaArbol.adyacentes(v)) == 1:
                hojas.append(v)
                
    return dm

#El codigo es greedy porque usa un regla iterativa para encontrar el global optimo.
#localiza las hojas en la copia del grafo y agrega (si cumple con las condiciones) al padre al dm
#Como armo el dm a traves de las hojas, siempre busco optimamente que vertice agregar al subconjunto. Ya que si existe unahoja
#sera mejor agregar al padre, ya que puede estar conectado con algun otro vertice. Por lo que domino mas vertices.
#Esta solucion siempre es optima, porque me aseguro de buscar la mejor forma de dominar los vertices, a traves de las hojas
#no da siempre la solucion mas optima, ej:

A = g.Grafo()
A.agregar_arista(1, 2,1)
A.agregar_arista(1, 3,1)
A.agregar_arista(2, 4,1)
A.agregar_arista(2, 5,1)
A.agregar_arista(3, 6,1)
A.agregar_arista(3, 7,1)

print(DMdeArbol(A))
