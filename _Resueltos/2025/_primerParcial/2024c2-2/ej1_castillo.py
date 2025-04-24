"""
Imaginá que estamos organizando un torneo de guardias en un castillo. El castillo tiene un suelo dividido en una
cuadrícula de tamaño n x m, y cada celda puede estar ocupada por un guardia o estar vacía. Los guardias tienen la
habilidad de vigilar todas las celdas adyacentes a su posición, incluidas las diagonales, es decir, pueden ver las celdas
vecinas que están justo al lado, arriba, abajo, a la izquierda, a la derecha o en las esquinas.
Se nos pide colocar la mayor cantidad posible de guardias en el castillo sin que ninguno pueda vigilar a otro. Esto
significa que no podemos colocar dos guardias en celdas adyacentes, ya que estarían vigilándose mutuamente.
Implementar un algoritmo greedy que permita colocar el mayor número posible de guardias en el castillo sin que se
vigilen entre sí. Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo
greedy. El algorimto, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo
"""

def guardias_ady(pos, guardias, matriz):
    cant_fil = len(matriz)
    cant_col = len(matriz[0])
    pos_x = pos[0]
    pos_y = pos[1]

    #arriba, abajo, der, izq
    if pos_x > 0:
        if (pos_x - 1, pos_y) in guardias:
            return True
    if pos_x < cant_col-1:
        if pos(pos_x + 1, pos_y) in guardias:
            return True
    if pos_y > 0:
        if (pos_x, pos_y - 1) in guardias:
            return True
    if pos_y < cant_col-1:
        if (pos_x, pos_y + 1) in guardias:
            return True
    
    #diagonales
    if pos_x > 0 and pos_y > 0:
        if (pos_x - 1, pos_y - 1) in guardias:
            return True
    if pos_x > 0 and pos_y < cant_col-1:
        if (pos_x - 1, pos_y + 1) in guardias:
            return True
    if pos_x < cant_col-1 and pos_y > 0:
        if (pos_x + 1, pos_y - 1) in guardias:
            return True
    if pos_x < cant_col-1 and pos_y < cant_col-1:
        if (pos_x + 1, pos_y + 1):
            return True
    
    #si no entro en un nigun if anterior, no tiene guardias adyacentes
    return False

def castillo(matriz):
    guardias = set()

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i,j) not in guardias and not guardias_ady((i,j), guardias, matriz):
                guardias.add((i,j))

    return guardias

#regla greedy: Para cada casillero del castillo (situacion local), compruebo si las celdas adyacentes tienen un guardia colocado, sino es asi,
#entonces coloco un guardia en la pos (i,j) y guardo esa posicion para siguiente comprobaciones

#Es optimo? Si ya que al tener que maximizar la cantidad de guardias colocoados sin poder vigialrse, al agregar en cada casilla que encuntro sin un guardia adyacente
#estoy maximizando el espacio que uso para los guardias colocados. Colocoando en la mayor cantidad de casillas posibles al ir casilla por casilla
            