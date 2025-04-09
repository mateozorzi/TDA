def is_arbol(arbol):
    conjunto = []

    while (len(arbol.obtener_vertices()) != 0):
        quitar = set()

        for v in arbol.obtener_vertices():
            if len(arbol.adyacentes(v)) == 1:
                #es una hoja, la quiero agregar al conjunto y borrar al padre
                conjunto.append(v[:])
                quitar.add(v)
                padre = arbol.adyacentes(v)[0]
                if padre not in quitar:
                    quitar.add(padre)
        
        for w in quitar:
            arbol.borrar_vertice(w)
    
    return conjunto

#regla greddy: En mi situacion mlocal busco agregar la conjunto is las hojas del grafo, luego actualizo borrando las hojas y los padres correspondientes
#Asi hasta que el grafo quede vacio


#es optimo, ya que al agregar las hojas del arbol local (que ira actualizando), maximizo la cantidad de vertices que agrego al conjunto
#agregando al hijo, saltendo al padre y terminare agregando al "abuelo"
