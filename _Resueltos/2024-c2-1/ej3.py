"""
Antonia: Dado un conjunto de invitados, un listado donde en
cada entrada tiene 2 personas que se llevan bien entre sí, y un número K, 
¿existe una forma de armar hasta K mesas para la fiesta del casamiento 
de tal forma que todos los integrantes de una mesa se lleven bien?

Para probar que este problema en NP-C:
1. validador polinomial, que demuetsre que el problema esta en NP
2. Reducir un problema concoido NP-C a este problema, para demostrar que es NP-C

SRC: Dado un grafo G y un numero R, es posible separar los vertices en hasta R cliques

Reduccion:
SRC(grafo, R) <=p Antonia(invitados,K)

Para esta reduccion, se realiza una transformacion para crear una instancia del problema de Antonia, para esto:
A partir del grafo G, se crea el set de invitados con las aristas del grafo. Cada vertice representara un invitado
y una arista significara que se lleva bien con este otro invitado, asi que por cad arista se agrega una entrada en invitados,
con las dos personas que se llevan bien.
Los R cliques que busca el problema de SRC, seran las K mesas que busca formar antonia, 
por lo que R == K.

Si hay SRC hay Antonia:
Si dado G, podemos crear a lo sumo R cliques, entonces podremos armar K mesas para la boda, dado que todos 
los invitados de las mesas se lleven bien entre si. Esto dado que cada clique represetna cada mesa, y las aritas
del grafo que invitados se llevan bien entre si, dado que un clique es un subgrafo compelto, en las mesas
todos se llevaran bien con todos. Por lo que, si dos vertices no son ady en G, no estaran anotados en las lista 
de invitados como "Amigos" y no se sentaran juntos en la mesa.

Si hay Antonia hay SRC:
Si se pudieron armar K mesas para la boda, dado que todos los invitados de la mesa se llevan bien entre si.
Estas mesas representarian los R cliques del grafo G, dado que cada invitado representa un vertice del grafo y
cada relacion de "amistad" una arista que uno dos vertices. Por lo que si dos invitados se pudieron sentar
en un mesa juntos, significara que en el grafo estos vertices esta unidos por una arista. Entonces en cada mesa formada,
los vertices forman un subgrafo completo.


"""

def validador(invitados, mesas, k):
    if len(mesas) > k:
        return False
    
    setAmigos = set(invitados)
    
    #n mesas
    #m personas x mesa
    #O((m)^2 * n )
    for mesa in mesas:
        for invitado in mesa:
            for invitado2 in mesa:
                if invitado == invitado2:
                    continue
                if (invitado, invitado2) not in setAmigos and (invitado2, invitado) not in setAmigos:
                    #dos personas no se llevan bien y estan sentadas juntas
                    return False
    #n mesas
    #m personas x mesa
    #O((n*m)^2 )
    for mesa in mesas:
        for mesa2 in mesas:
            if mesa == mesa2:
                continue
            for invitado in mesa:
                for invitado2 in mesa2:
                    if invitado == invitado2:
                        #se repite persona en mesas distintas
                        return False


    return True
#comñlejidad polinomial -> O( (m * n)^2 + (m)^2 * n )