"""
Actores = Dado un conjunto de n actores y la información de en cuáles obras actuaron, 
¿existe forma de seleccionar k de ellos para hacer la siguiente obra, 
sin que existan dos de ellos que hayan compartido elenco previamente?

Para comprobar si el problema Actores en NP-C:
1. Probar que Actores está en NP, con un vlaidador polinomial
2. Reduzco un problema NP-C al problema de los actores, para comprobar que actores es NP-C

Reduccion:
IS(grafo, m) <=p actores(actores, obras,k)
Dada la reduccion, la transformacion de un problema a otro, se puede hacer de la siguiente manera:
A partir del grafo se creara un array con los vertices, que sera el conjunto de n actores
Dada las aristas del grafo, se sabra con actores se compartio obra, es decir si dos acotores compartieron obra
estaran unidos por una arista del grafo
El valor de k y m sera el mismo, ya que se busca maximizar el conjunto solucion en los dos problemas, por lo que
m == k
Tenemos una caja negra que resuelv euna instancia del problema d elos acotres, devolviendo True si encutnra 
el conjunto de al menos k actores tal que ninguno compartio obra.

Si hay IS hay actores:
Dada la transformacion, si existen un conjunto de al menos k vertices dado que no sean adyacentes en el grafo, entnces
dado el conjunto de actores y las obras que compartieron, se podra seleccionar un elenco de al menos k actores dado que 
ninguno de ellos compartio obra con otro. Dado que cada actor esta representado por un vertice del grafo, y las aristas
unen con los otros actores con los que compartio. Si hay 2 vertices que no son ady en el grafo, entonces en el problema de 
los actores estos dos actores podran estar en la misma obra

Si hay actores hay IS:
Si hay actores, entonces hay al menos k acotres que no compartieron obra entres ellos y que pueden ser seleccionados para la sig,
esto implica que existen al menos k vertices independientes en el grafo, dado que cada vertice representa una actor del conjunto
y cada arista une a dos actores que compartieron obre. Por lo que si dos actores entran en la seleccion, los vertices que representan
podran entar en el conjunto independiente.


"""

# actores: conjunto de n actores
# obras: set de con que actores compartio obra
# seleccion: conjunto solucion
def validador(actores, obras, seleccion, k):
    if len(seleccion) < k:
        return False

    setActores = set(actores)
    for actor in seleccion:
        if actor not in setActores:
            return False
    
    for actor1 in seleccion:
        for actor2 in seleccion:
            setObras = set(obras[actor2])
            if actor1 == actor2:
                continue
            for obras1 in obras[actor1]:
                if obras1 in setObras:
                    return False
    
    return True
#Complejidad: O(s + s^2*o) -> s la cantidad de actores en el conjunto seleccion, o la cantidad de obras de un actor
#Tiene complejidad polinomial
            

    

    


