"""
Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de prestamos. ¿Cuál es el orden temporal de la solución implementada?

Creo nodos para los libros y para los alumnos. 
El flujo de salida de los libros sera de 3 y reciben de una superfuente con una entrda de 3 tambien.
Los alumnos pueden recibir hasta 10 libros, por lo que su flujo maximo de salida sera de 10


Si el problema tuviera que los libros tienen una cuota minima de uso
es decir Cm < flujo < 3 por ejemplo
FF resuelv ebien si puedo tener a 0 como flujo valido, por lo que tengo que 
construir un nuevo flujo valido que sera de ir de 0 a capacidad maxima menos cuota minima
Tengo que crear un nuevo grafo con estos valores
Construyo el poblema con DFS, como si tuviera un flujo inicial (la cuota minima)
"""
