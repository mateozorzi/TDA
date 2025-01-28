"""
Definir los problemas de decisión de Subset Sum y Problema de la Mochila. 
Sabiendo que Subset Sum es NP-Completo, demostrar que el Problema de la Mochila es NP-Completo.
"""

"""
Son NP? si

subSetSum(elementos, W): Dado un arreglo d elementos, existe una suma entre estos que de igual W?
NP-C

mochila(peso, valor, W): Cuanto es el valor maximo que puedo agregar en la mochila, sin que el
                        peso de los elementos sea mayor a W

Reduzco:
subSetSum <=p mochila
Se trata de una reduccion por caso especial a general. El problema de subset sum es un caso particular de la ochila
Para la reduccion, debo pasarle a la caja negra que resuelve la mochila los parametros
peso = elementos, valor = elementos y W = W. De esta manera el problema de la mochila reoslvera como si el arreglo
elementos fueran los pesos y los valores (siendo los numeros mas grandes mas valiosos)
Por lo que mochila es NP-C

"""