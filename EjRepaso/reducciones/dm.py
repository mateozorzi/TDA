"""
DM: Dado un grafo g, existe un subconjunto de vertices D de a los sumo k vertices
dado que para todo vertice v del grafo, v pertenece a D o es adyacente a un vertice de D?

1. Validador polinomial, para comprobar que DM esta en NP
2. Reducir un problema conocido de NP-C a DM, para comprobar que DM tambien es NP-C

VC = Dado un grafo g, existe un conjunto de vertices C de a lo sumo k vertices, donde por cada par de ady,
en el conjunto este presente al menos uno de los dos?

Reduccion:
VC(grafo,k) <=p DM(grafo',k')
Para esta reduccion, tenemos una caja negra que resuelve el problema de DM
Primero se realiza una copia el grafo original (grafo') donde por cada par de vertices ady, se crea un nuevo vertice que simboliza
su arista y se une a los dos vertices correspondientes. EL valor de k y k' es el mismo, ya que busco un conjunto minimo de vertices
que cumpla la condicion de DM y VC.

Si hay VC hay DM:
Si existe un conjunto C de vertices en los que se cumple las condiciones de VC. Dada la reduccion, en grafo'
habra un DM que que cumpla la condiciones de vertices dominados porquesi VC busca para cada par de vertices ady
que al menos uno este en el conjunto, entonces en DM siempre habra un vertice que este en conjunto y domine a sus ady,
y como se crearon vertices para las aristas, estos tambien seran dominados.


Si hay DM hay VC:
Si existe un conjunto D de vertices que cumple con las condiciones de DM en grafo', entonces dada la reduccion
este conjunto tambien sera un VC, ya que al crear vertices que representen las aristas de los vertices ady
del grafo original, se buscaran meter en el conjunto los vertices que tambien cumplan con la condicion 
de que todas las aristas esten cubiertas. En este caso al ser un DM, con que uno de los vertices de un par ady este
en el conjunto, tambien estara dominado el vertice creado que representa la arista. Y como todos los vertices deben ser dominados
todos los vertices de aristas seran ady a un vertice del conjunto.


"""

def validador(grafo, solucion, k):
    if len(solucion) > k:
        return False

    set_solucion = set(solucion)

    vertices = grafo.obtener_vertices()

    for v in vertices:
        if v in set_solucion:
            continue
        
        esAdy = False
        for s in solucion:
            if grafo.estan_unidos(v,s):
                break
        
        if esAdy:
            continue

        return False
    
    return True

#complejidad validador O(v * s)
