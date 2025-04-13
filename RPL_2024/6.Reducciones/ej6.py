"""
Definir el problema de decisión de las N-Reinas. 
Usar que N-Reinas es un problema NP-Completo para 
demostrar que Demostrar que Independent Set es un problema NP-Completo.
"""

"""
Solucion: 
Si tomo que el problema de N-Reinas es NP-Completo y logro reducir IS a N-Reinas, entonces
IS es NP-completo

N-Reinas <=p IS

N-Reinas    ->True, puedo colocar al menos n reinas en el tablero, sin que se puedan comer entre ellas
            -> False, no

Creo un grafo con:
Simbolizo cada casilla del tablero con un vertice,
uno cada vertice con otro, dependiendo de como se mueve la reina para cada casillero.
Le paso mi grafo a mi caja negra de IS, si consigue encontrar un subconjunto de al menos k vertices
independientes, es decir que se podra poner k reinas en el casillero sin quie se puedan comer

"""