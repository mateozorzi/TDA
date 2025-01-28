"""
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
El problema es dar la cantidad mínima de faros que se necesitan para que 
todos los submarinos queden iluminados, 
siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). 
¿Se encuentra este problema en NP? 
¿Qué problema NP-Completo visto en la cursada es parecido al problema definido? 
Definir en ambos casos el problema de decisión. 
¿qué reducción podríamos hacer? 
¿Podemos concluir que este problema es un problema NP-Completo?
"""

"""
Esta en NP? SI porque puedo crear un validador polinomial que valida una posible solucion en timeepo polinomial

Problema de desicion:
Submarino -> Existe un subconjunto minimo de vertices de tamaño  al menos k, donde poner faros y que todos los subamrinos sean ady por lo menos a uno de estos?
Hitting-Set -> Dado un conjuntio de elementos A, y subconjuntos B (con los elementos de A). 
                Devuelve true si existe un subconjunto C de elementos (tamaño <= k), tal que
                haya un elemento de cada subconjunto

Reduzco
HS <=p Submarino

Conversion:
Cada subconjunto representara las casillas adyacentes de los submarinos. Creo una matriz y 
le asigno una posicion del casillero a cada uno de estos subconjuntos y el submarino en cuestion.
Realizo busqueda binaria para el minimo k, llamo una cantidad polinomica de veces a mi caja negra 
de submarino, empezando con k = cant de elementos de A
Voy reduciendo hasta que la caja negra no encuentre el subconjunto C, cuendo no encuentr el subconjunto
tendre que fijarme en el sig k hasta que lo encuentre

Existe minimo de submarino, habra un HS valido?


si y solo si
 
Existe un HS, habra un solucion a submarino valida?


Con esto puedo decir que el submarino en NP-C

"""

