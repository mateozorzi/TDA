"""
Definir los problemas de decisión de Camino Hamiltoniano y Ciclo Hamiltoniano. 
Sabiendo que Ciclo Hamiltoniano es NP-Completo, demostrar que Camino Hamiltoniano es NP-Completo.

1. Demuestro que camino hamiltoniano es NP con un validador polinomial
2. Para demostrar que camino hamiltoniano en NP-C, debo poder reducir otro porblema
NP-C a camino hamiltoniano. Como por ejemplo ciclo hamiltoniano.

Reduccion:
CicloH(G, origen) <=p CaminoH(G, origen)
Dado el grafo G, parto en 2 el vertice origen:
siendo V el vertice origen solo con las salidas y
V' el vertice destino con las entradas

Si hay CicloH, hay caminoH:
Dados estos nuevos vertices, el caminoH ira del vertice V hasta el vertice V', asi no pasando dos veces por el vertice origen
ya que al estar partido sus entradas y salidas en 2, se toman como 2 vertices distintos entre si.
Dada esta particion seria un absurdo que no haya un camino hamiltoniano, ya que la entrada o salida del vertice origen
esta partida en 2 vertices distintos.
-------
Si hay CaminoH, hay CicloH:
Dado esta instancia del problema, como V y V' son representacion de la entrada y salida del vertice origen, respectivamente.
Podemos entener que V y V' forman un solo vertice, el origen. Por lo que si hay un camino hamiltoniano, que comienza
en V y termina en V', habra un ciclo hamiltoniao que empiece en el origen y termine en el origen.
"""

def validador(grafo, camino):
    if not camino:
        return False
    
    #verfico la cantidad de vertices por donde pasa
    if len(camino) != len(grafo.obtener_vertices()):
        return False
    
    #verifico que no pase por el mismo vertice 2 veces O(n^2)
    for i in range(len(camino)):
        for j in range(len(camino)):
            if i == j:
                continue #misma posicion
            if camino[i] == camino[j]:
                return False #Paso por el mismo vertice 2 veces
        
    #verifico que los vertices esten unidos O(n)
    for i in range(1,len(camino)): 
        if not grafo.estan_unidos(camino[i-1], camino[i]):
            return False #los vertices no estan unidos, no puede pasar por alli
    
    return True #solucion correcta
#complejidad O(n^2)
