"""
El problema de decisión de 3-SAT dice: 
dadas un número de cláusulas de variables booleanas, 
cada cláusula consta de la operación OR entre 3 términos, 
decidir si existe una configuración de las variables booleanas 
tal que sea posible cumplir todas las cláusulas. 
El problema de 3-SAT es NP-Completo. 
Dados los problemas de decisión de Independent Set y 3-SAT, 
demostrar que Independent Set es NP-Completo. 
Luego explicar de qué manera, con el trabajo hecho en la guía hasta este ejercicio, 
se puede afirmar que Vertex Cover es NP-Completo.
"""

"""
IS en NP? si, creo validaor polinomial

Reduzco:
3-SAT <=p IS

Creo un grafo con:
Creo un vertice para cada termina de las clausulas y su complemento.
Uno los vertices con sus complementos, para evitar que los dos pertenzcan al IS
Uno vertices por las clausulas
Le paso a mi metdoo IS el grafo
Como reduje un problema NP-C a IS, puedo deducir que IS es NP-C
Y como puedo reducir IS <=p VC, VC tambien sera NP-C
"""

