"""
El directorio de una empresa realizará una cena de fin de año. En total son “n” directivos
que se deben sentar alrededor de una mesa circular. Lamentablemente existen
conflictos entre algunos de ellos que impiden que se sienten uno al lado del otro. Dado
una instancia del problema, que incluye los n directivos y un listado donde se ven
aquellos pares de directivos que están peleados entre sí, determinar si es posible
sentarse en la mesa.
D: Dado una lista de directivos, y un listado de pares que no se  llevan bien. Es posible
sentar a los directivos en una mesa circular de forma tal que ninguno de los pares de se siente al lado?

1. verificador polinomial, comrpueba que D este en NP
2. Para probar que en NP-C, realizo una reduccion polinomial a un problema NP-C conocido como cicloH

CicloH: Dado un grafo G, determinar si esxiste un ciclo que pase una unica vez por todos los vertices del grafo
Reduccion:
cicloH(G) -> D(directivos, listado)

Para la reduccion se realiaz una trabnsfomarcion de la instancia del grafo del problema de cicloH a una instancia del problema de directivos
para usar caja negra que resuelve el problem D.
A partir de G, se crea una lista con los vertices del grafo, que representaria la lista de directivos.
Para crear una instancia para el listado de malas relaciones entre los directivos, se buscan los vertices que no son ady entre si en el grafo, 
por lo que en un ciclo no podrian estar contiguos.

Si hay cicloH hay D:
Si en el grafo G, existe un ciclo que pase una unica vez por cada vertice, y termine y comience en el mismo. Entonces, dada la transformacion
se podran sentar los n directivos en la mesa circular, sin tener a dos peleados sentados al lado. Esto ya que cada vertice del grafo representa
un directivo y cada par del listado las no ady de los vertices del grafo, que representan las enemistades entre los driectivos. Entonces si en G
el vertice A y B no son ady, al hacer la transofrmacion los directivos A y B tendran una tupla en el lisatdo de enemistades por lo que
no podran sentarse uno al lado del otro.

Si hay D hay cicloH:
Si dado los directivos y el listado de enemistades se consigue sentar a los n directivos en la mesa circular, entonces en G existira un ciclo que 
pase unaunica vez por todos los vertices del grafo. Esto dado que cada direcgtivo representra un vertice del grafo, y si dos directivos no estan juntos en 
el listado, es decir que se llevan bien y esto en el grafo se traduce a que son ady, por lo que si en la mesa ciruclar el directivo A y B estan sentados
juntos, en el grafo A yB seran ady por lo que el ciclo podra pasar por ellos.
"""

def validador(directivos, listado, sol):
    if len(sol) != len(directivos):
        return False

    setDirectivos = set(directivos)

    for n in sol:
        if n not in setDirectivos:
            return False
        
    #compruebo que no haya conflictos
    if (sol[-1], sol[0]) in listado or (sol[0], sol[-1]) in listado:
        #el primero y el utlimo se llevan mal
        return False
    
    for i in range(1, len(sol)):
        if (sol[i-1], sol[i]) in listado or (sol[i], sol[i-1]) in listado:
            #se llevan mal
            return False
        
    return True
#Complejidad O(n) -> n cantidad de directivos