"""
El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1,P2,⋯,Pc
de caminos dentro de dicho grafo y un número k, 
¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? 
Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con Independent Set.
"""

"""
Problema de desicion:
PS: existen al menos k caminos, tal que que ningun par de caminos comparta ningun nodo.

Es NP? SI, puedo crear un validador polinomial, que verifique que niguno de los camino compartan nodos.

Reduzco:
IS <=p PS

Las vertices del grafo original son los pedidos
la cantidad de vertices indep en el problema de IS, sera igual a la cantidad de caminos indep en PS
Los nodos se unen, si en G son ady, en G' no se podran elegir estos dos pedidos
Creo un nuevo G' dirigido, agrego las idas y vueltas. Convierto las aristas en vertices y los uno con los pedidos 

3. Si enecuntra al menos k caminos, habra al menos k nodos que son ady entre si

SI hay un PS, habra un IS valido?
Si existen k caminos independientes. Con la reduccion del rpblema, como cada vertice del grafo de la transformacion simboliza un camino,
si estan unidos significa que comparten un nodo en el grafo original. Al encontrar k caminos, habran al menosk vertices indepdientes en el grafo,
ya que los caminos que pasan por estos, son independientes

Si y solo si
Si hay IS, habra un PS valido?
Si tenemos al menos k vertices independietes en el grafo, con la transoformacion, podremos ver que los caminos que formados por estos verices seran 
independientes


"""