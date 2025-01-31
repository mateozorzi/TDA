"""
coty: Dada una lista de pares de invitados conocidos (n invitados), se pueden asignar a lo sumo k invitados que reciban
regalos, tal que para todo par de invitados conocidos, al menos uno de ellos reciba un regalo.

VC = Dado un grafo y un entero k, existe un conjunto de a lo sumo k vertices tal que cada arista del grafo este cubierta

1. Validador polinomial, comprueba que el problema esta en NP
2. Para comprobar si el problema de coty en NP-C, debo reducir un problema conocido NP-C a coty

Reduccion:
VC(grafo, v) <=p coty(invitados,k)

Para la reduccion tengo una caja negra que resuelve el problema de coty, devolvinedo True si existen a lo sumo k
invitados a los que darles un regalo, tal que dado cada para de invitados conocidos puedan hablar del regalo de uno
de los dos.
Para la transformacion, dado el grafo, se creara un set donde se iran agregando los pares de vertices adyacentes.
El valor de v sera igual al valor de k en la transformacion, dado que ambos porblemas buscan minimizar la cantidad
de elementos de la solucion.

Si hay VC hay coty:
Dado la instancia de grafo y v, existe un VC de a lo sumo v vertices. Entonces en el problema de coty existiran
a los sumo k invitados a los que darle el regalo, tal que todo par de invitados pueda hablar de un regalo. Esto es asi
ya que como VC busca cubrir cada arista del grafo, y cada vertice del grafo es convertido en un invitado de la fiesta
entonces si existen v vertices que cubren todas las aristas, estos seran los k invitados que reciban regalos, y como
se cubren todas las aristas, no quedara un par de invitados que se conocen y niguno hay recibido regalos, dado que conocerse
serian las aristas del grafo.

Si hay coty hay VC:
Del mismo modo, dada la instancia donde existen a los sumo k invitados que reciben regalos, tal que todo par de invitados
conocidos pueden hablar del ragalo de alguno, tambien existira un VC de a los umo v vertices. Esto es que dado que cada invitado
simboliza un vertice del grafo, y conocer a otro invitado hace que estos vertices sean ady. Si k invitados reciben regalos, y
ninguno queda invitado queda sin hablar de un regalo, en el grafo esto significaria que dados estos v vertices del conjunto
se estarian cubirneod todas las aristas del grafo. Dado que niguna arista quedaria sin cubrir, porque ningun invitado se queda
sin hablar de algun reagalo.


"""

#invitados: lista de pares de invitados conocidos
#solucion: set de invitados con regalos
#k: cantidad de invitados con regalos
#personas = set de todos los invitados
def validador(personas,invitados, solucion, k):
    if len(solucion) > k:
        return False
    
    for p in solucion:
        if p not in personas:
            return False
    
    for p1, p2 in invitados:
        if p1 not in solucion and p2 not in solucion:
            return False
        
    return True
#complejidad O(p + m) p = cantidad invitados, m = cantidad de pares de conocidos