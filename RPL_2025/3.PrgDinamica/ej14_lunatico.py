"""Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. 
Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. 
Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. 
Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, 
la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. 
Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. 
El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, 
si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. 
Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. 
El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. 
Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. 
Implementar un algoritmo que, por programación dinámica, obtenga 
la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. 
Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto."""