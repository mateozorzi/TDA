"""
Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para cumplir sus horarios. 
Podemos decir que podemos usar un avión para un segmento/vuelo 
i y luego para otro j si se cumple alguna de las siguientes condiciones:
a. El destino de i y el origen de j son el mismo. o b. 
Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente.

Decimos que el vuelo j es alcanzable desde el vuelo 
i si es posible usar el avión del vuelo i y después para el vuelo j.
Dados todos los vuelos con origen y destino, y el tiempo que tarda un avión entre cada par de ciudades queremos decidir: ¿Podemos cumplir con los m vuelos usando a lo sumo 
k aviones? Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se decide si es posible cumplir con la premisa. ¿Cuál es el orden temporal de la solución implementada?

Cada vertice seran destinos, tengo que tener en cuenta el horario de salida o llegada, para saber si puedo conectar tramos,
Cada arista tendra peso 1, o sea el flujo maximo sera la cantidad de aviones que use. Algunos vuelos los tendre que hacer si o si, por lo que tendra una cota minima de 1
Superfuente (conectada a otra fuente que le dice cuantos aviones tiene, K) con aristas de capacidad 1 (conectada a las salidas) y supersumidero con aristas de capacidad 1 (conectada a los destinos)
la funete tiene una demanda -K (da aviones) y el sumidero una demanda K (necesita aviones)

los destinos son obligatorios, luego puedo llegar por una ruta opcional (la que no tiene cota minima)

"""