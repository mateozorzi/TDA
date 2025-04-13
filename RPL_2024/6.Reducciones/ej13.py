"""
Realizar una reducción polinomial del siguiente problema a otro de los vistos durante la cursada. 
Ayuda: pensar en alguno de los vistos de programación dinámica. 
Dada esta reducción, ¿se puede afirmar que este problema es NP-Completo?

Dado un número n, encontrar la cantidad más económica (con menos términos) 
de escribirlo como una suma de cuadrados.
"""

"""
C^2 <=p cambio <=p subsetSum -> conviene hacerlo con cambio, pero no nos dice si esta en NP-C

Mi caja negrea de resolucion es el codigo del problema del cambio.
creo un arreglo con los valores de los numeros hasta raiz de n. Este arreglo lo uso como
el arreglo de las moenedas en el del cambio. Pero al ser el problema del cambio NP-C, no puedo asegurar que C^2 tambien lo sea.

"""