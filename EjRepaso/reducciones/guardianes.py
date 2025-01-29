"""
Guardianes = ¿Se pueden vigilar todas las calles con esta topología con al lo sumo K guardianes?

1. Verifico que que sea NP con un validador polinomial

2. Reduzco un problema NP-C al problema de los guardianes

VC(grafo, k) <=p guardianes(ciudad,k)

Dado el grafo y el valor que buscamos minimizar k, tenemos una caja negra que resuelve una isntancia del rpoblema
de los guardianes. El grafo representara la ciudad, cada vertice una esquina y sus adyacenctes las esquinas directas,
el valor de k se mantednria igual ya que queremos la enor cantidad de guarddianes para vigilar todas las calles.

Si hay VC hay guardianes:
Frente a un instancia de un grafo, donde existe un vc de a los sumo tamaño k, entonces en la ciudad podremos encontrar
a lo sumo k esquinas donde colocar los guardianes para que toda la calle esten vigiladas. Dados que en vertex cover, cada 
par de vertices ady, siempre uno de los dos se encuentra dentro del conjunto solucion, lo mismo pasara con las esquinas, siempre 
dado dos esuqinas ady una tendra un guardia.

Si hay guardianes hay VC:
Dada la instancia donde se encontro un conjunto de esuqinas dado que a lo sumo se necesitan k guardianes para
vigilar todas las calles de la ciudad, esta inastancia tambien representara un VC en el grafo original. Dado que si cada esuqina era
un vertice. Y las esquinas ady estaban conectadas por una arista, en el problema de VC dado dos vertics ady, a  lo sumo uno de
los dos vertices estara en el conjnto. Por lo que en el grafo, se conseguira un conjunto de vertices que representen un vertex cover, porque
vc cubre todas las aristas.


"""

def validador(ciudad, cuadras, k, guardianes):
    esquinas = set(cuadras)
    guardianes = set(guardianes)
    if len(guardianes) > k:
        return False
    
    for guardia in guardianes: #O(k)
        if guardia not in esquinas: #O(1)
            return False
    
    for cuadra in esquinas: #O(n)
        for ady in ciudad.adyacentes(cuadra): #O(n)
            if cuadra not in guardianes and ady not in guardianes: #O(1)
                return False
    
    return True

#complejidad O(n^2) es polinomial