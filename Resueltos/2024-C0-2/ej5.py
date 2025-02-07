"""
Indicar si las siguientes afirmaciones sobre Redes de Flujo son verdaderas o falsas, justificando detalladamente.

a. Si aumentamos la capacidad de todas las aristas por una constante K, implicará que el flujo máximo aumente en
[K × min (grado_salida[fuente], grado_entrada[sumidero])] unidades.

F, si se aumenta en k todas las aristas, las aristas de salida de la fuente y entrada del sumidero tambien son aumentadas en k unidades
por lo que podra fluir por toda la red de flujo. Por lo que, el flujo maximo aumentara en k unidades

b. En el caso del flujo máximo de la red, aumentarle la capacidad a una arista cuya capacidad no fue consumida no
tienen ningún efecto sobre el flujo máximo.

V, al no ser consumida, ya sea que no pase flujo o que haya pasado una parte, significa que en el/los caminos usados no era la arista de
capacidad minima, por lo que no acota el flujo de la red. Si no fue consumida por el flujo, al aumentar la capacidad no cambiara en nada
solo tendra mas excedente en su capacidad

c. Eliminar una arista al azar del grafo puede no afectar el flujo máximo, pero si eliminamos una arista que es parte
del corte mínimo, entonces obligatoriamente sí afectará al flujo máximo.

F, esto por el teorema de max-flow min-cut. Que explica la relacion que hay entre el corte minimo y el maximo flujo de la red.
Si se elimina una arista del corte minimo se vera afectado el flujo maximo, reduciendose en su valor. 
Aunque eliminar una arista al azar tambien puede afectar el flujo maximo, si es una arista utilizada, por donde pasa flujop, si es eliminada
y no existe otro camino por donde pasar este flujo, el maximo se vera reducido
"""