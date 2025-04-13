"""
(★) ¿Pertenece el siguiente problema a PSPACE? Dada una lista de enteros positivos L y un entero n obtener todos los subconjuntos de 
L que suman exactamente n.

No pertence a PSPACE, ya q1ue para guardar todos los subconjuntos de L, que sumen n, necesitaia de un espacio exponencial

(★) ¿Pertenece el siguiente problema a PSPACE? Dada una lista de enteros positivos 
L y un entero n obtener un subconjunto de 
L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n

Si pertenece a PSPACE, ya que solo tengo que guardar el que sume exactamente n o que mas se acerque a n sin pasarse,
por lo que solo estaria guardando un solo subconjunto y eso lo puedo hacer en espacio polinomico.
"""